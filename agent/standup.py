"""Async daily standup: the bot posts three questions each weekday morning.

People answer in the thread under the post, on days they worked on Luthien.
There is no meeting; blockers get picked up in the thread.
Turned on by setting STANDUP_CHANNEL_ID (empty means off).
"""

import asyncio
import os
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

TZ = ZoneInfo(os.environ.get("STANDUP_TZ", "America/Los_Angeles"))
# Post time, local to STANDUP_TZ, as HH:MM.
POST_AT = time.fromisoformat(os.environ.get("STANDUP_TIME", "08:00"))

QUESTIONS = (
    "1. What did you do?\n"
    "2. What's next, and for which weekly goal?\n"
    "3. What are you blocked on?"
)


def next_run(now: datetime) -> datetime:
    """The next weekday (Mon to Fri) at POST_AT, strictly after `now`."""
    now = now.astimezone(TZ)
    candidate = datetime.combine(now.date(), POST_AT, tzinfo=TZ)
    if candidate <= now:
        candidate += timedelta(days=1)
    # Skip Saturday (5) and Sunday (6).
    while candidate.weekday() >= 5:
        candidate += timedelta(days=1)
    return candidate


def standup_text(day: datetime) -> str:
    return (
        f"*Standup for {day:%a %b} {day.day}*: reply in this thread if you worked on Luthien.\n"
        f"{QUESTIONS}"
    )


async def run_forever(client, channel: str) -> None:
    """Sleep until the next post time, post, repeat. Errors are logged, never fatal."""
    while True:
        when = next_run(datetime.now(TZ))
        await asyncio.sleep((when - datetime.now(TZ)).total_seconds())
        try:
            await client.chat_postMessage(channel=channel, text=standup_text(when))
        except Exception as exc:  # a failed post shouldn't take the bot down
            print(f"standup post failed: {exc}")
