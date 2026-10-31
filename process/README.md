# Process docs

> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy.

Scott's working process for meetings, transcripts, standups and Claude behavior, published so contributors can read and reuse it. Scott's full Claude Code configuration (CLAUDE.md) is published separately at [scottwofford.com](https://scottwofford.com/building/claude-code-config.html).

These are generated copies of private files, with a small set of cuts (personal life, pay and funding amounts, performance management, NDA material, things shared in confidence, and secrets). Links into private repos (`sw-prv`, `luthien-org`, `meeting-transcripts`) are kept to show the structure; they 404 for anyone without access, by design. The `.json` files can't carry a header comment, so this index is their generated-copy notice.

- [`transcripts/plaud/WORKFLOW.md`](transcripts/plaud/WORKFLOW.md): How call recordings (Plaud, Gemini, Otter) become authoritative transcripts: capture paths, pipeline, ingest pass, gotchas.
- [`transcripts/README.md`](transcripts/README.md): Transcript storage layout, combining multiple captures of one call, naming, and the deletion/redaction runbook.
- [`transcripts/_merged/README.md`](transcripts/_merged/README.md): Rules for merged masters that reconcile more than one capture of a conversation: header schema and merge checklist.
- [`requirements/scott-response-req.md`](requirements/scott-response-req.md): Full bodies of Scott's 14 response requirements (R1-R14) and tenets; the one-line index is on scottwofford.com.
- [`requirements/cross-surface-context-mgmt-req.md`](requirements/cross-surface-context-mgmt-req.md): Cross-surface context requirements (continuity, verify before asserting, loaded-context introspection) and the surface capability matrix.
- [`call-agendas-and-notes/call-lifecycle-rules.md`](call-agendas-and-notes/call-lifecycle-rules.md): Behavior rules for the call lifecycle: meeting home, prep docs, raw notes, debriefs, action items. Renamed from CLAUDE.md so no agent auto-loads it here.
- [`call-agendas-and-notes/README.md`](call-agendas-and-notes/README.md): Format reference for call prep and debriefs: folder layout, filenames, debrief sections.
- [`call-agendas-and-notes/agenda-style-corpus.md`](call-agendas-and-notes/agenda-style-corpus.md): Agenda and discussion-topics format rules and authorship heuristics (the verbatim example entries stay private).
- [`meeting-notes-conventions.md`](meeting-notes-conventions.md): Standard structure for Luthien meeting notes: key takeaways, action items, transcript sources.
- [`debrief-publishing-design.md`](debrief-publishing-design.md): How debriefs reach collaborators in Slack as drafts Scott sends (Beeper prefill script).
- [`skills/share-debrief/SKILL.md`](skills/share-debrief/SKILL.md): Skill: publish a debrief to Slack as a prefilled draft.
- [`skills/standup-prep/SKILL.md`](skills/standup-prep/SKILL.md): Skill: prep Scott's two standup updates, each for its own audience.
- [`skills/standup-prep/requirements.md`](skills/standup-prep/requirements.md): Requirements and retro behind the standup-prep skill.
- [`skills/trello-conventions/SKILL.md`](skills/trello-conventions/SKILL.md): Skill: Trello conventions (ownership, ETAs, search before creating, prioritization).
- [`skills/scotts-writing-process/SKILL.md`](skills/scotts-writing-process/SKILL.md): Skill: Scott's five-step writing process for text he sends under his name.
- [`skills/gmail-search-heuristics/SKILL.md`](skills/gmail-search-heuristics/SKILL.md): Skill: search order for finding past email with a counterparty.
- [`skills/calendar-conventions/SKILL.md`](skills/calendar-conventions/SKILL.md): Skill: calendar conventions (both calendars, free/busy flags, self-only events).
- [`skills/google-docs-editing/SKILL.md`](skills/google-docs-editing/SKILL.md): Skill: editing Google Docs and Sheets with python, token handling, in-place edits.
- [`transcripts/plaud_reconcile.py`](transcripts/plaud_reconcile.py): Script: nightly gap filler that uploads Plaud recordings the Zapier mirror missed.
- [`transcripts/regenerate_mirrors.py`](transcripts/regenerate_mirrors.py): Script: renders each authoritative transcript to a Google Doc mirror.
- [`transcripts/ingest_cron.hardened.sh`](transcripts/ingest_cron.hardened.sh): Script: hardened, report-only unattended ingest pass with bash gates and a caged reviewer.
- [`transcripts/ingest-cron-settings.json`](transcripts/ingest-cron-settings.json): Settings (JSON, no header possible): deny list for the unattended ingest agent.
- [`transcripts/ingest-reviewer-settings.json`](transcripts/ingest-reviewer-settings.json): Settings (JSON, no header possible): deny list for the read-only reviewer.
- [`scripts/local-whisper/README.md`](scripts/local-whisper/README.md): Local Whisper transcription setup.
- [`scripts/local-whisper/clip_retranscribe.sh`](scripts/local-whisper/clip_retranscribe.sh): Script: re-transcribe a 30-60 second clip to settle a garbled passage.
- [`scripts/local-whisper/transcribe.sh`](scripts/local-whisper/transcribe.sh): Script: local Whisper transcription with optional diarization.
- [`scripts/local-whisper/transcribe_whisper.py`](scripts/local-whisper/transcribe_whisper.py): Script: Whisper runner used by transcribe.sh.
