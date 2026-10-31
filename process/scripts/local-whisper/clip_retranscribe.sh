#!/bin/zsh
# Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy. Source of truth: https://github.com/scottwofford/sw-prv/blob/main/scripts/local-whisper/clip_retranscribe.sh (private). This copy is a redacted mirror and may lag behind it.
# Re-transcribe a short stretch of a recording with local Whisper, to settle a garbled passage.
# Usage: clip_retranscribe.sh <audio-file-or-URL> <start HH:MM:SS> <end HH:MM:SS> [model]
#   audio: for Plaud, the presigned URL from the Plaud MCP get_file call (valid 24h).
#   model: faster-whisper model name, default "medium".
# Runs twice: once unprimed, then with names from $WHISPER_PROMPT if set. Report the unprimed
# reading first; a primed run can hallucinate the names it was given.
# The downloaded audio and the clip are deleted on exit: the recording stays in Plaud.
set -eu
src="$1"; start="$2"; end="$3"; model="${4:-medium}"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
if [[ "$src" == http* ]]; then curl -s -L -o "$tmp/audio" "$src"; src="$tmp/audio"; fi
ffmpeg -loglevel error -y -ss "$start" -to "$end" -i "$src" -ar 16000 -ac 1 "$tmp/clip.wav"
offset=$(echo "$start" | awk -F: '{print $1*3600+$2*60+$3}')
uv run --with faster-whisper python - "$tmp/clip.wav" "$model" "$offset" <<'PY' 2>&1 | grep -v -i -E "warn|download|Installed|fetching"
import os, sys
from faster_whisper import WhisperModel
clip, model, offset = sys.argv[1], sys.argv[2], float(sys.argv[3])
m = WhisperModel(model, device="cpu", compute_type="int8")
runs = [("unprimed", None)]
if os.environ.get("WHISPER_PROMPT"): runs.append(("primed", os.environ["WHISPER_PROMPT"]))
for label, prompt in runs:
    print(f"--- {label}")
    segs, _ = m.transcribe(clip, language="en", beam_size=5, initial_prompt=prompt)
    for s in segs:
        t = offset + s.start
        print(f"[{int(t//60):02d}:{int(t%60):02d}] {s.text.strip()}")
PY
