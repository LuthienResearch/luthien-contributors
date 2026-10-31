> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/LuthienResearch/luthien-org/blob/main/process/debrief-publishing-design.md (private). This copy is a redacted mirror and may lag behind it.

# Debrief publishing design

Extends the [relationship context architecture](https://github.com/LuthienResearch/luthien-org/blob/main/process/relationship-context-architecture.md): that doc says where debriefs live; this one says how they reach Luthien collaborators in Slack. Procedure: the [`share-debrief` skill](https://github.com/scottwofford/sw-prv/blob/main/skills/share-debrief/SKILL.md). Tool: [`publish-debrief.py`](https://github.com/scottwofford/sw-prv/blob/main/scripts/publish-debrief.py).

## Use case

Scott's meetings are debriefed and saved in the home the [meeting routing rule](https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/CLAUDE.md#meeting-home) assigns: luthien-org by default, meeting-transcripts for Control Tower team meetings and graduated meetings. The debrief is then published to Luthien collaborators, paid and unpaid, in the Slack channels where they already are, for example the Control Tower team in Redwood's `#linuxarena-devs` and Neolithic in `#scott-notes`. Personal topics (kept in sw-prv) are never published.

## Requirements

1. Agent-agnostic: Scott can run the flow with any agent he chooses. Nothing depends on one agent's tool permissions, hooks, or connectors.
2. The agent drafts; Scott edits and presses Send.
3. The draft is waiting in the chat's message box. No clipboard step.
4. The draft lands in the intended workspace and channel.
5. One debrief for all audiences; the full version stays in its repository.
6. Scott can find out whether a message went out without him pressing Send.

## Preferences

- Minimal manual effort per post.
- Free.
- One mechanism for every channel.
- Adding a future debrief takes one approval from Scott.
- No reminders outside the publishing flow.

## Constraints

- **Guests cannot install Slack apps.** In a workspace where Scott is a guest (Redwood: Multi-Channel Guest), no app can be installed. [Slack guest roles](https://slack.com/help/articles/202518103-Understand-guest-roles-in-Slack)
- **Slack's public Web API has no drafts method.** A personal app can post or schedule, but not create a composer draft. API-scheduled messages do not appear in Slack's Scheduled list, so Scott cannot edit them there (tested 2026-09-26).
- **Beeper can prefill a draft in any chat it bridges** through its local API (`focus` with `draftText`, plain text), signed in as Scott, with no workspace approval. Beeper Plus, which Scott has, allows 3 Slack accounts. [Beeper focus method](https://developers.beeper.com/desktop-api-reference/resources/$client/methods/focus)
- **Control Tower meetings are transparent by default.** Tyler (Aug 24): *"I would love it, Like if our Slack channel and all of our meetings were fully open to the public."* ([transcript](https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/call-transcripts-plaud/2026-08-24_tyler-scott.md)), codified as R3 in the [meeting-transcripts README](https://github.com/linuxarena/meeting-transcripts/blob/main/README.md#requirements), whose redaction rule governs exceptions. Content Scott marks private (for example post-call Slack threads) stays out.

## Design

**One mechanism: Beeper prefill, through one script.** Any agent runs `publish-debrief.py` from the shell. The script:

- builds the post from a debrief: title, takeaway headlines, action items, link to the full debrief (quotes stay in the file);
- checks that the target chat belongs to the expected Beeper account, and stops on a mismatch;
- opens the chat in Beeper with the post prefilled; it never sends;
- logs every draft to `~/Library/Logs/publish-debrief.log`;
- lists recent messages in a target (`--check`), so the agent can confirm Scott's post and record it.

Targets as of 2026-09-28: Redwood `#linuxarena-devs`, Neolithic `#scott-notes`, and a self-DM test target in Redwood, Neolithic, and BlueDot. Prefill tested in all three workspaces; plain text, so lists and line breaks survive, links become "text (URL)", and bold markers are dropped.

**Flow for each debrief** (details in the skill):

1. The debrief is final in its routed home.
2. The agent proposes channels; Scott approves or changes them.
3. The agent builds the post and shows it; Scott's wording changes go into the debrief too.
4. The agent prefills each channel; Scott edits and sends.
5. The agent confirms the post with `--check` and adds `Shared: <channel>, <date>` to the debrief. Anything unsent is reported in the same session.

## Revision history

| Date | Change |
|---|---|
| 2026-09-26 | First draft: official connector for full-member workspaces, Beeper for guest workspaces. |
| 2026-09-26 | After /devil review and Scott's decisions: agent-agnostic publish script; own app with scheduled messages replaces the official connector; debriefs published from their routed home, personal topics excluded; audience rule; unapproved-send section rewritten as what is and is not detectable. |
| 2026-09-26 | Scott's decisions on the second /devil review: reuse the existing Neolithic app; schedule 30 days out and surface pending items in the flow, not in separate reminders; Unverified Slack and Beeper behaviors moved into implementation tests. |
| 2026-09-26 | Tests: Beeper prefill works in Redwood and Neolithic. API-scheduled Slack messages do not appear in Slack's Scheduled list, so all publishing moved to Beeper (Scott is on Beeper Plus). |
| 2026-09-27 | Audience rule replaced with Tyler's transparency-by-default (R3): one debrief for all audiences, redact only for performance management, NDA, or on-call privacy requests. The earlier cross-audience-approval rule wrongly treated Control Tower meeting content as classified. |
| 2026-09-28 | Body rewritten to current state: one Beeper mechanism for all channels; share-debrief skill and publish-debrief.py build/check commands; scheduled-message path removed. |
