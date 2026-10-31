> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/requirements/cross-surface-context-mgmt-req.md (private). This copy is a redacted mirror and may lag behind it.

# Cross-Surface Claude Context Management Requirements

**Owner:** Scott
**Last updated:** 2026-09-14
**Method:** [luthien-org canonical format](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/2-versions-requirements/README.md).
**Feedback source:** Scott's direct usage of Claude across surfaces. Primary logs in [`../session-logs/`](../session-logs/).

---

## Epic

<u>Continuity or honest absence.</u> When I move between Claude surfaces, I want either to pick up where I left off, or be told clearly that the new surface doesn't have the prior context. "System asserts something stale or out-of-context with confidence" is worse than "system says it doesn't know."

---

## Requirements (user stories that ladder up to the Epic)

| # | Requirement (problem only) | Current state | Key evidence |
|---|---|---|---|
| **R1** | <u>Continuity across surfaces.</u> When I open a Claude chat on any device, it should know what I did on prior surfaces. | Partial. Claude Code ↔ Desktop continues via local filesystem MCP. claude.ai web ↔ mobile via shared backend. Code → mobile from cold has no view of auto-memory or recent session logs. | [Mobile session evidence](../session-logs/2026-04-29_thread-prioritization-context-pull.csv): mobile blocked because session-log push hadn't happened. |
| **R2** | <u>Honest absence and verify-before-asserting.</u> When the system doesn't know something, it should say so. When the system thinks it knows something time-sensitive or specific (a date, a name, a status), it should verify before asserting, not assume from stale context. | Unsatisfied. Claude has woven cross-track content into work chats; asserted stale dates with confidence; confused similarly-named entities; fabricated scene details Scott hadn't described. | [Apr 27 transcript](../session-logs/2026-04-29_thread-prioritization-context-pull.csv): personal content surfaced in work chat unflagged; Scott responded with an expletive. [Daily State](../session-logs/2026-04-29_thread-prioritization-context-pull.csv): created and deleted within 90 minutes after confidently presenting stale data. Investor priority claude.ai thread: stamped a date from 8 days prior on a fresh response. Another claude.ai thread: timezone confusion + name conflation + invented scene detail. |
| **R3** | <u>Loaded-context surfaceability.</u> I should be able to ask any Claude chat "what context have you loaded?" and get an accurate answer. | Unsatisfied. No first-class introspection surface. Claude often answers from inference, not actual knowledge. | [Connector test](../session-logs/2026-04-29_thread-prioritization-context-pull.csv): mobile didn't flag missing connectors (Slack `not_installed`, Trello no first-party connector). |

---

---

## Solution shapes ruled out

Approaches that have been considered and rejected. Future sessions should not re-propose these without addressing the falsification. Headlines are load-bearing; sources at the bottom of each entry are mostly for Claude.

### Project-scoped context loading

Untestable as a mechanism for satisfying mode-bleed. The proposal was that per-project Instructions would prevent personal content from surfacing in work chats, but no validation path existed; the proposal was relegated from a requirement to a design principle and then falsified when the actual mode-bleed failure (Apr 27 — personal content surfaced unflagged in a work chat, prompting an expletive from Scott) proved the project-scoping wasn't enforcing what it claimed to enforce.

*Source: /devil iteration that surfaced the lack of a falsification path; [Apr 27 transcript in session log](../session-logs/2026-04-29_thread-prioritization-context-pull.csv).*

### Project-scoped isolation as prioritization mechanism

Real prioritization requires choosing BETWEEN modes within a single attention window. Projects cannot isolate what attention has to prioritize. Concrete falsification: a message from my wife arriving the same hour as an investor follow-up — both compete for the same attention budget regardless of which "project" each is filed under. Per-project isolation only works if the underlying user has parallel attention budgets per project, which is not the case for a solo-founder workflow.

*Source: [`../claude-ai-project-knowledge/architecture.md`](../claude-ai-project-knowledge/architecture.md), project-scoped isolation note + 2026-05-01 falsification.*

### Daily State Drive doc as cross-surface context bridge

A daily-refreshed Drive doc to bridge Claude Code → claude.ai mobile context was adopted, then deleted within ~90 minutes of creation after it confidently presented stale data on its first read. Snapshot rot pattern: any derived doc that duplicates source data starts decaying the moment the source data changes. The right substrate for cross-surface context is the source systems themselves (Gmail / Slack / Trello / Drive reference docs) queried at chat time via account-level claude.ai connectors, not derived snapshots.

This is the canonical example of why source-system primacy ([`personal/scott-response-req.md`](personal/scott-response-req.md) Tenet 4) generalizes across data, rule definitions, and identity facts — same failure mode in all three.

*Source: [`../claude-ai-project-knowledge/architecture.md`](../claude-ai-project-knowledge/architecture.md), Daily State adoption + reversal.*

---

## Acceptance criteria

Per incident, binary Y/N:

- **R1** satisfied? Did the new surface know what prior surfaces did, or pull it via accessible source?
- **R2** satisfied? When the system didn't have context, did it say so? When the system asserted a time-sensitive or specific fact (date, name, status, dollar amount), did it verify before asserting?
- **R3** satisfied? Could Scott ask "what do you know about my situation?" and get an accurate inventory of what's loaded vs missing?

Aggregate = % satisfied over a measurement window. Track in session logs.

---

# Appendix

## A. Surface capability matrix

R1 + R2 are bounded by which tools and connectors are wired on the current surface. Where channels are missing, R2 (honest absence) is the load-bearing requirement: Claude must enumerate which channels it can and cannot see before asserting. Updated empirically per surface. Lens: tool/connector × surface for any Claude response behavior.

For read/write capability per source channel in the fundraise-database build (different lens: source × read/write, scoped to that pipeline), see [`luthien-org/fundraising/fundraising-db-requirements.md` § Tool/MCP boundaries](https://github.com/LuthienResearch/luthien-org/blob/main/fundraising/fundraising-db-requirements.md#toolmcp-boundaries-as-of-2026-05-01). Different consumer (fundraise-db design phase vs cross-surface Claude behavior); both load-bearing.

### Surfaces tracked

- **desktop-mac**: Claude Desktop on macOS with local MCP servers (Filesystem, iMessage, Office by Anthropic, Trello LOCAL DEV, Mac control, Chrome bridge)
- **mobile-ios**: Claude iOS app
- **web-claudeai**: claude.ai in any browser, no extension
- **chrome-extension**: Claude in Chrome side panel (extension active)
- **claude-code**: Claude Code CLI (laptop)
- **codex-local**: Codex on Scott's configured Mac; message access covered separately below.

### Capability matrix

Message access is maintained in [Current message access](#current-message-access), including Codex. Other cells derive from the dated probes below; re-probe before relying on them. Technical availability never authorizes sending messages.

| Tool / connector | Category | desktop-mac | mobile-ios | web-claudeai | chrome-extension | claude-code |
|---|---|---|---|---|---|---|
| GitHub Integration | cloud-MCP | ✅ Connected (not yet probed) | ❓ | ❓ | ❓ | n/a (uses native git via Bash) |
| Gmail | cloud-MCP | ✅ both accounts queryable | ⚠️ personal-only | ✅ verified (account scope not explicitly tested) | ❌ verified | ✅ personal + Luthien + sw4 local servers |
| Google Calendar | cloud-MCP | ✅ verified | ✅ verified (9 calendars incl both accounts) | ✅ verified (9 calendars incl both accounts) | ❌ verified | ✅ via MCP config |
| Google Drive | cloud-MCP | ✅ verified | ⚠️ personal-only | ✅ verified | ❌ verified | ✅ via MCP config |
| Trello | LOCAL DEV (custom MCP, desktop only) | ✅ desktop only | ❌ verified | ⚠️ available in registry, not connected | ❌ verified | ✅ via MCP config |
| Filesystem | local-MCP (DESKTOP) | ✅ verified | ❌ verified | ❌ verified (sandbox `/mnt/*` only, not Mac FS) | ❌ verified | ✅ native (Bash, Read, Edit, Write) |
| Read and Send iMessages | local-MCP (DESKTOP) | ✅ available, not directly probed | ❌ verified | ❌ verified | ❌ verified | ✅ read via Beeper (see Current message access) |
| Word/Excel/PowerPoint by Anthropic | local-MCP (DESKTOP) | ✅ available, not directly probed | ❌ verified | ❌ verified (replaced by `/mnt/skills` python-pptx/openpyxl/python-docx via bash) | ❌ verified | ❌ |
| Control your Mac (osascript) | local-MCP (DESKTOP) | ✅ available, not probed | ❌ | ❌ | ❌ | ❌ (would require osascript via Bash) |
| Control Chrome | local-MCP (DESKTOP) | ✅ available, not probed | ❌ | ❌ verified | ❌ verified (extension has its own browser tools, NOT Control Chrome MCP) | ❌ |
| Claude in Chrome (extension, native browser tools) | extension | ✅ via desktop bridge | ❌ | ❌ verified | ✅ native (read_page, find, computer, navigate, tabs_context, tabs_create, form_input, javascript_tool, read_console_messages, read_network_requests, gif_creator, etc.) | ❌ |
| web_search / web_fetch | Anthropic-built | ✅ verified | ✅ verified (9 results) | ✅ verified (9 results) | ❌ verified | ✅ via WebSearch / WebFetch |
| image_search | Anthropic-built | ✅ likely | ✅ available (untested) | ✅ available (untested) | ❌ | ❌ |
| bash_tool / computer-use sandbox | Anthropic-built | ✅ verified | ✅ verified (Linux 6.18.5 VM, Python 3.12.3, allowlisted egress) | ✅ verified (same Linux 6.18.5 sandbox) | ❌ verified | ✅ native (Bash) |
| conversation_search | Anthropic-built | ✅ verified | ✅ verified | ✅ verified | ❌ verified | ❌ |
| recent_chats | Anthropic-built | ✅ verified | ✅ verified | ✅ available | ❌ verified | ❌ |
| memory_user_edits | Anthropic-built | ✅ likely | ✅ available | ✅ available | ❌ | ❌ (Claude Code uses auto-memory + CLAUDE.md instead) |
| Native iOS event_* / reminder_* / calendar_search_v0 | Anthropic-built (iOS) | ❌ | ✅ verified (parallel to Google Calendar MCP) | ❌ | ❌ | ❌ |
| Browser-control (read_page, find, computer-tab, javascript_tool, gif_creator, etc.) | extension-native | ✅ via desktop bridge | ❌ | ❌ | ✅ verified | ❌ |

Legend: ✅ verified working · ❌ verified missing · ⚠️ partial / scoped · ❓ not yet probed · "likely" = inferred from architecture, not directly probed.

**Gmail account scope.** On local Claude Code/Codex, route reads to the configured account-specific `gmail-sw3`, `gmail-luthien`, and `gmail-sw4` servers and verify identity. The personal claude.ai Gmail connector's Workspace-sent blind spot does not apply to a separately authenticated Luthien server. On web/mobile, verify the connector's own account coverage; a negative personal-mail search does not establish absence in Workspace Sent. See [Gmail search guidance](https://github.com/scottwofford/sw-prv/blob/main/skills/gmail-search-heuristics/SKILL.md).

**Calendar `create_event` drops `location` (verified 2026-06-22 on claude-code, Camp CRAZ events).** The Google Calendar connector's `create_event` silently ignores the `location` field: the call succeeds and returns the event, but location is never set and no error is raised. Create, then call `update_event` to set location (it honors the field). Likely affects other optional fields too; treat silent field-drops as a class. Fuller quirk list (Gmail attachment bytes, gdrive scope/append limits): [`connector-quirks.md`](../connector-quirks.md).

**Drive write mode (asymmetric capability, verified 2026-05-09 on claude-code).** The matrix's ✅ for Google Drive collapses two very different capabilities. **Read** works on all supported file types (`read_file_content`, `download_file_content`, `search_files`, `get_file_metadata`, `list_recent_files`). **Write** is severely limited: native Google Doc append-to-end via `mcp__gdrive__append_to_document` is the only direct edit operation; create-new via `mcp__claude_ai_Google_Drive__create_file` works in folders where the OAuth principal has write permission (returned "User cannot add children to the specified folder" on the Prompt Eng folder); copy via `mcp__claude_ai_Google_Drive__copy_file`. **No edit / replace / mid-doc insert. No delete or trash. No write at all on .docx files** (`append_to_document` rejects with "This operation is not supported for this document. The document must not be an Office file."). Implication: Claude-authored content that needs revision over time must live in github, not Drive. Drive writes are appropriate only for one-shot append to existing native Google Docs, or net-new doc creation in OAuth-writable folders. The binding default is in [scott-response-req.md R9](personal/scott-response-req.md).

**Correction (verified 2026-06-14).** The append-only / "no mid-doc insert" limit above is the MCP **tools** only. Via python reusing the gdrive MCP OAuth token (`~/.config/mcp-gdrive/credentials.json`; scopes `spreadsheets documents drive.readonly`; identity `scott@luthienresearch.org`), native Google **Docs** edit fully through the Docs API (`documents.batchUpdate` — insert-at-index, delete-range, replace-all, formatting) and **Sheets** through gspread (`update_cell` / `batch_update`). Demonstrated by deleting a mid-doc line via `replaceAllText` (`occurrencesChanged: 1`). Still no write on Office files (`.docx`/`.xlsx`); the Docs/Sheets APIs only edit native Google types. So Claude-authored content that needs revision over time CAN live in a native Google Doc/Sheet, not only github — github still wins where git diff history is the point. Auth copy pattern: [`luthien-org/fundraising/pipeline/auth.py`](https://github.com/LuthienResearch/luthien-org/blob/main/fundraising/pipeline/auth.py). Full detail in [`../claude-ai-project-knowledge/architecture.md`](../claude-ai-project-knowledge/architecture.md) (2026-06-14 decisions).

### Verified allowed directories (desktop-mac, Filesystem MCP)

- `/Users/scottwofford/Library/CloudStorage/GoogleDrive-scottwofford3@gmail.com/.shortcut-targets-by-id/129u3BtHRFBeILTbIFf1N2X-NlyphvCoO/Luthien`
- `/Users/scottwofford/Dropbox`
- `/Users/scottwofford/build`
- `/Users/scottwofford/Downloads`
- `/Users/scottwofford/Desktop`

### Canonical local asset paths (desktop-mac, claude-code)

Within the verified allowed directories above, these specific locations hold durable Claude-asset content that recurs across context-restoration requests. Treat as known addresses; do not discover via search.

| Asset | Path | Format | Filename pattern |
|---|---|---|---|
| Claude Code session logs (~330+ files, Dec 2025–present) | `~/build/luthien-private-session-logs/` | named CSV | `YYYY-MM-DD_topic-slug.csv` |
| claude.ai chat backups, human-readable index | `~/build/claude-ai-sync/conversations/by-name/` | Markdown | `<chat title>.md` |
| claude.ai chat backups, raw | `~/build/claude-ai-sync/conversations/` | Markdown | `<uuid>.md` |
| Luthien Drive sync log | `~/Library/CloudStorage/GoogleDrive-scottwofford3@gmail.com/.shortcut-targets-by-id/129u3BtHRFBeILTbIFf1N2X-NlyphvCoO/Luthien/sync.csv` | CSV | `sync.csv` |
| Requirements + ops docs (this repo) | `~/build/private-claude-code-docs/` | git repo | various |

Sync mechanisms: `~/build/claude-ai-sync/sync-claude-ai.sh` runs the claude.ai chat backup; `~/build/luthien-private-session-logs/sessions_to_csv.py` produces the Claude Code CSVs.

### Context restoration SOP

When the user issues a context-restoration request — phrasings include "look at logs," "get context on X," "where were we," "review past chats about Y," "before I take this on the road" — execute the following:

1. **Extract scope.** Date (today / last N days / specific date) and topic (current chat topic OR explicit topic from the request).
2. **Filter at the filesystem level.** Use `ls ~/build/luthien-private-session-logs/ | grep <date-or-topic>` (or equivalent for the other canonical paths) rather than listing the directory in full. Per [`personal/scott-response-req.md`](personal/scott-response-req.md) R13 (filter chat output for signal), no full directory dumps to chat output.
3. **Read at most three candidates.** If filtering yields more, name the candidates in prose and ask which to read.
4. **For mobile handoff, materialize content inline as text in the chat.** Filesystem MCP is desktop-only per the matrix above, so file references do not survive the surface jump even when the same chat opens on mobile. Inline summary is the bridge; file paths in chat output are not.

The first three steps apply to any context-restoration request. Step 4 is specifically how output discipline (per R13 in `scott-response-req.md`) cashes out for R1 when a mobile handoff is signaled.

### Current message access

| Source | Local Claude Code and Codex on Scott's configured Mac | Other surfaces |
|---|---|---|
| WhatsApp, Signal, iMessage, Facebook Messenger, Instagram, LinkedIn messages, X, Beeper | Sample discovery, message reads, and literal search verified through Beeper on September 14, 2026 | No inherited localhost access; verify a separate connection |
| Redwood Research Slack | Two identities. Beeper holds Scott's Redwood guest account: internal channels (devops, linuxarena-devs) and DMs, senders rendered as Matrix IDs, no thread tool, initial sync still backfilling on September 14, 2026. `slack-redwood` holds his Seattle AI Safety identity and reads the Redwood channels shared via Slack Connect (linuxarena-general, linuxarena-aio, linuxarena-lab-notes, redwood-0labs, ext-redwood-luthien, redwood-api-attack-collab, cmft_to_ctower) with resolved names and thread reads | Verify workspace-specific access |
| Seattle AI Safety Slack | `slack` and `slack-redwood` servers (same identity) | Verify connected workspace on that surface |
| High Impact Professionals Slack | `slack-hip`, registered in both local clients. Simultaneous HIP/Seattle identity, channel, history, search and HIP thread checks passed September 22, 2026; [connection details](https://github.com/scottwofford/sw-prv/blob/main/setup.md#slack-lookup-preference). Existing sessions may need reconnect/restart. | No inherited local connection |
| Neolithic Slack | `slack-neolithic`, registered in both local clients. Six simultaneous Neolithic/HIP/Seattle identity, channel, history and search checks plus Neolithic thread reads passed September 22, 2026; [connection details](https://github.com/scottwofford/sw-prv/blob/main/setup.md#slack-lookup-preference). Existing sessions may need reconnect/restart. | No inherited local connection |
| Other Slack workspaces | Verify each remaining workspace separately. | Browser sign-in alone is not agent access |
| Phone/FaceTime logs, native Mail.app | Not established by the Beeper audit | Verify separately |

**Before reply/sent/follow-up claims**, query the corresponding live source, identify the ask, and read subsequent incoming/outgoing messages, thread replies, and enough history pages to cover the interval. If the channel is unspecified, check plausible channels from the relationship's history. Cite positive evidence; qualify any absence claim by the actual sources and interval checked. Empty results or incomplete access mean unverified status, not "no reply." Scott's direct confirmation is stronger than a tool-null. When asked "did I send X?" or "have I followed up?", explicitly enumerate which channels you can and cannot see and assert only within that visibility window; never make an absence-of-send claim without naming the caveat. This binds every agent, including agents without Beeper.

`get_accounts` omits iMessage despite working chat discovery and reads, and iMessage chats are not name-searchable: participants appear as opaque hashes and titles are phone numbers, short codes, or group names. Locate them by known number, group name, or a literal-word message search, then `list_messages`. Empty history with `hasMore: true` and null cursors means the chat is not yet synced (Beeper rate-limits the initial backfill; troubleshooting in setup.md), not that it is empty. Read access never authorizes sending messages.

Implementation, permissions, troubleshooting, and the nine-network audit: [Beeper message access](https://github.com/scottwofford/sw-prv/blob/main/setup.md#beeper-message-access). Primary evidence: [September 14 access session](https://github.com/scottwofford/sw-prv/blob/main/session-logs/2026-09-14_whatsapp-signal-access-codex.csv).

### `tool_search` blind spot rule

`tool_search` returning "no matching tools found" does NOT mean the tool is absent on the current surface. Verified failure case (desktop-mac): `tool_search "filesystem"` returned no matches, but `Filesystem:list_allowed_directories` direct call worked and returned 5 paths. Either `tool_search` only returns deferred (not-yet-loaded) tools, or certain local MCPs register without being in the searchable catalog.

**Rule:** before asserting "tool X is unavailable on this surface," attempt the direct namespace call. If the call name does not exist or returns a clear "tool not found" error, the tool is absent. If `tool_search` returns nothing but the direct call works, the tool is present and `tool_search` was unreliable.

### Historical per-surface probe evidence

These dated observations explain earlier failures, not current blanket access limits. Use the current message-access table and live checks for status claims.

**desktop-mac** (Claude Desktop on macOS). Verified via direct probe: Google Calendar (5 tools loaded), Gmail (`list_labels` returned 14 labels; queries hit both `scott@luthienresearch.org` and `scottwofford3@gmail.com` from a single call), Google Drive (`list_recent_files` returned 3 files including Roberto Bandarra meeting notes), Filesystem (5 Mac paths returned, NOT discoverable via `tool_search`), web_search (9 results), bash_tool (`echo hello` returncode 0), conversation_search ("luthien" returned 3 past chats), recent_chats. Connectors panel confirmed: GitHub Integration `Connected` (cloud-MCP); Gmail / Calendar / Drive cloud-MCPs; Trello `LOCAL DEV`; Filesystem / iMessage / Office / Mac control / Chrome control all `DESKTOP`; Claude in Chrome appears twice (cloud `INCLUDED Beta` + desktop-bridged 22-tool version).

**mobile-ios.** Source: [`../session-logs/2026-05-04_surface-capability-probes.csv`](../session-logs/2026-05-04_surface-capability-probes.csv). `bash_tool` runs on real Linux 6.18.5 x86_64 VM with allowlisted egress (PyPI/npm/GitHub/Anthropic API/Ubuntu repos), Python 3.12.3 callable from phone; `web_search` + `conversation_search` + `recent_chats` all verified working; Gmail / Calendar / Drive cloud MCPs all loaded via `tool_search` and direct-called; Drive auth confirmed personal (`scottwofford3@gmail.com`), not Workspace; Calendar `list_calendars` returned 9 calendars including both `scott@luthienresearch.org` and `scottwofford3@gmail.com`. Native iOS tools present in parallel to cloud MCPs: `event_create_v0/v1`, `event_search_v0`, `event_update_v0`, `event_delete_v0`, `calendar_search_v0`, full `reminder_*` family, `places_search` + `places_map_display_v0`, `chart_display_v0`, `recipe_display_v0`, `message_compose_v1`, `ask_user_input_v0`. Verified-missing: Filesystem, iMessage, Trello, Chrome / browser, Office MCPs, Slack/GitHub/Notion/Asana. Surprise: `tool_search` is fuzzy + Gmail-biased — single call insufficient to confirm absence (had to query "drive" with multiple phrasings to surface `list_recent_files` and `search_files`); reinforces the `tool_search` blind spot rule. Confidence (claude self-rating): 80%.

Mobile also has a personal-only Gmail OAuth scope: search returns `scottwofford3@gmail.com` only, not `scott@luthienresearch.org`. Single-account limitation also observed in earlier probes.

**web-claudeai** (Code Execution + File Creation enabled). Source: [`../session-logs/2026-05-04_surface-capability-probes.csv`](../session-logs/2026-05-04_surface-capability-probes.csv). Surface fingerprint identified by: `bash_tool` runs in Linux 6.18.5 sandbox with `/mnt/user-data/uploads`, `/mnt/transcripts`, `/mnt/skills/{public,examples}` mounted; network egress allowlisted (curl to `api.anthropic.com` works, arbitrary domains blocked); zero browser-control tools (rules out chrome-extension); no Filesystem/iMessage MCPs (rules out desktop-mac); full consumer suite present + `bash_tool` excludes mobile-only-without-bash framing. Verified-working: `bash_tool` (Python 3.12.3 + Node v22.22.2 in container); `view`/`create_file`/`str_replace` (sandbox FS rooted at `/mnt/`); `web_search` (9 results); `conversation_search` (returned 2 luthien chats); Google Calendar `list_calendars` (9 calendars incl both Scott accounts + Ping-Scott-Alert + Pike13); Gmail `list_labels` (INBOX, Banking, News, AMZN Consumer, etc.); Google Drive `list_recent_files`; `search_mcp_registry` (returned Notion, Slack, Egnyte, Shopify, Uber Eats, Thumbtack, Three.js — all `installState: "not_installed"`). Skills available at `/mnt/skills/public` for docx/pdf/pptx/xlsx + `frontend-design` (covers Office MCP absence via Python in `bash_tool`). Anthropic API in Artifacts (Sonnet 4 callable, can attach Calendar/Gmail/Drive MCP URLs). Verified-missing: Claude in Chrome / Control Chrome (browser MCPs); Filesystem MCP (Mac local FS — sandbox `/mnt/*` is separate); iMessage; Office MCPs (replaceable via skills). Confidence (claude self-rating): 92%.

**chrome-extension** (Claude for Chrome extension). Source: [`../session-logs/2026-05-04_surface-capability-probes.csv`](../session-logs/2026-05-04_surface-capability-probes.csv). Surface fingerprint: real Chrome 147 on macOS (UA verified via `javascript_tool`); tab context delivered via `<system-reminder>` with `availableTabs`/`initialTabId`; tools scoped to a Chrome tab and require `tabId` parameter. Verified-working: `read_page`, `find` (returned 3 refs on claude.ai tab including input/stop/attach buttons), `computer` (browser-tab-scoped click/type/scroll/screenshot/key/hover/zoom — NOT OS-level), `navigate`, `tabs_context`, `tabs_create`, `form_input`, `get_page_text`, `javascript_tool` (evaluated `document.title`/`location.href`/UA), `read_console_messages`, `read_network_requests`, `resize_window`, `upload_image`, `file_upload`, `gif_creator` (record→export browser session), `update_plan`, `turn_answer_start`, `browser_batch` (chains steps in one round-trip). Critical verified-missing: **`tool_search` itself is absent** on this surface (so the `tool_search` blind spot rule is moot here — there is no discovery layer at all); no cloud MCPs whatsoever (no Calendar, Gmail, Drive); no `web_search`, `web_fetch`, `bash_tool`, `conversation_search`, `recent_chats`; no Artifacts/REPL; no OS-level computer use. Net: **narrow + deep browser-automation agent** — extremely capable inside a Chrome tab (DOM, JS, network, console, screenshots, recordings, file inputs) and essentially powerless outside one. Heavy injection-defense framing in system prompt characteristic of agentic-browser surface where untrusted page content is in the loop.

**claude-code, Gmail MCP scope blocker.** Source: [`../session-logs/2026-05-02_investor-database-sync-mcp-account-blocker.csv`](../session-logs/2026-05-02_investor-database-sync-mcp-account-blocker.csv). Verified failure mode while Scott was trying to sync investor database from Gmail sent mail: `from:scott@luthienresearch.org newer_than:3d` returned 0 results; `from:scottwofford3@gmail.com newer_than:3d` returned only personal calendar acceptances. Diagnosis: the `mcp__claude_ai_Gmail__*` namespace on Claude Code is OAuth-wired to `scottwofford3@gmail.com` (personal), NOT `scott@luthienresearch.org` (Workspace). The "Luthien MCP" Scott set up via Google Cloud Provider was the gdrive MCP at `~/.config/mcp-gdrive/`, not Gmail. Incoming Luthien threads are readable only because Scott has a forward rule to personal; outgoing Workspace mail bypasses the personal mailbox entirely and is invisible from claude-code. **Implication for R2:** when asked "did I send X from Luthien?" claude-code MUST flag this gap — the verification path does not exist on this surface and no amount of waiting for "MCP indexer lag" recovers it. Workarounds: (a) add `scott@luthienresearch.org` to claude.ai Gmail connector, then re-probe; (b) sweep from a surface that has Workspace auth (claude.ai mobile/desktop) and drop JSON files into the existing `pipeline/sweeps/row*.json` workflow.

**claude-code, tool inventory.** Tools available: Bash, Read, Edit, Write, Glob, Grep, Agent, WebSearch, WebFetch, mcp__trello__*, mcp__claude_ai_Gmail__* (personal only, see above), mcp__claude_ai_Google_Drive__*, mcp__claude_ai_Google_Calendar__*, mcp__gdrive__*, mcp__otter__*, mcp__slack__* (via MCP config). Native filesystem access via Bash + Read/Edit/Write. No `conversation_search` / `recent_chats`.

### Open probes

| # | Probe | Surface | Priority | Protocol |
|---|---|---|---|---|
| 1 | GitHub Integration | desktop-mac | high | `tool_search "github"`, then attempt direct calls (`list_repos`, `read_file` on `scottwofford/private-claude-code-docs/requirements/cross-surface-context-mgmt-req.md`) |
| 2 | Gmail account-scope on web-claudeai | web-claudeai | medium | Explicitly run `from:scott@luthienresearch.org newer_than:1d` and `from:scottwofford3@gmail.com newer_than:1d` to confirm whether web-claudeai sees one account or both |
| 3 | Cloud-MCP auth persistence | cross-surface | low | Determine whether Calendar / Gmail / Drive cloud MCPs persist across surfaces with same auth, or require per-surface re-auth |

When a probe completes, update the matrix cell with date stamp + add to "Per-surface probe evidence" above.

## B. 5 Whys

1. **Surface problem:** When I open a chat on mobile, the assistant doesn't know what happened in my Claude Code session this morning. I have to re-explain context, and sometimes I forget what I already explained.
2. **Why?** Claude Code and claude.ai mobile don't share storage. Auto-memory and session logs live on the laptop; claude.ai sees only its own backend.
3. **Why does that matter beyond inconvenience?** Three real costs: (a) wasted time and forgotten context, (b) mobile chat can make decisions inconsistent with what was decided on the laptop earlier, (c) when bridging with a derived snapshot (the Daily State doc), the snapshot decayed silently and the mobile chat confidently told stale things; worse than no bridge at all.
4. **Why did the snapshot bridge fail?** It duplicated source data into a derived doc that only refreshed when an explicit job ran (snapshot rot). More fundamentally: the system asserted things confidently without flagging that the source data was stale. Asserting wrong things confidently is the root failure: snapshot rot is one cause, mode bleed is another, opening mobile from scratch with no context is a third.
5. **Why didn't we name the right requirement from the start?** No written requirements. Every new session re-invented "what does Scott need" and landed on a single proposed solution. Deeper root: Claude makes solution-shaped suggestions confidently without validating against user need; Scott often goes along until enough has been built to feel wrong.

**Root:** The cross-surface Claude setup needs the system to be honest about what it knows and doesn't know, at the moment of asserting context, not after Scott catches the lie.

## C. Open questions

1. **Mobile-from-scratch frequency.** R2 is most load-bearing when Scott opens claude.ai mobile fresh, with no prior context loaded from another surface. R1 (continuity) is most load-bearing when there IS a prior session to continue from. The relative leverage of R1 vs R2 depends on which pattern dominates Scott's actual mobile usage. **Instrument:** Scott tags each mobile session for one week as "continuation" (picking up from laptop) or "fresh" (no prior context) in the session-log CSV. **Decision rule:** if "fresh" is ≥10% of mobile sessions, R2 is the higher-leverage focus. If <10%, R1 (continuity-from-Desktop-bridge) wins.

2. **Completeness check: are R1-R3 missing failure modes?** Recent claude.ai threads + session logs surfaced four kinds of failure: stale-date stamping, UTC/PT timezone confusion, similarly-named-entity conflation, invented scene details. All four fit under R2 (verify-before-asserting). **Instrument:** Scott flags any future pain that doesn't fit R1, R2, or R3 as a candidate new requirement; re-analyze recent threads at next major doc revision.

3. **Surface-capability probes pending.** Desktop-mac and mobile-ios probes complete; web-claudeai, chrome-extension, and GitHub Integration probes pending. Process learning surfaced during the desktop probe: `tool_search` returning "no matching tools found" does NOT mean the tool is absent on the current surface (verified blind-spot via `Filesystem:list_allowed_directories` working despite `tool_search "filesystem"` returning nothing). **Instrument:** Scott runs the probe protocols documented in [`surface-capabilities.md`](surface-capabilities.md) on each pending surface, attempting both `tool_search` AND direct namespace calls. **Decision rule:** any new gaps found update the matrix; any new behavioral failure modes get added to R1-R3 evidence columns or surface a candidate new requirement.

## D. Method note

This doc was drafted by Claude. Scott endorsed direction, structure, and the Epic + sub-stories shape, then read R1, R2, R3 and the acceptance criteria and confirmed they broadly make sense. Validation is the user reading the requirements; this is a single-user repo with no other reviewers.

## E. R2 operational recipes (verify-before-asserting)

Relocated from CLAUDE.md (2026-06-03) to keep the always-loaded file lean. The imperative bindings stay in CLAUDE.md; the recipes and evidence live here and load on demand.

**Date and time.** Run `date` before answering anything time-sensitive. Do not anchor on chat-history timestamps or the system-context `currentDate` field (set at session start; goes stale across midnight or in long sessions).

**Derived dates in any artifact (weekday + duration + timezone).** Never type a weekday from memory. Before writing `Tue, May 8` style pairs in any doc, compute via `date -j -f "%Y-%m-%d" "$D" "+%a, %b %-d"` (batch all the doc's dates in one Bash call). For UTC Slack timestamps between 00:00-08:00 UTC (PDT) / 00:00-09:00 UTC (PST), the PT date is the PREVIOUS day; always compute, never assume same-day. Meeting durations cite the transcript's last section heading or are omitted. Before any commit that adds dated content: `grep -nE '(Mon|Tue|Wed|Thu|Fri|Sat|Sun), (Jan|Feb|Mar) [0-9]+' <files>` and cross-check every match against `date -j`. Established 2026-05-20 after 7 weekday + 1 duration errors landed in [luthien-org PR #19](https://github.com/LuthienResearch/luthien-org/pull/19) (Trajectory case study).

**Subagent date awareness.** When dispatching an Agent that may need date awareness, prepend the verified time to the subagent's prompt:

```
CURRENT-TIME (verified by parent agent via `date` at dispatch): <output of `date '+%Y-%m-%d %H:%M:%S %Z'`>

<actual subagent prompt>
```

Empirical evidence: 5/5 subagents reported "Today is 2026-05-01" by reading `currentDate` without running `date`; with prompt-injection, 10/10 used the injected time. `additionalContext` from hooks does NOT reliably override system context for subagents; prompt injection does. A `PreToolUse` hook on `Task|Agent` (`scripts/inject-date-into-agent-prompt.sh`) auto-prepends CURRENT-TIME to every Agent dispatch via `updatedInput`; verified 3/3 PASS on auto-injection. Idempotent; skips if the prompt already starts with CURRENT-TIME.

**Fact-to-source routing.** Recent message from X: search the relevant channel (Gmail / direct Slack / Beeper conversation, including iMessage and Signal; skill `gmail-search-heuristics` for search order). Meeting time / agenda / attendees: Google Calendar `mcp__claude_ai_Google_Calendar__list_events` (try `scott@luthienresearch.org` for work; primary for personal). Trello card status: `mcp__trello__get_card`. Person's role / company / fund affiliation: Gmail signature / WebFetch / known reference doc. Dollar amounts, LOI counts, traction stats: cite the canonical source inline. If verification is not available on the surface, say "I do not have that loaded right now"; failed verification satisfies R2, fabricated verification violates it.

## F. claude.ai Saved-memory hygiene

Saved memory is a nightly-regenerated snapshot, so Tenet 4 (source-system primacy) governs what belongs in it. Memory holds only: (1) durable identity facts still true 6+ months out (family, background, home, health patterns, gym equipment, childcare defaults); (2) standing preferences and tool notes; (3) pointers to canonical sources (file paths, doc IDs), never copies of their contents.

Memory must NOT hold:

- **In-flight negotiations, deals, or job conversations.** Verified 2026-07-17: a rapidly-evolving discussion was stored with a wrong org and wrong call date within days, plus a sensitive interpersonal note that should never have been snapshotted.
- **Open to-dos or pending confirmations.** Calendar / Trello / email are the source of truth; remembered copies sat stale for weeks (the Broerman-meeting and insurance-confirmation items).
- **Unresolved technical issues.** They outlive their fix; verified 2026-07-17: the Drive-connector item stayed "active" in memory after being resolved 2026-07-16.
- **Duplicates of rules in the fetched requirements docs.** Copies diverge from canonical; verified 2026-07-17: static calibration caps in memory contradicted R3, which had replaced them in May 2026.

Prefer dated past-tense facts over present-tense status claims. Storage test: still true, useful, and safe to act on in 6 months with no other context? The standing guidance was issued to the memory system 2026-07-17 via the Manage-memory instruction box; re-issue it if regeneration drifts.

## G. Propagate status corrections to canonical sources

When Scott corrects a stale task suggestion ("I already pinged Sevan", "that's done", "that changed"), acknowledging in chat is not enough: in the same turn, search the canonical surfaces that could regenerate the suggestion (Plan of Attack, Trello cards, objective.md, other planning docs) for mentions of that task, update each in place to current status, and report what was updated where. A correction that lives only in one session's context recurs in every future session that re-reads the stale source. Especially binding when the correction arrives via a source unavailable on the current surface (including screenshots): the doc update is the only durable record. On a surface that can't write to the stale source (e.g. claude.ai without the needed connector scope), name which source still carries the stale status so Scott or a Claude Code session can fix it.

*Origin: 2026-07-24 — "Request feedback from Sevan" re-suggested from Plan of Attack Tier 4 after Scott had sent Sevan the draft Jul 22 and corrected a prior session. Rule also in [`../CLAUDE.md`](../CLAUDE.md) Always-on conventions; rehomed here 2026-08-16 so it binds on claude.ai via the every-chat fetch.*

## Related docs

- [`../claude-ai-project-knowledge/architecture.md`](../claude-ai-project-knowledge/architecture.md): cross-surface architecture + design principles
- [`../CLAUDE.md`](../CLAUDE.md): Scott's Claude Code identity, workflow, preferences
- [`personal/scott-response-req.md`](personal/scott-response-req.md): Scott's personal Claude-response requirements (Customize / claude.ai surface)
- [`personal/quentin-response-req.md`](personal/quentin-response-req.md): Quentin Feuillade-Montixi's requirements distillation
- [`personal/matt-mandzel-response-req.md`](personal/matt-mandzel-response-req.md): Matt Mandzel's requirements distillation
- [`design-principles.md`](design-principles.md): meta doc on HOW to bind requirements to surfaces
- [luthien-org canonical format](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/2-versions-requirements/README.md)
- [Session logs](../session-logs/): primary evidence source
