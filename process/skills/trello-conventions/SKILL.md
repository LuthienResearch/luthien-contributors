---
name: trello-conventions
description: Scott's Trello board conventions — list naming, ownership defaults, ETA discipline, action-item scope, search-before-creating. Use when working with Scott's Luthien Trello board, creating cards, assigning owners, or referencing action items in any markdown doc. Required reading before adding/editing Trello cards or writing debriefs / agendas / meeting notes that reference team work.
---

> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy.

# Trello Conventions

Scott's primary action-item system. Source-of-truth for active commitments by humans on his team (Scott, Jai, Peter Stoica, Paolo Calvi, Ovidiu, Jen, etc.).

## Boards

- **Luthien** (primary): https://trello.com/b/ehoxykPf
- Personal & Professional: https://trello.com/b/d0R29w8R
- Digital Household: https://trello.com/b/SpTJHy0C
- Backburner: https://trello.com/b/8N7kQCz7

## List naming

- "In Progress (Today)" (id `67cf5d3518d519261ba9de2a`) — Scott's active work (renamed from "In Progress (SF)")
- "Current sprint/next up (SEA)" — Jai's queue
- DONE list id: `6a42f2f2b38dfc698d2befe8` (re-fetch with `get_lists` if a move returns 403; the old id `69cd6eeec0c8b6cae04a3d8a` failed 2026-09-30)
- Card aging is ON — faded cards = no activity in ~1-4 weeks. Activity = edits, moves, comments, checklist changes. Viewing doesn't count.
- Unassigned cards = Scott's. Don't filter by member assignment; if no one is assigned, assume it's Scott's.

## Action-item scope rules

**Trello = humans only.** Action items track work humans will do or are doing — engineering, design, writing, decisions, communications, ownership of customer relationships. Claude's session-level work (file edits, commits, doc updates, transcript fixes, Trello card creation) is just executed work, not a tracked action item. Don't write `Owner: Claude, ETA: Done` lines in debriefs or Trello — git log + commit messages already cover it.

**No recurring cards.** Trello cards are discrete tasks with owners and ETAs. Recurring tasks (monthly review, weekly sync, quarterly forecast) don't fit Trello's model — they are processes, not action items. Encode periodic deliverables as **a discrete dated card per cycle**: e.g., "May 2026 financial analysis" with due date June 10. When that card closes, create the next cycle's card with the next due date. Calendar events handle pure cadence; cadence + deliverable = dated card.

**Trello = whole team.** Cards for engineering bugs, partner deliverables, fundraise tasks all live here for Scott, Jai, Peter, Paolo, Ovidiu, Jen, etc. — not just Scott's.

**Action items live in Trello, full stop.** Markdown debriefs / call notes / docs can hold decisions, rationale, investigation outputs, narrative, and quotes — never tables or lists framed as action-item tracking. If a markdown section looks like it's tracking work-to-be-done with owners and dates, that's the anti-pattern: convert to Trello cards and reference inline with the URL.

**External-counterparty action items → meeting doc, not Trello.** Active commitments by people not on Scott's Trello boards (partners, prospects, advisors — Marius, Jeremy, Felix, etc.) stay in the meeting doc that captured them. Mixed-owner items: link the team-member portion to Trello; external portion stays in the meeting doc.

**Research / analysis / comparison output → GitHub or Drive, not Trello.** Per Scott 2026-05-17: "I use [Trello] only for action item tracking. Save [research outputs] in either GitHub or Google Drive." Apply when a Trello card asks for investigation, audit, survey, market scan, or comparison: produce the artifact in a committed-and-pushed file (default locations: Luthien-relevant team-shareable → `luthien-org/`; personal tooling research → `personal-site/dev/notes/`; cleanup audits / Scott-personal infra → `private-claude-code-docs/`). The Trello comment should be MINIMAL: link to the artifact + 1-line context, not a multi-paragraph summary. Trello is the index; the artifact is the source. Why: long Trello-embedded analyses clog the board's mental model of "what's the action," make the cards hard to scan, and force Scott to re-load context every time he opens the card. Verified failure mode 2026-05-17: Claude posted ~100-word summary comments on two cleanup/research cards; Scott flagged it explicitly and reminded "Trello is for action item tracking."

## Default ownership when unclaimed

**Every card Claude creates must have Scott as a member.** Hard rule, not advisory. Do NOT rely on auto-add: on 2026-07-15, four cards created via `add_card_to_list` all came back with empty `idMembers` (no auto-add of the token owner), contradicting the 2026-06-04 observation below. Always check the create response's `idMembers` and, when empty, call `assign_member_to_card` for Scott (`50b70a7fea357e737000497f`) — it returns `200` and adds him. If Scott was auto-added after all, the assign returns a benign, opaque `400` ("member is already on the card") — that `400` means done, not failed. Either way, a card must not be left member-less.

**Add other plausible owners alongside Scott.** When a teammate might claim the card (Jai for engineering, Peter for design, etc.), assign them too as a speculative addition. They can't pick it up if they're not visibly on it. Update when someone explicitly volunteers; the open card and check-in get discussed at the next sync.

**Never assign a teammate speculatively as the *sole* owner.** Scott stays on every card — *unless Scott explicitly names someone else as sole owner*. An explicit instruction overrides the default; a Claude guess does not.


Verified failure mode 2026-05-18: Claude created the Ryan Kidd MATS card on Luthien Next Up with empty `idMembers`. Scott flagged ("am I the owner of Ryan Kidd card?"). The skill already had a default-owner rule, but it was phrased as advisory ("assign Scott as default owner") rather than imperative. Tightened 2026-05-18.

Verified 2026-07-15: auto-add did NOT occur on four consecutive `add_card_to_list` creations (empty `idMembers` in every create response); explicit `assign_member_to_card` for Scott returned `200` each time. Treat auto-add as unreliable, not guaranteed.

Verified 2026-06-04: the `assign_member_to_card` `400` on Scott is Trello's idempotent "member is already on the card" response — the card creator is auto-added at creation. Confirmed by direct API: a freshly created card already listed Scott as a member, and assigning a non-creator board member (Adam) returned `200` and added him. So a `400` when assigning Scott to a card Claude just created is benign (already done); a `400` when assigning a *teammate* not yet on the card would be a real failure worth investigating (e.g. they're not a board member). The `@delorenj/mcp-server-trello` package surfaces Trello's response as an opaque "status code 400" without the message body, which is what made it look broken.

## ETA discipline

Don't fabricate ETAs. ETA must come from a stated commitment, a known dependency, or a calendar event. If none exists, write `TBD`.

"Today" / "this week" / aggressive deadlines invented to look responsive are anti-patterns. Better to write `TBD` and discuss at the next sync than invent urgency.

## Card creation from debriefs: propose first (Scott, 2026-05-27; instruction-only since 2026-09-15)

Never create a Trello card from a debrief or notes-processing task without Scott's in-the-moment go. Propose the card in chat first (name, list, owner, due date or TBD) and create it when he says so. A general task instruction ("debrief this call", "process these notes") is not approval. One approval covers one proposed batch, not future cards. Cards Scott asks for directly need no extra prompt.

Why: card triage is a judgment call Scott keeps (Scott, 2026-05-27: "I have to look at the proposed actions myself before creating Trello cards"). Verified failure 2026-07-15: Claude created two cards from the Leo McKee-Reid debrief autonomously; Scott had them archived the next day.

**No harness backstop (Scott, 2026-09-15).** The permissions `ask` gate on card creation is gone for good ("de-hobble the more intelligent [models] and trust fable / astra to re-measure instruction following adherence"). Adherence to this rule is measured from session logs instead of enforced by the harness; history and the measurement plan are in [claude-md-changelog.md](https://github.com/scottwofford/sw-prv/blob/main/claude-md-changelog.md).

**Shape proposed actions as the next step only.** The card/bullet names the immediate move, not the end goal, and a decision is not the next step while its inputs are missing. And no action depends on a counterparty acting first: if the expected path is "they do X," Scott's action is the failsafe ("if X hasn't happened by their-stated-window + a day, ping/escalate/proceed"); canonical rule: [`luthien-org/process/CLAUDE.md`](https://github.com/LuthienResearch/luthien-org/blob/main/process/CLAUDE.md). Full shaping rules + exemplars: [`call-agendas-and-notes/CLAUDE.md`](https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/CLAUDE.md#shape-each-action-around-the-real-next-step) ("Shape each action around the real next step"; also its sibling rule ["Waiting and scheduled states are not actions"](https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/CLAUDE.md#waiting-and-scheduled-states-are-not-actions-scott-2026-08-18), Scott 2026-08-18: waiting-on-counterparty and already-booked events never get action bullets, and DONE <date> is the only status label); gold exemplar: the [Evan Miyazono debrief](https://github.com/scottwofford/sw-prv/blob/main/personal/2026-07-13_evan-miyazono-atlas-debrief.md) action items.

## Referencing a card: say what it says (Scott, 2026-08-19)

When referencing a Trello card in chat or a doc, state its content, not just a link: name, current list, due/complete status, and the relevant description line. Scott should never have to open Trello to understand the reference. This extends the existing linking rule (card title as link text, never the short-ID): the title alone is also insufficient when the card's state or contents are what the reference turns on. (Origin: 2026-08-19, a "Berkeley-trip card still needs cleanup" loose end cited by title+link only; fetching it showed the card was already in Done, completed the prior afternoon.)

## Search before creating

**Hard rule: always search for an existing card before creating any new one.** Not optional. Critically, do **not** limit the search to the board you're about to create on — duplicates routinely live on a *different* board (a household-finance task already tracked on the Luthien board, or vice versa).

Search method, most-thorough first:
1. `mcp__trello__get_my_cards` returns every card assigned to Scott across all boards in one call. Save the (large) output to a file and `grep` it for the topic's keywords; that's the reliable cross-board check.
2. For topics a teammate might own (where Scott may not be assigned), also scan the relevant board's active lists via `get_lists` + `get_cards_by_list_id`.

If a card on the same topic already exists, add a comment / update it rather than spawning a duplicate. If you discover you already created a duplicate, archive it (`mcp__trello__archive_card`) and point to the original.

Verified failure mode 2026-05-27: Claude created a "Luthien reimbursements" card on the Digital Household board without checking other boards; a live card "Process Scott's Luthien reimbursements" already existed on the Luthien board ([#1359](https://trello.com/c/U178I5Q2)). Scott flagged it and asked that this rule be documented. Cross-board search first, every time.

**Check whether a matching card is complete before treating it as a duplicate.** A card that surfaces in the search may already be finished: in a Done / Deprioritized list, or with `dueComplete: true`, from earlier work. A completed card is NOT a live duplicate. Two failure modes to avoid: (1) suppressing a genuinely new action because an old, done card has a similar name; (2) citing a completed card in a debrief or action list as if it still covers the work. Before deciding, check the card's `idList` (is it a Done/Deprioritized list?) and its `dueComplete` flag via `get_card` — `get_my_cards` returns names but not always list context, so confirm status, don't infer from the title. If the old card is done and the new action is genuinely distinct, create the fresh card. Verified 2026-07-13: two older Lindley Lentati cards ([Panopticon integration](https://trello.com/c/Maw6BrSJ), [Debrief Lindley both convos](https://trello.com/c/yudpnBrH)) surfaced as possible duplicates of a new "reconnect with Lindley" action, but both were already complete, so the new card was correct and the old ones needed no edit.

## Weekly cross-board prioritization (due-date-as-rank)

**Scope: Scott-owned cards only (per Scott, 2026-07-13).** The plan-of-attack grooming/prioritization exercise covers only cards where Scott is an *explicit member*. Cards membered to teammates (Jai, Paolo, etc.) are theirs; leave them in place, never move or re-rank them as part of Scott's weekly pass. Note this is stricter than the "unassigned = Scott's" reading convention: for grooming *moves*, don't touch teammate-membered cards, and confirm before sweeping unassigned ones.

To turn four boards into one ranked list, overload the due-date field as a priority *rank*: the cross-board [Cards view](https://trello.com/u/scottwofford/cards) shows only dated cards sorted by date, so due dates are the only native cross-board sort key. Procedure, run at each Plan of Attack session (agreed with Scott 2026-08-13):

1. Claude: run the needs-reply sweep, then pull all 4 boards; surface real deadlines and flagged replies. **The sweep is email-by-email, not keyword search (Scott, 2026-08-14):** enumerate every message in each inbox (gmail-luthien + gmail-sw3 + gmail-sw4, `in:inbox`, incl. Google Docs comment notifications), assess each one individually for needs-Scott's-reply/action, and output the list. Targeted keyword searches are NOT a sweep — verified failure 2026-08-10→14: a reference request ("within the next few days") sat 4 days unflagged because every email lookup that week was keyword-targeted. **Paginate to the window edge — a single capped page is NOT a sweep (verified failure 2026-08-14):** the first email-by-email sweep ran `in:inbox newer_than:14d` with maxResults=50, silently covering only back to Aug 7 and missing the EUSAiR Aug 25 meeting-confirmation thread from Aug 3. Keep fetching until the oldest returned message is older than the window start, and state the achieved coverage ("through <date>, N messages") in the sweep output. The sweep also runs standalone whenever a planning session gets cut short — it is step 1 precisely so it survives truncated sessions.
2. Scott ranks the top ~10 cards in chat. Claude never assigns ranks or dates unprompted — verified failure 2026-08-13, when 25 Claude-assigned due dates had to be fully reverted.
3. Claude sets due dates in rank order, one day apart starting today, all at the sentinel time **11:47 PM** (local Seattle time). The sentinel marks a rank-date.
4. Real deadlines keep real dates and non-sentinel times; they interleave naturally in the Cards view.
5. Next session: bulk-clear every 11:47 PM date, then re-lay from the fresh ranking. Also strip dates off Back Burner / Done cards so they drop out of the view.

**Never treat an 11:47 PM due date as a real deadline, commitment ETA, or overdue alarm** — it is a rank encoding, safe to clear and re-lay. Conversely, never lay a rank-date at any other time.

This is the cross-board layer; within-board running priority is maintained separately. For the grooming that precedes the ranking (name the biggest deadline, sweep Done, demote to Back Burner, estimate effort per card in minutes), run the `jen` skill. Effort discipline lives there: estimate per card, never from category, since effort varies ~10x and isn't predictable by task type (`jen` Theme 6).

## Card order within a list carries meaning (Scott, 2026-08-12)

- **Uncategorized through Doing lists: order = priority.** Higher card = higher priority. Don't reorder these lists as a side effect of other work.
- **Done: most-recently completed at the top, and marked complete.** Moving a card to Done is always two calls on the official MCP, never the legacy `mcp__trello__move_card`: (1) `trelloWriteCard` `action: "move"`, `pos: "top"`; (2) `trelloWriteCard` `action: "mark_done"`. Then confirm the response shows `complete: true` and the card first in Done (Scott, 2026-10-13: "you always screw up the order"; the legacy move dropped [Book Flights to SF and back to SEA + SF lodging](https://trello.com/c/CncN3Ewd) mid-list and unchecked).
- **Mechanics:** the legacy `mcp__trello__move_card` has NO position parameter — it keeps the card's stale `pos` value, dropping it in an arbitrary spot (verified 2026-08-12 on [Send Tyler the Redwood trial proposal](https://trello.com/c/WH06BoXg)). Use the official Trello MCP instead: `mcp__trello-official__trelloWriteCard` with `action: "move"` and `pos` ("top" / "bottom" / number). It takes ARIs, not short links — fetch them via `trelloReadCard` or build from the id (`ari:cloud:trello::card/workspace/<workspaceId>/<cardId>`).

## Real-time meeting capture

When capturing action items mid-call, write inline with `(Trello: TBD)` placeholders. Create cards and fill the links post-meeting. Amazon-style meeting docs (Key Takeaways + Action Items + Agenda + Discussion Topics) work inside this rule: each action item gets a Trello link as captured.

## Default Trello tools

`mcp__trello__add_card_to_list`, `mcp__trello__get_card`, `mcp__trello__get_lists`, `mcp__trello__update_card_details`, `mcp__trello__add_comment`, `mcp__trello__assign_member_to_card`, `mcp__trello__move_card`. Active board: Luthien.
