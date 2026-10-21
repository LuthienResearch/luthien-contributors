"""Slack tools the agent can call, served in-process (no separate MCP server).

Each tool returns small, trimmed text: long tool outputs make sessions slow
and expensive.
"""

from claude_agent_sdk import create_sdk_mcp_server, tool
from slack_sdk.web.async_client import AsyncWebClient

MAX_CHARS = 6000


def text_result(text: str) -> dict:
    """Wrap text in the shape the SDK expects from a tool."""
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS] + "\n[truncated]"
    return {"content": [{"type": "text", "text": text}]}


def format_messages(messages: list[dict]) -> str:
    """One line per message: '<user>: <text>'."""
    return "\n".join(f"{m.get('user', m.get('bot_id', '?'))} ({m.get('ts')}): {m.get('text', '')}" for m in messages)


def build_slack_server(client: AsyncWebClient):
    """Create the 'slack' tool server. Tool names become mcp__slack__<name>."""

    @tool("read_thread", "Read every message in a Slack thread.", {"channel": str, "thread_ts": str})
    async def read_thread(args):
        resp = await client.conversations_replies(channel=args["channel"], ts=args["thread_ts"], limit=100)
        return text_result(format_messages(resp["messages"]))

    @tool("read_channel", "Read recent messages in a channel the bot is a member of.", {"channel": str, "limit": int})
    async def read_channel(args):
        resp = await client.conversations_history(channel=args["channel"], limit=min(args.get("limit", 30), 100))
        # Slack returns newest first; flip so the agent reads top to bottom.
        return text_result(format_messages(list(reversed(resp["messages"]))))

    @tool("list_channels", "List channels the bot is a member of, with their IDs.", {})
    async def list_channels(_args):
        resp = await client.users_conversations(types="public_channel,private_channel", limit=200)
        return text_result("\n".join(f"#{c['name']} {c['id']}" for c in resp["channels"]))

    @tool(
        "send_message",
        "Post a message. Posting outside the current thread needs the requester's approval.",
        {"channel": str, "text": str, "thread_ts": str},
    )
    async def send_message(args):
        resp = await client.chat_postMessage(channel=args["channel"], text=args["text"], thread_ts=args.get("thread_ts") or None)
        return text_result(f"Posted, ts={resp['ts']}")

    return create_sdk_mcp_server(name="slack", tools=[read_thread, read_channel, list_channels, send_message])
