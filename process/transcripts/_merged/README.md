> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy.

# transcripts/_merged/

Home for **authoritative one-file-per-conversation masters that reconcile more than one capture** of the same conversation (Plaud + SuperWhisper + Gemini + Otter, in any mix). A master here takes the best capture per field, per the model in [`transcripts/README.md` → Combining multiple sources](https://github.com/scottwofford/sw-prv/blob/main/transcripts/README.md#combining-multiple-sources-into-one-transcript).

This folder settles gap 3 in that README (a cross-source master had no defined home) and gives gaps 1-2 a working answer (below).

## Scope: full build, no deferrals

Governing requirements: [`requirements/transcript-system-req.md`](https://github.com/scottwofford/sw-prv/blob/main/requirements/transcript-system-req.md) (T1-T8). Scott overruled the earlier deferred-minimal scope on 2026-07-11 (*"I don't want to defer anything... build it one time and for it to just work"*; his bottleneck is cognitive load and context switching, not over-build risk). The full build ships in one pass:

1. This folder as the home for cross-capture masters; the one existing master (a 2026-07-07 personal conversation, not published) migrates in as the exemplar, with its live inbound links updated in the same commit.
2. The naming convention, the master→sources citation rule, the header contract, and the merge checklist (below), all binding.
3. The Drive mirror of every authoritative transcript (Stage 4 below), the scheduled ingest pass with its health report, the redaction runbook, and the one-time backlog sweep, per the requirements doc.

## What lives here vs `plaud/`

The test is **capture count, not folder count**: *did the authoritative file reconcile more than one capture of the conversation?* A capture is any of: a source-folder file, a manual paste (SuperWhisper pastes never become `local-whisper/` files), or a raw preserved only in a git commit.

- **Single-capture resolution stays in its source folder.** A Plaud-only transcript that just needs `Speaker N` resolved to real names is not a merge; it stays in [`plaud/`](https://github.com/scottwofford/sw-prv/tree/main/transcripts/plaud) per [`plaud/WORKFLOW.md`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/WORKFLOW.md). Name resolution from Scott's head or a calendar invite does not make it a merge.
- **More than one capture reconciled → `_merged/`.** The exemplar is SuperWhisper wording (a paste) spliced against Plaud structure (raw preserved in commit `6730436`): two captures, so it belongs here even though only one *folder* was involved.

This settles the two "where does the master live" rules that were open in `objective.md`: `plaud/WORKFLOW.md` stage 3 sends a single-capture Plaud file to `plaud/`; multi-capture masters come here.

## Naming convention

Identical to the rest of the repo: `<YYYY-MM-DD>_<slug>.md`

- Date is the conversation date, not the merge date.
- `<slug>` is the participant name for personal / 1:1 convos, or `<fund-slug>_<participant>` for fund calls, matching [`transcripts/README.md` → Naming convention](https://github.com/scottwofford/sw-prv/blob/main/transcripts/README.md#naming-convention).
- No `_merged` token in the filename; the folder already says it.

Folder name ruled by Scott, 2026-07-11: **`_merged/`** (his vocabulary; a `masters/` rename was considered and declined).

## Linking convention (gaps 1-2)

**Master → sources is the required link.** The master's header carries a Sources table (schema below) citing each capture it drew from: a GitHub URL for a live file, the preserving **git commit** for a folded-in raw, or "pasted by Scott <date>" for a paste. This works for every capture topology, including the exemplar's (paste + commit, zero live source files).

**"Has this conversation been reconciled?" is answered by grepping `_merged/`** for the date + participant. One folder to check, works from any session.

**Source → master banners are conditional, not required.** When a live source file did feed a master (e.g. a hosted meeting captured as both a `gemini/` file and a `plaud/` file), add a one-line banner atop the source:

```markdown
> Merged into: [<master title>](<GitHub URL of the master>). This file is a source input, not the authoritative version; edits go to the master.
```

The banner is cheap when the file exists and worthless as a required convention: in the modal case (SuperWhisper paste, folded-in Plaud raw) there is no live file to banner. The Drive/disk raws can never carry banners either (read-only rclone mirror). So the banner is a bonus signpost, and the Sources table plus the `_merged/` grep are the actual mechanism.

## Header-block schema (reference; codifies the exemplar)

**The exemplar's prose header is the canonical form.** The exemplar (a personal conversation, not published) already carries every invariant below (per-capture provenance, coverage spans, speaker map, mistranscription glosses) as prose, and it is not reformatted to match this block: a reformat of a sensitive verbatim transcript's header risks silently dropping a coverage caveat or a gloss for zero gain. The block below is an **illustrative** re-expression showing the invariants a new master must carry, extending the plaud/ speaker-tagging header ([canonical example](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/2026-04-19_matt-macdermott-coefficient-giving-controlconf.md)); prose that carries the same invariants is equally valid.

```markdown
# <YYYY-MM-DD> <Title>

**Date:** <weekday, Month D, YYYY>
**Time:** <time / duration>
**Location / event:** <if any>
**Participants:** <full names, roles where useful>
**Language:** <if not English>
**Context:** <one-line, sourced>

## Sources
| Capture | Supplied | Coverage | Authoritative for |
|---|---|---|---|
| SuperWhisper (pasted by Scott <date>) | words | 00:02:49–02:02:37 | wording |
| Plaud raw (preserved in commit `<sha>`) | speaker labels, timestamps | full | diarization, times |
| [Gemini](<GitHub URL>) | summary, action items | end-time only | summary panel |

**Speaker map:** Speaker 2 = <Name>; Speaker 3 = <Name>
**Summary (source: <Gemini auto-notes / Plaud panel>):** <3-5 bullets, extracted, never mixed into the verbatim body>
**Action items (source: <...>):** <list, or "none">
**Merge notes:** built <date> by <Claude / Scott>. Bracketed italic lines in the body are merge annotations, not speech. <Coverage-gap or crosstalk caveats.>
```

Rules that keep the block honest:

- **Per-field provenance is explicit** so any part of the body traces to its capture in one hop (cite-primary-sources rule). "Authoritative for" is the tiebreak when two captures cover the same field.
- **Summary and actions live in the header, never inline** (extracted from Gemini auto-notes or Plaud's JSON panel, gap 4). The verbatim body stays verbatim.
- **Coverage spans are recorded** where a capture does not cover the whole conversation, so gap-filled passages are marked, not silently blended.
- Verify wording against the authoritative capture, not the noisiest one; leave Scott-recognizable mistranscriptions in place with an inline gloss rather than silently "correcting."

## Merge procedure (reference checklist)

1. Content-grep every capture for the conversation (date + participant across `plaud/ gemini/ otter/ local-whisper/ claude/`; auto-titles are topic-based, so grep content, not filenames).
2. One capture → resolve in place per WORKFLOW.md, stop. More than one → continue.
3. Pick best capture per field: words = SuperWhisper › Otter › Plaud; names = Gemini invitees / Otter / Plaud web-UI; times = Plaud / Otter; summary = Gemini / Plaud panel.
4. Assemble the body; overlay names + timestamps; mark coverage gaps and crosstalk with bracketed-italic annotations.
5. Write the header block, including the Sources table and extracted summary/actions.
6. Banner any live source files (conditional rule above).
7. Place as `_merged/<YYYY-MM-DD>_<slug>.md`; log the merge in the session CSV.

**When two captures conflict and context does not decide, cut the clip.** Precedence rules and surrounding-turn reasoning both run out on the hard cases: on the [2026-04-14 Trajectory call](https://github.com/scottwofford/sw-prv/blob/main/transcripts/_merged/2026-04-14_trajectory-labs_sami-jawhar.md), one capture had Jai saying a method *was* a good proxy for Luthien's value and the other had him saying it *wasn't*, and both readings fit the turns on either side. Do not guess and do not silently pick the higher-precedence source. Locate the phrase in the SuperWhisper `meta.json` `segments` array (word-level start/end times), cut ~12 seconds around it with `ffmpeg`, and put it in front of Scott as a local HTML page with the audio inlined as a base64 `data:` URI plus the competing readings and the adjacent turns. Fifteen seconds of his ear beats any amount of model arbitration, and the original `output.wav` survives in `~/Documents/superwhisper/recordings/<id>/` for exactly this. Keep the page local; never publish call audio.

## Stage 4: reachability (ships in the build)

The repo is invisible to Claude mobile, and the shipped pipeline in [`plaud/WORKFLOW.md`](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/WORKFLOW.md#dataflow-the-pipeline) says a transcript is done only once every surface can load it. Every authoritative transcript (merged master, or best single-capture file where no merge exists) mirrors to Drive by default; Scott confirmed 2026-07-11 (*"mirror merged or best transcript to drive makes sense to me"*). Requirements: [T3 (reachability)](https://github.com/scottwofford/sw-prv/blob/main/requirements/transcript-system-req.md), [T5 (mirror contract)](https://github.com/scottwofford/sw-prv/blob/main/requirements/transcript-system-req.md), [T6 (privacy/ownership)](https://github.com/scottwofford/sw-prv/blob/main/requirements/transcript-system-req.md). The binding constraints:

- **Personal account only.** The mirror Doc and its Drive folder are owned by `scottwofford3@gmail.com` via the personal token, never the Luthien identity. Another personal mirror script authenticates as `scott@luthienresearch.org`; copying it literally would put the most personal content in this repo under the org account. Copy the Context-mirror pattern (`woffieta-data/regenerate_context_mirror.py`, personal-account-owned) instead.
- **Mirror-by-default, opt-out flag.** No per-file ask (it would violate T1 zero-thought); Scott can mark any file no-mirror at any time and the renderer respects it on every regeneration.
- **The repo master is the only edit surface.** The mirror Doc opens with a "generated from the repo master on <date>; do not edit here, edits are overwritten" line, because a mobile edit to the Doc is silently clobbered on the next regeneration (the same clobber failure mode `connector-quirks.md` documents).
- **Drive folder name stays distinct from the repo folder** (`Transcript Masters`, never `_merged`) so a Drive object never reads as the same thing as the repo folder.
- The renderer script is written **before** the first mirror (a manual copy is a fork, not a mirror; it diverges the moment the master is edited). Cheap to write: copy the Context-mirror pattern.
- Mirror freshness is checked by the scheduled ingest pass (T8), which closes the drift risk an earlier mirror precedent demonstrated (its companion doc lagged its data by two weeks with no git trace of the last regeneration).

## Stage 2 note: Drive raw staging (done, 2026-07-12)

New Plaud auto-drops land in [Drive `2.2 Transcripts/Plaud raw/`](https://drive.google.com/drive/folders/1KXmNaAo7a2IFS00HjW86saPxRWogxPte). Scott reorganized the Drive on 2026-07-12: the old `2.2 Plaud` folder was renamed to `Plaud raw` and moved under a new `2.2 Transcripts` parent (alongside `Transcript Masters` and the Chrome-export archive). The rename kept the folder's ID, so the Plaud→Drive Zap's ID-based destination still resolves to it (verified: a test file landed in parent `1KXmNaAo7a2...`, the same ID as the old folder). The disk-path references (CLAUDE.md, WORKFLOW.md, this repo's docs) were repointed to `2.2 Transcripts/Plaud raw/` in the same pass, so the corpus does not read as split. This supersedes the earlier parked `_raw/` subfolder idea (a whole-folder rename achieved the same staging hygiene).

## Model economics: Fable vs Opus, and cross-session handoff

Fable 5 is both smarter and scarcer / more usage-intensive than Opus (~15% Fable budget left as of 2026-07-11); Opus is the capable workhorse.

**Fable was spent where it changes the answer (already done for this objective):** the two `/devil` red-team gates and the design-revision judgment. **Everything remaining is Opus:** the migration commit, README/WORKFLOW updates, and future mechanical merges. Re-engage Fable only on a genuinely ambiguous future call: a subtle high-stakes merge (heavy crosstalk, ambiguous diarization, high-value conversation) or the privacy call on mirroring a personal transcript.

Rule of thumb: Fable when a wrong call is expensive to reverse or needs subtle judgment; Opus for everything mechanical.

**Cross-session context handoff.** The repo is the shared memory, not any model's session context. A fresh session (either model) picks up cold by reading, in order: [`objective.md`](https://github.com/scottwofford/sw-prv/blob/main/objective.md) → this doc → the latest [session log](https://github.com/scottwofford/sw-prv/tree/main/session-logs). Keep objective.md's pointer current, keep this doc rewritten to current state, and log each merge.

## Revision history

| Date | Change |
|---|---|
| 2026-07-11 | Initial design proposal (Step 1). Pre-red-team. |
| 2026-07-11 | Revised after the Step-2 `/devil` red-team: cut to a minimal core (folder + exemplar migration + naming + Sources-table citation) with explicit triggers for the deferred rest; split test recast from folder-count to capture-count (the exemplar failed the old test); source→master banner demoted to conditional (the exemplar's captures are a paste + a git commit, nothing to banner); stage-4 mirror deferred behind a felt-mobile-need trigger with personal-account-only + privacy-crossing + do-not-edit-here constraints; `_raw/` repoint parked as an atomic bundle; exemplar migration gains a fix-live-inbound-links substep; `_merged/` vs `masters/` folder name flagged as a Scott decision. |
| 2026-07-11 | Step-4 `/devil` (plan red-team) amendment: the exemplar's prose header is canonical and is never reformatted to the schema table; the table is illustrative only. |
| 2026-07-11 | Reconciled to Scott's evening no-deferral overrule + the new [transcript-system requirements](https://github.com/scottwofford/sw-prv/blob/main/requirements/transcript-system-req.md): full build (mirror ships, schema/checklist binding, scheduled ingest + health report, backlog sweep, redaction runbook); mirror-by-default with opt-out flag replaces both the felt-need trigger and any per-file privacy ask. |
