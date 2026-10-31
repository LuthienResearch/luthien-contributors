> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/LuthienResearch/luthien-org/blob/main/process/meeting-notes-conventions.md (private). This copy is a redacted mirror and may lag behind it.

# Meeting Notes Conventions

Standard format for all Luthien meeting notes. Claude should follow these conventions when synthesizing transcripts or taking live notes.

**Last updated:** 2026-06-04

---

## Structure

Every meeting note follows this structure:

```
# Meeting Title — YYYY-MM-DD

Date | Participants: Name, Name, Name

**Transcript:** [Source](link) (Otter, Gemini, etc.)

---

### Key Takeaways

1. First takeaway. One to two sentences, substantive, declarative. Include specific numbers, names, and decisions — not vague summaries.

2. Second takeaway. Written as plain text, no bold. Each one should stand alone — a reader skimming just this section gets the full picture.

### Action Items

- Description of what needs to happen, written as a complete sentence starting with a verb (Owner: Name, ETA: M/DD) [Trello](URL)

- Second action item with measurable outcome (Owner: Name, ETA: M/DD)
```

---

## Rules

### Key Takeaways

- Numbered list (1, 2, 3...)
- Plain text — no bold, no bullet nesting
- Each takeaway is 1-2 complete sentences
- Substantive and specific: include numbers, names, quotes, decisions
- Written as declarative statements about what was learned, decided, or revealed
- A reader skimming only takeaways should understand what happened in the meeting
- Novel only: each takeaway states something that emerged in the conversation (a fact, number, decision, or insight) beyond what was already in the agenda, discussion topics, or pre-read. Positive test: if you deleted the agenda, this line still carries new information. Incoming context that someone brought in stays in the prep doc, not in Key Takeaways.
- Aim for 3-8 takeaways per meeting (more for longer/denser meetings)

### Action Items

- **Bullets, NEVER tables.** (The Seldon weekly template uses tables — that's a legacy format. New notes use bullets.)
- Every action item must have:
  - **Description:** Complete sentence starting with a verb. Measurable, binary pass/fail outcome.
  - **Owner:** One person's name (not "team" or "both")
  - **ETA:** Specific date (M/DD) or "This week" / "ASAP" — never "ongoing" or "TBD" without a date to revisit
  - **Trello link:** If a card exists or should be created
- Format: `- Description (Owner: Name, ETA: M/DD) [Trello](URL)`
- No bold in action items
- No PASS/FAIL status tracking in the notes — that lives in Trello
- If an action item recurs, define the first concrete milestone instead of marking it "ongoing"

### Header

- Format: `Date | Participants: Name, Name`
- Include roles/affiliations on first meeting only (e.g., "Tyler (Redwood), Scott (Luthien)")
- Note transcript source with link

### What NOT to Do

- Reserve Key Takeaways for what emerged in the conversation; incoming agenda/pre-read context stays in the prep doc, not in the notes (see the novel-only rule above).
- Don't use bold for takeaway content
- Don't put owner names in action item descriptions (that's what the Owner field is for)
- Don't write action items as noun phrases ("Review landing page") — write them as measurable sentences ("Provide written feedback on what changed between v10.6 and v10.7")
- Don't use unexplained acronyms or jargon — define on first use

---

## Examples

### Example: Apollo/Luthien Kick-off (Mar 5, 2026)

Source: `luth-gdrive-clone/_Seldon_labs/Apollo Collab/Apollo / Luthien Collab Kick-off.md`

**Key Takeaways (excerpt):**

1. Both teams align on three monitoring modes: real-time blocking (1-20% overhead on Claude Code), parallel non-blocking (~30s lag), and async/batch (30-60s default, up to 1hr for high-precision). Luthien infra adds 5-15ms without an LLM call.


2. Near-term integration direction is Luthien pushes data to Apollo (JSONL or request-response pairs), not the reverse. Apollo pulling from Luthien is a distant enterprise feature, not on the radar.

**Action Items (excerpt):**

- Share database schema link in the Google Doc for Apollo to scope translation effort (Owner: Scott, ETA: Done)
- Exchange sample data — JSONL sessions with policy metadata (Owner: Jai + Jeremy, ETA: 3/19)
- Discuss what public statements both sides are comfortable endorsing about the collaboration before Demo Day (Owner: Scott + Marius, ETA: 4/10)

### Example: Redwood/Luthien Office Hours (Mar 3, 2026)

Source: `luth-gdrive-clone/_mtg notes/2-Redwood/Notes | Redwood/Luthien Office Hours.md`

**Key Takeaways:**

1. Trust barrier is quantitative, not conceptual. Tyler gets the idea and thinks it's "inherently interesting" for Redwood. But without benchmark data, "it probably doesn't work, just like every other random thing." A before/after failure rate result would change that.

2. Bash Arena is the benchmark. Tyler recommended it over ImpossibleBench. Show attacker success rate drops with Luthien, utility doesn't drop. Two data points, one graph.

3. Trust signals > features. Video walkthrough at top of repo, credible quote (OpenAI/Fabian), or coding YouTuber coverage would move Tyler more than additional policy examples.

**Action Items:**

- Run Bash Arena benchmark — before/after Luthien safety + utility metrics (Owner: Jai, ETA: TBD) [Trello](https://trello.com/c/87seMBXH)
- Fix README + trial doc — remove "cloud account" confusion, fix broken anchor links, clarify threshold direction (Owner: Scott, ETA: this week) [Trello](https://trello.com/c/ThvVdHDA)

---

## When to Use This Format

- **All external meetings** (advisors, investors, partners, users)
- **Internal strategy meetings** (fundraising calls, co-founder debriefs)
- **Seldon weekly** — uses its own template (`call-agendas-and-notes/call-prep-agendas-debriefs/seldon-weekly/template/`) but key takeaway/action item rules still apply

## Debriefs

A debrief is a meeting note for a conversation with a running thread across sessions (coaching, recurring advisor, customer/user, investor, partner). Same Key Takeaways + Action Items rules, plus two debrief-only sections:

- **Agenda (as set):** the planned topics (from the calendar event or prep doc), verbatim. This is context, not takeaways — see the novel-only rule above.
- **Threads carried forward:** continuity vs the prior session's debrief / prep. Mark each thread resolved / changed / open so the next prep picks up cleanly.

Types and where they live:

- Customer / user / investor / partner debriefs → `call-agendas-and-notes/call-prep-agendas-debriefs/` (this repo); filename per that folder's README.
- Internal strategy / co-founder debriefs → this repo.
- Coaching sessions and everything else: follow [Meeting home](https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/CLAUDE.md#meeting-home), the one routing rule.

## Transcript Sources (in priority order)

Reflects Scott's current capture tooling (as of 2026-06). Use the best available; name it in the transcript line and flag if none is synced.

1. Plaud — in-person / audio recordings (Scott's primary device). Files land in `sw3-google-drive/drive/2.2 Plaud/`. Primary.
2. Google Meet / Gemini — auto-transcribes virtual meetings if recording is on. Primary for virtual. **Caution: misattributes speakers when people share a mic.** Lands in Drive `_mtg notes/`.
3. Otter.ai — occasional (`otter_search` / `otter_list_transcripts`); verify it's actually synced, it goes stale.
4. superwhisper — occasional local recordings; transcripts land in Drive `_mtg notes/`.
5. Manual / pasted notes — last resort when nothing synced.

## Post-Meeting Checklist

- [ ] Key takeaways written (not just raw notes)
- [ ] Action items have owners + ETAs
- [ ] Trello cards created for non-trivial action items
- [ ] Relationship-changing evidence propagated per the [relationship context architecture](relationship-context-architecture.md)
- [ ] Notes committed and pushed to luthien-org
- [ ] Shared with participants if appropriate
