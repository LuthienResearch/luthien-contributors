> Generated from Scott Wofford's private docs on 2026-10-31 by an export script. Do not edit here; edits are overwritten. Scott's agents never read this copy.

# Local Whisper transcription pipeline

Built overnight 2026-07-06 from Trello card [Set up local Whisper transcription pipeline](https://trello.com/c/6TuqaBRS).

Live scripts: `~/scripts/transcribe.sh` + `~/scripts/transcribe_whisper.py` (this folder holds the git-tracked copies; if you edit one, sync the other).

## Usage

```bash
~/scripts/transcribe.sh recording.m4a                 # any audio or video file
~/scripts/transcribe.sh meeting.mp4 -o ~/Desktop      # override output dir
~/scripts/transcribe.sh call.wav -m medium            # bigger model, better accuracy
```

Output: speaker-tagged markdown in `~/build/sw-prv/transcripts/local-whisper/` (NOT `~/Dropbox/transcripts/` as the March card said; Dropbox is being cancelled).

## How it works

1. ffmpeg extracts 16 kHz mono WAV from any audio/video input.
2. faster-whisper transcribes (default model: `small`, a good speed/accuracy balance for meeting audio on this laptop; use `-m medium` or `-m large-v3` when accuracy matters more than speed). Dependencies are managed by uv inline-script metadata; no venv to maintain. First run downloads the model (~460 MB for small) to `~/.cache/huggingface/`.
3. pyannote.audio diarizes (who spoke when) and each transcript line gets a speaker tag. This step activates automatically once a HuggingFace token exists; until then output is whisper-only with a generic `SPEAKER` tag.

## Enabling speaker diarization (one-time, ~5 min)

1. Create a free HuggingFace account at huggingface.co if you don't have one.
2. Accept the gated-model terms on BOTH model pages (free, instant):
   - https://huggingface.co/pyannote/speaker-diarization-3.1
   - https://huggingface.co/pyannote/segmentation-3.0
3. Create a read-scope token at https://huggingface.co/settings/tokens and save it:
   ```bash
   mkdir -p ~/.cache/huggingface && printf '%s' 'hf_yourtoken' > ~/.cache/huggingface/token
   ```
4. Run `transcribe.sh` on any file. It detects the token, installs pyannote via uv on first use (~2 GB of PyTorch downloads, one time), and outputs `SPEAKER_00` / `SPEAKER_01` tags.

## Verified

Tested 2026-07-06 on a two-voice synthetic clip (macOS `say`, Samantha + Daniel) and an mp4 wrapper of the same audio. Whisper transcription was word-for-word accurate; sample output in [`transcripts/local-whisper/test_two_speakers.md`](../../transcripts/local-whisper/test_two_speakers.md). Diarization untested pending HuggingFace token.
