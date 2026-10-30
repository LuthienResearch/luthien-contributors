#!/bin/zsh
# Start the agent. Bitwarden is the saved source of truth for the three secrets;
# macOS Keychain holds a runtime copy, read into this process only.
set +x
set -eu
umask 077
cd "$(dirname "$0")/.."

read_secret() {
  /usr/bin/security find-generic-password -s luthien.slack-agent -a "$1" -w 2>/dev/null \
    || { print -u2 "Missing Keychain item luthien.slack-agent / $1 (see README)."; exit 1; }
}
export SLACK_BOT_TOKEN="$(read_secret slack-bot-token)"
export SLACK_APP_TOKEN="$(read_secret slack-app-token)"
export ANTHROPIC_API_KEY="$(read_secret anthropic-api-key)"
[[ "$SLACK_BOT_TOKEN" == xoxb-* ]] || { print -u2 'slack-bot-token must start with xoxb-'; exit 1; }
[[ "$SLACK_APP_TOKEN" == xapp-* ]] || { print -u2 'slack-app-token must start with xapp-'; exit 1; }

# The brain is a contributors-level repo, separate from luthien-org (see README).
export BRAIN_DIR="${BRAIN_DIR:-$HOME/build/luthien-contributors-brain}"
# Daily async standup in #luthien-contributors (set STANDUP_CHANNEL_ID= to turn off).
export STANDUP_CHANNEL_ID="${STANDUP_CHANNEL_ID-C0APTJLNWN6}"
exec uv run python -m agent.app
