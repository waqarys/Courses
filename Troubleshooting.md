# Troubleshooting (errors we already hit on Windows)

| Message | Fix |
|---|---|
| `Could not find lesson "1"` | Run from the repo folder or `tools\`; use `01` or `01_Hello_World`. |
| `no images in …\images` | Run `tools\import_images.py` or preview with `--placeholder`. Missing single scenes reuse the previous picture. |
| `Kokoro model not found` | Put `kokoro-v1.0.onnx` and `voices-v1.0.bin` in `tools\kokoro\` (or set `KOKORO_DIR`). Download: github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 |
| ffmpeg `Unable to parse option value "C"` / subtitles font error | The script copies Fredoka into `render\_work\fonts` and uses a relative `fontsdir` (the `C:` colon breaks ffmpeg). Use the current script; don't run from another drive's root. |
| `ffmpeg not found on PATH` | `winget install Gyan.FFmpeg`, then open a NEW terminal. |
| `--gpu: NVENC not available` | Update the NVIDIA driver; the render still works on CPU. GPU limits parallel encodes, which the script handles. |
| `live_02: NOT FOUND` | File must be `lessons\NN_*\live\live_02.mp4` (.mkv/.mov ok). Number = the `code 2` line in Segments.txt. |
| Live clip starts with fumbling | `live\trim.json`: `{"live_02": {"start": 4}}` |
| Intro is a black video | CapCut voice-only export – fine, only its audio is used, over the thumbnail. |
| Captions for my live talk missing | Expected: SRT covers AI narration. Use YouTube auto-captions, or `pip install faster-whisper` + `--whisper`. |
| Edited Script.md, voice didn't change | It does – the TTS cache is keyed by the text. Delete `.tts_cache\` if in doubt. |
