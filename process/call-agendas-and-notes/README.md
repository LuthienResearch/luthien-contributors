> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/LuthienResearch/luthien-org/blob/main/call-agendas-and-notes/README.md (private). This copy is a redacted mirror and may lag behind it.

# Call Notes and Agendas

Folder for call prep, agendas, transcripts, and debriefs for outbound conversations (BD, customer, partner, investor).

**This doc = the format reference:** folder layout, filename conventions, and the section-by-section structure of agendas and debriefs (the "what it looks like"). The behavior rules for Claude — the call-lifecycle workflow, what counts as a takeaway, minimalism, Trello triage — live in [`CLAUDE.md`](call-lifecycle-rules.md). Format here, behavior there; put a rule in exactly one file and cross-link rather than restate.

Pending transfers: [EU AI Office debrief publication backlog](https://github.com/scottwofford/sw-prv/blob/main/prv-luth/redwood/eu-ai-office/eu-ai-office-publication-backlog.md).

## Repository routing

Apply [Meeting home](call-lifecycle-rules.md#meeting-home) before using this layout. A meeting's subject or participants do not by themselves graduate it to `meeting-transcripts`.

## Folder layout

- `call-prep-agendas-debriefs/` — pre-call prep docs, shared agendas, and post-call debriefs, filed by counterparty or recurring workstream.
- `call-transcripts-plaud/` — verbatim call transcripts (Plaud, Gemini, or Otter; the folder name is historical). Don't summarize here; commit the raw export. Light corrections (e.g., diarization artifact fixes) are OK if annotated inline as `[was: <original>]` and noted in an editor's note at the top.

## Filename convention

Prep/agenda/debrief files are filed in a **folder per person or recurring workstream**, named by date-first:

- **Folder:** the counterparty's first name (`Esben/`, `Kris/`, `Ivan/`). When the first name is common across Scott's contacts, disambiguate with `First-Last` (`Matt-Broerman/`, `Adam-Kaufman/`, `Aryan-Bhatt/`, `Tyler-Tracy/`, `John-Yan/`).
- **Recurring workstream folder:** use the stable lowercase slug, such as `control-tooling-sync/`.
- **Filename:** `YYYY-MM-DD_<TheirName>_<type>.md` (and `.docx` if a Word version is needed). `<TheirName>` matches the folder token. `<type>` ∈ {`topics`, `agenda`, `prep`, `debrief`, `notes`}. Examples: `Kris/2026-05-06_Kris_debrief.md`, `Adam-Kaufman/2026-06-15_Adam-Kaufman_prep.md`.
- **Seldon monthly debriefs:** file each in the corresponding `call-agendas-and-notes/call-prep-agendas-debriefs/seldon-weekly/YYYY-MM-DD/` folder as `YYYY-MM-DD_seldon-monthly_debrief.md`.
- **One-off non-person docs stay unfoldered at the root**, such as `2026-05-15_close-out-triage.md`.
- **Transcripts** (in `call-transcripts-plaud/`): `YYYY-MM-DD_<their-first-name>-<our-first-name>.md`, lowercase, hyphen-separated. Multi-attendee: `YYYY-MM-DD_<name1>-<name2>-<name3>.md` (e.g., `2026-05-06_kris-yash-scott.md`).

## Debrief format

Mirror the structure of the [Apollo / Luthien Collab Kick-off — Mar 5, 2026](https://docs.google.com/document/d/1zLxLyxEn_A_yaP-2pAjxpwZCuv7ILH4FlB0a73yY0aE/edit?tab=t.0) doc. Gold exemplar of a finished debrief: the Simon Haberfellner debrief, Jul 8 2026 (private; teammates ask Scott). Scott, Jul 8 2026: "great debrief btw, love the quotes ... you one-shotted that!" What carried it: verbatim counterparty quotes under every takeaway, and facts verified against calendar/Gmail before writing. Sections in order:

### 1. Header

```
# <calendar invite title, verbatim> — <YYYY-MM-DD HH:MMam/pm PT>
```

The H1 is the calendar event's title exactly as it appears on the invite (e.g., `Allister/Scott re-connect`), so the debrief matches what Scott sees on his calendar. Don't add org names or an invented descriptor. Only when the call had no calendar event (in-person, ad hoc), use the attendees' names (`Scott / Byron`). (Scott, 2026-09-23: "it should be names of cal invite.")

### 2. Attendees

Bullet list. One line per person:

```
- **<First Last>** (<Org>) — <role> → <attended | attended late | declined | didn't attend>
```

### 3. Goal

One-sentence statement of what the call was for.

### 4. Transcript link (if recorded)

Inline link to the verbatim transcript in `call-transcripts-plaud/`. State the start time and the **last timestamped utterance** in the transcript so the reader can compute duration without inference. **Don't fabricate run-length** — if you don't know when the call ended, look it up; never anchor on phrases like "we ran long" without a citation.

**Always link the discussion-topics / agenda doc AND Scott's raw-notes doc here, when they exist** (Scott, 2026-08-28). Both are first-class sources — counterparties annotate the shared prep doc, and Scott's raw notes carry live signal the transcript can miss (the Jo raw notes held the Buck-directs org layer absent from the recording-derived debrief). The [post-call re-read gate](call-lifecycle-rules.md#re-read-the-shared-topics-doc-after-the-call-hard-gate) depends on a reader finding both from the debrief. One line each: `Topics doc: [<title>](<url>)` / `Raw notes: [<title>](<url>)`.

**Garble/ASR and name-fix notes belong with the transcript, not the debrief.** ASR corrections (`[was: …]`) and name/attribution fixes live in the transcript's editor's note (below the transcript link), where a reader chasing a garble will look. Keep them out of the debrief. And **don't spend a debrief bullet summarizing what the call covered** ("the second half was personal catch-up") — the reader was on the call, so it adds nothing.

### 5. Key Takeaways & Action Items section

```
## **<Org A> / <Org B> [descriptor] — Key Takeaways & Action Items**

<Date> | Attendees: <names>
```

#### Key Takeaways

Numbered list, ~6–10 takeaways. Lead each with a **bold header that is a complete topic sentence summarizing the whole item** (not a label or fragment), then support it with **indented, lettered sub-bullets (a., b., c. — sub-bullets are always letters, never dashes; Scott, 2026-08-28)** carrying the specifics, quotes, numbers, contacts, and links. Encoding: write the letters literally with a backslash hard-break at the end of the preceding line and an `&emsp;` indent prefix — GitHub renders nested markdown ordered lists as roman numerals, so literal letters are the only encoding that shows a./b./c. as rendered. (Earlier debriefs packed everything into one prose line per takeaway; sub-bullets are the current format — they make a dense call scannable.) Each takeaway captures one of:

- A factual observation from the call (numbers, mechanics, capabilities, behavioral observations)
- A named person's stated position, ask, or commitment
- A relationship state-change (handoff, ownership shift, role assignment)

**Ordering:** group related takeaways adjacently first (all items about one funder, topic, or thread together — never interleaved), then order the groups chronologically by when each came up on the call, leading with the counterparty's own update. Grouping wins over chronology when the two conflict.

**Link funders/orgs to their source of truth.** When a takeaway or the Funding-opportunities section names a funder Luthien already tracks, link its [fund file](https://github.com/LuthienResearch/luthien-org/tree/main/fundraising/funds) (e.g. Coefficient Giving) rather than restating its status inline. Link people/orgs to their own page, and existing work to its Trello card.

Each item should read like a note a human took during the call; keep action items in their own section below. What counts as a takeaway worth keeping, the rewrite-from-transcript rule, and the verify-attributions gate live in [`CLAUDE.md`](call-lifecycle-rules.md#key-takeaways--new-to-scott-signal-only).

#### Action Items

Numbered list. One line per item:

```
1. <description> (Owner: <Name>, ETA: <YYYY-MM-DD | trigger | TBD>)
```

For completed items, use the [shared completed-actions convention](https://github.com/linuxarena/meeting-transcripts/blob/main/4-takeaways-actions/AGENTS.md#completed-actions); this file does not define a separate completion format. For open items tracked in Trello, link the card inline at the end of the line: `... (Owner: Scott, ETA: 5/11) — [Trello](<url>)`.

**Action items are for humans only.** Owner must always be a human team member (Scott, Peter, Paolo, Jai, etc.) — never Claude. Things Claude executes during the session (file edits, transcript fixes, doc updates, Trello card creation) are just done work, not tracked actions. The git log covers what Claude did; don't pollute Action Items with `Owner: Claude` lines.

## Action items live in Trello

This folder holds debriefs and notes; **action items live in Trello, full stop**. The Action Items section in a debrief is a snapshot at debrief-time, not an ongoing tracker. Claude surfaces the items; Scott triages each into a card himself. Full rule (never auto-create cards) in [`CLAUDE.md`](call-lifecycle-rules.md#never-auto-create-trello-cards-from-a-debrief).

## Don't fabricate

- Don't invent attendees, durations, end times, or quotes.
- If the transcript stops at 00:43:11 and the call started at 7:30 AM PT, the end time is ~8:13 AM PT — not "~8:45 AM" or any other inference.
- If you didn't witness it and can't cite it, don't write it as a Key Takeaway.
