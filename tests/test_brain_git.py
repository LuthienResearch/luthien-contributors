"""Tests that brain commits stay inside the brain folder of a bigger repo."""

import subprocess

from agent.brain_git import commit_and_push


def run(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True).stdout


async def test_commit_only_touches_brain_folder(tmp_path):
    run(tmp_path, "init", "-q")
    run(tmp_path, "config", "user.email", "t@example.com")
    run(tmp_path, "config", "user.name", "t")
    brain = tmp_path / "brain"
    brain.mkdir()
    (brain / "index.md").write_text("# Index\n")
    (tmp_path / "other.md").write_text("team file\n")
    run(tmp_path, "add", "-A")
    run(tmp_path, "commit", "-q", "-m", "seed")

    # The agent edits the brain while someone else has an unrelated change in the repo.
    (brain / "index.md").write_text("# Index\n- new page\n")
    (tmp_path / "other.md").write_text("team file, edited\n")
    await commit_and_push(str(brain), "brain update")

    assert run(tmp_path, "show", "--name-only", "--format=", "HEAD").split() == ["brain/index.md"]
    assert "other.md" in run(tmp_path, "status", "--short")
