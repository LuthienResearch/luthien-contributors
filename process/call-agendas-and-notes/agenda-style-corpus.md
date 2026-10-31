> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/agenda-style-corpus.md (private). This copy is a redacted mirror and may lag behind it.

# Scott Agenda + Discussion-Topics Style Corpus

Reference set of Scott-authored meeting prep docs. Future Claude sessions: read this file before drafting any agenda or discussion-topics list, pick 2-3 tag-matched positive entries as the format model, audit against the negative bucket.

Auto-maintained per the rules in [`call-lifecycle-rules.md`](call-lifecycle-rules.md). Each entry verified Scott-authored (positive bucket) or Claude-authored (negative bucket) using the heuristics below.

---

## Conventions

- Each entry has a tag header: `[format] [counterparty-type] [variant]` + title + date.
- **Format tags:**
  - `[agenda]` — Scott owns the meeting, numbered items, possibly time-allocated. Prescriptive.
  - `[discussion-topics]` — Scott provides context + URLs + open ask. Counterparty drives. Light.
- **Counterparty-type tags:** `[peer-founder]` · `[advisor-1:1]` · `[investor]` · `[customer]` · `[team-internal]` · `[coaching]` · `[research-partner]` · `[contractor]`.
- **Variant tags (optional):** `[share]` (sent to counterparty) · `[internal]` (Scott's private prep) · `[script]` (1:1 with running threads, evolves week-to-week).
- Content is verbatim Scott prose. The Drive doc is canonical when present; the markdown excerpt is for quick reference. Always link the Drive source.

## Format rule for discussion-topics (critical)

**Discussion topics use OUTLINE format with sub-bullets, NOT flat lines.** 3-5 main topics, max 7. Each main topic can carry indented sub-bullets that elaborate context, links, or sub-questions.

Wrong (flat list):

> Pilot stalled
> Two possible fixes
> Notes link
> Want your read

Right (outline with nesting):

> - Pilot with our first design partner stalled after week 2:
>     - https://example.com/pilot-notes
>         - Their security team wants self-hosting before adding seats
> - Two fixes we're weighing: a hosted trial or a self-host guide
> - Given all this, I'd love your read on which to try first

(Made-up example.) The nesting carries meaning: the self-hosting blocker is a sub-detail under the notes link (deepest level), under the pilot topic. Flattening loses the structure.

## Authorship verification heuristics

Apply ALL checks before adding to the positive bucket. Default to "Mixed-or-unclear" if signals conflict.

**Positive signals (Scott-authored):**
- No em dashes anywhere in the body.
- Terse bullets in outline format.
- First-name-only references (matches [`README.md`](README.md) convention).
- Scott-native abbreviations: "(db)" for the investor database, "1:1," "TBD," counterparty initials when Scott has used them.
- Discussion-topics shape: 3-5 outline-form topics with sub-bullets; ends with one open-ended ask.
- Agenda shape: numbered items with optional time allocations like "(2 min)" / "(15 min)"; topics framed as discussion points not Claude-style sub-questions.
- Personal context Claude wouldn't invent: "family emergency," "Per Adam," "Throttle back availability."
- Git history (`git log --follow --pretty='%an %ad' -- <file>`) shows Scott as author with no `Co-Authored-By: Claude` trailer.

**Negative signals (Claude-authored or AI-tainted):**
- `Co-Authored-By: Claude` git trailer.
- `Prepared by Claude` header or footer.
- Em dashes.
- "Frame swap" / "Reciprocity" / "Quick demo first" / "Tradeoff to surface" / numbered timeboxes paired with 5+ sub-questions per item.
- Templated section labels: "Who's Who," "Since We Last Spoke," "What I Owe," "Context & Agenda (Prepared by Claude)," "Claude's Questions for X."
- LinkedIn URLs with full profile pulls (Claude over-includes these; Scott doesn't).
- Multi-paragraph synthesis at the top before any actionable content.
- Flat list of topics with no sub-bullets (when discussion-topics format).

**Edge case — share vs internal:** Scott often writes BOTH a counterparty-facing share version and an internal prep version of the same call. Both go in the positive bucket, tagged `[share]` vs `[internal]`.

**Discretion clause:** entries with sensitive personal content (personal life, health, emotional reflection) are excluded from this team-visible corpus. If the structural pattern is uniquely useful, capture the SHAPE with personal content paraphrased and a private-Drive link.

**Partial-entry rule:** when only PART of a source doc is Scott-authored exemplar quality (e.g., Scott's top-level topics are good but the doc also has rough notes or a Claude draft underneath), include only the exemplar section as the corpus excerpt. Note in the entry what was excluded and why.

**This public copy** carries only the conventions and format rules above. The verbatim example entries (positive and negative buckets) quote real prep docs and stay in the private copy.

---
