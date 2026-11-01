"""music_bed.py - background music for the render scripts (shared by the Science Olympiad and Python for Kids pipelines).

Music files: <series>/music/*.mp3|m4a|wav|ogg|flac (see music/CREDITS.md). theme_*.mp3 plays under the intro/outro
and cards in every video (channel sound); one of the other tracks plays under the explainer, chosen by a hash of the
video name (stable on re-renders). --music FILE uses one file for everything. --no-music turns it off. No music folder -> no music, no error.

Levels (edit here or use --music-level to shift everything by N dB):
    track is first normalised to MUSIC_LUFS, then per section:
    'bed'    intro / outro / title & end cards   BED_DB     (music clearly audible under your voice)
    'under'  AI narration, explainer, quiz text  UNDER_DB   (+ sidechain ducking while the voice speaks)
    'silent' quiz countdown, live coding clips   silence    (faded over FADE seconds)
The video stream is copied (no re-encode), so --gpu/--quick don't matter here.
"""
import hashlib, json, os, subprocess, sys
from pathlib import Path

MUSIC_LUFS = -28.0   # loudness the track is normalised to before the section gains
BED_DB = 0.0         # intro/outro/cards: about -28 LUFS, ~12-14 dB under a -14..-16 LUFS voice
UNDER_DB = -8.0      # narration sections, before ducking (~-36 LUFS)
FADE = 0.5           # seconds for every level change
DUCK = 'threshold=0.03:ratio=8:attack=20:release=400'   # sidechaincompress settings
EXTS = ('.mp3', '.m4a', '.wav', '.ogg', '.flac', '.aac')


def pick_track(root, name, music=None, no_music=False):
    """-> (theme, explainer) Paths or None. theme_*.mp3 = channel sound under intro/outro/cards; the other tracks
    rotate under the explainers (chosen by a hash of the video name, so re-renders keep the same track)."""
    if no_music:
        return None
    if music:
        p = Path(str(music).strip('"\'').replace('\\', '/'))
        for c in ([p] if p.is_absolute() else [Path.cwd() / p, Path(root) / p, Path(root) / 'music' / p]):
            if c.exists():
                return c.resolve(), c.resolve()
        sys.exit(f'--music file not found: {music}')
    d = Path(root) / 'music'
    files = sorted(p for p in d.glob('*') if p.suffix.lower() in EXTS) if d.exists() else []
    if not files:
        print(f'  music: none (put .mp3/.m4a/.wav files in {d} to add background music)')
        return None
    themes = [f for f in files if f.name.lower().startswith('theme')]
    rest = [f for f in files if f not in themes] or files
    under = rest[int(hashlib.md5(name.encode()).hexdigest(), 16) % len(rest)]
    return (themes[0] if themes else under), under


def credit(tracks, out_txt):
    """Write 'Music: ...' lines (+ attribution from music/CREDITS.md entries or <track>.txt) for the YouTube description."""
    lines = []
    for t in dict.fromkeys(tracks):
        txt = Path(t).with_suffix('.txt')
        cr = Path(t).parent / 'CREDITS.md'
        row = next((l for l in (cr.read_text(encoding='utf-8').splitlines() if cr.exists() else []) if f'`{Path(t).name}`' in l), '')
        c = [x.strip() for x in row.split('|')]
        if txt.exists():
            lines.append(txt.read_text(encoding='utf-8').strip())
        elif len(c) > 4:
            lines.append(f'Music: "{c[2]}" by {c[3]} (CC0) {c[4]}')
        else:
            lines.append(f'Music: {Path(t).stem.replace("_", " ")}')
    Path(out_txt).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return lines


def _gain_expr(sections, level_db, kinds):
    """sections: [(start, end, kind)] -> ffmpeg volume expression for the given kinds (linear gain, FADE-second ramps)."""
    g = {k: v for k, v in {'bed': BED_DB + level_db, 'under': UNDER_DB + level_db}.items() if k in kinds}
    terms = []
    for a, b, kind in sections:
        if kind not in g or b - a <= 0.05:
            continue
        lin = 10 ** (g[kind] / 20)
        r = min(FADE, (b - a) / 2)
        terms.append(f'{lin:.4f}*clip((t-{a:.3f})/{r:.3f}+0.5,0,1)*clip(({b:.3f}-t)/{r:.3f}+0.5,0,1)')
    return '+'.join(terms) or '0'


def add_music(video, sections, tracks, level_db=0.0, out=None):
    """Mix the track under the existing audio of `video` (in place unless out is given)."""
    video = Path(video); out = Path(out) if out else video.with_name(video.stem + '_m' + video.suffix)
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(video)],
                               capture_output=True, text=True).stdout.strip())
    theme, under = tracks
    e_bed, e_under = _gain_expr(sections, level_db, ('bed',)), _gain_expr(sections, level_db, ('under',))
    dbg = bool(os.environ.get('MUSIC_DEBUG'))   # also writes <video>.music.wav (music stem) for level checks
    if dbg:
        Path(str(video) + '.music.json').write_text(json.dumps(sections))
    prep = f'aresample=48000,aformat=channel_layouts=stereo,atrim=duration={dur:.3f},loudnorm=I={MUSIC_LUFS}:TP=-6:LRA=11,aresample=48000'
    fc = (f"[1:a]{prep},volume='{e_bed}':eval=frame[mb];[2:a]{prep},volume='{e_under}':eval=frame[mu];"
          f'[mb][mu]amix=inputs=2:duration=first:normalize=0,afade=t=out:st={max(0, dur - 1.5):.3f}:d=1.5[m];'
          f'[0:a]aresample=48000,aformat=channel_layouts=stereo,asplit=2[v][sc];'
          f'[m][sc]sidechaincompress={DUCK}' + (',asplit=2[md][stem];' if dbg else '[md];') +
          f'[v][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]')
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', str(video), '-stream_loop', '-1', '-i', str(theme), '-stream_loop', '-1', '-i', str(under),
           '-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
           '-movflags', '+faststart', '-t', f'{dur:.3f}', str(out)]
    if dbg:
        cmd += ['-map', '[stem]', '-t', f'{dur:.3f}', str(video) + '.music.wav']
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(r.stderr[-2000:]); print(f'  music: mixing failed for {video.name}, kept the video without music')
        return False
    if out.name.endswith('_m' + video.suffix):
        out.replace(video)
    return True
