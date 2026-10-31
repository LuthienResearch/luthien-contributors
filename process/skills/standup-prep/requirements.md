> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/skills/standup-prep/requirements.md (private). This copy is a redacted mirror and may lag behind it.

# Standup prep: requirements

Skill: [SKILL.md](https://github.com/scottwofford/sw-prv/blob/main/skills/standup-prep/SKILL.md). Built 2026-10-21 from a retro on 15 Claude Code prep sessions (Aug 28 to Oct 21, 2026), every dated entry in [standup Scott's raw notes](https://docs.google.com/document/d/1uxHTW1vRd8bWG806BKt9Laoz3wroC89BEdgwEzxg-eo/edit), and the Oct 2, 7, 13, 14, 15 and 20 standup transcripts in `rdwrs/meeting-transcripts/3-transcripts/`.

## Requirements

1. **Audience first (Scott's writing process).** The reader is the Control Tower Standup, not Scott. Scott, 2026-10-21: "skill should be inspired by writing proces to keep in mind that audience is ct standup, so they don't know what is cg application so gimme bullets tailored to my audience."
2. **Past entries define good.** Scott, 2026-10-21: "use past standup raw dates as the source of truth and examples of what good looks like."
3. **Concise.** Scott: "too verbose" (Aug 28); "number them and be way more concise, and make liberal use of links" (Oct 12, Control Tooling Sync update); "it should be just the 3 bullets with concise descriptions of each PR" (Oct 13).
4. **Facts verified live.** PR status was wrong twice: "2257 is in draft, not open for review" (Oct 5); "114 is draft... idk how u missed that?" (Oct 8). PRs opened by the Claude app were missed (Oct 12).
5. **Scott's plan is ground truth.** Read his latest planning transcript before suggesting priorities; don't challenge the premise. Scott, 2026-10-21: "dude, I'm in charge, don't challenge my premise... treat that as the plan and ground truth."
6. **Pre-answer what tools can answer.** Scott, Oct 13: "also read past standup transcripts to see if you can figure out the answer to these questions yourself."
7. **Doc writes only on request**, never into a section Scott is typing in (Oct 2 and Oct 12 stops; [COE-2026-09-21](https://github.com/scottwofford/sw-prv/blob/main/coes/COE-2026-09-21-active-google-doc-drafting.md)).
8. **Fast.** Requests arrive 8:43 to 9:35am PT, mostly after 9:10 for a 9:30 meeting. No padding in the reply.
9. **Nothing private in team surfaces.** Scott, Oct 8: "don't propose to send nda stuff in dev channel!"
10. **One skill, both standups, separate updates per audience.** Scott, 2026-10-21: "make standup prep skill generic so it can be used in either standup and prepare for both seperately to consider the audience of my standup updates." Scott already shares his Control Tower updates with the Luthien team in Slack (Oct 20 thread "Scott's Standup Updates to ControlTower team"); the Luthien version should be rewritten for that team, not pasted, and must respect the cross-team rule in the [access tiers](https://github.com/LuthienResearch/luthien-contributors/blob/main/README.md#who-can-see-what-access-tiers).

## Examples of good (verbatim from the doc)

**Oct 13** (blockers style)
- Last 24 hours/since last standup
  - Meetings
  - Meridian email
- Next 24 hours/until next standup
  - Docs overhaul + Redwood website improvements
  - EAG NYC prep
- Blockers and/or discussion topics
  - Henri: docs can't deploy from main until the public settings are ported to the env API (LIN-1875); same failure turns the docs check red on #2407. ETA? Can the docs build skip unported settings?
  - Henri: leaderboard prod deploys off since #353, deliberate? Merge order #376 vs #383?
  - Marshall: control-tower-docs.redwoodresearch.org still doesn't resolve; #2293 is approved and only waiting on that DNS record
  - Blog post: who owns it, and does it wait until leaderboard prod deploys are back on?

**Oct 1** (outsider role spelled out)
- Blockers and/or discussion topics
  - GPU sandbox for ResearchArena: can our EC2 fleet run GPU instances, or another runner? Who owns?
  - Test-set flaw: fix the environment or leave it? Defer until the port lands?

**Oct 21** (Luthien-internal work in team terms)
- Last 24 hours/since last standup
  - Started a bunch of slack
  - Met open-source security eng → read report → forwarded to Miguel + posted in slack

**Oct 20, Luthien Slack** (Control Tower update shared with the Luthien team; verbatim excerpt)
- Next 24 hours/until next standup
  - Redwood Security Bot
  - EAG follow-ups. Build the cyber-eval collaborator list (Tom Clarke from Faculty action item 1).

**Oct 20** (follow-ups filled live)
- Follow-ups / reactions to what people said live during standup
  - 30 papers left? so 30 papers * 5 hrs each = 150 hrs ish?

## Retro findings

- **Worked:** reading the previous entry and takeaways; PR and Linear status with links; Sent-mail checks on commitments; leaving out work that isn't for this team (Oct 2); a short "what am I missing" list (Sep 28 caught a done task, a missing commitment and a vague blocker).
- **Failed:** couldn't find the doc and opened the wrong one (Sep 3); wrong PR status (Oct 5, Oct 8); missed Claude-app PRs and couldn't read the -dev Slack channel (Oct 12); an EAG meeting count of 58 from the calendar instead of about 50 from Swapcard (Oct 20); challenged Scott's plan instead of reading it (Oct 21); off-topic asides padded replies.
- **Live vs prepped:** Scott speaks Last/Next nearly verbatim and adds context live; Blockers drive the discussion (about 15 minutes on Oct 20). He sometimes pastes into a Slack standup thread.
- **Doc hygiene:** Scott copies the template block and often leaves it titled `Date template`, so headings don't reliably date the content; the skill writes a real date heading.

## Revision history

| Date | Change |
|---|---|
| 2026-10-21 | Created from retro |
| 2026-10-21 | Renamed from ct-standup-prep; covers the Luthien async standup too, one update per audience |
