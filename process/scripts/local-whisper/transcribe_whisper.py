#!/usr/bin/env python3
# Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy.
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "faster-whisper>=1.0",
# ]
# ///
"""Transcribe a 16 kHz mono WAV file to speaker-tagged markdown.

Called by transcribe.sh (which handles ffmpeg audio extraction).
Diarization uses pyannote.audio, which is NOT in the inline dependencies
above; the wrapper adds it via `uv run --with pyannote.audio` only when a
HuggingFace token is available. Without a token the script runs
whisper-only and tags every line SPEAKER (diarization pending).
"""

import argparse
import datetime
import os
import sys
from pathlib import Path


def find_hf_token() -> str | None:
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    if token:
        return token.strip()
    for path in (Path.home() / ".huggingface" / "token",
                 Path.home() / ".cache" / "huggingface" / "token"):
        if path.is_file():
            content = path.read_text().strip()
            if content:
                return content
    return None


def transcribe(wav_path: str, model_size: str):
    from faster_whisper import WhisperModel

    print(f"[whisper] loading model '{model_size}' (first run downloads it)...",
          file=sys.stderr)
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(wav_path, vad_filter=True)
    result = []
    for seg in segments:
        text = seg.text.strip()
        if text:
            result.append({"start": seg.start, "end": seg.end, "text": text})
    return result, info


def diarize(wav_path: str, token: str):
    """Return list of (start, end, speaker_label) turns, or None on failure."""
    try:
        from pyannote.audio import Pipeline
    except ImportError:
        print("[diarize] pyannote.audio not installed; skipping diarization.",
              file=sys.stderr)
        return None
    try:
        print("[diarize] loading pyannote speaker-diarization pipeline...",
              file=sys.stderr)
        pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1", use_auth_token=token)
        annotation = pipeline(wav_path)
        turns = [(turn.start, turn.end, speaker)
                 for turn, _, speaker in annotation.itertracks(yield_label=True)]
        return turns
    except Exception as exc:  # gated-model 403, network, etc.
        print(f"[diarize] diarization failed ({exc}); falling back to "
              "whisper-only output.", file=sys.stderr)
        return None


def speaker_for_segment(seg, turns) -> str:
    """Pick the diarization speaker with maximum time overlap."""
    best, best_overlap = None, 0.0
    for start, end, speaker in turns:
        overlap = min(seg["end"], end) - max(seg["start"], start)
        if overlap > best_overlap:
            best, best_overlap = speaker, overlap
    return best or "SPEAKER"


def fmt_ts(seconds: float) -> str:
    total = int(seconds)
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("wav", help="16 kHz mono WAV input")
    parser.add_argument("output_md", help="markdown output path")
    parser.add_argument("--model", default="small")
    parser.add_argument("--source-name", default=None,
                        help="original media filename, for the header")
    args = parser.parse_args()

    segments, info = transcribe(args.wav, args.model)

    token = find_hf_token()
    turns = diarize(args.wav, token) if token else None
    if not token:
        print("[diarize] no HuggingFace token found; whisper-only output.",
              file=sys.stderr)

    source = args.source_name or Path(args.wav).name
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Transcript: {source}",
        "",
        f"- Transcribed: {now} (local whisper, model: {args.model})",
        f"- Language: {info.language} (p={info.language_probability:.2f})",
        f"- Diarization: {'pyannote/speaker-diarization-3.1' if turns else 'off (no HuggingFace token or pipeline unavailable)'}",
        "",
    ]

    # Merge consecutive segments from the same speaker into one block.
    current_speaker, block_start, block_texts = None, None, []
    def flush():
        if block_texts:
            lines.append(f"**{current_speaker}** [{fmt_ts(block_start)}]: "
                         + " ".join(block_texts))
            lines.append("")

    for seg in segments:
        speaker = speaker_for_segment(seg, turns) if turns else "SPEAKER"
        if speaker != current_speaker:
            flush()
            current_speaker, block_start, block_texts = speaker, seg["start"], []
        block_texts.append(seg["text"])
    flush()

    Path(args.output_md).write_text("\n".join(lines))
    print(args.output_md)


if __name__ == "__main__":
    main()
