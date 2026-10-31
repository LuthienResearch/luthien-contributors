> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy.

# call-agendas-and-notes — Claude Code Instructions

Folder-scoped behavior rules for Claude working in this directory, organized **chronologically along the call lifecycle**: decide to meet → seed a topics list → book → write the prep doc → take raw notes during the call → debrief afterward. Mirrors and extends the global `~/build/CLAUDE.md` rule "Meeting prep: agenda vs discussion topics (Scott's vocabulary)."

**This doc = the behavior rules:** how Claude should act at each stage of the call lifecycle (what counts as a takeaway, minimalism, Trello triage, rewrite-from-transcript). The format reference — folder layout, filenames, and the section-by-section structure of a debrief — lives in [`README.md`](README.md). Behavior here, format there; put a rule in exactly one file and cross-link rather than restate.

The two cross-cutting rules that apply at every stage:

- **Minimalism.** Fewest words that communicate the idea. Simplify and remove, don't add. No repetition.
- **Match the format Scott asks for.** "Agenda" and "discussion topics" are distinct (see Stage 3).

## Meeting home

This is the canonical routing rule for Scott's meetings. It moved here on 2026-10-09, when `meeting-transcripts` removed its inclusion gate: anyone with write access can add any meeting there ([Adding meetings](https://github.com/linuxarena/meeting-transcripts/blob/main/AGENTS.md#adding-meetings)). This rule governs where Scott's agents file his own meetings; it does not restrict other `meeting-transcripts` writers.

Pick the home before writing prep, filing a transcript, writing a debrief, or deriving people/status updates:

| Meeting | Home |
|---|---|
| A potential Luthien hire: the person might join Luthien | `sw-prv`; people-sensitive material in [`prv-luth/people/<first-last>/`](https://github.com/scottwofford/sw-prv/blob/main/prv-luth/AGENTS.md), team-safe debriefs here |
| Scott-personal conversations (coaching, family), and private passages from an otherwise Luthien meeting | `sw-prv` |
| Control Tower team meetings: series synced via `2-scripts/meetings.yml`, and one-off team meetings such as a strategy session | `meeting-transcripts` |
| Scott's other individual meetings: researcher, collaborator, and introductory calls | Here, by default |

**Conference conversations (EAG, EAGx and similar) default here, transcripts included (Scott, 2026-10-20).** Rationale, in Scott's words: "I asked for permission every time I recorded, and I need to scale." Teammates who fold conference signal into Luthien work (for example the Coefficient Giving application) read the transcripts directly instead of routing every question through Scott; all luthien-org members may read them (Scott confirmed the full collaborator list, 2026-10-20). This default overrides the potential-hire row for conference conversations. File each conversation under `call-transcripts-plaud/<event>/` (for example `eag-nyc-2026/`) as a team copy. Default: include everything; make only the surgical cuts listed in the [prv-luth routing rule](https://github.com/scottwofford/sw-prv/blob/main/prv-luth/AGENTS.md#routing-rule-which-repo) (exact pay numbers, marked off-the-record spans, NDA spans), replace each cut with a `[redacted: <category>; unredacted original in Scott's private notes]` marker, and keep the unredacted original in `sw-prv/transcripts/`. If the person asked that the recording itself not be shared, or Scott told them it was just for him, the whole conversation stays in `sw-prv`. Align with Scott on a table of proposed redactions before dispatching agents or pushing (2026-10-20: agents applied unagreed criteria and a commit went out before review). Only real redactions go in that table; header, speaker-map and editor's-note fixes are judgment calls to just make, never items for Scott to review (Scott, 2026-10-20).

### Performance-management redaction

**Before committing any transcript, debrief, or notes here, cut performance-management material (Scott, 2026-10-21).** Same bar as the `meeting-transcripts` [R3 rule, footnote 1](https://github.com/linuxarena/meeting-transcripts/blob/main/0-requirements/mtg-trans-repo-req.md#requirements): private personnel facts or identities attached to private personnel judgments, for example doubts about a teammate's ability to deliver, plans to move someone's role, or a verdict on a contractor's judgment. Every luthien-org collaborator can read this repository, including the people being discussed. A mention of someone's work, feedback, or hiring is not by itself a reason to redact.

- Replace each cut span with `[Redacted: performance-management discussion.]` and add a **Redactions:** line under the title saying the unredacted original is retained outside this repository.
- Put the unredacted original in [`sw-prv/prv-luth/people/<first-last>/`](https://github.com/scottwofford/sw-prv/blob/main/prv-luth/AGENTS.md), with a pointer to the team copy.
- Check before the first commit: git history keeps anything pushed, and a later redaction does not remove it.

**Graduating an individual meeting to `meeting-transcripts`.** Scott decides. A prep or debrief request, a public people-dossier entry, relevance to Control Tower, or a misplaced existing file is not that decision; finish the work here without waiting for one. An unattended ingest pass never graduates a meeting. When Scott approves:

1. Redact the copy per the `meeting-transcripts` [R3 redaction rule](https://github.com/linuxarena/meeting-transcripts/blob/main/0-requirements/mtg-trans-repo-req.md#requirements) (performance management, NDA-restricted information, funding and payment amounts).
2. File the meeting's prep, transcript, and debrief together under that repository's layout, recording Scott's approval date and source in the promoted artifact.
3. Verify the destination copy, then update inbound links and meeting-derived people/status entries.
4. Remove the old live copies here, except when the destination copy is redacted: then keep the unredacted original here with a pointer to the redacted copy, and never delete it.

Moving files does not imply rewriting Git history or changing recording permissions. Filing mechanics below apply after selecting the home.

## Artifact-resolution gate

**"Debrief" means an authored post-call repo file in its approved home (`*_debrief.md` in this repository, or the corresponding `4-takeaways-actions/` file for an approved meeting-transcripts meeting).** "Notes by Gemini" is an AI-generated summary, not a debrief, transcript, or Scott's raw notes. Never substitute one artifact type for another, and never use or edit Gemini's summary or suggested actions when Scott asks about a debrief. Before concluding that a debrief is missing, search the current checkout, `origin/main`, and git history.

---

## Stage 1 — Decide to meet + seed a high-level topics list

Before anything is booked, the artifact is a short, high-level list of what Scott wants out of the conversation. It is a seed, not the polished prep doc. A few terse bullets in Scott's voice, often pasted straight into the booking message.

Scott-authored exemplar (Ryan Kidd, MATS — answer to "Please share anything that will help prepare for our meeting"):

> Your "AI safety undervalues founders" post has been super validating and helpful. I'd like to discuss:
> - Luthien updates since Seldon labs demo day, constraints
> - Gather context behind [program]
> - the right format/mentors for me over the next few months

Note the shape: one warm opener, then 3 terse topic lines. No sub-questions, no timeboxes, no context Scott didn't give. If a topic needs a lookup (e.g. "slack messages to Aryan/Adam/James — search slack please"), do the lookup; don't pad the list.

## Stage 2 — Booking

Either Scott books or the counterparty books. No artifact to produce here; the calendar holds the event.

## Stage 3 — Write the prep doc before the call

This is where most Claude work happens, and where most failures happen.

**One Google Doc per person, not per meeting (Scott, 2026-10-30).** Before saying a topics doc doesn't exist, search Drive by the person's name and open any match, including the source doc linked from older prep files. A new call gets a new dated section at the top of that person's doc, never a new doc. Dated repo filenames are per call and say nothing about whether the shared doc exists. (Caught 2026-10-30: Claude said John Yan had no doc for the call, when "Scott/John Yan Links for discussion" had already surfaced in the Drive search.)

**Read [`agenda-style-corpus.md`](agenda-style-corpus.md) first.** It holds Scott-authored exemplars (positive bucket) and Claude-authored failures with explicit reasons (negative bucket). Pick 2-3 entries whose tags match the meeting type, use them as the format model, and audit your draft against the negative bucket before showing Scott.

Common tag combinations: `[discussion-topics] [peer-founder]`, `[discussion-topics] [advisor-1:1]`, `[discussion-topics] [investor]`, `[discussion-topics] [research-partner]`, `[agenda] [advisor-1:1]`, `[agenda] [customer]`, `[agenda] [team-internal]`, `[agenda] [investor]`.

### Match the format Scott asks for

- **Agenda** = prescriptive. Scott owns the meeting; numbered items, possibly time-allocated. Default: structured 1:1s with running threads, formal stakeholder meetings.
- **Discussion topics** (also "potential discussion topics," "topics for X," "links for X") = light. Scott provides context + raw URLs + ONE open-ended ask; counterparty drives. Default: peer / advisor chats.

If Scott says "discussion topics" and you produce a numbered timeboxed agenda with sub-questions, that's the John Yan v1 failure mode (negative bucket).

### Discussion-topics format

Use OUTLINE format with sub-bullets, NOT flat lines. 3-5 main topics, max 7. Each main topic can carry indented sub-bullets that elaborate context, links, or sub-questions. The nesting carries meaning — flattening loses structure.

**Number/letter outline markers, not dashes** (Scott, 2026-07-17): top-level topics numbered (`1)`, `2)`), sub-items lettered (`a)`, `b)`). No `-` bullets in topics docs. **Docs API mechanics:** in a Google Doc using native auto-numbered lists, never insert literal `1)`/`a)` characters into the list range (they stack onto the auto-numbering: "1. 1) Neolithic"). Either use the doc's native list formatting or insert plain paragraphs outside the list. This holds for every agenda or topics list Claude writes into a Google Doc, including ones with no existing list: build the outline with `createParagraphBullets` (leading tabs set the nesting level), never with typed "1." / "a." characters (repeat miss 2026-09-10 on the Control Tooling Sync agenda; Scott: "Why do I have to remind you to use Google Docs native outline format?"). And in a doc Scott is actively drafting in, don't insert Claude-drafted outlines at all: propose lines in chat, Scott types them (caught 2026-07-17 on the Leo topics doc; Claude's block was deleted and Scott's own bullets kept).

**Scott-only prep goes in his private "<Name> raw" Google Doc, not a repo file (Scott, 2026-10-26).** For a 1:1, the shared topics doc gets only counterparty-safe topics; Scott's private context (background, comp, questions only he should see) goes into his unshared raw doc for that person (e.g. "<Name> raw"), the same doc he takes call notes in. Find it by title in Drive (or ask for its link if he hasn't made one yet); don't create a parallel `*_prep.md` in `sw-prv` or here. Insert above anything Scott has already typed, and never edit his existing lines. (Caught 2026-10-26 on a 1:1 prep: "you should know by now I use the raw convention for my private docs.")

**Counterparty-readable vocabulary in any doc the counterparty may see.** No internal names or shorthand the counterparty doesn't know: "my wife," not her first name; org names over nicknames; nothing that requires Scott's context to parse. (Caught 2026-07-17 on the Leo topics doc: a line used Scott's wife's first name, assuming Leo knew who she was; Scott flagged it as a repeat failure mode.)

### Feedback redlines

Preserve the complete outline and links, and follow [R5's word-level redline rule](https://github.com/scottwofford/sw-prv/blob/main/requirements/personal/scott-response-req.md#r5-voice-fidelity-responses-sound-like-scott-would-have-written-them-not-like-ai).

### Minimalism (the most-repeated correction)

> "you're way too verbose and repetitive, and you're mixing topics across [sections] and [adding] questions that don't need to be asked at all. In general, you love adding stuff, but I want you to be thoughtful and minimalist, think about how to simplify and remove items, not add more bullets especially ones that are repetitive. Then the bullets themselves should be concise using the fewest number of words possible to communicate an idea."
>
> (Scott, 2026-06-17, retro on the Erin Robertson prep)

Operationalize this:

- **Remove before adding.** When you think a topic needs another bullet, first check whether an existing bullet already covers it. Default to cutting, not appending.
- **One idea per topic; don't mix.** If two sub-bullets restate the same point under different headers, merge them. A point lives in exactly one place.
- **Cut questions that don't need asking.** If Scott already knows the answer, or the counterparty's answer wouldn't change anything, drop the bullet.
- **Fewest words per bullet.** Tight noun phrases over full sentences. No voiceover, no "Question for X:" preamble.

Gold exemplar for a finished discussion-topics doc: Scott's [Erin Robertson topics](https://docs.google.com/document/d/1s5C4sNYYeJILgh43pzyUZncwXAd-fcqhjPA8NEacYmc/edit) (and its corpus entry).

### Audience cold-read gate (hard gate)

The counterparty reads the doc cold, without Scott's context. After drafting, re-read the doc as the counterparty and check every proper noun (person, org, program, doc) against THEIR context, not Scott's (Scott knowing who "Leo" is doesn't count):

- Would the counterparty recognize it from their own prior contact with Scott? If not, first mention carries full name + a short org/role gloss + a link (personal site, org site, or team page). Use the full name on every mention, never last-name-only shorthand (Scott, 2026-07-16).
- Link as many nouns as have a good landing page. This coexists with minimalism: links add no words.
- Every link must open for the counterparty. Find the readers from the doc's sharing settings (the checker lists them); if the doc is for a meeting and not shared yet, the readers are the meeting's attendees. Private GitHub repos (`luthien-org`, `sw-prv`, `linuxarena/meeting-transcripts`) 404 for anyone without access: link a public profile or a shared Google Doc instead, or leave the text unlinked. Run [`check_doc_private_links.py`](https://github.com/scottwofford/sw-prv/blob/main/scripts/check_doc_private_links.py) before calling a shared Google Doc done ([COE 2026-10-06](https://github.com/LuthienResearch/luthien-org/blob/main/process/coes/2026-10-06-private-repo-links-in-shared-docs.md)).
- Google Doc artifacts: links must render as real hyperlinks (blue). Text inserted via the Docs API is never auto-linked; apply `updateTextStyle` with `link` + underline + link-blue (#1155cc) to each link range. A raw pasted URL is a broken deliverable even when the URL is correct.

Caught 2026-07-16 on the Alexandra Bos topics doc: bare first names ("Leo", "Evan") with no gloss or links, plus raw non-clickable URLs. Scott: "you have to consider the audience! she probably won't know who Leo or Evan are so use last names and link to their personal sites."

### Anti-patterns (never produce unless the corpus has a positive entry doing the same thing for the same meeting type)

- Numbered timeboxes ("(1 min)", "(15 min)") in a discussion-topics doc.
- Pre-written sub-questions under a main bullet ("here are the 5 things to ask").
- "Frame swap" / "Reciprocity" / "Quick demo first" sections.
- Editorial wrappers on URLs ("(server returned 403)", "(team page)", "Scott shared on May 13").
- Inventing context Scott didn't give (LinkedIn pulls, full bios at the top).
- Em dashes anywhere.
- "Co-Authored-By: Claude" trailers in counterparty-facing artifacts (commit messages only).

## Stage 4 — The call: raw notes

During the call Scott may capture raw notes in a scratch doc. These are his, unedited, and feed the debrief. Don't reformat or "clean up" raw notes into prose; they are a source, like a transcript.

Reference shape: [Scott's raw call-notes doc](https://docs.google.com/document/d/1Qo2D5zrtuHO2MF6wJX4v86sJPm-YAmCNwKWPJTcFJvM/edit).

For a call whose home is this repository under [Meeting home](#meeting-home), the verbatim transcript (Plaud / Otter / Gemini) goes in `call-transcripts-plaud/`; when two sources exist, merge them into one authoritative transcript with ASR fixes annotated `[was: …]` (example: [2026-06-17_erin-scott.md](call-transcripts-plaud/2026-06-17_erin-scott.md)).

**Anti-pattern: waiting for Scott to point out a transcription error.** Treat machine transcription as a lead, not an authority. Before filing or deriving takeaways, proactively search for suspect names, numbers, roles, decisions, and terminology; resolve each against the best independent source available (a second capture, raw notes, calendar, email, chat, or primary public source). When evidence settles an error, correct the transcript with a `[was: …]` annotation and update every derived debrief or linked transcript record. Do not preserve ambiguity in a debrief once the correct reading is established. When a garbled passage could change a takeaway or action and a recording exists, re-transcribe that stretch with local Whisper before hedging or asking Scott to listen ([how](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/WORKFLOW.md#gotchas)).

**How to actually get the recording.** The export + speaker-tagging mechanics (Plaud Zapier auto-mirror to disk, Claude-in-Chrome speaker tagging, plaud-toolkit API, Otter MCP) live in the private [`transcripts/plaud/WORKFLOW.md`](https://github.com/scottwofford/private-claude-code-docs/blob/main/transcripts/plaud/WORKFLOW.md) (Scott-only repo; teammates: ask Scott). Always check **Plaud first**, Scott’s default: read the mirror at `~/build/sw3-google-drive/drive/2.2 Transcripts/Plaud raw/` and check live Plaud, including newest recordings by date/time if a name search misses. Then check **Google Meet / Gemini** for meetings Scott owns or where recording/transcription was enabled and a capture is accessible, using the calendar event’s attachment. **Always check the calendar event, and re-fetch it before concluding there is no Gemini capture** (Scott, 2026-09-24): Gemini attaches its doc late, sometimes hours after the call, and Drive searches and Gemini's notification email can miss a doc the event carries. A missing attachment means *not yet*. Do not assume every Meet call has a transcript. (Caught 2026-09-24: the tailwind-homework debrief shipped Plaud-only saying no Gemini capture existed, while the Notes-by-Gemini doc was attached to the event by 3:57pm.) **Otter last.** Search available captures before asking Scott which recorder he used.

## Stage 5 — Debrief after the call

The debrief produces **Key Takeaways + Action Items as numbered lists** (format in [`README.md`](README.md)); top-level items are numbered, with indented sub-bullets under each. Produce those items and stop. Show Scott the list. Minimalism applies here too — terse takeaways, no synopsis prose.

**The debrief is a committed repo file, never chat-only (Scott, 2026-07-31).** File it at `call-prep-agendas-debriefs/<Person>/YYYY-MM-DD_<TheirName>_debrief.md` (or in its other approved home under [Meeting home](#meeting-home)), commit + push, and open the GitHub URL; chat carries the link plus only what needs Scott's judgment (Trello triage, open decisions). "Show Scott the list" governs the no-auto-Trello-cards rule below, not the delivery medium. (Origin: the Miguel Brandão debrief was delivered chat-only and Scott had to ask for the file.)

### Sharing default: transparent, one version

Control Tower meeting content is shareable by default: Tyler (Aug 24) would "love it... if our Slack channel and all of our meetings were fully open to the public" ([meeting-transcripts README, R3](https://github.com/linuxarena/meeting-transcripts/blob/main/README.md)). Write one debrief for all audiences; redact only what the meeting-transcripts repo's [redaction rule](https://github.com/linuxarena/meeting-transcripts/blob/main/README.md#requirements) requires. Do not propose audience-specific versions or cross-audience approvals for ordinary meeting content. (Caught 2026-09-26: a review proposed a separate redacted Neolithic version of the Sep 25 JJ debrief; Scott: "I'd like to not have different versions of the debrief.") Publishing mechanics: [debrief publishing design](https://github.com/LuthienResearch/luthien-org/blob/main/process/debrief-publishing-design.md).

### One debrief in the approved home

The [Meeting home](#meeting-home) rule determines the repository. Once a meeting is in `meeting-transcripts`, its `4-takeaways-actions/` file is the canonical team debrief: do not create a duplicate in `luthien-org`.

When private passages require a restricted counterpart, keep that material in the appropriate private home and link the team debrief rather than duplicating unchanged findings. Scott-personal career and hiring material stays in `sw-prv`; do not disclose it to Luthien or Redwood merely to keep a meeting together. Preserve the unredacted source there. Reconcile any affected counterpart when shared findings change.

**Trello triage for a meeting-transcripts debrief happens in chat and on the cards Scott creates, never in a duplicate file.** The team file carries no Luthien-internal process text (Scott, 2026-09-10): no Trello-search preamble, Trello card links, staging notes, or Luthien-only action items; its action items link Linear or nothing. Report the Trello search result (what was searched, which live cards match) in the chat reply that links the debrief. (Caught 2026-09-10: the Trello-search preamble naming Scott's Personal board landed in the meeting-transcripts takeaways file. Caught 2026-09-15: a full luthien-org twin of the unredacted Yulia Volkova Sep 14 debrief was created just to hold the Trello triage; Scott: "anything redacted? if not, it should only live in meeting-transcripts".)

### Key Takeaways = new-to-Scott signal only

Capture what the **counterparty** contributed that Scott wouldn't already hold: their independent reads, pushback, estimates, decisions, rapport signals, and what they committed to do next. Scott was on the call, so write for the version of him reading the debrief weeks later — keep a bullet when the answer to "would Scott learn something from this?" is yes.

Write each round of takeaways from scratch off the transcript. Never reference or patch a prior version of the takeaways; re-derive them from the source so the framing reflects current understanding.

**A takeaway is what the reader needs to know, not what was said (Scott, 2026-09-10).** Test every sub-bullet against the reader of the notes (Scott in a month, a teammate who was not there): does it change what they know or do? If not, it is not a takeaway, however true or well-quoted. The usual failures record how the conversation went instead of what it produced: alternatives floated and dropped, reasoning narrated on the way to a position, examples given as illustration, context the reader already has, a counterparty's bare agreement. Amazon's version of the test: "Consider the readers: What do they want to know?" and "Is there data that is not relevant?" (Write Like an Amazonian workbook, Scott's copy); ex-Amazon shorthand: notes are "execution fuel, not documentation": decisions, open questions, action items ([How I Take Notes That People Actually Use](https://brettrobertmiller.substack.com/p/how-i-take-notes-that-people-actually)). Origin: the [Sep 10 Tyler debrief](call-prep-agendas-debriefs/Tyler-Tracy/2026-09-10_Tyler-Tracy_debrief.md), where takeaway 1 shrank from four sub-bullets to two quotes.

### Re-read the shared topics doc after the call (hard gate)

Counterparties annotate the shared topics/agenda doc during or after the call: for example, a counterparty typed funder links into the topics doc during the call. Before a debrief is done, re-fetch the live topics doc and reconcile it: (a) every call-time link AND every answer the counterparty typed into the doc is accounted for in Key Takeaways or Action Items (typed answers are counterparty testimony, same standard as transcript quotes — caught 2026-07-31 when Miguel Brandão's typed positions, including his bio correction and his opt-in deployment critique, were reconciled only after Scott asked); (b) doc annotations resolve ASR-garbled proper nouns (the transcript's "Exanti" was Ex-Ante, linked in the doc all along), so check the doc before flagging a name unverified. The prep-time snapshot of the doc is stale the moment the call starts. The same gate covers Scott's raw-notes doc when one exists: pull it and reconcile before the debrief is done — raw notes can carry whole topics the recording missed. **Precedence when raw notes and the ASR transcript conflict (Scott, 2026-08-28): when in doubt, trust Scott's raw notes over ASR.** His contemporaneous hearing wins by default; keep the ASR variant visible as a `[transcript heard: …]` note rather than erasing it, and escalate to Scott only when the two readings change a decision and neither can be verified elsewhere. (Origin: transcript "ecosystem things" vs raw-notes "Equistamp things", Aug 24.) The debrief links both docs in its transcript/sources section (format: [README §4](README.md)).

### Verify every org / title / name attribution before finalizing (hard gate)

ASR garbles proper nouns, and bios collide. Before a debrief is done, check each person's role, title, employer, and each org name against a primary source: the person's own org page, the authoritative topics doc the counterparty typed (their spellings/links override ASR), or the relevant [fund file](https://github.com/LuthienResearch/luthien-org/tree/main/fundraising/funds). Prefer the links the counterparty themselves pasted over what the transcript heard. When a primary source contradicts the transcript, fix it and surface the change to Scott; when a name collides with something already in Luthien's records (same org name, different firm), flag it rather than silently merge. (Caught 2026-06-26 in the Ryan Kidd debrief: ASR "Sequence" → **Sequent**, "RAI" → **FAR.AI**, a dropped **AE Studio**, and a "Juniper Ventures" on Boston Nyer's bio that is a different firm from the Juniper Ventures already in Luthien's pipeline.)

### Calibrate against recency bias

Don't promote the last-mentioned or newest item to "best" / "top" / "primary" just because it came up most recently or felt exciting. Rank by the weight the counterparty actually gave it across the whole call. (Caught 2026-06-26: a freshly-surfaced RFP was headlined "the best-fit new funder" when the counterparty's strongest, most-repeated emphasis was on a different, already-known path.)

### Write key takeaways like a macroeconomist (calibrate; no over-claims) (Scott, 2026-07-18)

Every takeaway is calibrated to the evidence behind it. The failure mode is upgrading a weak or fragmentary signal into a confident claim, especially about a person's internal state or a cause. Hedge to what the transcript actually supports: "a factor," "one consideration," "appears to," "as they sketched it," not "her real reason is X," "this is the mechanism," "the cause is Y." Never assert someone's "real" / "main" / "actual" reservation, motive, or intent unless they said it plainly; when a point is fragmentary or you had to interpret it, say so and quote the fragment rather than resolving it into a clean claim. A line the counterparty responded to with "so what's your point" is not yet a takeaway. Scrub every draft's key takeaways for these over-claims before showing Scott. (Caught 2026-07-18 on a personal-conversation debrief: an ASR-garbled "we need to raise money" fragment was written up as a confident "Luthien still needs to raise money" reminder, and a logistics factor was asserted as the other person's "real reservation" about travel; both were over-reads of the evidence.) This applies to transcript-debrief key takeaways in `sw-prv/transcripts/` too, not only call debriefs here. **It also applies at the roll-up/compression step:** when condensing per-meeting takeaways into a consolidated debrief, never drop an anecdote's resolution — compressing "she got a scare from a large spend email, but it turned out to be another team's usage" into "a large eval-spend alert went out during the runs" flips a resolved false alarm into an asserted incident. Re-check each compressed line against the full source bullet before shipping. (Caught 2026-08-26 on the Aug 24-25 Control Tower roll-up, exactly this example.)

### Quote the counterparty verbatim, don't paraphrase

When a takeaway turns on what the counterparty said, use their exact words in quotes, not a paraphrase. Scott reads the debrief weeks later and weights the counterparty's literal phrasing; a paraphrase silently editorializes. (Caught 2026-06-26: "the CG proposal 'looks really good'; adapt it lightly per funder" replaced with Ryan's verbatim "I looked over your CG grant proposal here; it looks really good" + "obviously you'd want to modify it a little bit for these different funders.")

### Link people and orgs to a profile/source; don't restate what a source-of-truth file already holds

Link every named person/org to a profile or source wherever one exists (LinkedIn, the org's team page, the [fund file](https://github.com/LuthienResearch/luthien-org/tree/main/fundraising/funds), a past-call transcript). And don't duplicate content between Key Takeaways and the detail sections: takeaways carry the call's new signal and verbatim quotes; the detail section carries mechanics; and when a source-of-truth file exists (a fund file, a tracked doc), link it instead of restating its contents. Only attribute a person to an org they actually belong to (caught 2026-06-26: "Agus at Kairos" was wrongly listed under CG contacts — he's at Kairos, and Ryan only named him as someone to ask).

### Check the source before proposing an action (hard gate)

Before writing an action bullet, open the source-of-truth doc/system and confirm the action isn't already done. If the live doc already addresses the feedback, say so and drop the action — don't propose work that's complete. (Caught 2026-06-26: an action to add a framing to a grant application was already covered in the draft, so it was not a live action.)

### Re-check Slack against every open action, every turn (Scott, 2026-10-06)

While working on a debrief's actions, before each status report or edit, search the Slack channels where the actions play out (#luthien, the relevant Redwood/Neolithic channels and DMs) for every open action in every debrief in play, and update statuses from what you find. A status checked earlier in the session is stale. (Caught 2026-10-06: check-in 4 action 9 was reported WIP after Matt's progress had already landed.)

### Waiting and scheduled states are not actions (Scott, 2026-08-18)

An action item is a concrete move Scott can execute, written verb-first with its trigger inline ("Send Miguel the outcome when he returns after Aug 24"). Two states masquerade as actions and never get their own bullet:

- **Waiting on a counterparty.** The ball in their court is status: a trailing sentence on the parent item with an as-of time ("Sevan's confirmation was outstanding as of Tue 3:25pm"), never a WAITING bullet. If the wait needs protection, write the failsafe action with a trigger date (the `process/CLAUDE.md` rule).
- **Already-scheduled events.** A booked meeting lives on the calendar; "NEXT: hold the call" is noise. If context helps, record it as an unlabeled status sentence.

Completed-action display and status labels follow the [shared completed-actions convention](https://github.com/linuxarena/meeting-transcripts/blob/main/4-takeaways-actions/AGENTS.md#completed-actions). That is the canonical rule; update it there rather than maintaining a second version here. Luthien’s Trello selection and approval rules below still apply.

### No speculative action items

Every action bullet names a concrete, owned next step (owner + what + ideally trigger/ETA). Drop "may resurface," "could become relevant," "worth keeping an eye on" items — a thing that might become an action later is not an action now, and it pads the list Scott has to triage. (Caught 2026-06-23: removed a "nonprofit-vs-PBC routing may resurface via Erin's team" bullet from the Erin debrief.)

**Don't route actions through someone who has said they're heads-down; check what they're doing first.**

### Search Trello BEFORE listing Action Items (hard gate)

For each candidate action, search the Luthien board (lists + `get_my_cards`) for a card that already covers it. Link the existing card inline; do not re-propose it as new. Flag only genuinely-new items as new. The board carries dozens of live cards (CG, MATS, Redwood, Apollo, advisor mechanics, etc.), so without this step the Action Items read as net-new when most are re-proposals.

This is a gate, not a suggestion: **do the search, and state what you searched.** Never write "not yet in Trello" without having actually searched. (Caught 2026-06-17: action items came out repetitive because the board wasn't searched first.)

**Check the card's owner (`idMembers`), not just its list.** A live card membered to a teammate (Paolo, Jai, Peter, etc.) is *their* work; never cite it as an "existing card" covering one of Scott's actions, and never let it suppress a genuinely-new Scott action. Note the owner inline when a teammate's card is topically adjacent. Resolve member IDs via `get_board_members`; "unassigned = Scott's" applies to reading, per skill `trello-conventions`. (Caught 2026-07-13 in the Evan Miyazono debrief: Paolo's "List of Questions for Sami" card was cited as related coverage for Scott's ask-Sami action.)

**A card in a Done list doesn't count as live.** Check each candidate card's list (`get_card` → `list.name`), not just whether a card exists. A Done card means that work is finished, so don't cite it as the "existing" card for a still-open action — the action is either complete or genuinely fresh. Cite only cards in live lists (Next Up, Doing, Backlog), and note when a related card is Done so Scott sees the prior attempt without mistaking it for active. (Caught 2026-06-26: the Longview, "send to Julian", MATS-founder-track, and two pitch-deck cards were all in Done; citing them as "existing" would have read as already-tracked when each action was actually fresh.)

**Check Scott's existing plans too, not just Trello (Scott, 2026-09-27).** Before listing an action, also check the non-Trello trackers that hold committed work: the Coefficient Giving application backlog in [`dev/OBJECTIVE.md`](https://github.com/LuthienResearch/luthien-org/blob/main/dev/OBJECTIVE.md#edit-backlog-not-yet-in-the-app) and the [Plan of Attack](https://docs.google.com/document/d/1w3wJMjb_VxlL6xJtdN8K0S8_IovuxCCwWaY5tjRphy0/edit). Also check what Scott said on the call itself. A plan Scott describes as his own ("by next week I hope to have a rewrite") is status, not a new action. Put such items in one "already on your plan" line that links the tracker, and fold any new input from the counterparty (a number, a name, a caveat) into that tracker item instead of opening a new action. Only moves the call created get numbered actions. (Caught 2026-09-27 on a debrief: three of four actions restated work already in the backlog.)

### Shape each action around the real next step

Action items aren't a transcription of everything mentioned; they're the concrete next moves Scott has to make. Shaping rules (all caught 2026-06-26 on the Ryan Kidd debrief):

- **Drop anything resolved live on the call.** If Scott already handled it during the conversation (corrected a stale link, answered the question), it's done, not an action — the live-call companion to "check the source before proposing an action."
- **Sequence against existing actions and relationships.** When a new step depends on another (e.g., a heads-up to an existing contact before approaching the new person they referred Scott to), state the order and link the existing live card for the dependency. Search Trello for relationship context, not just duplicate-detection.
- **Show dependent steps as sub-bullets.** When one numbered action contains two or more ordered steps, make the action the parent and list each step as an indented sub-bullet in execution order. Do not compress a sequence such as "send, wait, schedule" into one sentence. Keep independent messages as separate numbered actions per the next rule.
- **One message = one bullet.** Separate emails/DMs to separate people are separate tasks; never bundle multiple recipients into one action (split "send the deck to A and B" into two bullets).
- **Name the real cognitive step, which is often a decision, not execution.** For a list of leads/mentors/options, the action is usually "decide which (if any) to prioritize," not "reach out to all of them." Don't presume execution Scott hasn't committed to.
- **No action depends on someone else acting first; write the failsafe.** Canonical rule + example: [`process/CLAUDE.md`](../process/CLAUDE.md) (Scott, 2026-07-15, on the Leo debrief).
- **Propose the logical next step, not the final outcome.** Scope the immediate move, not the end goal: "evaluate fit and scope the effort to apply to X," not "pursue X"; "look at flights and clear travel with cofounders," not "be in SF." A decision is not the next step while its inputs are still missing: write the action that gathers the inputs, and let the decision become an action once they land. (Caught 2026-07-15: "Decide on a paid work-trial offer" jumped past the real next step: reply to the follow-up and get the missing inputs. Gold exemplar of next-step shaping with sub-steps: the [Evan Miyazono debrief](https://github.com/scottwofford/sw-prv/blob/main/personal/2026-07-13_evan-miyazono-atlas-debrief.md) action items, e.g. "Ping Sami: up for a 20-30 min call?" rather than "get Sami to vouch to CG.")
- **When the needed action is ambiguous, ground it in a verbatim quote.** If it's unclear exactly what to do or who owns it (who pings vs who emails, what the ask is), append the counterparty's or Scott's exact words rather than a paraphrase that bakes in a guess.

### Never auto-create Trello cards from a debrief

Scott reviews the proposed action-item bullets himself and triages each one: surface it to a new Trello card, knock it out live during the debrief, or drop it. That triage is a judgment call he keeps. This holds **even when the debrief's source card says "convert action items to Trello cards"** — that means "produce the bullet list for Scott to review," not "create the cards." Create cards only when Scott explicitly says so in the moment.

> "I have to look at the proposed actions myself before creating Trello cards ... I like to look at the key takeaways and the action items in bullet format first to confirm that no judgment calls are needed on what actually surfaces to a Trello card versus what we can just knock out right now during the debrief."
>
> (Scott, 2026-05-27)

**Where the rule lives.** Claude created two cards from the Leo debrief on 2026-07-15 before this folder-scoped file had loaded (folder CLAUDE.mds load on first touch of the subtree), so the rule also lives in the `trello-conventions` skill, required reading before any card work. There is no harness gate: Scott removed the permissions `ask` on card creation for good on 2026-09-15 ("trust fable / astra to re-measure instruction following adherence"), and adherence is measured from session logs instead; history and the measurement plan are in the [sw-prv changelog](https://github.com/scottwofford/sw-prv/blob/main/claude-md-changelog.md).

---

## Filing & naming

Filing and filename conventions (folder-per-person, `YYYY-MM-DD_<TheirName>_<type>.md`, multi-person/non-person edge cases at the root, transcript naming) live in [`README.md`](README.md#filename-convention). One Claude-specific exception: `agenda-style-corpus.md` is filed at the root, not per-person — it's a cross-counterparty reference, not a single-call artifact.

## Auto-maintenance loop

Three triggers fire during natural session work. Execute the action without prompting Scott:

1. **Scott rejects a Claude-drafted prep doc.** Signal: "didn't use it," "rewrote," "scrap," "that sucked," "too verbose," "my actual version was…" plus a pasted Scott version. Action: append BOTH versions to [`agenda-style-corpus.md`](agenda-style-corpus.md) negative bucket with a "Why it failed" section (reasons from Scott verbatim where given; otherwise from the diff).

2. **Scott authors a fresh agenda or discussion-topics doc.** Signal: a new file matching `*agenda*.md` / `*discussion-topics*.md` / `*topics-for-*.md` / `*links-for-*.md` appears in git, or Scott pastes one. Action: verify Scott authorship via the corpus-header heuristics; if verified, append to the positive bucket with format + counterparty tags.

3. **Authorship-verification gate.** Before adding ANY entry to the positive bucket, confirm Scott authored it (not Claude): no em dashes, terse bullets, no "Frame swap" / "Reciprocity" / templated "Who's Who" sections, no `Co-Authored-By: Claude`. When in doubt, mark "Mixed-or-unclear" and ask Scott rather than guessing.

Where prep docs and debriefs sit in the wider relationship flow (chronologies, People Database, action tracking): [relationship context architecture](https://github.com/LuthienResearch/luthien-org/blob/main/process/relationship-context-architecture.md).
