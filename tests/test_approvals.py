"""Tests for the approval gate: the one file that enforces the safety rules."""

import asyncio

import pytest
from claude_agent_sdk import PermissionResultAllow, PermissionResultDeny

from agent import approvals
from agent.approvals import ApprovalGate, RequestContext, call_key

CTX = RequestContext(requester_id="U1", channel="C1", thread_ts="111.1")


@pytest.fixture
def brain(tmp_path):
    (tmp_path / "index.md").write_text("# Index\n")
    return str(tmp_path)


def gate(brain, cards=None, preapproved=None):
    async def post_card(pending):
        if cards is not None:
            cards.append(pending)

    return ApprovalGate(CTX, brain, post_card, preapproved)


async def test_reads_inside_brain_allowed(brain):
    assert isinstance(await gate(brain)("Read", {"file_path": "index.md"}, None), PermissionResultAllow)


async def test_reads_outside_brain_denied(brain):
    g = gate(brain)
    for path in ["/etc/passwd", "../secrets.txt", f"{brain}/../x"]:
        assert isinstance(await g("Read", {"file_path": path}, None), PermissionResultDeny), path


async def test_unknown_tool_denied(brain):
    assert isinstance(await gate(brain)("Bash", {"command": "ls"}, None), PermissionResultDeny)


async def test_reply_in_own_thread_skips_approval(brain):
    cards = []
    result = await gate(brain, cards)("mcp__slack__send_message", {"channel": "C1", "thread_ts": "111.1", "text": "hi"}, None)
    assert isinstance(result, PermissionResultAllow) and not cards


async def test_post_elsewhere_waits_for_click(brain):
    cards = []
    task = asyncio.create_task(gate(brain, cards)("mcp__slack__send_message", {"channel": "C2", "text": "hi"}, None))
    await asyncio.sleep(0.01)
    assert len(cards) == 1
    cards[0].future.set_result(True)  # simulate the requester clicking Approve
    assert isinstance(await task, PermissionResultAllow)


async def test_deny_click(brain):
    cards = []
    task = asyncio.create_task(gate(brain, cards)("mcp__slack__send_message", {"channel": "C2", "text": "hi"}, None))
    await asyncio.sleep(0.01)
    cards[0].future.set_result(False)
    assert isinstance(await task, PermissionResultDeny)


async def test_timeout_queues(brain, monkeypatch):
    monkeypatch.setattr(approvals, "APPROVAL_WAIT_SECONDS", 0.01)
    cards = []
    result = await gate(brain, cards)("mcp__slack__send_message", {"channel": "C2", "text": "hi"}, None)
    assert isinstance(result, PermissionResultDeny) and "Queued" in result.message
    assert cards[0].id in approvals.PENDING  # still waiting for a late click


async def test_preapproved_call_is_single_use(brain, monkeypatch):
    args = {"channel": "C2", "text": "hi"}
    g = gate(brain, cards=[], preapproved=call_key("mcp__slack__send_message", args))
    assert isinstance(await g("mcp__slack__send_message", args, None), PermissionResultAllow)
    # A second identical call is not covered by the one approval.
    monkeypatch.setattr(approvals, "APPROVAL_WAIT_SECONDS", 0.01)
    assert isinstance(await g("mcp__slack__send_message", args, None), PermissionResultDeny)


async def test_stale_pending_approvals_expire(brain, monkeypatch):
    monkeypatch.setattr(approvals, "APPROVAL_WAIT_SECONDS", 0.01)
    cards = []
    await gate(brain, cards)("mcp__slack__send_message", {"channel": "C2", "text": "hi"}, None)
    cards[0].created -= approvals.PENDING_EXPIRY_SECONDS + 1  # pretend it was queued yesterday
    approvals.drop_expired()
    assert cards[0].id not in approvals.PENDING
