#!/usr/bin/env bash
# Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy.
# transcribe.sh: local Whisper transcription with optional speaker diarization.
#
# Usage: transcribe.sh <audio-or-video-file> [-o output_dir] [-m model]
#   -o output_dir   default: ~/build/sw-prv/transcripts/local-whisper
#   -m model        whisper model size (tiny|base|small|medium|large-v3), default: small
#
# Pipeline: ffmpeg extracts 16 kHz mono WAV -> faster-whisper transcribes ->
# pyannote.audio diarizes (only if a HuggingFace token is present) ->
# speaker-tagged markdown written to the output dir.
#
# Diarization activates automatically when a HuggingFace token exists in
# $HF_TOKEN, ~/.huggingface/token, or ~/.cache/huggingface/token AND you have
# accepted the gated-model terms for pyannote/speaker-diarization-3.1 and
# pyannote/segmentation-3.0 on huggingface.co. Without a token, output is
# whisper-only with a generic SPEAKER tag.

set -euo pipefail

DEFAULT_OUT="$HOME/build/sw-prv/transcripts/local-whisper"
MODEL="small"
OUT_DIR="$DEFAULT_OUT"

usage() { grep '^#' "$0" | head -16 | sed 's/^# \{0,1\}//'; exit 1; }

[ $# -ge 1 ] || usage
INPUT="$1"; shift

while getopts "o:m:h" opt; do
    case "$opt" in
        o) OUT_DIR="$OPTARG" ;;
        m) MODEL="$OPTARG" ;;
        *) usage ;;
    esac
done

[ -f "$INPUT" ] || { echo "error: input file not found: $INPUT" >&2; exit 1; }
command -v ffmpeg >/dev/null || { echo "error: ffmpeg not installed (brew install ffmpeg)" >&2; exit 1; }
command -v uv >/dev/null || { echo "error: uv not installed" >&2; exit 1; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="$SCRIPT_DIR/transcribe_whisper.py"
[ -f "$PY_SCRIPT" ] || { echo "error: $PY_SCRIPT not found" >&2; exit 1; }

mkdir -p "$OUT_DIR"
BASE="$(basename "$INPUT")"
STEM="${BASE%.*}"
OUT_MD="$OUT_DIR/${STEM}.md"

# 1. Extract 16 kHz mono WAV (whisper + pyannote both want this).
TMP_WAV="$(mktemp -t transcribe).wav"
trap 'rm -f "$TMP_WAV"' EXIT
echo "[ffmpeg] extracting audio from $BASE ..." >&2
ffmpeg -y -loglevel error -i "$INPUT" -vn -ac 1 -ar 16000 -c:a pcm_s16le "$TMP_WAV"

# 2. Detect HuggingFace token; if present, pull in pyannote for diarization.
HF_PRESENT=""
if [ -n "${HF_TOKEN:-}" ] || [ -n "${HUGGING_FACE_HUB_TOKEN:-}" ] \
   || [ -s "$HOME/.huggingface/token" ] || [ -s "$HOME/.cache/huggingface/token" ]; then
    HF_PRESENT="yes"
fi

UV_ARGS=()
if [ -n "$HF_PRESENT" ]; then
    echo "[diarize] HuggingFace token found; enabling pyannote diarization." >&2
    UV_ARGS+=(--with "pyannote.audio>=3.1")
else
    echo "[diarize] no HuggingFace token; running whisper-only (see script header to enable diarization)." >&2
fi

# 3. Transcribe (+ diarize) to markdown.
uv run ${UV_ARGS[@]+"${UV_ARGS[@]}"} "$PY_SCRIPT" "$TMP_WAV" "$OUT_MD" \
    --model "$MODEL" --source-name "$BASE"

echo "transcript: $OUT_MD"
