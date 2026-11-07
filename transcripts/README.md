# Transcripts

Merged, speaker-attributed transcripts of Luthien contributors meetings: meetings run for the contributors access level, such as contributor onboarding + Q&A. Each file combines every available capture of one meeting (Google Meet's Gemini transcript, Plaud, local Whisper) into a single transcript and records what the speech recognition got wrong.

The recordings and Notes by Gemini docs for the same meetings are indexed in [`meetings/`](../meetings/README.md). A meeting with anything on the exceptions list there (exact pay or funding figures, NDA material, performance management, things shared in confidence, unreleased security findings) stays private and is not filed here.

## File name

`<YYYY-MM-DD>_<slug>.md`, using the meeting date. Example: `2026-10-29_luthien-contributor-onboarding-qa.md`.

## File format

```markdown
# <YYYY-MM-DD> <Meeting title>

**Date:** <Weekday, Month D, YYYY>, <start time> Pacific, <duration>
**Participants:** <full names>
**Recording:** <link>  ·  **Notes by Gemini:** <link>

## Sources
| Capture | Supplied | Coverage | Authoritative for |
|---|---|---|---|
| Gemini Transcript tab (<link>) | words, speaker names | full | names |
| Plaud | words, timestamps | full | timestamps, wording tie-break |

**Speaker map:** <how each speaker was identified, for example "Speaker 2 = Jane Doe (Gemini names)">

## Transcription fixes

### Errors fixed
| Time | Heard (capture) | Fixed to | Evidence |
|---|---|---|---|
| 00:12:40 | "Lucian" (Plaud) | Luthien | Gemini transcript; org name |

### Uncertainties
| Time | Passage | Best reading | Why unsure |
|---|---|---|---|
| 00:31:05 | "[inaudible] eval set" | "the control eval set" | crosstalk; captures disagree |

## Transcript

**Jane Doe** [00:00:12]: ...
```

Rules:

- **Real names on every turn.** Resolve `Speaker N` labels using the Gemini names, Plaud's label for Scott, and context. If a speaker can't be identified, name them by role ("Attendee 3") and list them under Uncertainties.
- **Mark fixes inline too.** Each fix in the body carries `[was: <heard text>]` right after the corrected words, so a reader sees it in place.
- **Use only the Gemini Transcript tab.** The Notes and summary tabs are paraphrases, never a source for wording.
- **The body is verbatim.** Annotations go in `[brackets, italic]`. Summaries and action items do not go in this file.
