---
name: gmail-search-heuristics
description: Search past Gmail correspondence efficiently. Default search order for finding past messages with a specific person — domain over name, subject keywords, company name fallback. Use when searching Gmail for emails with investors, partners, prospects, or any external counterparty. Avoids the personal-name false-positive trap and the from:scott@luthienresearch.org sent-thread blind spot.
---

> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/skills/gmail-search-heuristics/SKILL.md (private). This copy is a redacted mirror and may lag behind it.

# Gmail Search Heuristics

Default search order when looking for a past message with a specific person:

## 1. Counterparty's email domain or address — first

Personal names like "Nick Fitz" return false positives (e.g., "Fitzpatrick" in unrelated emails). Use the domain or a partner sharing the domain instead:

- `to:name@fund.example` — direct address
- `griff` — partner sharing the domain (lands the thread in one query)

## 2. Subject keywords or distinctive body phrases — second

Project name, specific dollar figure, LOI count, etc.

## 3. The other party's company name — fallback

`juniper`, `engineering capital`, `realpage`, etc.

## What to avoid as primary searches

- **Workspace-sent searches through the personal Gmail connector alone** miss outgoing Luthien mail. On local Claude Code/Codex, use the separately authenticated `gmail-luthien` server for `scott@luthienresearch.org`; use `gmail-sw3` and `gmail-sw4` for the two personal accounts. Verify the selected server identity. Web/mobile account coverage must be checked independently.
- **Personal name strings** — false positives (Fitz / Fitzpatrick, Pan / Pancho).

## A null result is NOT evidence the email wasn't sent

The personal claude.ai Gmail connector can miss outgoing Workspace mail. That limitation is not a lack of access through the separately authenticated local Luthien server. Never tell Scott an email "wasn't sent" or mark a send "overdue/pending" based on a null Gmail search, and never re-challenge after he says he sent it. If Scott says he sent it, it's sent. (Per CLAUDE.md highest-emphasis rule #1: trust Scott's direct assertions over tooling; a null tool result is not evidence of absence.) Verified 2026-05-27 on a Seldon intro Claude wrongly flagged as not-sent.

## Cross-channel message status

Do not assume a relationship's messages are all email. Before "no reply," "not sent," or a follow-up suggestion, check the other channels the relationship uses; on this Mac, Beeper covers WhatsApp, Signal, iMessage and more ([inventory](https://github.com/scottwofford/sw-prv/blob/main/setup.md#beeper-message-access); rule: [R3](https://github.com/scottwofford/sw-prv/blob/main/requirements/personal/scott-response-req.md#r3-truth-seek-with-calibrated-uncertainty-verify-before-asserting-cite-primary-sources-never-fabricate)). Email-only absence is not a cross-channel conclusion.

## Iteration rule

If the first search returns nothing or noise, try a different axis (different domain, different subject, switch from name to company) rather than tightening the same one.

## Context for the rule's existence

Real wasted-time incident: ~5 min of failed searches for a Nick Fitz / Juniper Ventures email; `griff` would have found it in one query (Griff Foxley shares the domain).
