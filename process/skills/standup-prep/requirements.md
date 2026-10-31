> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/skills/standup-prep/requirements.md (private). This copy is a redacted mirror and may lag behind it.

# Standup prep: requirements

Skill: [SKILL.md](https://github.com/scottwofford/sw-prv/blob/main/skills/standup-prep/SKILL.md). Built 2026-10-21 from a retro on 15 Claude Code prep sessions (Aug 28 to Oct 21, 2026), every dated entry in [standup Scott's raw notes](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit), and the Oct 2, 7, 13, 14, 15 and 20 standup transcripts in `rdwrs/meeting-transcripts/3-transcripts/`.

## Requirements

Format: the [luthien-org requirements standard](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/2-versions-requirements/README.md).

| # | Requirement (problem only) | Current state as of 2026-10-31 | Key evidence |
|---|---|---|---|
| R1 | <u>Written for the room.</u> When I give an update, the people in that meeting understand it without knowing my other team's context. | Step 1 names the audience; the table lists what each audience doesn't know; step 5 translates. | Scott, 2026-10-21: "audience is ct standup, so they don't know what is cg application so gimme bullets tailored to my audience." |
| R2 | <u>Looks like mine.</u> My update matches the style of my past entries for that meeting. | SKILL.md links each meeting's doc and example tabs as the format source. | Scott, 2026-10-21: "use past standup raw dates as the source of truth and examples of what good looks like." |
| R3 | <u>Concise and linked.</u> I can read my update in seconds and click through to anything in it. | Step 4: 1 to 3 linked fragments; the sync is numbered with links throughout. | Scott: "too verbose" (Aug 28); "number them and be way more concise, and make liberal use of links" (Oct 12); "just the 3 bullets with concise descriptions of each PR" (Oct 13); "w/ links (high info density)" (Oct 20). |
| R4 | <u>Correct status.</u> Every status I report (PR draft or ready, merged, done) is true at the time I report it. | Step 2 reads status from `gh` and Linear, including PRs opened by the Claude app. | "2257 is in draft, not open for review" (Oct 5); "114 is draft... idk how u missed that?" (Oct 8); Claude-app PRs missed (Oct 12). |
| R5 | <u>My plan, not a new one.</u> My Next items reflect the priorities I already set, without my premise being challenged. | Step 2 treats the latest planning transcript as ground truth; step 4 takes Next from it, not from Gemini action items. | Scott, 2026-10-21: "dude, I'm in charge, don't challenge my premise... treat that as the plan and ground truth." |
| R6 | <u>Only real asks.</u> The questions I raise are ones nobody has already answered and that I would raise myself. | Step 2 reads the last meeting's transcript to pre-answer; step 4 limits asks to attendees and never routes them through Tyler. | Scott, Oct 13: "read past standup transcripts to see if you can figure out the answer to these questions yourself"; Oct 5: "shop asking tyler shit!!" |
| R7 | <u>My doc stays mine.</u> Nothing gets written into my doc unless I ask, and never into a section I'm typing in. | Step 7: writes only on request, re-reads first, stops if Scott is drafting. | Oct 2 and Oct 12 stops; [COE-2026-09-21](https://github.com/scottwofford/sw-prv/blob/main/coes/COE-2026-09-21-active-google-doc-drafting.md). |
| R8 | <u>Nothing private leaks.</u> Nothing from one team's private spaces, and nothing under NDA or personal, appears in another team's update. | Step 5 cross-team rule; borderline items go to the gap check. | Scott, Oct 8: "don't propose to send nda stuff in dev channel!"; [access tiers](https://github.com/LuthienResearch/luthien-contributors/blob/main/README.md#who-can-see-what-access-levels). |
| R9 | <u>One ask, any meeting.</u> I can prep any of my recurring team meetings the same way, each update separate and written for its own team. | One meeting-agnostic skill; "prep for standup" is read from the current day, time and upcoming or ongoing meetings. | Scott, 2026-10-21: "make standup prep skill generic so it can be used in either standup and prepare for both seperately"; 2026-10-31: "make the skill agnostic." |
| R10 | <u>Recent, real attendees.</u> My sync update covers only the recent past and the people who actually came, with no assumptions about when a meeting happens. | Sync: last 7 days only; attendees checked against transcripts; schedule from the calendar event. | Scott, Oct 26: "only include stuff in the past 7 days"; "look at red-team transcript to see who actually attended"; 2026-10-31: meeting cadence is ad hoc, so the skill assumes none. |

## Examples of good

In the [raw notes doc](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit): [Oct 13: blockers](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit?tab=t.0#heading=h.z6ksad4826cq) · [Oct 1: outsider role spelled out](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit?tab=t.0#heading=h.ululegpwlqqh) · [Oct 20: follow-ups filled live](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit?tab=t.0#heading=h.kbtrq8ma8jjp) · [Oct 21: other team's work in this team's terms](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit?tab=t.0#heading=h.fq9x101lg1vz)

## Retro findings

- **Worked:** reading the previous entry and takeaways; PR and Linear status with links; Sent-mail checks on commitments; leaving out work that isn't for this team (Oct 2); a short "what am I missing" list (Sep 28 caught a done task, a missing commitment and a vague blocker).
- **Failed:** couldn't find the doc and opened the wrong one (Sep 3); wrong PR status (Oct 5, Oct 8); missed Claude-app PRs and couldn't read the -dev Slack channel (Oct 12); an EAG meeting count of 58 from the calendar instead of about 50 from Swapcard (Oct 20); challenged Scott's plan instead of reading it (Oct 21); off-topic asides padded replies.
- **Live vs prepped:** Scott speaks Last/Next nearly verbatim and adds context live; Blockers drive the discussion (about 15 minutes on Oct 20). He sometimes pastes into a Slack standup thread.
- **Doc hygiene:** Scott copies the template block and often leaves it titled `Date template`, so headings don't reliably date the content; the skill writes a real date heading.

## Revision history

| Date | Change |
|---|---|
| 2026-10-21 | Created from retro |
| 2026-10-21 | Renamed from ct-standup-prep; covers the Luthien standup too, one update per audience |
| 2026-10-31 | Requirements recast in the luthien-org requirements table format; the speed requirement dropped; examples are links to the doc's headings, not copies. Meeting-agnostic: no Luthien standup specifics (it is ad hoc); "prep for standup" read from context. Covers the Control Tooling Sync; no assumed cadence; team names and schedule come from the calendar event; the prep docs are linked instead of described |
