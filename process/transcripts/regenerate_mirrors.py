# Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/transcripts/regenerate_mirrors.py (private). This copy is a redacted mirror and may lag behind it.
"""Regenerate the Drive mirrors of every authoritative transcript.

Each authoritative transcript in this repo (merged masters in ``_merged/`` plus
the best single-capture file in each source folder) is mirrored to a personal-
account Google Doc under a ``Transcript Masters`` Drive folder, so it is loadable
as context from Claude web and mobile (T3). The repo file is the ONLY edit
surface; every mirror opens with a "generated ... do not edit here" line (T5).

    uv run --with google-api-python-client --with google-auth python transcripts/regenerate_mirrors.py            # full run
    uv run --with google-api-python-client --with google-auth python transcripts/regenerate_mirrors.py --list     # print mirror set + count, no writes
    uv run --with google-api-python-client --with google-auth python transcripts/regenerate_mirrors.py --only <relpath>   # render one file (dry-run gate)

Auth: the PERSONAL token (``scottwofford3@gmail.com``), never the Luthien token,
so the most personal content never lands under the org identity (T6). The token
carries the ``drive.file`` scope (folder + doc create/edit).

Mirror set = files under ``transcripts/**`` that carry a header block (a
``**Date:**`` label), EXCLUDING the Otter ``archived backup`` corpus (opt-in via
``**Mirror:** yes``) and any file carrying ``**Mirror:** no``.

State lives in ``transcripts/.mirror-map.json`` (tracked; a machine map, exempt
from the R13 no-raw-IDs rule which governs human-facing output): the folder id
plus, per file, its Doc id + content hash. The hash skips unchanged files and
lets a mid-run failure resume; a 404/trashed Doc is recreated and the entry
rewritten.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import time
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

HERE = Path(__file__).resolve().parent           # transcripts/
REPO = HERE.parent
MAP_PATH = HERE / ".mirror-map.json"
TOKEN = Path.home() / ".config/mcp-gdrive/credentials-personal.json"
FOLDER_NAME = "Transcript Masters"

# Google Docs indices are UTF-16 code units; for BMP text (all normal
# transcript content, incl. accented Spanish) that equals Python len().
# Keep each inserted chunk well under the per-request payload ceiling.
CHUNK_CHARS = 20000
MAX_MIRROR_SET = 5000        # guard against a mirror_set() regression mass-creating Drive docs; corpus was 178 on 2026-09-08 (was 60 at launch, corpus ~40)
HEADER_SCAN_LINES = 40


# ---------------------------------------------------------------- auth
def make_services():
    creds = Credentials.from_authorized_user_file(str(TOKEN))
    if not creds.valid and creds.refresh_token:
        creds.refresh(Request())
        TOKEN.write_text(creds.to_json())
    docs = build("docs", "v1", credentials=creds)
    drive = build("drive", "v3", credentials=creds)
    return docs, drive


def with_backoff(fn, *, tries=6):
    """Retry an API call on 429 / 5xx with exponential backoff."""
    delay = 2.0
    for attempt in range(tries):
        try:
            return fn()
        except HttpError as e:
            code = getattr(e, "status_code", None) or getattr(e.resp, "status", None)
            if code and int(code) in (429, 500, 502, 503, 504) and attempt < tries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise


# ---------------------------------------------------------------- mirror-set selection
# Meta/doc files under transcripts/** that are not transcripts.
SKIP_BASENAMES = {"README.md", "WORKFLOW.md", "ingest-log.md", "backlog-dispositions.md", "INDEX.md"}


def header_flags(text):
    """The header region carries the exclusion flags. Every real transcript here
    has a header (labeled or prose), so mirror-by-default is expressed as the
    exclusion set below, not a header-label allowlist that mis-drops the many
    prose/"Editor's note" headers in the corpus."""
    head = "\n".join(text.splitlines()[:HEADER_SCAN_LINES])
    archived = "archived backup" in head
    mirror_no = bool(re.search(r"\*\*Mirror:\*\*\s*no\b", head, re.I))
    mirror_yes = bool(re.search(r"\*\*Mirror:\*\*\s*yes\b", head, re.I))
    return archived, mirror_no, mirror_yes


def mirror_set():
    out = []
    for p in sorted(HERE.rglob("*.md")):
        if p.name in SKIP_BASENAMES:
            continue
        archived, mirror_no, mirror_yes = header_flags(p.read_text())
        if mirror_no:
            continue
        if archived and not mirror_yes:          # Otter archive is opt-in
            continue
        out.append(p)
    return out


def title_of(path, text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


# ---------------------------------------------------------------- markdown parsing (from woffieta regenerate_context_mirror.py)
def parse_inline(s):
    runs, i = [], 0
    while i < len(s):
        m = re.match(r"\[([^\]]+)\]\(([^)]+)\)", s[i:])
        if m:
            runs.append({"text": m.group(1), "link": m.group(2)}); i += m.end(); continue
        m = re.match(r"\*\*(.+?)\*\*", s[i:])
        if m:
            for r in parse_inline(m.group(1)):
                r["bold"] = True; runs.append(r)
            i += m.end(); continue
        m = re.match(r"`([^`]+)`", s[i:])
        if m:
            runs.append({"text": m.group(1), "code": True}); i += m.end(); continue
        m = re.match(r"\*(.+?)\*", s[i:])
        if m:
            for r in parse_inline(m.group(1)):
                r.setdefault("italic", True); runs.append(r)
            i += m.end(); continue
        j = i
        while j < len(s) and s[j] not in "[*`":
            j += 1
        if j == i:
            j = i + 1
        runs.append({"text": s[i:j]}); i = j
    return runs


def is_sep_row(cells):
    return cells and all(re.match(r"^:?-{2,}:?$", (c or "-")) for c in cells)


def parse_table(tbl_lines):
    rows = []
    for ln in tbl_lines:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if not is_sep_row(cells):
            rows.append(cells)
    width = max(len(r) for r in rows)
    for r in rows:
        r += [""] * (width - len(r))
    return rows


def parse_blocks(md):
    md = md.replace("—", "-")  # no em dashes
    lines = md.split("\n")
    blocks, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1; continue
        if line.startswith("#"):
            lvl = len(line) - len(line.lstrip("#"))
            blocks.append(("heading", lvl, line.lstrip("#").strip())); i += 1; continue
        if line.lstrip().startswith("|"):
            tbl = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                tbl.append(lines[i]); i += 1
            blocks.append(("table", parse_table(tbl))); continue
        if re.match(r"^\s*[-*] ", line):
            blocks.append(("bullet", re.sub(r"^\s*[-*] ", "", line).rstrip())); i += 1; continue
        if line.strip() == "---":
            i += 1; continue
        stripped = line.strip()
        if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            blocks.append(("italic_para", stripped[1:-1])); i += 1; continue
        blocks.append(("para", stripped)); i += 1
    return blocks


def runs_to_reqs(runs, start, force_italic=False):
    text, reqs, idx = "", [], start
    for r in runs:
        t = r["text"]
        ts = {}
        if r.get("bold"): ts["bold"] = True
        if r.get("italic") or force_italic: ts["italic"] = True
        if r.get("code"): ts["weightedFontFamily"] = {"fontFamily": "Consolas"}
        if r.get("link"): ts["link"] = {"url": r["link"]}
        if ts:
            reqs.append({"updateTextStyle": {
                "range": {"startIndex": idx, "endIndex": idx + len(t)},
                "textStyle": ts, "fields": ",".join(ts.keys())}})
        text += t; idx += len(t)
    return text, reqs


# ---------------------------------------------------------------- per-doc renderer
class DocRenderer:
    def __init__(self, docs, doc_id):
        self.docs = docs
        self.doc_id = doc_id
        self.cursor = 1
        self.buf = ""
        self.preqs = []      # paragraph-style requests
        self.treqs = []      # text-style requests
        self.breqs = []      # bullet requests

    def clear(self):
        doc = with_backoff(lambda: self.docs.documents().get(documentId=self.doc_id).execute())
        end = doc["body"]["content"][-1]["endIndex"]
        if end > 2:
            with_backoff(lambda: self.docs.documents().batchUpdate(
                documentId=self.doc_id,
                body={"requests": [{"deleteContentRange": {
                    "range": {"startIndex": 1, "endIndex": end - 1}}}]}).execute())

    def flush(self):
        if not self.buf:
            return
        reqs = [{"insertText": {"location": {"index": self.cursor}, "text": self.buf}}]
        reqs += self.preqs + self.treqs + self.breqs
        with_backoff(lambda: self.docs.documents().batchUpdate(
            documentId=self.doc_id, body={"requests": reqs}).execute())
        self.cursor += len(self.buf)
        self.buf, self.preqs, self.treqs, self.breqs = "", [], [], []

    def emit(self, runs, kind, level=None, italic=False):
        if len(self.buf) >= CHUNK_CHARS:   # chunk at a block boundary
            self.flush()
        start = self.cursor + len(self.buf)
        text, stys = runs_to_reqs(runs, start, force_italic=italic)
        text += "\n"
        self.buf += text
        end = start + len(text)
        if kind == "heading":
            self.preqs.append({"updateParagraphStyle": {
                "range": {"startIndex": start, "endIndex": end},
                "paragraphStyle": {"namedStyleType": f"HEADING_{min(level, 4)}"},
                "fields": "namedStyleType"}})
        elif kind == "bullet":
            self.breqs.append({"createParagraphBullets": {
                "range": {"startIndex": start, "endIndex": end},
                "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
        self.treqs.extend(stys)

    def _find_table_at(self, cursor):
        doc = with_backoff(lambda: self.docs.documents().get(documentId=self.doc_id).execute())
        for el in doc["body"]["content"]:
            if "table" in el and el["startIndex"] >= cursor - 1:
                return el
        raise RuntimeError("table not found")

    def emit_table(self, rows):
        self.flush()
        R, C = len(rows), len(rows[0])
        with_backoff(lambda: self.docs.documents().batchUpdate(
            documentId=self.doc_id,
            body={"requests": [{"insertTable": {
                "location": {"index": self.cursor}, "rows": R, "columns": C}}]}).execute())
        tbl = self._find_table_at(self.cursor)
        cells = []
        for ri, row in enumerate(tbl["table"]["tableRows"]):
            for ci, cell in enumerate(row["tableCells"]):
                cells.append((cell["content"][0]["startIndex"], rows[ri][ci]))
        cells.sort(key=lambda x: x[0], reverse=True)   # insert descending so indices hold
        reqs = []
        for cstart, md in cells:
            if not md:
                continue
            text, stys = runs_to_reqs(parse_inline(md), cstart)
            reqs.append({"insertText": {"location": {"index": cstart}, "text": text}})
            reqs.extend(stys)
        if reqs:
            with_backoff(lambda: self.docs.documents().batchUpdate(
                documentId=self.doc_id, body={"requests": reqs}).execute())
        tbl = self._find_table_at(self.cursor)
        self.cursor = tbl["endIndex"]

    def render(self, banner, blocks):
        self.clear()
        self.emit(parse_inline(banner), "para", italic=True)
        for b in blocks:
            if b[0] == "heading":
                self.emit(parse_inline(b[2]), "heading", b[1])
            elif b[0] == "bullet":
                self.emit(parse_inline(b[1]), "bullet")
            elif b[0] == "italic_para":
                self.emit(parse_inline(b[1]), "para", italic=True)
            elif b[0] == "para":
                self.emit(parse_inline(b[1]), "para")
            elif b[0] == "table":
                self.emit_table(b[1])
        self.flush()


# ---------------------------------------------------------------- Drive folder + doc lifecycle
def load_map():
    if MAP_PATH.exists():
        return json.loads(MAP_PATH.read_text())
    return {"folder_id": None, "files": {}}


def save_map(m):
    MAP_PATH.write_text(json.dumps(m, indent=2, sort_keys=True) + "\n")


def resolve_folder(drive, m):
    fid = m.get("folder_id")
    if fid:
        try:
            meta = with_backoff(lambda: drive.files().get(
                fileId=fid, fields="id,trashed").execute())
            if not meta.get("trashed"):
                return fid
        except HttpError as e:
            if int(getattr(e.resp, "status", 0)) != 404:
                raise
    created = with_backoff(lambda: drive.files().create(
        body={"name": FOLDER_NAME, "mimeType": "application/vnd.google-apps.folder"},
        fields="id").execute())
    m["folder_id"] = created["id"]
    save_map(m)
    return created["id"]


def doc_alive(docs, doc_id):
    try:
        with_backoff(lambda: docs.documents().get(
            documentId=doc_id, fields="documentId").execute())
        return True
    except HttpError as e:
        if int(getattr(e.resp, "status", 0)) in (403, 404):
            return False
        raise


def ensure_doc(docs, drive, folder_id, title, entry):
    """Return a live doc_id, creating/recreating as needed."""
    if entry and entry.get("doc_id") and doc_alive(docs, entry["doc_id"]):
        return entry["doc_id"], False
    created = with_backoff(lambda: drive.files().create(
        body={"name": title, "mimeType": "application/vnd.google-apps.document",
              "parents": [folder_id]}, fields="id").execute())
    return created["id"], True


def banner_for(relpath, gen):
    return (f"Generated from the repo master {relpath} on {gen}; do not edit here, "
            "edits are overwritten. Canonical source is the sw-prv repo.")


def render_one(docs, drive, folder_id, m, path, *, force=False):
    rel = str(path.relative_to(REPO))
    text = path.read_text()
    sha = hashlib.sha256(text.encode()).hexdigest()
    entry = m["files"].get(rel, {})
    gen = dt.date.today().isoformat()
    doc_id, created = ensure_doc(docs, drive, folder_id, title_of(path, text), entry)
    if not force and not created and entry.get("sha") == sha:
        return doc_id, "unchanged"
    blocks = parse_blocks(text)
    DocRenderer(docs, doc_id).render(banner_for(rel, gen), blocks)
    m["files"][rel] = {"doc_id": doc_id, "sha": sha, "rendered_at": gen}
    save_map(m)                          # per-doc write so a mid-run failure resumes
    return doc_id, ("created" if created else "updated")


# ---------------------------------------------------------------- entry points
def cmd_list():
    files = mirror_set()
    print(f"Mirror set: {len(files)} files")
    for p in files:
        print(f"  {p.relative_to(REPO)}")
    if len(files) > MAX_MIRROR_SET:
        print(f"\nANOMALY: mirror set {len(files)} exceeds {MAX_MIRROR_SET}; "
              "stop and curate (log an ingest-log anomaly row).", file=sys.stderr)
        return 2
    return 0


def cmd_only(relpath):
    path = (REPO / relpath).resolve()
    if not path.exists():
        print(f"no such file: {relpath}", file=sys.stderr)
        return 1
    docs, drive = make_services()
    m = load_map()
    folder_id = resolve_folder(drive, m)
    doc_id, status = render_one(docs, drive, folder_id, m, path, force=True)
    print(f"{status}: {relpath} -> https://docs.google.com/document/d/{doc_id}/edit")
    return 0


def cmd_all():
    files = mirror_set()
    if len(files) > MAX_MIRROR_SET:
        print(f"ANOMALY: mirror set {len(files)} exceeds {MAX_MIRROR_SET}; "
              "stop and curate before rendering.", file=sys.stderr)
        return 2
    docs, drive = make_services()
    m = load_map()
    folder_id = resolve_folder(drive, m)
    counts = {"created": 0, "updated": 0, "unchanged": 0}
    for p in files:
        doc_id, status = render_one(docs, drive, folder_id, m, p)
        counts[status] += 1
        print(f"  {status:9} {p.relative_to(REPO)}")
    print(f"\nDone: {counts['created']} created, {counts['updated']} updated, "
          f"{counts['unchanged']} unchanged, {len(files)} total in folder {folder_id}.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Regenerate Drive mirrors of authoritative transcripts.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--list", action="store_true", help="print the mirror set + count, no writes")
    g.add_argument("--only", metavar="RELPATH", help="render a single file (dry-run gate)")
    args = ap.parse_args()
    if args.list:
        return cmd_list()
    if args.only:
        return cmd_only(args.only)
    return cmd_all()


if __name__ == "__main__":
    sys.exit(main())
