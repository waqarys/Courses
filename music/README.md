# Background music

Background music for every video, mixed in automatically by `tools/render_video.py`.

## The tracks
Five CC0 tracks are already here – see [CREDITS.md](CREDITS.md). `theme_happy_ukulele_island.mp3` is the channel
sound under every intro/outro; the others rotate under the explainers. Nothing to do.

To add your own: only CC0/public-domain files (OpenGameArt "CC0", Free Music Archive "CC0"). Name a file
`theme_….mp3` to make it the intro/outro theme (first one alphabetically wins). For a CC-BY track put the exact
credit line in `<track>.txt` next to it; it is copied into `render/<video>_music.txt` for the description.
Don't add YouTube Audio Library / Pixabay files to the repo (no redistribution) or trending songs (Content ID).

## How it is mixed
| Part | Music |
|---|---|
| Intro / outro / title / end cards | clearly audible bed (~−28 LUFS, well under the voice) |
| AI narration, explainer, quiz questions | very quiet, and ducked further while the voice speaks |
| Quiz 5-4-3-2-1 countdown, live coding clips | silent (0.5 s fade) |
| Short | same "quiet under narration" rule |
The track loops if it is shorter than the video and fades out over the last 1.5 s.

## Flags
```
--no-music                 render without music
--music music/other.mp3    use this track instead of the automatic pick
--music-level -3           all music 3 dB quieter (+3 = louder)
```
Fine-tune constants at the top of `tools/music_bed.py` (BED_DB, UNDER_DB, FADE, DUCK).
No files here → the video renders exactly as before (one info line, no error).
