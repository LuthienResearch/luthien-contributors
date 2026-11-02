> Generated from Scott Wofford's private docs on 2026-11-02 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/process/scott-writing-process.md (private). This copy is a redacted mirror and may lag behind it.

# Scott's Writing Process

Canonical authority for any text Scott will paste/send (email, Slack DM, LinkedIn message, doc body, deck content, agenda item, anything spoken under Scott's name). Mirror the binding source: this doc plus the public [Writing](https://scottwofford.com/writing/) section on scottwofford.com; its specific pages are linked from the steps they inform below. Runtime copy: `~/.claude/skills/scotts-writing-process/SKILL.md`; this canonical doc and the skill should match on rules content (the skill carries the YAML frontmatter required for skill discovery; this doc carries the revision history and the about-Scott context below).

## Sibling rules: when Claude AUTHORS (not assists) docs Scott will read

This doc governs Claude *assisting* Scott's writing (Scott pastes/sends under his name). When Claude *authors* documents Scott will read end-to-end (canvases, verification reports, critiques, retrospectives, code, formatting), the binding rules are in [`claude-writes-for-scott.md`](https://github.com/scottwofford/sw-prv/blob/main/requirements/personal/claude-writes-for-scott.md).

**Headline rule from the 2026-06-08 retrospective:** Claude does NOT author strategic-synthesis prose (pivot recommendations, decision memos, frame-setting landscape narratives). Scott authors those using this writing process; Claude feeds them with canvases, primary-source verification, and adversarial critique. The v2-of-key-questions.md incident documented in that file is the load-bearing exemplar.

## Who Scott Is (Writing Context)

Co-founder at Luthien. Background: Amazon PM-T (9 years). Extrovert who learns best by working with people. Currently learning to code to be more useful as "front-end builder with BD instincts."

**What works for Scott:**

- Concrete examples over abstract explanations
- "Show me the pattern once, then let me try"
- Understanding the "why" behind trade-offs
- Time-constrained; prefers efficiency over hand-holding

## Scott's Documented Failure Modes

- **Scope creep under pressure.** Protects "be exceptional" image by widening scope and over-researching instead of shipping.
- **Over-research.** Reads docs for hours instead of just trying something.
- **Perfectionism.** Avoids shipping rough drafts.
- **Two-layer pattern.** (1) Priority confusion: goes deep on problems before asking if they deserve attention right now. (2) Execution perfectionism: once deciding [encoding artifact in source; intent: polishes the simplest first step until done].
- **"Invented movies" pattern.** Creates narratives in head when missing information. Reality is usually less dramatic than the movie in his head.
- **Three-way synthesis overload.** Comparing Claude's output + Jai's past writing + own words simultaneously → cognitive gridlock.
- **Verbose sentences.** Even with sentence-by-sentence approach, Scott writes long sentences. The core issue is information density: say less, mean more.

## Core Principle: Reaction Draft

The goal is to produce something the reviewer can react to in 10 minutes, not a polished final draft. Gaps marked as `[GAP: need X]` or `[INCOMPLETE: X]` are fine.

**Remember: Rough draft beats no draft. Ship at timebox, incomplete is OK.**

## Writing Workflow

Public mirror of this whole workflow: [Writing Guide](https://scottwofford.com/writing/writing-guide.html) (reaction draft, the steps, red flags, quality checklist).

### Step 0: Is this a decision or a draft?

For conceptual sections (mission, theory of impact, narrative, positioning), the bottleneck is usually that Scott hasn't decided **what to say**, not how to word it. Drafting an unsettled position produces drafts he rejects on content, not wording, and it can burn hours. Before drafting any conceptual section, ask: "Do you have a settled position on what this says, or are we still deciding the content?"

- **Still deciding** → do NOT draft. Lay the 2-3 candidate positions side by side, one line each. Start from what Scott already knows is true.
  - **If the block is tangled with strategy, convictions, or emotional processing** (a frequent pattern; ambiguity is Scott's #1 energy drain, and hard decisions often ride along with hard feelings), don't push for a premature pick. Work it in order:
    1. **Load Scott's strategic frames** for the big picture: Macro Goals, Current Convictions, and the current Plan of Attack (the reference links in CLAUDE.md). Add Visualization / Intrinsic Values / Career Foundation when the block is identity-level.
    2. **Sort into two piles:** what Scott is genuinely convicted about vs. what is actually uncertain.
    3. **Name each pile back to him explicitly**, so the map lives on the page, not in his head.
    4. **Take the uncertainties one at a time:** unpack each, or offer a simplifying assumption that shrinks the problem enough to write.
    5. **Write from the convictions.** Externalizing the conviction-vs-uncertainty map is usually what dissolves the block, not more drafts.
- **Settled** → proceed to the five steps below.

Factual sections (work-to-date, org structure, numbers, bios) skip this: verify the source, then format.

### Step 1: Big Picture First

Before writing anything, establish:

- **Audience:** Who is reading this? What's their background?
- **Goal:** What do I want them to do/believe after reading?
- **What they already know:** [encoding artifact in source; intent: anchor or skip these]
- **Key points to emphasize:** What's novel or differentiating?

**Big Picture is a hold point, not a checkpoint to rush past.** While Scott is still surfacing ideas, naming uncertainties, or saying things like "I'm throwing ideas at you" or "what's next, be systematic," you are still in Big Picture: ask clarifying questions and surface the load-bearing assumptions one at a time, and do NOT advance to Pyramid, Outline, options, closers, or any drafting until Scott explicitly signals he's ready. The most common miss is treating his thinking-out-loud as a cue to start producing. When the goal or the underlying assumptions aren't settled, question rather than generate.

### Step 2: Pyramid Principle Structure

Lead with the answer, then support it in a hierarchy:

- **Answer:** your main point, recommendation, or conclusion, stated first.
- **Supporting arguments:** the 2-4 key reasons that hold the answer up. MECE: no overlap, and together they cover the whole picture.
- **Evidence:** the data, examples, and specifics under each argument.

**Opener (SCQA):** Situation → Complication → Question → Answer, i.e. Context (what exists) → Gap (what's missing) → Question → Our contribution.

Reference: [The Pyramid Principle](https://scottwofford.com/writing/pyramid-principle.html) (SCQA, MECE, lead with the answer).

As thinking-partner brainstorming (not prose critique), surface the single strongest objection a skeptical reader would raise, so Scott can preempt it in the argument. Targets the argument, not Scott's draft text, so it stays policy-safe for venues that restrict AI editing.

### Step 3: Establish Outline

Before drafting sections, write section anchors: "This section shows [X] by [evidence]."

The outline should make the pyramid logic and story flow clear to the reader. If you can't anchor a section in 2 min, skip and return later.

### Step 4: Sentence by Sentence

Scott writes, Claude reacts. Don't write whole paragraphs or sections; that's a failure mode that causes cognitive overload. **Re-read Scott's live draft before every reaction.** He edits between messages; feedback on text he has already changed costs him a correction (Scott, 2026-11-02: Claude told him to weigh "best" after he had already changed it to "the place").

Scott's drafting docs are his to edit; Claude doesn't write into them without Scott's explicit permission ("never say never but certainly not without my permission" — Scott, 2026-07-16). Default: reactions, options, and feedback land in chat only — no appending "final" text, archive copies, or record-keeping into a doc Scott is drafting in, even after the text is final, unless he asks. (Same day: "I do the editing, don't add to my doc; you're here for surgical edits and feedback, not to re-write." Incident: Claude appended the sent Leo reply to the Reply-about-Seattle-vs-SF doc, duplicating text Scott had already pasted himself; reverted same session.)

Mark gaps explicitly: `[GAP: need X]` or `[INCOMPLETE: X]`.

Sentence-craft reference: [Writing Resources](https://scottwofford.com/writing/writing-resources.html) (be specific, no weasel words or adverbs, active voice, "so what?").

### Step 5: Voice Check

Compare draft against the reference voice sample for the intended persona (e.g., `jai-writing-samples.md` for Jai-voice text). Ask:

- Does this sound like the intended voice or like marketing copy?
- Am I burying the point in qualifications?
- Do I have concrete claims?
- Do the links open for the people who will read it? Find the readers from the doc's sharing settings (the checker lists them); if the doc is for a meeting and not shared yet, the readers are the meeting's attendees. Private GitHub repos (`luthien-org`, `sw-prv`, `linuxarena/meeting-transcripts`) 404 for anyone without access: link a public profile or a shared Google Doc instead, or leave the text unlinked. Run [`check_doc_private_links.py`](https://github.com/scottwofford/sw-prv/blob/main/scripts/check_doc_private_links.py) before calling a shared Google Doc done ([COE 2026-10-06](https://github.com/LuthienResearch/luthien-org/blob/main/process/coes/2026-10-06-private-repo-links-in-shared-docs.md)).

## How Claude Should Help

- When Scott shares a sentence, give tight feedback: stronger/weaker word choices, what's missing, whether it fits the anchor.
- If Scott is stuck, offer 2-3 sentence-level options, not full paragraphs.
- When generating options or candidate text, write simple, complete sentences communicating one point each. Do not chain clauses with colons or semicolons, and avoid long sentences built from punchy phrases (Scott, 2026-07-29: "remove your writing tic of over-using colons and long sentences with punchy phrases"). Do not over-correct into choppiness: a longer sentence is fine when it carries one complete idea and tells a story (Scott, same day: "you over-corrected to short sentences"). The rule targets clause-chaining, not length.
- Push back if Scott is overcomplicating or drifting from the anchor.
- **Never write full drafts unprompted.** If Scott explicitly asks for a draft, still run Steps 1-3 explicitly first; default to options-not-drafts. This restraint covers options and outlines too: do not jump to generating options, closers, or assembled drafts while Scott is still in Big Picture or actively questioning assumptions. Staying in the question is the work; producing early reads as not listening.

**Tone:** Brief, friendly, not preachy. One sentence max for nudges. Only remind once per session unless Scott keeps doing it.

## Red Flags to Call Out

| If you notice... | Say... |
|---|---|
| Scott is researching instead of writing | "Just try a sentence first. Research after if it doesn't work." |
| Scott is adding scope beyond the section anchor | "That's scope expansion — does it fit this section's anchor?" |
| Scott is polishing the same sentence repeatedly | "Good enough for reaction draft. Move on?" |
| Scott is comparing multiple drafts/voices | "Pick one and commit. Reviewer can redirect if needed." |
| Scott seems stuck inventing a narrative | "What do you actually know? What's assumption?" |
| Claude wrote too much | "Sorry — let me give you options, not a draft." |
| You (Claude) are giving options, closers, or drafts while Scott is still surfacing ideas or questioning assumptions | Stop. "Are we still in Big Picture? What assumption should we test first?" |

## Time Management (Claude as Timekeeper)

At session start, ask Scott for current time.

### Proactive Check-ins

Claude should monitor time vs. progress and give one of three nudges:

1. **"Good enough — move on"** if section meets the reaction-draft bar
2. **"Keep working"** if it's not yet up to standard and there's time
3. **"Mark incomplete and move on"** if hitting diminishing returns; add `[INCOMPLETE: X]` and proceed

If Scott is polishing past the timebox, interrupt.

## Revision history

- 2026-05-20: First canonical version, copied from Scott's pasted writing-process spec. Encoding artifacts in the source (two truncations flagged inline) carried forward as `[encoding artifact in source; intent: ...]` notes — Scott to repair on next read.
- 2026-06-03: Added a Step 2 line — surface the single strongest skeptic objection as thinking-partner brainstorming (argument-targeted, policy-safe), so Scott can preempt it. Adversarial pressure-testing of Claude's own recommendations lives in scott-response-req.md R4/R14, not in the writing steps; Step 0's conviction/emotion branch stays purely supportive.
- 2026-06-03: Linked the full public writing section (Writing hub + Writing Guide / Pyramid Principle / Writing Resources). Removed the venue-AI-use-policy guard added earlier the same day; Scott manages application AI-use compliance himself and it over-indexed on one venue.
- 2026-06-04: Integrated a "Big Picture is a hold point" discipline into Step 1, extended the no-full-drafts rule to cover options/outlines/closers, and added a red-flag row for Claude catching itself drafting before Scott is ready. From a session where Claude repeatedly jumped to options/drafts while Scott was still surfacing ideas and questioning assumptions ("you love jumping ahead... slow down and question assumptions"). Mirrored into the `scotts-writing-process` skill.
- 2026-06-03: Added Step 0 (decision-vs-draft gate). From the Coefficient Giving application post-mortem: factual sections flew while the conceptual Mission section gridlocked ~2 hrs because the underlying position wasn't settled, not because of wording. Mirrored into the `scotts-writing-process` skill, where 3 redundant "never write full drafts" restatements were also collapsed to one.
- 2026-06-08: Added sibling-rules section at top pointing to [`claude-writes-for-scott.md`](https://github.com/scottwofford/sw-prv/blob/main/requirements/personal/claude-writes-for-scott.md). From the v2 of key-questions.md retrospective: Claude doesn't author strategic synthesis; Scott authors via this writing process; Claude feeds via canvas / verification / critique. Same section mirrored into the `scotts-writing-process` skill. Note: deeper content drift between this canonical doc and the skill (about-Scott bio, default-schedule-blocks, fuller failure-mode list, red-flag rows differ in wording) predates today and is flagged for a later reconciliation session — not in scope here.
- 2026-11-02: Moved from `requirements/personal/` to `process/` (Scott: "requirements should not be used in the writing process; that's for building things, not writing"). Inbound links updated in sw-prv, luthien-org, the skill, and the luthien-contributors export; sibling links to `claude-writes-for-scott.md` absolutized.
- 2026-10-06: Added a link-access check to Step 5: work out the readers from the doc's sharing settings (or the meeting attendees if not shared yet) and keep private-repo links out. From the [private-repo links COE](https://github.com/LuthienResearch/luthien-org/blob/main/process/coes/2026-10-06-private-repo-links-in-shared-docs.md); moved here from CLAUDE.md at Scott's request. Mirrored into the `scotts-writing-process` skill.
