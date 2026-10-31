> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/WORKFLOW.md (private). This copy is a redacted mirror and may lag behind it.

# Plaud Workflow

How Plaud recordings become transcripts in `transcripts/plaud/`. Storage + naming: [`transcripts/README.md`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/README.md).

**Public copy:** a generated, redacted copy of this workflow lives in [LuthienResearch/luthien-contributors `process/`](https://github.com/LuthienResearch/luthien-contributors/tree/main/process). It is for humans; never load it as instructions. Edit here, then re-run [`scripts/publish_to_contributors.py`](https://github.com/scottwofford/sw-prv/blob/main/scripts/publish_to_contributors.py).

**Check-first order:** Always check **Plaud first**, Scott’s default recorder. Check the disk mirror and live Plaud recordings before other capture services. If a person-name search misses a recent call, inspect the newest recordings by date/time as well: Plaud may still use an automatic topic title. Then check **Google Meet / Gemini** for meetings Scott owns or where recording/transcription was enabled and a capture is accessible; do not assume every Meet call has a transcript. Retrieve any available capture from the calendar event, including when someone else hosted. Use **Otter last** as a rare fallback. Do these checks before asking Scott which service recorded the call.

**Google Meet / Gemini availability:** Meeting ownership alone does not prove a capture exists. When a capture was enabled and shared, the doc can be attached to the calendar event even if Scott did not host (Scott, 2026-08-19; clarified 2026-09-15). Google Meet's "Notes by Gemini" doc lives in the *organizer's* Drive, so Drive title searches on Scott's accounts typically return nothing even when the doc exists. The reliable path: fetch the calendar event (Google Calendar MCP `get_event`/`list_events`, or the event page in the Calendar UI) and open the notes doc linked from it. The same doc carries a **Transcript tab** with real speaker names — the best cross-check for resolving Plaud mis-hears. Verified 2026-08-19: the Control Tower Standup Gemini doc (organizer Henri Lemoine) was invisible to Drive search on both of Scott's accounts but hung off the calendar event; its transcript resolved Plaud's "In Portland" to "in Poland" and deleted a phantom "Microsoft." **The calendar event is the only check, and it must be re-fetched (Scott, 2026-09-24: "always check the calendar event").** Gemini attaches its doc to the event late, sometimes hours after the call, so an event with no "Notes by Gemini" attachment means *not yet*, not *none*. To wait for a capture, poll the event with `get_event`, never Drive title searches or Gemini's notification email: both missed a doc that the event carried. Never write "no Gemini capture" into an artifact until a fresh `get_event` still shows none. Verified 2026-09-24: the Tailwind-homework call ended 12:42pm; the event had no Gemini attachment at 12:56pm, Drive and Gmail polls through 2:56pm found only the video, and the Notes-by-Gemini doc (with Transcript tab) was on the event by 3:57pm.

## Select the home before filing

Apply [Meeting home](https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/CLAUDE.md#meeting-home) before the transfer, merge, or mirror steps below. Those steps describe `sw-prv` captures only; they do not override the initial-home decision. For Scott's individual meetings use `luthien-org` conventions; for Control Tower team meetings use `meeting-transcripts` conventions. An unattended ingest pass must not promote an individual meeting.

## The three paths

Each path is an *input*, not a finished transcript. All three yield Plaud's structural transcript; they differ in effort and whether real speaker names come along. Combining them into one file: see Dataflow below.

### 1. Zapier path (auto, real-time) — the default

Plaud finishes a recording, Zapier mirrors it to [Drive `2.2 Transcripts/Plaud transcripts/`](https://drive.google.com/drive/folders/1KXmNaAo7a2IFS00HjW86saPxRWogxPte), rclone one-way-copies it to local disk `~/build/sw3-google-drive/drive/2.2 Transcripts/Plaud transcripts/`. Each recording is one extensionless file named `<auto-title> <YYYY-MM-DD HH:MM:SS>`, body = `Speaker N HH:MM:SS` blocks. Live since 2026-05-07.

- **Pro:** zero effort; on disk within the sync interval, no manual export; Claude Code reads it directly.
- **Con:** no real names (generic `Speaker N`); content-based auto-title frozen at Zap time (later web-UI renames never reach the mirror).
- **Free plan, backed by a nightly gap filler (Scott, 2026-09-28).** Zapier's free plan stops after 100 recordings per billing month (around the 20th at current volume). Instead of paying, [`transcripts/plaud_reconcile.py`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud_reconcile.py) runs nightly at 23:30 on the Mac (launchd `com.scott.plaud-reconcile`, log `~/Library/Logs/plaud-reconcile.log`): it compares the last 14 days of Plaud recordings to the Drive folder by local start time and uploads anything missing for more than 2 hours, in the Zap's format (with real speaker names where tagged). So after the cap, recordings arrive next night instead of within minutes, and not at all while the Mac is away. Revisit a paid Zapier plan if that lag hurts. Decision record: [COE-2026-09-28](https://github.com/scottwofford/sw-prv/blob/main/coes/COE-2026-09-28-zapier-task-cap-plaud-mirror-gap.md).

### 2. Plaud MCP path (live query / tagged names / backfill) — official server, added 2026-07-31

The `plaud` MCP server (`mcp__plaud__*`; official `@plaud-ai/mcp`, pinned per [setup.md](https://github.com/scottwofford/sw-prv/blob/main/setup.md)) queries Plaud cloud headlessly: `list_files` (keyword match on *current* recording names + date filters), `get_transcript` (timestamps + speaker labels), `get_note` (Plaud's AI summary / action items), `get_file` (metadata + 24h presigned audio URL).

- **Pro:** speaker names tagged in the web UI come through (`speaker: "Matt MacDermott (CG)"`, positional label preserved as `original_speaker`; verified 2026-07-31) — tagged-name retrieval no longer needs a browser. No Zap/rclone lag; `list_files` sees Scott's manual renames ("buck", "aryan"), which the frozen disk-mirror titles never show; also the cheap way to diagnose suspected mirror gaps (compare cloud directly against disk).
- **Con:** read-only — it cannot *tag* speakers (that still takes the web UI: Scott by hand or Claude in Chrome, see operational notes). Transcripts paginate at 50 segments per call (`next_cursor`); `page_size` minimum is 10.

### 3. Manual transcript paste (quick one-off)

Scott copies a transcript from the Plaud web UI (or elsewhere) and pastes it into chat.

- **Pro:** fastest for one convo; carries real names if Scott tagged them in the UI first.
- **Con:** loses metadata (filename timestamp, source title, duration); never lands in Drive/repo unless written to a file; an un-tagged paste adds nothing the disk file or MCP lacks.

**Where Claude in Chrome went (2026-07-31):** the Chrome path's fetch duties (backfill, batch name retrieval) moved to the MCP path. Chrome remains only for what requires the auth-gated web UI itself: tagging speaker names at source. Operational notes below.

## Dataflow: the pipeline

Four stages, in order. Data flow comes first; reachability is the final stage, not a parallel concern.

`record → transfer raw to the github folder → merge (if applicable) → make the final version reachable on all surfaces`

```
  1. RECORD        Plaud device -> Plaud cloud (speech-to-text + diarization)
                                       |
             +-------------------------+------------------------+
             v                         v                        v
   +------------------+     +------------------+     +--------------------+
   | 1. Zapier path   |     | 2. Plaud MCP     |     | 3. Manual          |
   |    (default)     |     |    (live query)  |     |    transcript      |
   |                  |     |                  |     |    paste           |
   | auto -> Drive    |     | headless cloud   |     | Scott pastes into  |
   |   -> disk        |     | fetch: search,   |     | chat (Plaud UI or  |
   | STRUCTURE:       |     | transcript, note |     | SuperWhisper)      |
   | timestamps,      |     | REAL NAMES if    |     |                    |
   | Speaker N,       |     | web-UI tagged    |     | REAL NAMES if      |
   | auto-title.      |     | (tagging itself: |     | tagged first,      |
   | NO names.        |     | Chrome/by hand)  |     | else none          |
   +--------+---------+     +--------+---------+     +---------+----------+
            |                        |                         |
            +------------------------+-------------------------+
                                     v
  2. TRANSFER RAW    Claude Code writes the raw into repo `transcripts/plaud/`
     -> GITHUB       (github is the canonical home; Drive/disk raw is staging)
                                     v
  3. MERGE           skeleton from Zapier + names, cheapest source that works wins:
     (if applicable) Gemini names / Plaud's Scott label -> content-inference -> MCP fetch of
                     web-UI tags -> tag via Chrome then MCP -> paste
                                     v
   +----------------------------------------------------------------+
   | AUTHORITATIVE FILE                                              |
   | skeleton + resolved names + header block                        |
   | (date/time/duration, participants, linked sources,              |
   |  "Speaker N = name" map, summary/actions)                       |
   | single service -> its source folder; multiple services          |
   | (Plaud & SuperWhisper, Plaud & Gemini, ...) -> `_merged/`       |
   +----------------------------------------------------------------+
                                     v
  4. MAKE REACHABLE  mirror to Drive `Transcript Masters` (regenerated Google Doc,
     ON ALL SURFACES personal account) -> loadable from Claude Code, desktop, web,
                     and mobile
```

**Stages:**

1. **Record.** Plaud device to Plaud cloud. Output is Plaud's structural transcript: `Speaker N` blocks, a content-based auto-title, no real names.
2. **Transfer raw to github.** Zapier auto-forwards the raw transcript to Drive `2.2 Transcripts/Plaud transcripts/`, rclone one-way-copies it to local disk, and Claude Code writes it into the repo `transcripts/plaud/`. Github is the canonical home, so edits happen only in the repo, never on the Drive/disk raw (the mirror is read-only and re-downloads anything deleted). Paths 2 and 3 bring the same raw transcript in by other routes when names or backfill are needed.
3. **Merge, if applicable.** Resolve `Speaker N` to real names (Gemini transcript-tab names where the call was on Meet, plus Plaud's automatic label for Scott, to content-inference to MCP fetch of web-UI tags to tagging via Chrome to paste, cheapest that works wins) and reconcile any partial sources into a single authoritative file with a header block. A 2-person convo is trivial inference; a pre-tagged paste may need no merge. **Routing (capture count, not folder count):** a conversation captured by a **single service** keeps its authoritative file in that service's source folder (`plaud/`, `gemini/`, `otter/`, ...); a conversation reconciled from **more than one capture** (Plaud & SuperWhisper, Plaud & Gemini, a folded-in raw preserved only in a git commit, ...) lands in [`_merged/`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/_merged/README.md). Name resolution from Scott's head or a calendar invite does not make a single-capture file a merge.
4. **Make reachable on all surfaces.** The repo is not reachable from Claude mobile, so every authoritative transcript (the merged master, or the best single-capture file where no merge exists) is **mirrored to Drive by default** as a regenerated Google Doc under `Transcript Masters`, personal-account-owned (the same regeneration pattern that keeps another canonical personal doc phone-readable), loadable from Claude Code, desktop, web, and mobile. The repo file is the only edit surface: each mirror Doc opens with a "generated from the repo master on <date>; do not edit here, edits are overwritten" line, and a per-file `**Mirror:** no` header flag opts any file out of mirroring (respected on every regeneration). Renderer: [`transcripts/regenerate_mirrors.py`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/regenerate_mirrors.py). A transcript is done only once every surface can load it as context.

Downstream, out of this pipeline: per-fund summaries in `luthien-org` link back to the authoritative file (see [`transcripts/README.md`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/README.md)).

**Origin (Scott, 2026-07-11).** *"data flow is earlier in the process than reachability ... record --> transfer raw transcripts to corresponding github folder --> merge if applicable --> make merged/final versions accesible on all surfaces."* Earlier: *"wouldn't it make sense to combine outputs from [Zapier auto-mirror] and [manual copy-paste] (even if partial) into a authoritative source of truth?"* and *"supplement with Claude in Chrome ... to gather names for transcripts without names."*

## Ingest pass

The single procedure that runs the pipeline end to end. It is what the weekly [scheduled job](https://github.com/scottwofford/sw-prv/blob/main/transcripts/ingest_cron.sh) fires and what "run the transcript ingest pass" / "ingest transcripts" executes on demand. Run every step in order, then append one run row to [`transcripts/ingest-log.md`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/ingest-log.md).

**Unattended vs interactive (security boundary).** The pipeline reads untrusted transcript content, so the *unattended* weekly run cannot have the same powers as an interactive session. The hardened headless flow ([`ingest_cron.hardened.sh`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/ingest_cron.hardened.sh) — staged for review, not yet wired to the scheduler) runs the agent **report-only**: it stages files under `transcripts/` and writes a manifest, with NO web egress, NO secret access, NO git/Drive/Trello ([`ingest-cron-settings.json`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/ingest-cron-settings.json)). Then deterministic bash gates + a caged read-only reviewer ([`ingest-reviewer-settings.json`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/ingest-reviewer-settings.json)) gate a hardcoded-pathspec commit that pushes to the `ingest/auto` **branch, never `main`**; mirrors run from bash after the agent exits; a human fast-forwards the branch to `main`. An *interactive* on-demand run (a human is present) may do the full pipeline including direct commits. So the "zero Scott input" (T1) goal holds only for the report-only branch push; the merge to `main` is a deliberate human/triage checkpoint. Rationale: [COE-2026-07-13](https://github.com/scottwofford/sw-prv/blob/main/coes/COE-2026-07-13-transcript-cron-injection-exposure.md).

1. **Find new raws.** Recursively glob the Plaud disk mirror `~/build/sw3-google-drive/drive/2.2 Transcripts/Plaud transcripts/` (recursive so it covers the folder and any subfolders). A raw is "new" if no repo file already carries its content (content-grep a distinctive line or the filename timestamp against `transcripts/**`, since auto-titles are topic-based). Count files found.
2. **File to repo.** Write each genuinely-new raw into the repo under the [naming convention](https://github.com/scottwofford/sw-prv/blob/main/transcripts/README.md#naming-convention) (`<YYYY-MM-DD>_<slug>.md`, conversation date), provisionally into its source folder (`plaud/`). Github is canonical; never edit the read-only disk/Drive raw.
3. **Resolve names.** Map `Speaker N` to real names, cheapest source that works wins (Gemini transcript-tab names for Meet calls, plus Plaud's automatic label for Scott -> content-inference -> MCP `get_transcript` for web-UI tags -> tag via Chrome then re-fetch -> paste). `Speaker N` is positional, re-derive per file (see Gotchas). Note: the weekly cron can climb the ladder as far as read-only lookups. Since 2026-09-15 the global read-only allowlist ([setup.md](https://github.com/scottwofford/sw-prv/blob/main/setup.md#read-only-tool-allowlist-global-settings-2026-09-15)) grants every session, headless included, Calendar reads (who was invited), Plaud cloud reads (web-UI speaker tags and Scott's recording titles), Drive reads (the Notes-by-Gemini transcript tab on a meeting's calendar event), Gmail reads (signatures, invite threads), and Slack, Beeper, Otter, Linear, and Notion reads. A headless session cannot ask for permission, so every send, create, or tagging tool is simply unavailable to it. It needs no Trello: anomalies go in the log row, not a card.
4. **Disposition (single vs multi-service).** For each conversation, decide: was it captured by more than one service? Single-capture -> authoritative file stays in its source folder. Multi-capture (a second capture exists as a `gemini/`/`otter/` file, a SuperWhisper paste, or a raw preserved only in a git commit) -> it is a merge; continue to step 5. The test is capture count, not folder count ([`_merged/README.md`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/_merged/README.md#what-lives-here-vs-plaud)).
5. **Merge if multi-service.** Follow the [merge checklist](https://github.com/scottwofford/sw-prv/blob/main/transcripts/_merged/README.md#merge-procedure-reference-checklist): best capture per field, overlay names + timestamps, mark coverage gaps and crosstalk, write the header block with the Sources table, place as `_merged/<YYYY-MM-DD>_<slug>.md`. A **low-confidence high-value merge stops and waits for a Fable pass** instead of committing (heavy crosstalk or ambiguous diarization on a personal conversation); every high-value merge records a confidence row in the ingest log (reconciled, diarization confidence, unresolved crosstalk spans).
6. **Regenerate mirrors.** Run [`transcripts/regenerate_mirrors.py`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/regenerate_mirrors.py) so every authoritative transcript's Drive mirror matches the repo (T3/T5). The renderer reports its target list + count; the ingest pass records the mirror check (freshness, target-count vs authoritative-count).
7. **Reconcile + log.** Append a run row to `transcripts/ingest-log.md`: date, files found / processed / dispositioned, mirror check, anomalies. Reconcile recordings-on-disk vs processed vs dispositioned (T7); a fully-powered-off week is caught here by the next run's disk-vs-processed delta.
8. **Anomalies.** Any anomaly (zero new recordings in an active week, mirror gap, disk/Drive count mismatch, a nonzero renderer/script exit, an undispositioned multi-capture) **leads the log row**; the log row is the only record (no Trello card: removed 2026-09-15 at Scott's decision, the row is where Scott reads anomalies). **Screen for benign patterns before calling something an anomaly** (per the diagnose-before-alarming gate in CLAUDE.md): device-sync lag is not an anomaly — multiple recordings landing on Drive within minutes of each other, days after their recording dates, means the Plaud device just flushed a backlog; the pipeline is healthy, log it and move on. Verify a suspected mirror gap stage by stage (Plaud cloud `list_files` → Drive folder listing → Zapier alert emails, including task-limit / held-task alerts → rclone log) and card only confirmed breakage. A file in Plaud cloud but absent from Drive is a Zap-stage failure, not device lag: check the Zapier task cap first (see Gotchas). (2026-07-15: a 2-day "gap" was device sync lag; Zap and rclone were both healthy.) Read the tail of `~/Library/Logs/plaud-reconcile.log` each pass: nightly uploads mean the Zap is missing recordings (expected after the monthly cap, around the 20th to the 25th; an anomaly at other times), and a `FAILED` line or a missing run is always an anomaly.

## Gotchas

- **Always read the full transcript (Scott, 2026-10-28).** Before using a recording for anything (a debrief, takeaways, a draft message, an answer to Scott's question), read the whole raw transcript: Plaud `get_transcript` with `limit: 500`, repeating with `next_cursor` until it is null; for Meet calls, the Gemini Transcript tab. Plaud's `get_note` summary and Gemini's Notes tabs are an index for finding the right recording, never a source: they garble names and invent structure (action items nobody agreed to). Origin: takeaways from a walk with a funder's contact were drafted from two summaries; the full transcripts added the real reasons the summaries left out.
- **Never quote Gemini's AI-notes wording (Scott, 2026-08-10).** A Gemini notes doc has two kinds of content: the raw **Transcript tab** (a capture; usable) and the AI-generated **Notes/summary tabs** (paraphrase; never quote or source claims from them). When wording is unclear, read both raw transcripts (Plaud + Gemini transcript tab) and infer the garbled word from context and verifiable sources (e.g. a GitHub org member list settled "Jurges"/"Jurgus"/"Yurgis" → Jurgis Kemeklis on the 2026-08-10 Control Tooling Sync). Origin: the 8/10 sync debrief quoted "not sufficiently modular" from Gemini's summary; the raw transcript said "our monitors just aren't that generic."
- **`Speaker N` is positional, not stable across recordings.** Re-derive names per file from content cues; never reuse a `Speaker N` = name mapping across files.
- **Plaud STT mis-hears names** (Sean to Shon, Ron to Roy) and can apply confidently-wrong or cross-contaminated labels. Verify against prep notes or the email addresses in Plaud's action-items panel. Override wrong labels; leave partial auto-names ("Jai", "Ryan G") as-is.
- **Plaud automatically labels only Scott's voice (since early October 2026).** Plaud's in-app notice "An update to auto speaker labeling" says auto labeling "now focuses on your own voice, so other participants' details stay private"; saved profiles for other speakers "have been permanently removed"; everyone else appears as `Speaker 1`, `Speaker 2`, renamed manually per recording. Past transcripts keep their labels. Verified in `get_transcript`: the Oct 5 Control Tower standup still auto-labeled Miguel Brandão and Radek Budzyński from saved profiles; the Oct 12 and Oct 13 standups labeled only Scott Wofford. Consequences: never expect a non-Scott name from Plaud on new recordings; for Meet calls take names from the Gemini transcript tab; for in-person calls (no Gemini) names come from content inference, Scott's raw notes, or tagging in the Plaud web UI per recording. Diarization still splits voices, but without profiles it can merge several people under one label (Oct 13: one `Speaker 2` covered at least three people), so attribute line by line.
- **Zapier free plan caps the mirror at 100 recordings per billing month.** One recording = one Zapier task. When the cap hits, Zapier *holds* every new run until the monthly reset (around the 25th), so Drive and disk silently stop receiving files while Plaud cloud keeps them. Symptom: recordings in Plaud `list_files` with `created_at` more than 2 hours old that are missing from disk. That is never device-sync lag (lag means Plaud cloud also lacks the file). Diagnose with a Gmail search (`from:alerts@mail.zapier.com`, lands in `scott@luthienresearch.org`): subjects "You've reached your task limit" / "N held Tasks". The nightly gap filler (see the Zapier path above) refills these automatically; to refill immediately, run `uv run python transcripts/plaud_reconcile.py`. Then *delete* the held tasks in Zapier rather than replaying them (replay creates duplicates and burns the new month's tasks). Incident: [COE-2026-09-28](https://github.com/scottwofford/sw-prv/blob/main/coes/COE-2026-09-28-zapier-task-cap-plaud-mirror-gap.md).
- **Garbled passage that could change a takeaway or action: re-transcribe it yourself, automatically (Scott, 2026-09-28).** Do not hedge in the debrief or ask Scott to listen. Get the recording's presigned URL (Plaud MCP `get_file`), then run [`scripts/local-whisper/clip_retranscribe.sh`](https://github.com/scottwofford/sw-prv/blob/main/scripts/local-whisper/clip_retranscribe.sh) `<url> <start> <end>` over a 30-60 second window. It runs local Whisper unprimed, plus a second run primed with names when `WHISPER_PROMPT` is set; lead with the unprimed reading, since priming can make Whisper hear the names you gave it. Cross-check against Scott's raw notes, record the correction inline (`[was: ...]`) with the method in the transcript's editor's note, and let the script delete its audio copy. Settled 2026-09-27/28 on a call where a garbled word and a list of org names changed the takeaways.
- **Bulk Chrome export can under-count vs the web UI** (rclone rate-limit downstream). Download missing files individually; don't trust the bulk count.

## Finding a past recording

Disk-mirror auto-titles are topic-based and frozen at Zap time, so a filename grep for a person's name won't find their call. Order:

1. MCP `list_files` with `query: "<person>"` — matches *current* recording names, including Scott's manual web-UI renames the disk mirror never sees (verified 2026-07-31: "buck", "aryan", "Julie OpenAI" all findable this way). **It scans only the 500 most recent recordings**, and date filters hit the same cap, so a miss on anything older is not absence: page back with `page`/`page_size: 100` (no filters) until you reach the date. (2026-10-28: an Apr 14 2026 recording was invisible to a name query and only turned up on page 7.)
2. Content-grep speaker labels on disk: `grep -rl "Ryan Kidd" "~/build/sw3-google-drive/drive/2.2 Transcripts/Plaud transcripts/"`.
3. Known date: MCP `list_files` with `date_from`/`date_to`, or filter disk files by date/mtime, then content-check.
4. Filename grep last resort.

**Durable home:** the mirror is a one-way `rclone copy`, so a local rename doesn't reach Drive and the original re-downloads as a duplicate. To make a recording findable by name, file it into the repo.

## Claude-in-Chrome operational notes

Only relevant when *tagging* speaker names in the auth-gated Plaud web UI (the one job MCP can't do; fetching tagged names afterward is MCP `get_transcript`).

- **Speaker rename:** click the speaker pill, type the name, pick the dropdown suggestion explicitly, save, confirm the "updated successfully" toast.
- **Navigation:** no date filter in the left-nav; search by title.
- **Export:** no native per-file Drive export (only the workspace Zapier auto-forward). Download locally, then hand the path to Claude Code for ingestion.
- **Autonomous by default:** run the whole batch, one structured summary at the end (`file ID -> final title -> Drive URL -> speaker map`); pause only on a real blocker.
- **Derive the speaker set from the transcript, not the attendee list.** Invitees can be silent, and in-person recordings pick up bystanders, so diarization can invent a "participant" out of a passing voice. Count distinct speakers from what was actually said before mapping names; when a "speaker's" entire contribution is a sub-10-second fragment, it is usually mis-diarized crosstalk or a passer-by — delete the fragment rather than assigning it a name. Review short clips too; they hide exactly this contamination.

## Speaker-tagging convention

- Use real names, not `Speaker N`.
- Header block at the top of each file: date/time/duration; location/event; participants (full names); Plaud source auto-title (preserved); `Speaker N = name` map.
- Canonical example: [Matt MacDermott ControlConf file](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/2026-04-19_matt-macdermott-coefficient-giving-controlconf.md).

## Appendix: plaud-toolkit path (DEPRECATED 2026-07-31)

Unofficial TypeScript toolkit (fork of [sergivalverde/plaud-toolkit](https://github.com/sergivalverde/plaud-toolkit)) cloned at `~/build/plaud-toolkit`; wrapped Plaud's private API. Never wired into `~/.claude.json`, no creds on this machine. Fully superseded by the official `plaud` MCP server (path 2 above; install + secret handling in [setup.md](https://github.com/scottwofford/sw-prv/blob/main/setup.md)). Do not use; the clone can be deleted.

## Appendix: worked example, one call captured by all four services

The maximal case, to make the model concrete. First the correction that unlocks it:

**The three Plaud paths are not three captures.** Plaud records the call once and its cloud transcribes + diarizes it once. Zapier / MCP / manual paste are three *routes to fetch that same single Plaud transcript*, differing only in whether real names ride along (Zapier = nameless `Speaker N`; MCP = names if tagged in the web UI; paste = names if tagged first). You land **one** Plaud raw, via whichever route carries names (cheapest that works wins). There is no combining among the three paths. A "capture" that gets cited and merged is a distinct *service's* transcription, not a Plaud delivery route. (The one exception inside path 3: a SuperWhisper paste is a genuinely separate re-transcription, so it is its own capture.)

Scenario: **2026-06-15, investor call with Dana Kim (Acme Ventures)**, hosted on Google Meet, also recorded on Plaud, a key stretch re-transcribed in SuperWhisper, and Otter also running. Four services fire.

1. **Record.** Four independent captures of the one call: Plaud (Speaker N + timestamps), Gemini (named + summary, notes not verbatim), SuperWhisper (best words, no names, no times), Otter (named + times + decent words).
2. **Transfer raw to github.** Each distinct capture lands as a raw: Plaud into `plaud/` (tag Dana's name in the web UI, then MCP `get_transcript` fetches the named copy, still one file), Gemini into `gemini/`, Otter into `otter/`, the SuperWhisper re-transcription pasted into chat and folded straight into the merge (never a `local-whisper/` file). This is not the combining step; it is just getting each raw in.
3. **Merge (multi-service, so it goes to `_merged/`).** Best source per field: words = SuperWhisper where it covers, else Otter, else Plaud; names overlaid from Gemini invitees / Otter / Plaud web-UI tags; timestamps from Plaud (or Otter); summary + action items from Gemini auto-notes into the header, never the body; coverage gaps and crosstalk marked with bracketed-italic annotations. Result: `_merged/2026-06-15_acme-ventures_dana-kim.md`, whose Sources table cites every capture at the *service* level:

   ```markdown
   ## Sources
   | Capture                             | Supplied              | Coverage     | Authoritative for  |
   |-------------------------------------|-----------------------|--------------|--------------------|
   | SuperWhisper (pasted by Scott 6-15) | words                 | 00:02:49-end | wording            |
   | Plaud raw (commit `abc123`)         | speaker labels, times | full         | diarization, times |
   | [Otter](url)                        | words, names, times   | full         | tie-break words    |
   | [Gemini](url)                       | summary, action items | end-time only| summary panel      |
   ```

   The live source files (`gemini/`, `otter/`) get a `> Merged into: ...` banner; the SuperWhisper paste has no file to banner; the Plaud raw is cited by its commit SHA.
4. **Reachable.** `regenerate_mirrors.py` renders the master to a Drive Doc in `Transcript Masters`, loadable on web + mobile.

Simple case, for contrast: a Plaud-only call that just needs `Speaker N` resolved to names is **not** a merge (one capture), so it stays in `plaud/`.

## Cross-references

- Cross-source merges (Plaud + Gemini + SuperWhisper + Otter): [`transcripts/README.md` -> Combining multiple sources](https://github.com/scottwofford/sw-prv/blob/main/transcripts/README.md#combining-multiple-sources-into-one-transcript)
- Storage + naming: [`transcripts/README.md`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/README.md)
- [Drive `2.2 Transcripts/Plaud transcripts/` folder](https://drive.google.com/drive/folders/1KXmNaAo7a2IFS00HjW86saPxRWogxPte) (Zapier destination; renamed from `2.2 Plaud` on 2026-07-12, same folder ID; syncs to `~/build/sw3-google-drive/drive/2.2 Transcripts/Plaud transcripts/`)
- [Plaud bulk-downloads folder](https://drive.google.com/drive/folders/1o8cfZLmdZzrr0Pz4ExUxpidje-0I7ETy)
- [scottwofford/drive-sync](https://github.com/scottwofford/drive-sync) (rclone throttle fixes)

## Revision history

- 2026-10-13: Plaud stopped auto-labeling anyone but Scott and deleted saved profiles for other speakers. Name ladder now starts from Gemini names plus Plaud's Scott label; added the gotcha with the Oct 5 vs Oct 12/13 evidence.
- 2026-07-31: Official Plaud MCP server (`@plaud-ai/mcp`) replaces Claude-in-Chrome as path 2 for fetching (verified: web-UI speaker tags come through `get_transcript`; `list_files` sees current renames). Chrome relegated to tagging-only; plaud-toolkit appendix deprecated; person-name search added to Finding a past recording. Setup + hardening: setup.md, sw-prv commit `4fffc3c`.
- 2026-07-12: Added the worked-example appendix (one call, all four services) with the "three Plaud paths are not three captures" correction and a maximal-case Sources table, per Scott.
- 2026-07-11 (4th pass): Dataflow diagram now shows the three input paths (Zapier / Claude in Chrome / manual paste) feeding stage 2, per Scott; stage 3 names `transcripts/_merged/` as the multi-service master home.
- 2026-07-11 (3rd pass): Recast the Dataflow section as Scott's linear four-stage pipeline (record -> transfer raw to github -> merge if applicable -> make reachable on all surfaces). Reachability is now the final stage, not a parallel axis. Dropped the unachievable "discard the raw disk copy" step (the Drive/disk raw is an immutable staging inbox that rclone re-downloads; github is canonical). Added stage 4 (mirror final to a mobile-reachable Drive location) and a downstream pointer to per-fund summaries.
- 2026-07-11 (2nd pass): Restructured to minimalist. Replaced the plaud-toolkit path in the main list with **manual transcript paste**; moved plaud-toolkit to an appendix. Added pros/cons per path. Compressed the Claude-in-Chrome operational details (17 bullets to 5) and the gotchas table (5 rows to 3), dropping one-time incident retellings.
- 2026-07-11 (1st pass): Added the Dataflow section (one structural source plus a name-resolution ladder, merge procedure, Scott's origin quotes).
- 2026-06-22: Added the local synced mirror path so Claude Code reads new recordings off disk with zero manual export. Added the plaud-toolkit path. Renamed paths from A/B/C to descriptive names. Added Scott's recording habit (Plaud-first since Jan 2026; Gemini for self-hosted; rarely Otter).
- 2026-05-20: First canonical version. Encodes learnings from the 5/07 setup session (Zapier ship + Chrome bulk + rclone rate-limit) and the 5/20 ControlConf debrief (auto-titles are not person-based; `Speaker N` is positional).
