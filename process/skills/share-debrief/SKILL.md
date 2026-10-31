---
name: share-debrief
description: Publish a meeting debrief to Luthien collaborators in Slack (or any Beeper-connected chat) as a draft Scott edits and sends. Use when Scott says to share, post, or publish a debrief or readout to a channel (#scott-notes, #linuxarena-devs, a DM), or asks which channels a debrief should go to.
---

> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/skills/share-debrief/SKILL.md (private). This copy is a redacted mirror and may lag behind it.

# Share a debrief

Design and rationale: [debrief publishing design](https://github.com/LuthienResearch/luthien-org/blob/main/process/debrief-publishing-design.md). Tool: [`scripts/publish-debrief.py`](https://github.com/scottwofford/sw-prv/blob/main/scripts/publish-debrief.py). Works from any agent with a shell; Beeper Desktop must be running.

**The agent never sends.** The script only prefills a draft. Scott edits and presses Send.

## Steps

1. **Start from the final debrief.** It lives in its routed home (luthien-org or meeting-transcripts); personal topics are never published. One version for all audiences: apply the meeting-transcripts [redaction rule](https://github.com/linuxarena/meeting-transcripts/blob/main/README.md#requirements) and nothing else. Leave out anything Scott marks private, such as post-call Slack threads.
2. **Pick channels.** List the targets (`--targets`) and propose the audiences the meeting involved; Scott approves or changes them.
3. **Build the post** and show it to Scott in chat:
   `uv run python publish-debrief.py --build <debrief.md> /tmp/post.txt`
   It carries the title, takeaway headlines, action items, and one link. **Match links to the channel's readers** ([COE 2026-10-06](https://github.com/LuthienResearch/luthien-org/blob/main/process/coes/2026-10-06-private-repo-links-in-shared-docs.md)): most channel members can't open private repos (`luthien-org`, `meeting-transcripts`), so by default the script drops private-repo URLs (keeping the link text) and links the debrief's Notes by Gemini doc instead, or a doc you pass with `--share-link`. Pass `--private-ok` only when every member of the target channel has access to that repo (e.g. Redwood and EquiStamp people for `meeting-transcripts`). If you link a Google Doc, check it is shared with the channel. If Scott edits wording, apply it to the debrief file too, so there is one version.
4. **Draft into each channel:** `uv run python publish-debrief.py <target> /tmp/post.txt --agent <your name>`. The result "prefilled, not verified" is expected: Beeper's API cannot confirm the draft box. A second prefill into the same chat replaces the text in the message box.
5. **Scott edits and sends.** If he wants a short post instead (for example a doc link), that is his call.
6. **Confirm and record.** Run `--check <target>` to find Scott's post, then add `· **Shared:** <channel>, <date>` to the debrief's header line. Report anything still unsent in the same session; no separate reminders.

## Adding a target

Find the chat ID with Beeper's API (`GET /v1/chats/search?query=<name>&accountIDs=<account>`) and add an entry to `TARGETS` with its account ID, which the pre-write workspace check verifies. Beeper Plus allows 3 Slack accounts; all 3 are used (Redwood, Neolithic, BlueDot) as of 2026-09-28. Test with the matching `*-self` DM target first.

## Formatting

Beeper prefills plain text: line breaks and "1." / "-" lists survive; links render as "text (URL)"; bold markers are dropped.
