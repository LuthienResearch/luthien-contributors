> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/transcripts/README.md (private). This copy is a redacted mirror and may lag behind it.

# transcripts/

Raw call recordings, transcripts, and personal correspondence captures, grouped by source.

How multiple sources combine into one authoritative transcript: see [Combining multiple sources](#combining-multiple-sources-into-one-transcript) below. Combining the Plaud paths specifically: [`plaud/WORKFLOW.md`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/WORKFLOW.md).

This directory holds private transcripts and debriefs. Select the meeting home using the routing rule below. Fundraising-specific privacy requirements remain in [H11](https://github.com/LuthienResearch/luthien-org/blob/main/fundraising/fundraising-db-requirements.md#h11-privacy-boundary--call-transcripts-live-in-private-repo-per-fund-md-files-in-public-team-repo-only-carry-summaries--links).

## Routing

Before ingesting or filing a meeting, apply [Meeting home](https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/CLAUDE.md#meeting-home). Potential Luthien hires start privately in this repository; Scott's other individual meetings default to `luthien-org`; Control Tower team meetings go to `meeting-transcripts`. An individual meeting graduates from `luthien-org` to `meeting-transcripts` only with Scott's explicit approval.

Scott-personal conversations and private passages remain here. A private conversation's transcript and debrief may share one file under `transcripts/<source>/`, with the debrief above the verbatim capture. Apply this repository's capture and mirror mechanics only after selecting it as the home. Do not move existing recordings or widen access merely because the default for new individual meetings is `luthien-org`.

## Layout

| Folder | Source | Notes |
|---|---|---|
| `claude/` | claude.ai conversation exports (chat sessions, Plaud uploads to claude.ai) | legacy landing spot for Plaud-recorded calls; new recordings now auto-mirror to disk (see `plaud/` row) |
| `otter/` | Otter.ai transcripts | usually downloaded as `*_otter_ai*.txt` then moved here; Otter MCP (`mcp__otter__*`) can pull these directly |
| `plaud/` | raw Plaud recordings | new recordings auto-mirror to `~/build/sw3-google-drive/drive/2.2 Transcripts/Plaud transcripts/` (read off disk, no manual export). See [`plaud/WORKFLOW.md`](plaud/WORKFLOW.md) for all three paths (Zapier auto-forward / Claude-in-Chrome bulk / plaud-toolkit API) + speaker-tagging mechanics |
| `gemini/` | Google Meet auto-notes | mirrored from Drive — original lives in Drive too |
| `imessage/` | iMessage screenshots / text exports | manual paste/screenshot until iMessage MCP exists |
| `whatsapp/` | WhatsApp screenshots / text exports | manual paste/screenshot until WhatsApp MCP exists |
| `slack/` | exports of Slack workspaces no MCP reaches (e.g. Neolithic) | one dated file per workspace export; each file's header states its capture timestamp so a later pull only fetches newer messages. The Seattle AI Safety workspace is NOT exported here: query it live via `mcp__slack__*` |
| `_merged/` | not a source: the home for authoritative masters that reconcile more than one capture of one conversation | see [`_merged/README.md`](_merged/README.md) for the capture-count test, the header/Sources-table schema, and the merge checklist |

## Combining multiple sources into one transcript

When one conversation is captured by more than one source, the authoritative transcript is a single file that takes **the best source per field**. This generalizes the Plaud-only case in [`plaud/WORKFLOW.md`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/WORKFLOW.md) (structural skeleton + name-resolution layer). The mechanics are now defined, not ad hoc: masters live in [`_merged/`](_merged/README.md) with a Sources-table header, built per its merge checklist, mirrored to Drive, and fed by the [ingest pass](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/WORKFLOW.md#ingest-pass). The full requirements are in [`requirements/transcript-system-req.md`](https://github.com/scottwofford/sw-prv/blob/main/requirements/transcript-system-req.md) (T1-T8).

What each source is good at:

| Source (folder) | Verbatim words | Speaker names | Timestamps | Summary / actions | Full vs notes | Coverage |
|---|---|---|---|---|---|---|
| **Plaud** `plaud/` | medium (STT errors) | positional `Speaker N`; real names via web UI | yes, per block | yes (Plaud panel, in the raw file's JSON) | full transcript | almost everything Scott records |
| **Gemini** `gemini/` | notes, not verbatim | named (calendar invitees) | end-time only | yes (auto summary + next steps) | notes / summary | meetings Scott hosts on Google Meet |
| **Otter** `otter/` | good | named diarization | yes | limited | full transcript | older / fallback captures |
| **SuperWhisper** `local-whisper/` | best (authoritative wording) | none | none | none | full transcript | manual re-transcribe of high-value convos |
| **claude** `claude/` | varies | varies | varies | n/a | export | legacy claude.ai / Plaud-to-claude uploads |
| **iMessage / WhatsApp** | exact text | named | per-message | n/a | full thread | text conversations (screenshot / paste) |

Two asymmetries drive the model:

- **Words and structure trade off across sources.** SuperWhisper has the most accurate words but no speaker labels or timestamps. Plaud has speaker labels and timestamps but noisier words. Gemini has named speakers and a clean summary but is notes, not verbatim. No single source is best at everything.
- **Coverage barely overlaps, by design.** Plaud catches almost everything; Gemini only self-hosted meetings; SuperWhisper only what Scott chooses to re-transcribe. So multi-source overlap happens on exactly the high-value conversations, which is where a merge is worth the effort.

The model: pick the best source per field.

```
   same conversation, captured N ways
   +-----------+   +-----------+   +--------------+   +-----------+
   | Plaud     |   | Gemini    |   | SuperWhisper |   | Otter     |
   | words~    |   | names     |   | words+       |   | words+    |
   | names N   |   | summary   |   | (no names,   |   | names     |
   | times+    |   | (notes)   |   |  no times)   |   | times     |
   +-----+-----+   +-----+-----+   +------+-------+   +-----+-----+
         |               |                |                 |
         +-------- pick best source PER FIELD --------------+
                              v
              AUTHORITATIVE FILE (one per conversation)
              best words + resolved names + timestamps
              + summary/actions in header block
```

- **Words:** SuperWhisper if it exists, else Otter, else Plaud.
- **Speaker labels:** Gemini invitees, Otter diarization, or Plaud web-UI names; overlay onto the chosen words.
- **Timestamps:** Plaud (or Otter). SuperWhisper and Gemini cannot supply these.
- **Summary / action items:** Gemini auto-notes or Plaud's summary panel, in a header block, never mixed into the verbatim body.

Which source supplies the skeleton changes per conversation, and more than one field can be missing at once. Worked examples: one master combines SuperWhisper wording with Plaud speaker labels and timestamps; another combines a Plaud Chrome-export verbatim transcript with a Gemini summary.

How the earlier open questions resolved:

1. **Linking a conversation's copies** is done by the master's Sources table plus a `_merged/` grep by date + participant; live source files also carry a "Merged into" banner where one exists.
2. **Merges follow a defined checklist** ([`_merged/README.md`](_merged/README.md)), run inside the [ingest pass](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/WORKFLOW.md#ingest-pass); they are Claude-executed per checklist rather than a standalone script.
3. **The cross-source master's home is [`_merged/`](_merged/README.md)** (multi-capture); a single-capture file stays in its source folder. The test is capture count, not folder count.
4. **Plaud/Gemini summaries + action items are extracted into the header block**, never mixed into the verbatim body.
5. **SuperWhisper stays manual and rare** by design, so authoritative-words coverage is limited to what Scott re-transcribes (a coverage reality, not a gap).

Home: a single-capture conversation's authoritative file stays in its source folder (`plaud/`, `gemini/`, ...); a conversation reconciled from more than one capture lives in [`_merged/`](_merged/README.md).

## Naming convention

`<YYYY-MM-DD>_<fund-slug>_<participants>.<ext>`

Examples:
- `2026-04-24_acme-ventures_dana-kim.md` (Gemini auto-notes for Dana call)
- `2026-04-29_methodology-advisory_lee-park.md` (Plaud transcript of Lee call)
- `2026-04-20_example-capital_sam-ortiz.md` (in-person debrief notes)

For non-fund sources (e.g., Finn 1:1, Esben 1:1, mentor calls), use the participant name as the slug:
- `2026-05-01_finn-1on1.md`
- `2026-05-04_esben-1on1.md`

## Cross-repo linking pattern

In the public per-fund MD file at `luthien-org/fundraising/funds/<slug>.md`, link to the transcript via GitHub URL:

```markdown
- Transcript: [Apr 24 Gemini auto-notes](https://github.com/scottwofford/sw-prv/blob/main/transcripts/gemini/2026-04-24_acme-ventures_dana-kim.md)
```

Team members without access to this private repo see the link as informational ("a transcript exists, ask Scott if you need it"); Scott resolves the link directly. Per [H11](https://github.com/LuthienResearch/luthien-org/blob/main/fundraising/fundraising-db-requirements.md#h11-privacy-boundary--call-transcripts-live-in-private-repo-per-fund-md-files-in-public-team-repo-only-carry-summaries--links).

## What goes in the public summary

The public per-fund MD file's call entry should carry:
- 3-5 bullet summary of what was discussed
- Verbatim quotes ONLY when load-bearing (per [Scott's confabulation-prevention rule](https://github.com/scottwofford/sw-prv/blob/main/CLAUDE.md))
- Decisions made + action items
- Link to the raw transcript here

The raw transcript here carries everything: full text, timestamps, off-topic exchanges, sensitive details.

## Deleting a transcript (redaction runbook)

A transcript can exist in up to five storage layers, each with different permanence. **Git permanence is the accepted default** (Scott, 2026-07-11): deleting the repo file and committing is enough for almost every case, and the file stays in git history unless you actively purge it. The `git filter-repo` runbook below is the escape hatch for genuinely sensitive removal (T8). Removal is only complete once every layer that holds the content is cleared.

### Permanence table

| Layer | Where | Deleting the repo file removes it? | How to fully remove |
|---|---|---|---|
| Repo file | `transcripts/**/<file>.md` (working tree) | yes | `git rm <file> && git commit` |
| Git history | every past commit that touched the file | **no** | `git filter-repo` runbook below (rewrites history) |
| Drive raw | the Zapier-forwarded original in [`2.2 Transcripts/Plaud transcripts/`](https://drive.google.com/drive/folders/1KXmNaAo7a2IFS00HjW86saPxRWogxPte) | no (independent of the repo) | trash the file in Drive, then empty Drive trash |
| Drive mirror | the generated Doc in the `Transcript Masters` folder | no (regenerated separately) | trash the Doc in Drive + empty trash, and remove its entry from [`transcripts/.mirror-map.json`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/.mirror-map.json) so the renderer doesn't treat it as live |
| Disk mirror | `~/build/sw3-google-drive/drive/2.2 Transcripts/Plaud transcripts/<raw>` | no | delete the Drive raw **first** (else `rclone copy` re-downloads it), then delete the disk copy. `rclone copy` is one-way and does not delete disk files when the Drive source disappears, so the disk copy must be removed by hand |

Deleting the repo file (and regenerating mirrors, which drops it from the mirror set) covers the everyday case. Reach for the history purge only when the content itself must not survive in the clone.

### Git-history purge runbook (`git filter-repo`)

`git filter-repo` rewrites the **entire** clone; it is not scoped by a branch, so never run it "on a branch" of the working checkout and never against the working checkout at all. Always rehearse and run in a fresh throwaway clone, then force-push the rewritten history.

Install once (installed 2026-07-11): `uv tool install git-filter-repo` (lands `git-filter-repo` on `~/.local/bin`, invokable as `git filter-repo`).

Rehearsed 2026-07-11 on a throwaway clone (removed a test file from all 889 commits, verified gone, deleted the clone):

```bash
# 1. Fresh, disposable clone under the scratchpad (NEVER the working checkout).
git clone --no-local /Users/scottwofford/build/private-claude-code-docs /tmp/redact-clone
cd /tmp/redact-clone

# 2. Confirm the target is present in history first.
git log --oneline --all -- transcripts/<folder>/<file>.md

# 3. Remove it from ALL history (whole-clone rewrite; --invert-paths = drop these paths).
git filter-repo --path transcripts/<folder>/<file>.md --invert-paths --force

# 4. Verify it is gone from every commit.
git log --oneline --all -- transcripts/<folder>/<file>.md      # expect zero lines
git log --all -p | grep -c "<a distinctive line from the file>" # expect 0

# 5. Push the rewritten history, then re-sync the working checkout.
git push origin --force --all
git push origin --force --tags
#   in the working checkout: git fetch origin && git reset --hard origin/main
#   (or delete and re-clone). Then delete /tmp/redact-clone.
```

After the purge, also clear the Drive raw, Drive mirror + map entry, and disk mirror per the permanence table; the history rewrite only touches the repo. Force-pushing rewrites shared history, so any other clone must re-clone or hard-reset.
