"""Slack entry point: listens over Socket Mode, runs a session per request.

Socket Mode means the bot opens an outbound connection to Slack, so it needs
no public URL and nothing on the host is exposed to the internet.
Run with: scripts/run.sh
"""

import asyncio
import json
import os
from datetime import datetime

from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler
from slack_bolt.async_app import AsyncApp

from . import approvals, standup
from .approvals import PENDING, PendingApproval, RequestContext, call_key
from .session import run_session

app = AsyncApp(token=os.environ["SLACK_BOT_TOKEN"])
BOT = {}  # filled at startup: bot user id + workspace (team) id
# Optional comma-separated Slack user IDs; empty means anyone in the workspace.
ALLOWED_USERS = {u for u in os.environ.get("ALLOWED_USER_IDS", "").split(",") if u}
# Optional comma-separated Slack user IDs who may approve any pending action, not just their own.
ADMIN_USERS = {u for u in os.environ.get("ADMIN_USER_IDS", "").split(",") if u}


def allowed(event: dict) -> bool:
    """Only answer people from our own workspace (not Slack Connect guests from other orgs)."""
    if event.get("bot_id") or event.get("subtype"):
        return False
    if event.get("user_team", event.get("team")) != BOT["team_id"]:
        return False
    return not ALLOWED_USERS or event.get("user") in ALLOWED_USERS


async def post_card(pending: PendingApproval) -> None:
    """Post the Approve/Deny card into the requester's thread."""
    summary = json.dumps(pending.tool_input, indent=1)[:1500]
    await app.client.chat_postMessage(
        channel=pending.ctx.channel,
        thread_ts=pending.ctx.thread_ts,
        text=f"Approval needed: {pending.tool_name}",
        blocks=[
            {"type": "section", "text": {"type": "mrkdwn", "text": f"<@{pending.ctx.requester_id}>, OK to run *{pending.tool_name}*?\n```{summary}```"}},
            {
                "type": "actions",
                "elements": [
                    {"type": "button", "text": {"type": "plain_text", "text": "Approve"}, "style": "primary", "action_id": "approve", "value": pending.id},
                    {"type": "button", "text": {"type": "plain_text", "text": "Deny"}, "style": "danger", "action_id": "deny", "value": pending.id},
                ],
            },
        ],
    )


async def handle_request(event: dict, prompt_extra: str = "", preapproved: str | None = None) -> None:
    channel = event["channel"]
    thread_ts = event.get("thread_ts", event["ts"])
    ctx = RequestContext(requester_id=event["user"], channel=channel, thread_ts=thread_ts)

    # Give the agent the whole thread so far as context.
    history = await app.client.conversations_replies(channel=channel, ts=thread_ts, limit=50)
    transcript = "\n".join(f"<@{m.get('user', 'bot')}>: {m.get('text', '')}" for m in history["messages"])
    prompt = (
        f"Requester: <@{ctx.requester_id}>\nChannel: {channel}\nThread: {thread_ts}\n"
        f"Time: {datetime.now().astimezone().isoformat(timespec='minutes')}\n\n"
        f"Thread so far:\n{transcript}\n\n{prompt_extra}"
    )

    placeholder = await app.client.chat_postMessage(channel=channel, thread_ts=thread_ts, text="Working on it…")
    try:
        reply = await run_session(prompt, ctx, app.client, post_card, preapproved)
    except Exception as exc:  # report failures in Slack instead of going silent
        reply = f"Sorry, something went wrong: {exc}"
    await app.client.chat_update(channel=channel, ts=placeholder["ts"], text=reply)


@app.event("app_mention")
async def on_mention(event):
    if allowed(event):
        asyncio.create_task(handle_request(event))


@app.event("message")
async def on_dm(event):
    # Mentions in channels arrive as app_mention; here we only want direct messages.
    if event.get("channel_type") == "im" and allowed(event):
        asyncio.create_task(handle_request(event))


async def on_click(ack, body, action, approve: bool):
    await ack()
    approvals.drop_expired()
    pending = PENDING.get(action["value"])
    clicker = body["user"]["id"]
    if not pending:
        return
    if clicker != pending.ctx.requester_id and clicker not in ADMIN_USERS:
        await app.client.chat_postEphemeral(channel=pending.ctx.channel, user=clicker, text="Only the person who asked (or an admin) can approve this.")
        return
    # Replace the buttons with the outcome so nobody clicks twice.
    await app.client.chat_update(
        channel=body["channel"]["id"], ts=body["message"]["ts"],
        text=f"{'Approved' if approve else 'Denied'} by <@{clicker}>: {pending.tool_name}", blocks=[],
    )
    if not pending.future.done():
        # The agent is still waiting: hand it the answer directly.
        pending.future.set_result(approve)
        return
    # The agent gave up waiting. On a late approval, start a new session that
    # is allowed to make exactly this one call.
    PENDING.pop(pending.id, None)
    if approve:
        event = {"channel": pending.ctx.channel, "thread_ts": pending.ctx.thread_ts, "ts": pending.ctx.thread_ts, "user": pending.ctx.requester_id}
        extra = f"Approved: make exactly this call now: {pending.tool_name}({json.dumps(pending.tool_input)})"
        asyncio.create_task(handle_request(event, extra, call_key(pending.tool_name, pending.tool_input)))


@app.action("approve")
async def on_approve(ack, body, action):
    await on_click(ack, body, action, True)


@app.action("deny")
async def on_deny(ack, body, action):
    await on_click(ack, body, action, False)


async def main():
    auth = await app.client.auth_test()
    BOT.update(user_id=auth["user_id"], team_id=auth["team_id"])
    # Daily async standup post, if a channel is configured.
    if channel := os.environ.get("STANDUP_CHANNEL_ID"):
        asyncio.create_task(standup.run_forever(app.client, channel))
    await AsyncSocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start_async()


if __name__ == "__main__":
    asyncio.run(main())
