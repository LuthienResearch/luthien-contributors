"""Approval gate: decides, in code, which tool calls the agent may make.

Every tool call the agent attempts passes through ApprovalGate.__call__.
Nothing is auto-approved by the SDK itself (we never set allowed_tools),
so this file is the single place that enforces the safety rules.
"""

import asyncio
import json
import os
import time
import uuid
from dataclasses import dataclass, field
from typing import Awaitable, Callable

from claude_agent_sdk import PermissionResultAllow, PermissionResultDeny

# Tool categories. A tool not listed anywhere is denied (fail closed).
READ_TOOLS = {
    "Read",
    "Glob",
    "Grep",
    "WebSearch",
    "WebFetch",
    "mcp__slack__read_thread",
    "mcp__slack__read_channel",
    "mcp__slack__list_channels",
}
BRAIN_WRITE_TOOLS = {"Write", "Edit"}
EXTERNAL_WRITE_TOOLS = {"mcp__slack__send_message"}

# File tools that take a path; we check the path stays inside the brain.
PATH_KEYS = {"Read": "file_path", "Write": "file_path", "Edit": "file_path", "Glob": "path", "Grep": "path"}

APPROVAL_WAIT_SECONDS = 60
# A queued approval nobody clicks is dropped after a day, so stale actions never run.
PENDING_EXPIRY_SECONDS = 24 * 60 * 60


@dataclass
class RequestContext:
    """Who asked, and where. Built fresh for every Slack request."""

    requester_id: str
    channel: str
    thread_ts: str


@dataclass
class PendingApproval:
    """One external write waiting for a human click."""

    id: str
    tool_name: str
    tool_input: dict
    ctx: RequestContext
    created: float = field(default_factory=time.time)
    # Resolved with True/False when someone clicks while the agent is still waiting.
    future: asyncio.Future = field(default_factory=lambda: asyncio.get_running_loop().create_future())


# Shared across sessions so the Slack button handler can find a pending request by id.
PENDING: dict[str, PendingApproval] = {}

# Posts the Approve/Deny card. Supplied by app.py so this file doesn't depend on Slack.
CardPoster = Callable[[PendingApproval], Awaitable[None]]


def drop_expired() -> None:
    """Forget queued approvals older than PENDING_EXPIRY_SECONDS."""
    cutoff = time.time() - PENDING_EXPIRY_SECONDS
    for pid in [pid for pid, p in PENDING.items() if p.created < cutoff]:
        del PENDING[pid]


def call_key(tool_name: str, tool_input: dict) -> str:
    """A stable string for 'this exact tool with these exact arguments'."""
    return tool_name + json.dumps(tool_input, sort_keys=True)


def inside(path: str, root: str) -> bool:
    """True if path (after resolving symlinks and '..') is within root."""
    real_root = os.path.realpath(root)
    real_path = os.path.realpath(os.path.join(real_root, path))
    return real_path == real_root or real_path.startswith(real_root + os.sep)


class ApprovalGate:
    def __init__(self, ctx: RequestContext, brain_dir: str, post_card: CardPoster, preapproved: str | None = None):
        self.ctx = ctx
        self.brain_dir = brain_dir
        self.post_card = post_card
        # Set when a late approval restarts a session: this one exact call is allowed.
        self.preapproved = preapproved

    async def __call__(self, tool_name: str, tool_input: dict, _context) -> PermissionResultAllow | PermissionResultDeny:
        # File tools must stay inside the brain folder, or the agent could read
        # anything on the host machine (SSH keys, other repos).
        if tool_name in PATH_KEYS:
            path = tool_input.get(PATH_KEYS[tool_name])
            if path and not inside(path, self.brain_dir):
                return PermissionResultDeny(message="Only files inside the brain folder are allowed.")

        if tool_name in READ_TOOLS or tool_name in BRAIN_WRITE_TOOLS:
            # Reads are harmless; brain writes are recorded by git after the session.
            return PermissionResultAllow()

        if tool_name in EXTERNAL_WRITE_TOOLS:
            return await self._external_write(tool_name, tool_input)

        return PermissionResultDeny(message=f"Tool {tool_name} is not enabled for this agent.")

    async def _external_write(self, tool_name: str, tool_input: dict):
        # Replying in the thread the requester is already in needs no approval.
        if tool_input.get("channel") == self.ctx.channel and tool_input.get("thread_ts") == self.ctx.thread_ts:
            return PermissionResultAllow()

        # A late approval restarted this session for exactly this call.
        if self.preapproved and self.preapproved == call_key(tool_name, tool_input):
            self.preapproved = None  # single use
            return PermissionResultAllow()

        # Otherwise ask the requester: post a card, then wait briefly for a click.
        pending = PendingApproval(id=uuid.uuid4().hex[:12], tool_name=tool_name, tool_input=tool_input, ctx=self.ctx)
        drop_expired()
        PENDING[pending.id] = pending
        await self.post_card(pending)
        try:
            approved = await asyncio.wait_for(asyncio.shield(pending.future), APPROVAL_WAIT_SECONDS)
        except asyncio.TimeoutError:
            # Leave it in PENDING: a later click re-runs the call (see app.py).
            return PermissionResultDeny(
                message="Queued for approval. Continue without it and tell the user it will run once they click Approve."
            )
        PENDING.pop(pending.id, None)
        if approved:
            return PermissionResultAllow()
        return PermissionResultDeny(message="The user denied this action.")
