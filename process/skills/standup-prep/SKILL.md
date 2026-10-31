---
name: standup-prep
description: Prep Scott's update for any recurring team meeting, written for that meeting's audience - for example the Control Tower Standup (prepped in his "standup Scott's raw notes" Google Doc) or the Control Tooling Sync (prepped in its agenda doc). Use when Scott says "prep for standup", "ct standup", "standup raw", "help me fill out standup", "what should I ask in standup", "summarize what I worked on since last standup", "standup update", "prep for control tooling sync", "update my bullets in the sync doc", "agenda for the sync", or asks to open today's standup template.
---

> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/skills/standup-prep/SKILL.md (private). This copy is a redacted mirror and may lag behind it.

# Recurring-meeting prep

Requirements and the retro behind them: [requirements.md](https://github.com/scottwofford/sw-prv/blob/main/skills/standup-prep/requirements.md). **Scott's past entries are the source of truth for format**; when this file and those entries disagree, match the entries.

Each meeting gets its own update, written for its own audience ([access tiers](https://github.com/LuthienResearch/luthien-contributors/blob/main/README.md#who-can-see-what-access-levels)). "Prep for standup" should be interpreted contextually, based on the current day and time and upcoming or ongoing meetings. Schedule, host and attendees come from the calendar event; never assume them.

| Meeting | Where Scott preps | Audience doesn't know |
|---|---|---|
| Control Tower Standup | [standup Scott's raw notes](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit) (scottwofford3@gmail.com: Chrome profile `Default`, personal token) | Luthien internals |
| Control Tooling Sync | Newest tab of the [Control Tooling Sync agenda doc](https://docs.google.com/document/d/1QzawH8tf3PuLQJ6QWT6JcSthf6BRIPbCKqCSKrqHxpg/edit) (scott@luthienresearch.org: Chrome profile `Profile 1`, Luthien token). Format: [Oct 12 tab](https://docs.google.com/document/d/1QzawH8tf3PuLQJ6QWT6JcSthf6BRIPbCKqCSKrqHxpg/edit?tab=t.2a1hj7mtfs45), [Oct 26 tab](https://docs.google.com/document/d/1QzawH8tf3PuLQJ6QWT6JcSthf6BRIPbCKqCSKrqHxpg/edit?tab=t.j12xjvqkim6c); agenda vs discussion topics per [call-agendas Stage 3](https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/CLAUDE.md#stage-3--write-the-prep-doc-before-the-call) | Luthien internals |

Requests often arrive minutes before or after the meeting starts.

## Steps

0. **Control Tower Standup: first, before anything else, give Scott a section to draft in.** Copy the [template](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit?tab=t.0#heading=h.9n80tyvpa3d6) to a new section titled with today's date (Heading 4, like `Oct 21`) at the top of the doc, unless today's section already exists, then open it in Chrome profile `Default`. Scott drafts there live while Claude does the full sweep below; from then on that section is his, so Claude's bullets go in chat.
1. **Big picture ([writing process](https://github.com/scottwofford/sw-prv/blob/main/requirements/personal/scott-writing-process.md), one line per meeting, no hold point).** Name the audience and the goal: what Scott did and will do on *their* work, and the answers he needs from named people. If Scott states a goal for the meeting, that is the goal.
2. **Gather since the last meeting** (in parallel):
   - Scott's previous entry for this meeting. Its Next becomes today's Last; open blockers carry over as "(still open from <date>)". For the sync, also the last [debrief](https://github.com/LuthienResearch/luthien-org/tree/main/call-agendas-and-notes/call-prep-agendas-debriefs/control-tooling-sync) and its open actions.
   - The last meeting's transcript or takeaways, to pre-answer questions so only real asks remain.
   - Both calendars since then, and Scott's meetings with attendees in between (their debriefs and transcripts; check who actually attended).
   - Scott's PRs and Linear issues, **with draft/ready/merged status from `gh` / Linear, never from memory**, including PRs opened by the Claude app.
   - Sent mail in all three accounts, and Slack/Beeper threads with the attendees.
   - The latest planning transcript is the ground truth for Scott's plan. Do not challenge its premise.
   - Any specific question Scott asked: answer it first, with links.
3. **Sort each item by meeting.** An item that matters to two meetings appears in both, written differently. Work for neither stays out.
4. **Write in Scott's style** (examples: requirements.md and the docs above):
   - Last / Next: 1 to 3 terse fragments each, linked; "→" marks a result or hand-off. The sync: numbered, links throughout, last 7 days only.
   - Asks and blockers: 0 to 6; each starts with the person it's for ("Henri: ..."), links the PR, issue or doc, and ends in a question. Only asks Scott himself would raise, to people who attend. Never route asks through Tyler ([rule](https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/CLAUDE.md#no-speculative-action-items)), and quote him only from a transcript or his own text. Never ask reviewers about Scott's own draft PRs, and never resurface someone else's action item as Scott's blocker. When nothing qualifies, leave the empty bullet.
   - No dashes of any kind: no em or en dashes, and no hyphenated words ("quick start", "check in"). Keep "→".
   - Don't repeat yourself: drop anything Scott already reported, including the same work under a different name.
   - Next comes from Scott's stated priorities, not from Gemini auto-generated action items.
   - Control Tower Standup: leave Follow-ups / reactions empty; Scott fills it live.
5. **Translate for the audience.** Reduce another team's internals to a short label or what it means for this audience. Spell out an outsider's role once. Nothing from one team's private spaces goes into another team's update beyond Scott's own work in plain terms, unless Scott approves; flag anything borderline in the gap check. Never put NDA or personal items in anything a team reads.
6. **Deliver in chat**, one block per meeting, plus a 1 to 3 item gap check per block ("what am I missing"). Scott sends; Claude only drafts.
7. **Other doc edits only on request.** Beyond step 0, "fill out", "add", "update my bullets" or "open the template" authorize writing. Re-read the doc first: if Scott is typing in that section, show the text in chat and stop ([R1 active-drafting rule](https://github.com/scottwofford/sw-prv/blob/main/requirements/personal/scott-response-req.md#r1-maximize-scotts-leverage-the-unit-of-impact-is-scotts-preferences-realized-not-generic-helpfulness)). Use native Google Docs lists via skill `google-docs-editing`, with the token in the table. Then open the doc in its Chrome profile and give Scott the URL.
   - Control Tower: write only into today's section from step 0, and only where Scott hasn't typed. Never leave content under a `Date template` heading. Never leave content under a `Date template` heading.
   - Control Tooling Sync: write in the newest tab, or create the tab when Scott asks.
