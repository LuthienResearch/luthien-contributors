"""Commits whatever the agent changed in the brain, so git is the audit log.

The brain can be a folder inside a bigger repo (luthien-org/brain), so every
git command here is limited to that folder with the "." path."""

import asyncio


async def git(brain_dir: str, *args: str) -> tuple[int, str]:
    proc = await asyncio.create_subprocess_exec(
        "git", "-C", brain_dir, *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT
    )
    out, _ = await proc.communicate()
    return proc.returncode, out.decode()


async def pull_latest(brain_dir: str) -> None:
    # Only fast-forward: if the brain has diverged, keep the local copy and let a human sort it out.
    code, remotes = await git(brain_dir, "remote")
    if code == 0 and remotes.strip():
        await git(brain_dir, "pull", "-q", "--ff-only")


async def commit_and_push(brain_dir: str, message: str) -> None:
    # Stage only the brain folder, never other changes elsewhere in the repo.
    await git(brain_dir, "add", "-A", "--", ".")
    # Exit code 0 from 'diff --cached --quiet' means nothing changed: skip the commit.
    changed, _ = await git(brain_dir, "diff", "--cached", "--quiet")
    if changed == 0:
        return
    await git(brain_dir, "commit", "-q", "-m", message, "--", ".")
    # Push only if the brain has a remote configured.
    code, remotes = await git(brain_dir, "remote")
    if code == 0 and remotes.strip():
        pushed, _ = await git(brain_dir, "push", "-q")
        if pushed != 0:
            # Someone else pushed to the repo meanwhile: replay our commit on top and retry once.
            await git(brain_dir, "pull", "-q", "--rebase")
            await git(brain_dir, "push", "-q")
