"""Runs one agent session for one Slack request and returns the reply text."""

import asyncio
import os
from pathlib import Path

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient, ResultMessage

from .brain_git import commit_and_push, pull_latest
from .approvals import ApprovalGate, CardPoster, RequestContext
from .slack_tools import build_slack_server

PROMPT = (Path(__file__).parent / "prompt.md").read_text()
# Built-in Claude Code tools the agent gets. No Bash: it can't run commands.
BUILTIN_TOOLS = ["Read", "Write", "Edit", "Glob", "Grep", "WebSearch", "WebFetch"]
# Isolated config folder so the host user's own Claude Code settings, hooks and
# CLAUDE.md files never leak into the agent.
CONFIG_DIR = Path(__file__).resolve().parent.parent / ".agent-claude-config"

# One session at a time, so two sessions never edit the brain repo at once.
SESSION_LOCK = asyncio.Lock()


async def run_session(prompt: str, ctx: RequestContext, slack_client, post_card: CardPoster, preapproved: str | None = None) -> str:
    brain_dir = os.environ["BRAIN_DIR"]
    CONFIG_DIR.mkdir(exist_ok=True)
    options = ClaudeAgentOptions(
        system_prompt=PROMPT,
        tools=BUILTIN_TOOLS,
        cwd=brain_dir,
        mcp_servers={"slack": build_slack_server(slack_client)},
        # Every tool call goes through the gate; allowed_tools stays empty on purpose,
        # because anything listed there would skip the gate.
        can_use_tool=ApprovalGate(ctx, brain_dir, post_card, preapproved),
        permission_mode="default",
        setting_sources=[],
        model=os.environ.get("AGENT_MODEL", "claude-sonnet-5-5"),
        max_turns=40,
        max_budget_usd=float(os.environ.get("MAX_BUDGET_USD", "3")),
        # Slack replies are often more than 5 minutes apart, so the default prompt cache
        # keeps expiring and the whole thread is re-sent at full price.
        env={"CLAUDE_CONFIG_DIR": str(CONFIG_DIR), "CLAUDE_CODE_PROMPT_CACHE_TTL": "1h"},
    )
    async with SESSION_LOCK:
        # Start from the latest brain, in case someone edited it on GitHub.
        await pull_latest(brain_dir)
        async with ClaudeSDKClient(options=options) as client:
            await client.query(prompt)
            reply = ""
            async for message in client.receive_response():
                # The final ResultMessage carries the agent's last answer.
                if isinstance(message, ResultMessage):
                    reply = message.result or ""
        # Commit inside the lock so the next session starts from a clean brain.
        await commit_and_push(brain_dir, f"Brain update from a request by {ctx.requester_id}")
        return reply or "(no reply)"
