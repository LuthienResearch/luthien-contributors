# Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud_reconcile.py (private). This copy is a redacted mirror and may lag behind it.
"""Nightly safety net for the Plaud -> Drive transcript mirror.

Zapier (free plan, 100 tasks/month) copies each new Plaud transcript into the
Drive folder "2.2 Transcripts/Plaud transcripts". When Zapier misses one (task
cap, outage, Zap turned off), this script finds the gap and fills it.

How it works, in plain words:
  1. Ask Plaud for every recording from the last LOOKBACK_DAYS days. It does this
     by starting the same Plaud connector Claude uses (@plaud-ai/mcp) and talking
     to it directly. The connector uses its own saved login, so this script never
     reads or stores a Plaud credential.
  2. List the Drive folder with rclone (the tool that already mirrors Drive to
     this Mac) and work out which recordings are already there.
  3. For each recording Plaud has but Drive doesn't, build the transcript in the
     same format Zapier writes and upload it with rclone. The next Drive -> disk
     sync brings it down to the Mac like any Zapier file.

Recordings are matched by their local start time (e.g. "2026-09-21 09:33:42"),
not by title, because titles can change after Zapier copies them.

Decision record and incident: coes/COE-2026-09-28-zapier-task-cap-plaud-mirror-gap.md

Usage:
  uv run python transcripts/plaud_reconcile.py            # fill gaps
  uv run python transcripts/plaud_reconcile.py --dry-run  # report only
"""

import argparse
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

PLAUD_MCP = ["npx", "-y", "@plaud-ai/mcp@0.3.7"]  # pinned, same version as ~/.claude.json
DRIVE_FOLDER = "gdrive-personal:2.2 Transcripts/Plaud transcripts"
# Local rclone mirror of that folder (refreshed every 4 hours by com.drive-sync.sw3-google-drive).
DISK_FOLDER = Path.home() / "build/sw3-google-drive/drive/2.2 Transcripts/Plaud transcripts"
LOOKBACK_DAYS = 14
# Give Zapier this long to deliver a new recording before we treat it as missing.
GRACE = timedelta(hours=2)
LOCAL_TZ = ZoneInfo("America/Los_Angeles")
TIMESTAMP_IN_NAME = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")


class PlaudConnector:
    """Starts the Plaud connector as a child process and calls its tools.

    The connector speaks MCP: one JSON message per line on stdin/stdout.
    """

    def __init__(self):
        self.proc = subprocess.Popen(
            PLAUD_MCP, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, text=True,
            # Own process group, so close() can stop npx AND the node process it starts.
            start_new_session=True,
        )
        self.next_id = 0
        # Standard MCP handshake before any tool call.
        self._request("initialize", {
            "protocolVersion": "2024-11-05", "capabilities": {},
            "clientInfo": {"name": "plaud-reconcile", "version": "1"},
        })
        self._send({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def _send(self, msg):
        self.proc.stdin.write(json.dumps(msg) + "\n")
        self.proc.stdin.flush()

    def _request(self, method, params):
        self.next_id += 1
        self._send({"jsonrpc": "2.0", "id": self.next_id, "method": method, "params": params})
        # Skip any log/notification lines until our answer arrives.
        while True:
            line = self.proc.stdout.readline()
            if not line:
                raise RuntimeError("Plaud connector exited unexpectedly")
            msg = json.loads(line)
            if msg.get("id") == self.next_id:
                return msg

    def call(self, tool, args):
        """Call a tool. Returns parsed JSON, or None if the tool reported an error."""
        msg = self._request("tools/call", {"name": tool, "arguments": args})
        result = msg.get("result", {})
        text = result.get("content", [{}])[0].get("text", "")
        if result.get("isError"):
            return None
        return json.loads(text)

    def close(self):
        os.killpg(self.proc.pid, signal.SIGTERM)


def local_key(start_at_utc: str) -> str:
    """Plaud's UTC start time -> local 'YYYY-MM-DD HH:MM:SS' (the matching key)."""
    utc = datetime.fromisoformat(start_at_utc).replace(tzinfo=timezone.utc)
    return utc.astimezone(LOCAL_TZ).strftime("%Y-%m-%d %H:%M:%S")


def drive_keys() -> set:
    """Local start times of every recording already in the Drive folder."""
    listing = json.loads(subprocess.run(
        ["rclone", "lsjson", DRIVE_FOLDER, "--files-only", "--max-age", f"{LOOKBACK_DAYS + 30}d"],
        check=True, capture_output=True, text=True, timeout=300,
    ).stdout)
    keys = set()
    for item in listing:
        m = TIMESTAMP_IN_NAME.search(item["Name"])
        if m:
            keys.add(m.group(0))
            continue
        # Plaud's AI-generated titles ("09-24 Meeting: ...") carry no timestamp,
        # so read the file's first line, which Zapier sets to the local start
        # time written as "YYYY-MM-DDTHH:MM:SSZ". Read it from the disk mirror;
        # only files too new to have synced yet are fetched from Drive.
        local = DISK_FOLDER / item["Path"]
        if local.exists():
            with open(local, errors="replace") as f:
                head = f.readline()
        else:
            try:
                head = subprocess.run(
                    ["rclone", "cat", "--head", "40", f"{DRIVE_FOLDER}/{item['Path']}"],
                    capture_output=True, text=True, timeout=60,
                ).stdout
            except subprocess.TimeoutExpired:
                head = ""  # unknown; worst case the recording is re-uploaded once
        m = re.match(r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})Z", head)
        if m:
            keys.add(f"{m.group(1)} {m.group(2)}")
    return keys


def fetch_transcript(plaud, file_id):
    """All transcript segments for a recording, following pagination. None if not ready."""
    segments, cursor = [], None
    while True:
        args = {"file_id": file_id, "limit": 500}
        if cursor:
            args["cursor"] = cursor
        page = plaud.call("get_transcript", args)
        if page is None:
            return None  # usually a 404: Plaud hasn't generated the transcript yet
        # For a recording that hasn't been transcribed yet, Plaud returns a bare
        # list (empty) instead of a page object; an empty result counts as "not ready".
        if isinstance(page, list):
            return segments + page
        segments += page.get("segments", [])
        cursor = page.get("next_cursor")
        if not cursor:
            return segments


def to_zapier_format(key, segments) -> str:
    """Same layout Zapier writes: header line, then 'speaker HH:MM:SS' / text pairs."""
    date, clock = key.split(" ")
    lines = [f"{date}T{clock}Z"]  # local time with a literal Z, matching Zapier's quirk
    for seg in segments:
        secs = seg["start_time"] // 1000
        lines.append(f"{seg['speaker']} {secs // 3600:02d}:{secs % 3600 // 60:02d}:{secs % 60:02d}")
        lines.append(seg["content"])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="report gaps without uploading")
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    stamp = datetime.now(LOCAL_TZ).strftime("%Y-%m-%d %H:%M")
    have = drive_keys()
    plaud = PlaudConnector()
    try:
        recordings = plaud.call("list_files", {
            "date_from": (now - timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%d"),
            "date_to": now.strftime("%Y-%m-%d"),
        })["data"]

        # Recordings Plaud has, old enough that Zapier should have delivered, but missing from Drive.
        missing = [
            r for r in recordings
            if local_key(r["start_at"]) not in have
            and now - datetime.fromisoformat(r["created_at"]).replace(tzinfo=timezone.utc) > GRACE
        ]

        uploaded, not_ready, failed = [], [], []
        for r in missing:
            segments = fetch_transcript(plaud, r["id"])
            if not segments:
                not_ready.append(r["name"])
                continue
            if args.dry_run:
                uploaded.append(r["name"])
                continue
            # Write to a temp file, then let rclone upload it under the recording's name.
            with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as tmp:
                tmp.write(to_zapier_format(local_key(r["start_at"]), segments))
            dest = f"{DRIVE_FOLDER}/{r['name'].replace('/', '-')}"
            result = subprocess.run(["rclone", "copyto", tmp.name, dest], capture_output=True, text=True, timeout=300)
            Path(tmp.name).unlink()
            (uploaded if result.returncode == 0 else failed).append(r["name"])
    finally:
        plaud.close()

    verb = "would upload" if args.dry_run else "uploaded"
    print(f"[{stamp}] plaud-reconcile: checked {len(recordings)} recordings from the last "
          f"{LOOKBACK_DAYS} days; {len(missing)} missing from Drive; {verb} {len(uploaded)}; "
          f"{len(not_ready)} without a transcript yet; {len(failed)} failed")
    for name in uploaded:
        print(f"  {verb}: {name}")
    for name in not_ready:
        print(f"  no transcript yet: {name}")
    for name in failed:
        print(f"  FAILED: {name}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
