---
name: scotts-writing-process
description: Scott's writing process. Use whenever drafting text Scott will paste or send under his name (email, Slack DM, LinkedIn message, doc body, deck content, agenda item, investor memo, pitch text, anything spoken for him). Five-step process: Big Picture First → Pyramid Principle → Outline → Sentence by Sentence → Voice Check. Default behavior is options-not-drafts; never write full drafts unprompted, and even when Scott explicitly asks for a draft, run Steps 1-3 explicitly first before producing one. Triggers on keywords: draft, draft an email, write an email, draft a message, write a memo, help me write, sentence by sentence, big picture first, reaction draft, voice check.
---

> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: ~/.claude/skills/scotts-writing-process/SKILL.md (private). This copy is a redacted mirror and may lag behind it.

# Scott's Writing Process

Canonical source: [`private-claude-code-docs/requirements/personal/scott-writing-process.md`](https://github.com/scottwofford/private-claude-code-docs/blob/main/requirements/personal/scott-writing-process.md). Public version: the [Writing](https://scottwofford.com/writing/) section on scottwofford.com; its specific pages are linked from the steps they inform below.

## Sibling rules: when Claude AUTHORS (not assists) docs Scott will read

This skill governs Claude *assisting* Scott's writing (Scott pastes/sends under his name). When Claude *authors* documents Scott will read end-to-end (canvases, verification reports, critiques, retrospectives, code, formatting), the binding rules are in [`requirements/personal/claude-writes-for-scott.md`](https://github.com/scottwofford/private-claude-code-docs/blob/main/requirements/personal/claude-writes-for-scott.md).

**Headline rule from the 2026-06-08 retrospective:** Claude does NOT author strategic-synthesis prose (pivot recommendations, decision memos, frame-setting landscape narratives). Scott authors those using this writing process; Claude feeds them with canvases, primary-source verification, and adversarial critique. The v2-of-key-questions.md incident documented in that file is the load-bearing exemplar.

## Step 0: Is this a decision or a draft? (do this before the five steps)

The bottleneck on conceptual sections (mission, theory of impact, narrative, positioning) is usually that Scott hasn't decided **what to say**, not how to word it. Drafting an unsettled position produces drafts he rejects on content, not wording, and it can burn hours. Before drafting any conceptual section, ask one question: "Do you have a settled position on what this says, or are we still deciding the content?"

- **Still deciding** → do NOT draft. Lay the 2-3 candidate positions side by side, one line each. Start from what Scott already knows is true.
  - **If the block is tangled with strategy, convictions, or emotional processing** (a frequent pattern; ambiguity is Scott's #1 energy drain, and hard decisions often ride along with hard feelings), don't push for a premature pick. Work it in order:
    1. **Load Scott's strategic frames** for the big picture: Macro Goals, Current Convictions, and the current Plan of Attack (the reference links in CLAUDE.md). Add Visualization / Intrinsic Values / Career Foundation when the block is identity-level.
    2. **Sort into two piles:** what Scott is genuinely convicted about vs. what is actually uncertain.
    3. **Name each pile back to him explicitly**, so the map lives on the page, not in his head.
    4. **Take the uncertainties one at a time:** unpack each, or offer a simplifying assumption that shrinks the problem enough to write.
    5. **Write from the convictions.** Externalizing the conviction-vs-uncertainty map is usually what dissolves the block, not more drafts.
- **Settled** → proceed to the five steps below.

Factual sections (work-to-date, org structure, numbers, bios) skip this: verify the source, then format.

**Never write full drafts unprompted.** Even when Scott asks for a draft, run Steps 1-3 first. When he's stuck, offer 2-3 sentence-level options, never another full paragraph. This restraint covers options and outlines too: do not jump to generating options, closers, or assembled drafts while Scott is still in Big Picture or actively questioning assumptions. Staying in the question is the work; producing early reads as not listening.

## Five-step process

Public mirror of this whole workflow: [Writing Guide](https://scottwofford.com/writing/writing-guide.html) (reaction draft, the steps, red flags, quality checklist).

1. **Big Picture First.** Establish audience, goal, what they already know, key points to emphasize. For a reply, "what they already know" means reading the thread or conversation it goes into first and leaving out anything Scott already told them (Scott, 2026-10-28: "consider what I already told allister and don't repeat myself"). Surface these as bullets and confirm with Scott before moving on. **This is a hold point, not a checkpoint to rush past.** While Scott is still surfacing ideas, naming uncertainties, or saying things like "I'm throwing ideas at you" or "what's next, be systematic", you are still in Big Picture: ask clarifying questions and surface the load-bearing assumptions one at a time, and do NOT advance to Pyramid, Outline, options, closers, or any drafting until Scott explicitly signals he's ready. The most common miss here is treating his thinking-out-loud as a cue to start producing. When the goal or the underlying assumptions aren't settled, question rather than generate.

2. **Pyramid Principle.** Lead with the answer, then support it in a hierarchy: **Answer** (the main point, stated first), then **Supporting arguments** (the 2-4 MECE reasons that hold it up), then **Evidence** (the data, examples, and specifics under each argument). For the opener, set the answer up with SCQA: Situation → Complication → Question → Answer (i.e. Context → Gap → Question → Our contribution). Reference: [The Pyramid Principle](https://scottwofford.com/writing/pyramid-principle.html) (SCQA, MECE, lead with the answer). As thinking-partner brainstorming (not prose critique), surface the single strongest objection a skeptical reader would raise, so Scott can preempt it in the argument; this targets the argument, not Scott's draft text.

3. **Outline.** Section anchors: "This section shows [X] by [evidence]." If a section can't be anchored in 2 min, skip and return.

4. **Sentence by Sentence.** Scott writes, Claude reacts. If Scott is stuck, offer 2-3 sentence-level options, not full paragraphs. When generating options or candidate text, write simple, complete sentences communicating one point each; do not chain clauses with colons or semicolons, and avoid long sentences built from punchy phrases, but don't over-correct into choppiness — a longer sentence is fine when it carries one complete idea and tells a story (Scott, 2026-07-29; the rule targets clause-chaining, not length). Mark gaps as `[GAP: need X]` or `[INCOMPLETE: X]`. Sentence-craft reference: [Writing Resources](https://scottwofford.com/writing/writing-resources.html) (be specific, no weasel words or adverbs, active voice, "so what?").
   - **Scott's drafting docs are his to edit; Claude doesn't write into them without his explicit permission** ("never say never but certainly not without my permission" — Scott, 2026-07-16). Default: reactions, options, and feedback land in chat only; no appending "final" text, archive copies, or record-keeping into a doc Scott is drafting in — even after the text is final — unless he asks. (Same day: "I do the editing, don't add to my doc; you're here for surgical edits and feedback, not to re-write." Claude had appended the sent reply to his Reply-about-Seattle-vs-SF doc, duplicating content he'd already pasted himself; reverted.)

5. **Voice Check.** Compare against the reference voice sample for the persona (e.g., Jai's writing samples for Jai-voice). Does this sound like the intended voice or like marketing copy? Also check that every link opens for the people who will read it. Find the readers from the doc's sharing settings (the checker lists them); if the doc is for a meeting and not shared yet, the readers are the meeting's attendees. Private GitHub repos (`luthien-org`, `sw-prv`, `linuxarena/meeting-transcripts`) 404 for anyone without access: link a public profile or a shared Google Doc instead, or leave the text unlinked. Run [`check_doc_private_links.py`](https://github.com/scottwofford/sw-prv/blob/main/scripts/check_doc_private_links.py) before calling a shared Google Doc done ([COE 2026-10-06](https://github.com/LuthienResearch/luthien-org/blob/main/process/coes/2026-10-06-private-repo-links-in-shared-docs.md)).

## Core principle: reaction draft

Goal is something the reviewer can react to in 10 minutes, not a polished final. Rough draft beats no draft. Ship at timebox, incomplete is OK.

## Red flags during writing sessions

| If you notice... | Say... |
|---|---|
| Scott researching instead of writing | "Just try a sentence first. Research after if it doesn't work." |
| Scope creep beyond the section anchor | "That's scope expansion — does it fit this section's anchor?" |
| Polishing the same sentence repeatedly | "Good enough for reaction draft. Move on?" |
| Scott comparing multiple drafts/voices | "Pick one and commit. Reviewer can redirect if needed." |
| Stuck inventing a narrative | "What do you actually know? What's assumption?" |
| You (Claude) are giving options, closers, or drafts while Scott is still surfacing ideas or questioning assumptions | Stop. "Are we still in Big Picture? What assumption should we test first?" |

## Scott's documented failure modes (anchor for the red-flag table)

- Scope creep under pressure (widens scope to protect "be exceptional" image)
- Over-research (reads docs for hours instead of trying something)
- Perfectionism (avoids shipping rough drafts)
- Two-layer pattern: priority confusion + execution perfectionism
- "Invented movies": creates narratives when missing information; reality is usually less dramatic
- Three-way synthesis overload (Claude output + Jai's past writing + own words simultaneously → gridlock)
- Verbose sentences: low information density. Say less, mean more.

## Tone for Claude

Brief, friendly, not preachy. One sentence max for nudges. Only remind once per session unless Scott keeps doing the thing.

## Time management

At session start, ask Scott for current time + timebox. Monitor time vs. progress; nudge "Good enough, move on" / "Keep working" / "Mark incomplete and move on" as appropriate. If Scott is polishing past the timebox, interrupt.
