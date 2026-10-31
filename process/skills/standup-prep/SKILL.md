---
name: standup-prep
description: Prep Scott's standup updates for either or both of his standups, each written for its own audience - the Control Tower Standup (Henri's 9:30am PT meeting with the EquiStamp and Redwood team, prepped in his "standup Scott's raw notes" Google Doc) and the Luthien async standup (daily thread in the Luthien Slack channel, plus the Friday weekly). Use when Scott says "prep for standup", "ct standup", "luthien standup", "standup raw", "help me fill out standup", "what should I ask in standup", "summarize what I worked on since last standup", "standup update", or asks to open today's standup template.
---

> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/skills/standup-prep/SKILL.md (private). This copy is a redacted mirror and may lag behind it.

# Standup prep

Requirements and the retro behind them: [requirements.md](https://github.com/scottwofford/sw-prv/blob/main/skills/standup-prep/requirements.md). **Scott's past entries are the source of truth for what good looks like**; when this file and those entries disagree, match the entries.

Scott sits on two teams with separate standups ([access tiers](https://github.com/LuthienResearch/luthien-contributors/blob/main/README.md#who-can-see-what-access-tiers)). Each standup gets its own update, written for its own audience. "Prep for standup" with no team named means both, as two separate blocks.

| | Control Tower Standup | Luthien standup |
|---|---|---|
| When | 9:30am PT weekdays, live (Henri runs it) | Async daily thread in Slack; live Friday weekly |
| Where Scott preps | [standup Scott's raw notes](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit) (owner scottwofford3@gmail.com; Chrome profile `Default`; edit only via skill `google-docs-editing`, personal token) | Luthien Slack channel `C0C47248JF7` (Seattle AI Safety workspace; the luthien-agent bot posts the 8am thread when it's running). Scott posts; Claude only drafts. |
| Audience | Henri, Miguel, Shaheen, Tomas, Odelya, Adam and other EquiStamp/Redwood folks | Luthien core team: Allister, Matt, Jesse, Byron, Hernan |
| They know | Control Tower, Inspect, Meridian, JJ, Tyler, Hawk, PR and Linear numbers | Luthien internals: the Coefficient Giving application, funders, hiring, EAG contacts, project briefs |
| They don't know | Luthien internals | Control Tower internals: PR and Linear numbers, who Henri or Miguel are, Redwood process |
| Headings | Follow-ups / reactions · Last 24 hours · Next 24 hours · Blockers and/or discussion topics | What did you do? · What's next, and for which weekly goal? · What are you blocked on? |

Requests arrive between 9:10 and 9:35, often after the Control Tower meeting has started. Speed beats completeness: first bullets in the first response, gap check after. When both are asked for, deliver Control Tower first (it's live).

## Steps

1. **Big picture (writing process, one line per standup, no hold point).** Name the audience and the goal: tell them what Scott did and will do on *their* work, and get answers from named people.
2. **Gather once, for both** (run in parallel):
   - The previous entry for each standup: the last dated block in the doc, and Scott's last thread in the Luthien channel. Its Next becomes today's Last; open blockers carry over as "(still open from <date>)".
   - Both calendars since the last standup, and today's meetings until the next one.
   - Scott's PRs and Linear issues touched since then, **with draft/ready/merged status from `gh` / Linear, never from memory**, including PRs opened by the Claude app.
   - Sent mail in all three accounts, and Slack/Beeper threads with each team.
   - The latest relevant planning transcript (Plaud / meeting-transcripts / Luthien check-ins) is the ground truth for Scott's plan. Do not challenge its premise.
   - The last standup's transcript or takeaways, to pre-answer questions so only real asks remain.
   - Luthien weekly goals: the latest Friday weekly or the goals posted in the Luthien channel.
3. **Sort each item by team.** Control Tower work goes in the Control Tower update; Luthien work goes in the Luthien update. An item that matters to both appears in both, written differently. Work for neither team stays out.
4. **Write in Scott's style** (examples in requirements.md):
   - Last / Next (or did / next): 1 to 3 terse fragments each; "→" marks a result or hand-off ("Tyler meeting → docs"). No links in the Control Tower Last/Next.
   - Blockers: 0 to 6 items; each starts with the person it's for ("Henri: ..."), links the PR, issue or doc, and ends in a question.
   - No dashes of any kind in standup text: no em or en dashes, and no hyphenated words ("quick start", "red teaming", "check in"). Keep "→".
   - Don't repeat yourself: drop any Last item Scott already reported in an earlier block, including the same work under a different name (the people.md link he gave Oct 27 is the org chart update merged that day).
   - Next comes from Scott's stated priorities (the latest planning transcript, sync commitments he owns), not from Gemini auto-generated action items.
   - Blockers are only asks Scott himself would raise: addressed to people who attend this standup (Tyler doesn't), about things Scott can explain in one breath. Never ask reviewers about Scott's own draft PRs, and never resurface another person's action item from a meeting's notes as Scott's blocker. When nothing qualifies, leave the empty bullet.
   - Control Tower only: leave Follow-ups / reactions empty; Scott fills it live.
   - Luthien only: tag each Next item with its weekly goal; if no goal fits or none is posted, write "(goal?)" and raise it in the gap check.
5. **Translate for the audience.** Use the table's "don't know" row: reduce the other team's internals to a short label ("Luthien funding work", "Control Tower docs work") or say what it means for this team. Spell out an outsider's role once ("Tom Clarke (Faculty AI Safety & Security lead)"). **Cross-team rule:** nothing from one team's private spaces (Redwood Slack, meeting-transcripts, luthien-org, Luthien Slack) goes into the other team's update beyond Scott's own work in plain terms, unless Scott approves; flag anything borderline in the gap check. Never put NDA or personal items in anything a team reads.
6. **Deliver in chat**, one block per standup with its own headings, plus a 1 to 3 item gap check per block ("what am I missing": stale items already done, a commitment missing from Next, a vague blocker, a missing weekly goal). The Luthien block is ready to paste into Slack; Scott sends it. Keep everything else out of the reply.
7. **Control Tower doc edits only on request.** "Fill out", "add" or "open the template" authorize writing. Before writing, re-read the top of the doc: if today's heading exists, use it; if Scott is typing in that section, show the text in chat and stop ([R1 active-drafting rule](https://github.com/scottwofford/sw-prv/blob/main/requirements/personal/scott-response-req.md#r1-maximize-scotts-leverage-the-unit-of-impact-is-scotts-preferences-realized-not-generic-helpfulness)). A new day block goes at the top: Heading 4 `Oct 21` (no weekday or year), then the four headings below as bullets, each with one empty nested bullet. Never leave content under a `Date template` heading. Then open the doc in Chrome profile `Default` and give Scott the URL (a `#heading=` link when the heading has an id).

## Control Tower template (exact text)

- Follow-ups / reactions to what people said live during standup
- Last 24 hours/since last standup
- Next 24 hours/until next standup
- Blockers and/or discussion topics
