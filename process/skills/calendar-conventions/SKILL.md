---
name: calendar-conventions
description: Scott's Google Calendar conventions: query both calendars, free/busy flags, self-only events need no approval (and the hook that enforces it), Calendly bookings don't signal intent. Use for any availability check, "is it booked?", calendar event create/update, or finding a meeting's recording or Notes by Gemini.
---

> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy.

# Calendar conventions

Moved verbatim from CLAUDE.md on 2026-09-24; CLAUDE.md keeps a one-line trigger.

**Check a calendar event's free/busy flag before assuming it occupies Scott's time.** Calendar events carry a free/busy (transparency) status. A `transparent` / "free"-marked event (e.g. an FYI hold) does NOT block Scott; only `busy`/opaque events do. Read the flag before treating an event as a constraint on availability; never infer "busy" from the title or time alone. **Scott has two calendars and external invites land on either: `scottwofford3@gmail.com` (primary; Calendly/booking-page and most researcher invites, e.g. Yulia's Sep 14 call) and `scott@luthienresearch.org` (Luthien; Tyler's syncs, Scott-organized team meetings). Query BOTH on every availability or "is it booked?" check; one calendar is never the answer (Scott, 2026-09-08: "always check both").** Verified 2026-06-04 when Claude treated a 4-6pm event marked free/transparent as eating Scott's writing afternoon, twice, after even noting it was "marked free."

**The Calendar connector can read but not write the Luthien calendar (verified 2026-10-15).** The `mcp__claude_ai_Google_Calendar__*` connector is signed in as `scottwofford3@gmail.com`, which has read-only access to `scott@luthienresearch.org` (`accessRole: reader`; `update_event` returns "The caller does not have permission"). The personal local Google token is Docs/Sheets/Drive only (per `google-docs-editing`); the Luthien token's scopes are unverified because reading its file is blocked by a deny rule, so don't try to use it for Calendar. So for an edit to a Luthien-calendar event, don't retry: open the event in Chrome `Profile 1` and tell Scott the one change to make. Permanent fix (Scott's call): share the Luthien calendar with scottwofford3@gmail.com as "Make changes to events".

**Self-only calendar events need no approval (Scott, 2026-09-22).** Creating or updating a Google Calendar event whose only attendees are Scott's own accounts (or his wife) is pre-authorized. Just do it and report the link, with no confirmation question and no permission prompt. Only an event that would send an invite to someone else goes through a prompt, since that notifies another person. Enforced by the PreToolUse hook `~/.claude/hooks/calendar-self-only-autoapprove.sh` (local to this Mac, not in a repo) on `create_event|update_event`. Do not add those tools to `permissions.ask` in `~/.claude/settings.json`: an `ask` rule overrides the hook's allow and brings the prompt back (the root cause on 2026-09-22).

**Calendar bookings via Calendly do NOT signal user-vs-investor intent.** Scott uses the same Calendly intake link for both prospective Luthien users and prospective investors. Determine bucket from the introduction context (who introduced them, what was the email about, what's their LinkedIn/role), not from "they booked via the trial Calendly."

**A meeting's Gemini notes, transcript, and recording live on the calendar event (Scott, 2026-09-24: "always check the calendar event").** Fetch the event (`get_event`) and read its attachments before searching Drive or Gmail. Gemini attaches late, sometimes hours after the call, so a missing attachment means *not yet*: re-fetch the event rather than concluding there is no capture. Full procedure: [transcripts/plaud/WORKFLOW.md](https://github.com/scottwofford/sw-prv/blob/main/transcripts/plaud/WORKFLOW.md) (Google Meet / Gemini availability).
