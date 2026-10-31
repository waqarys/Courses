#!/usr/bin/env python3
"""render_video.py - Python for Kids Fast Pipeline: one command turns a lesson folder into a finished video.

    python tools/render_video.py 01                       # lessons/01_Hello_World -> render/01_Hello_World_full.mp4
    python tools/render_video.py 01 --gpu                 # NVIDIA NVENC encode (RTX 3050 ok), CPU fallback
    python tools/render_video.py 01 --placeholder --quick # preview: colour cards, dummy live clips, 720p
    python tools/render_video.py --all --gpu              # every lesson that has images (or all with --placeholder)
    python tools/render_video.py 01 --intro my_intro.m4a --outro my_outro.m4a   # override voice/intro.* & voice/outro.*
    python tools/render_video.py 01 --ai-intro-outro      # ignore recordings, AI voice reads Intro_Outro.md

Video = INTRO + body + OUTRO.  The body order comes from <lesson>/Segments.txt:
    explain 1-3            Script.md scenes 1..3: AI voice (Kokoro) + images/scene_NN.jpg|png OR scene_NN.mp4 clip
    code 1 | Hello, World! "Let's code: Hello, World!" card, then live/live_01.(mp4|mkv|mov) - your OBS recording
    yourturn               "Your turn" challenge card read by the AI voice (Challenge.md)
    quiz                   optional Quiz.md questions with a 5-second countdown
INTRO: voice/intro.* (your CapCut voice, ~10 s) or - if missing - the AI voice reads Intro_Outro.md. Picture = this
lesson's thumbnail. OUTRO: voice/outro.* or AI voice, over the NEXT lesson's thumbnail + "UP NEXT" ribbon.

Live clips: any resolution / fps / aspect -> scaled + padded to 1920x1080 30 fps, audio loudness-normalised.
Optional live/trim.json: {"live_01": {"start": 3.0, "end": 95.5}, "live_02": {"start": 1}}
Missing live clip -> a "record live_NN here" card (or a dummy code screen with --placeholder), so a render never fails.

Outputs (lessons/NN_Topic/render/, git-ignored):
    NN_Topic_full.mp4   1920x1080 30 fps H.264 + AAC (explainer captions burned in)
    NN_Topic_full.srt   captions: AI narration + intro/outro (+ live speech with --whisper)
    NN_Topic_chapters.txt   YouTube chapters with real timestamps
    NN_Topic_thumb.jpg  1280x720 thumbnail     NN_Topic_short.mp4  1080x1920 Short (first explainer, <= 45 s)

Needs: Python 3.9+, ffmpeg on PATH, `pip install pillow numpy soundfile kokoro-onnx`
Kokoro model files (kokoro-v1.0.onnx + voices-v1.0.bin) in tools/kokoro/ or %KOKORO_DIR%.
Optional: `pip install faster-whisper` and --whisper to caption your live coding talk in the SRT.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LESSONS = ROOT / 'lessons'
sys.path.insert(0, str(HERE))
import prep_video as pv  # noqa: E402

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SR = 24000
W, H = 1920, 1080
FPS = 30
NAVY, CREAM, MINT, YEL, BLUE = (13, 27, 62), (255, 248, 225), (72, 199, 142), (255, 212, 59), (55, 118, 171)
FONT = HERE / 'fonts' / 'Fredoka.ttf'
MASCOT = ROOT / 'Character' / 'Minty_reference.png'
PRESET, CRF, GPU = ['veryfast'], ['20'], [False]
IMG_EXT, VID_EXT = ('.png', '.jpg', '.jpeg', '.webp'), ('.mp4', '.mov', '.webm', '.mkv')
LUFS = -16.0
EMOJI = re.compile('[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u200D\u20E3]')
SERIES = 'Python for Kids'


# ---------------------------------------------------------------- helpers
def venc(preset=None, crf=None):
    preset, crf = preset or PRESET[0], crf or CRF[0]
    if GPU[0]:
        return ['-c:v', 'h264_nvenc', '-preset', 'p1' if preset == 'ultrafast' else 'p5', '-rc', 'vbr',
                '-cq', str(int(crf) + 1), '-b:v', '0']
    return ['-c:v', 'libx264', '-preset', preset, '-crf', crf]


AENC = ['-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2']


def run(cmd, cwd=None):
    r = subprocess.run([str(c) for c in cmd], cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode:
        sys.stderr.write(r.stderr[-3000:])
        raise SystemExit(f'ffmpeg failed: {" ".join(map(str, cmd[:8]))} ...')
    return r


def local_fonts(work):
    """Copy the font next to the work files; a RELATIVE fontsdir avoids the Windows 'C:' colon breaking ffmpeg."""
    d = Path(work) / 'fonts'; d.mkdir(parents=True, exist_ok=True)
    if FONT.exists() and not (d / FONT.name).exists():
        shutil.copy2(FONT, d / FONT.name)
    return 'fonts'


def font(size, weight='Bold'):
    try:
        f = ImageFont.truetype(str(FONT), size)
        try:
            f.set_variation_by_name(weight)
        except Exception:
            pass
        return f
    except Exception:
        for c in ['C:/Windows/Fonts/arialbd.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']:
            if os.path.exists(c):
                return ImageFont.truetype(c, size)
        return ImageFont.load_default()


def mono(size):
    for c in ['C:/Windows/Fonts/consola.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf']:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return font(size, 'Regular')


def noemoji(s):
    return re.sub(r'\s{2,}', ' ', EMOJI.sub('', s)).strip()


def media_dur(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def has_audio(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a', '-show_entries', 'stream=index',
                        '-of', 'csv=p=0', str(p)], capture_output=True, text=True)
    return bool(r.stdout.strip())


def load_audio(path):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-vn', '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'],
                       stdout=subprocess.PIPE, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).copy()


def silence(sec):
    return np.zeros(int(max(0, sec) * SR), dtype=np.float32)


def srt_time(t):
    ms = int(round(max(0, t) * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'


def write_srt(cues, path):
    with open(path, 'w', encoding='utf-8') as f:
        for i, (a, b, t) in enumerate(cues, 1):
            f.write(f'{i}\n{srt_time(a)} --> {srt_time(b)}\n{t}\n\n')


def split_caption(text, maxc=42):
    words, lines, cur = text.split(), [], ''
    for w_ in words:
        if cur and len(cur) + len(w_) + 1 > maxc:
            lines.append(cur); cur = w_
        else:
            cur = (cur + ' ' + w_).strip()
    lines.append(cur)
    return ['\n'.join(lines[i:i + 2]) for i in range(0, len(lines), 2)]


def sentences(lines):
    out = []
    for l in lines:
        if l.startswith('[EDIT'):
            continue
        for part in re.split(r'(\(pause\))', l):
            part = part.strip()
            if part == '(pause)':
                out.append(None)
            elif part:
                out += [s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z*"\'#])', part) if s.strip()]
    return out


# ---------------------------------------------------------------- voice
class Voice:
    def __init__(self, voice, speed, cache):
        self.voice, self.speed, self.cache, self.k = voice, speed, cache, None
        cache.mkdir(parents=True, exist_ok=True)

    def say(self, text):
        text = text.replace('–', ', ').replace('…', '...').replace('#', 'hash sign ')
        key = hashlib.md5(f'{self.voice}|{self.speed}|{text}'.encode()).hexdigest()
        p = self.cache / f'{key}.npy'
        if p.exists():
            return np.load(p)
        if self.k is None:
            from kokoro_onnx import Kokoro
            cands = [Path(os.environ['KOKORO_DIR'])] if os.environ.get('KOKORO_DIR') else []
            cands += [HERE / 'kokoro', Path('/workspace/tts')]
            d = next((c for c in cands if (c / 'kokoro-v1.0.onnx').exists() and (c / 'voices-v1.0.bin').exists()), None)
            if d is None:
                sys.exit(f'Kokoro model not found: put kokoro-v1.0.onnx and voices-v1.0.bin in\n  {(HERE / "kokoro").resolve()}\n'
                         '  Download: https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 (see Troubleshooting.md)')
            self.k = Kokoro(str(d / 'kokoro-v1.0.onnx'), str(d / 'voices-v1.0.bin'))
        a, _ = self.k.create(text, voice=self.voice, speed=self.speed, lang='en-us')
        a = a.astype(np.float32); np.save(p, a)
        return a


# ---------------------------------------------------------------- cards (PIL, 1920x1080)
def fit_cover(img, w, h):
    r = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * r + 1), int(img.height * r + 1)), Image.LANCZOS)
    x, y = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def wrap(draw, text, f, maxw):
    words, lines, cur = text.split(), [], ''
    for w_ in words:
        t = (cur + ' ' + w_).strip()
        if draw.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur:
        lines.append(cur)
    return lines


def outlined(d, xy, text, f, fill=(255, 255, 255), stroke=NAVY, sw=8, anchor='la'):
    d.text(xy, text, font=f, fill=fill, stroke_width=sw, stroke_fill=stroke, anchor=anchor)


def mascot():
    return Image.open(MASCOT).convert('RGBA') if MASCOT.exists() else None


def paste_m(bg, m, h, x, y):
    if m:
        o = m.resize((int(m.width * h / m.height), h)); bg.paste(o, (x if x >= 0 else bg.width - o.width + x, y), o)


def card_bg(base=None):
    if base is not None:
        bg = fit_cover(base.convert('RGB'), W, H).filter(ImageFilter.GaussianBlur(18))
        return Image.blend(bg, Image.new('RGB', (W, H), MINT), .5)
    bg = Image.new('RGB', (W, H)); d = ImageDraw.Draw(bg)
    for i in range(H):
        d.line([(0, i), (W, i)], fill=(40 + i // 40, 170 - i // 18, 130 - i // 30))
    return bg


def badge(d, x=60, y=50, s=1.0, text='PYTHON FOR KIDS'):
    f = font(int(44 * s)); w_ = d.textlength(text, font=f)
    d.rounded_rectangle((x, y, x + w_ + 60 * s, y + 80 * s), radius=int(40 * s), fill=YEL)
    d.text((x + 30 * s, y + 40 * s), text, font=f, fill=NAVY, anchor='lm')


def title_card(title, sub, base, m):
    bg = card_bg(base); d = ImageDraw.Draw(bg)
    f = font(110); lines = wrap(d, noemoji(title), f, 1250)
    y = H // 2 - len(lines) * 65 - 40
    for l in lines:
        outlined(d, (120, y), l, f); y += 130
    outlined(d, (124, y + 10), sub, font(56, 'SemiBold'), fill=YEL, sw=6)
    badge(d); paste_m(bg, m, 620, -80, H - 680)
    return bg


def code_card(task, n, base, m):
    """'Let's code' card shown before each live clip."""
    bg = card_bg(base); d = ImageDraw.Draw(bg)
    d.rounded_rectangle((110, 200, 1300, 880), radius=40, fill=(30, 30, 46), outline=NAVY, width=8)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse((150 + i * 50, 235, 180 + i * 50, 265), fill=c)
    outlined(d, (170, 330), "LET'S CODE!", font(120), fill=YEL, sw=8)
    f = font(76, 'SemiBold')
    for k, l in enumerate(wrap(d, noemoji(task), f, 1050)[:3]):
        d.text((170, 520 + k * 95), l, font=f, fill=(255, 255, 255))
    d.text((170, 800), f'Live coding {n}  •  pause and type along!', font=font(44, 'SemiBold'), fill=(160, 230, 200))
    badge(d); paste_m(bg, m, 600, -60, H - 660)
    return bg


def yourturn_card(lines, base, m):
    bg = card_bg(base); d = ImageDraw.Draw(bg)
    outlined(d, (120, 90), 'YOUR TURN!', font(130), fill=YEL, sw=10)
    d.rounded_rectangle((110, 290, 1340, 960), radius=40, fill=CREAM, outline=NAVY, width=6)
    f = font(62, 'SemiBold'); y = 340
    for k, l in enumerate(lines[:5], 1):
        for j, w_ in enumerate(wrap(d, noemoji(l), f, 1050)[:2]):
            d.text((170, y), (f'{k}. ' if j == 0 else '    ') + w_, font=f, fill=NAVY); y += 80
        y += 20
    paste_m(bg, m, 640, -60, H - 700)
    return bg


def lower_third(text):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    text = noemoji(text)
    if text:
        f = font(64, 'SemiBold'); lines = wrap(d, text, f, 1500)[:2]; h = 40 + 80 * len(lines)
        d.rounded_rectangle((180, 60, 1740, 60 + h), radius=36, fill=CREAM + (235,), outline=NAVY, width=6)
        for i, l in enumerate(lines):
            d.text((W // 2, 120 + i * 80), l, font=f, fill=NAVY, anchor='mm')
    return im


def quiz_card(n, total, q, opts, ans=None, count=None, why=None, base=None):
    cols = [(229, 57, 53), (30, 136, 229), (67, 160, 71), (251, 140, 0)]
    bg = card_bg(base); d = ImageDraw.Draw(bg)
    outlined(d, (80, 60), f'QUIZ {n}/{total}', font(60), fill=YEL, sw=6)
    f = font(66); y = 170
    for l in wrap(d, noemoji(q), f, 1500)[:3]:
        outlined(d, (100, y), l, f, sw=7); y += 84
    top = max(y + 30, 470)
    for i, (L, o) in enumerate(zip('ABCD', opts)):
        x0 = 100 + (i % 2) * 860; y0 = top + (i // 2) * 190; col = cols[i]
        if ans and L != ans:
            col = tuple(int(c * .45 + 110) for c in col)
        d.rounded_rectangle((x0, y0, x0 + 820, y0 + 160), radius=80, fill=col,
                            outline=(255, 255, 255) if ans == L else NAVY, width=12 if ans == L else 5)
        d.text((x0 + 410, y0 + 80), f'{L}. {noemoji(o)}', font=font(54, 'SemiBold'), fill=(255, 255, 255), anchor='mm')
    if count is not None:
        d.ellipse((1660, 40, 1860, 240), fill=(255, 255, 255), outline=YEL, width=14)
        d.text((1760, 140), str(count), font=font(120), fill=NAVY, anchor='mm')
    if why:
        fw = font(46, 'SemiBold'); d.rounded_rectangle((100, H - 130, 1820, H - 40), radius=30, fill=CREAM)
        d.text((W // 2, H - 85), wrap(d, noemoji(why), fw, 1650)[0], font=fw, fill=NAVY, anchor='mm')
    return bg


def thumbnail(art, text, m, lesson_no):
    t = fit_cover(art.convert('RGB'), 1280, 720) if art else card_bg(None).resize((1280, 720))
    d = ImageDraw.Draw(t)
    f = font(120); lines = wrap(d, noemoji(text).upper(), f, 760)
    while len(lines) > 2 and f.size > 70:
        f = font(f.size - 10); lines = wrap(d, noemoji(text).upper(), f, 760)
    y = 170
    for l in lines[:3]:
        outlined(d, (50, y), l, f, sw=10); y += f.size + 10
    badge(d, 40, 30, .8, f'PYTHON • LESSON {int(lesson_no)}')
    if not art and m:
        o = m.resize((int(m.width * 600 / m.height), 600)); t.paste(o, (1280 - o.width - 20, 110), o)
    return t


def banner(img, text, colour=(229, 57, 53)):
    im = img.convert('RGB').resize((1280, 720)); d = ImageDraw.Draw(im)
    f = font(54); w_ = d.textlength(text, font=f) + 70
    d.rounded_rectangle((1280 - w_ - 30, 600, 1250, 690), radius=45, fill=colour)
    d.text((1280 - 30 - w_ / 2, 645), text, font=f, fill=(255, 255, 255), anchor='mm')
    return im


def fake_code_png(code, path):
    """Placeholder 'screen recording' frame: an editor window with the code (used only with --placeholder)."""
    im = Image.new('RGB', (1600, 900), (245, 245, 245)); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1600, 50), fill=(220, 220, 225)); d.text((20, 12), 'Thonny  -  lesson.py  (PLACEHOLDER live clip)', font=mono(26), fill=(60, 60, 60))
    y = 90
    for i, l in enumerate(code.splitlines()[:14], 1):
        d.text((30, y), f'{i:>2}', font=mono(34), fill=(150, 150, 150)); d.text((110, y), l, font=mono(34), fill=(20, 20, 120)); y += 48
    d.ellipse((1270, 570, 1570, 870), fill=(255, 200, 160), outline=(255, 255, 255), width=8)   # webcam circle
    d.text((1420, 720), 'cam', font=font(50), fill=NAVY, anchor='mm')
    im.save(path)


# ---------------------------------------------------------------- ffmpeg pieces (all parts: same size/fps/codec)
def norm_vf(w, h):
    return (f'scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color=0x0d1b3e,'
            f'setsar=1,fps={FPS},format=yuv420p')


def visual_clip(src, dur, out, size, overlay=None, kb=True):
    """Still (Ken Burns zoom) or Imagine video (looped/trimmed, muted) -> silent mp4 of exactly dur seconds."""
    w, h = size; frames = max(1, int(round(dur * FPS)))
    src = Path(src)
    if src.suffix.lower() in VID_EXT:
        cmd = ['ffmpeg', '-y', '-v', 'error', '-stream_loop', '-1', '-i', src]
        base = f'[0:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1,fps={FPS},format=yuv420p'
    else:
        cmd = ['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', FPS, '-i', src]
        if kb:
            base = (f"[0:v]scale={w * 2}:{h * 2}:force_original_aspect_ratio=increase,crop={w * 2}:{h * 2},"
                    f"zoompan=z='1+0.08*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={w}x{h}:fps={FPS},format=yuv420p")
        else:
            base = f'[0:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={FPS},format=yuv420p'
    if overlay:
        cmd += ['-loop', '1', '-framerate', FPS, '-i', overlay]
        fc = f'{base}[b];[1:v]scale={w}:{h},format=rgba[o];[b][o]overlay=0:0,format=yuv420p'
    else:
        fc = base
    run(cmd + ['-filter_complex', fc, '-frames:v', frames, '-an', *venc(), '-pix_fmt', 'yuv420p', out])


class Part:
    """A rendered piece of the final video: path, duration, captions (relative), chapter title."""
    def __init__(self, path, dur, cues=(), chapter=None, kind=''):
        self.path, self.dur, self.cues, self.chapter, self.kind = path, dur, list(cues), chapter, kind


def slideshow(items, out, work, size, burn=True, tag='p'):
    """items: list of (visual_path, audio np @24k, kb, overlay_png, caps[(s,e,text)]) -> Part (mp4 with burned captions)."""
    clips, auds, cues, t = [], [], [], 0.0
    for k, (vis, aud, kb, ov, caps) in enumerate(items):
        dur = max(len(aud) / SR, 0.5)
        c = work / f'{tag}_{k:02d}.mp4'; visual_clip(vis, dur, c, size, ov, kb); clips.append(c)
        auds.append(np.concatenate([aud, silence(dur - len(aud) / SR)]))
        for s, e, txt in caps:
            pieces = split_caption(txt)
            for j, pc in enumerate(pieces):
                cues.append((t + s + (e - s) * j / len(pieces), t + s + (e - s) * (j + 1) / len(pieces), pc))
        t += dur
    import soundfile as sf
    sf.write(work / f'{tag}.wav', np.concatenate(auds), SR)
    (work / f'{tag}_list.txt').write_text(''.join(f"file '{c.name}'\n" for c in clips))
    write_srt(cues, work / f'{tag}.srt')
    style = ("Fontname=Fredoka,Fontsize=21,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H003E1B0D,"
             "BorderStyle=1,Outline=3,Shadow=0,MarginV=28")
    fd = local_fonts(work)
    vf = f"subtitles={tag}.srt:fontsdir='{fd}':force_style='{style}'" if (burn and cues) else 'null'
    run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', f'{tag}_list.txt', '-i', f'{tag}.wav',
         '-vf', vf, '-af', f'loudnorm=I={LUFS}:TP=-1.5:LRA=11', *venc(), '-pix_fmt', 'yuv420p', *AENC,
         '-t', f'{t:.3f}', Path(out).resolve()], cwd=work)
    return Part(out, t, cues)


def live_part(src, out, size, trim):
    """Your OBS recording -> same format as the rest: scaled+padded, 30 fps, loudness-normalised, optional trim."""
    w, h = size
    pre = (['-ss', str(trim['start'])] if trim.get('start') else []) + (['-to', str(trim['end'])] if trim.get('end') else [])
    cmd = ['ffmpeg', '-y', '-v', 'error', *pre, '-i', src]
    if has_audio(src):
        af = ['-af', f'loudnorm=I={LUFS}:TP=-1.5:LRA=11,aresample=48000']
    else:
        cmd += ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']; af = ['-map', '0:v', '-map', '1:a', '-shortest']
    run(cmd + ['-vf', norm_vf(w, h), *af, *venc(), '-pix_fmt', 'yuv420p', *AENC, out])
    return Part(out, media_dur(out), kind='live')


def concat_parts(parts, out, work):
    """Join same-format parts with short 0.3 s crossfades into the final video."""
    XF = 0.3
    ins, fl = [], []
    for i, p in enumerate(parts):
        ins += ['-i', Path(p.path).resolve()]
    v, a, t = '[0:v]', '[0:a]', parts[0].dur
    starts = [0.0]
    for i, p in enumerate(parts[1:], 1):
        fl.append(f'{v}[{i}:v]xfade=transition=fade:duration={XF}:offset={t - XF:.3f}[v{i}]')
        fl.append(f'{a}[{i}:a]acrossfade=d={XF}[a{i}]')
        starts.append(t - XF); v, a, t = f'[v{i}]', f'[a{i}]', t + p.dur - XF
    cmd = ['ffmpeg', '-y', '-v', 'error', *ins]
    if fl:
        cmd += ['-filter_complex', ';'.join(fl), '-map', v, '-map', a]
    run(cmd + [*venc(), '-pix_fmt', 'yuv420p', *AENC, '-movflags', '+faststart', out])
    return starts, t


# ---------------------------------------------------------------- lesson files
def resolve_lesson(arg):
    raw = str(arg).strip().strip('"\'').replace('\\', '/').rstrip('/')
    c = Path(raw)
    for p in ([c] if c.is_absolute() else [Path.cwd() / c, LESSONS / c, ROOT / c]):
        if (p / 'Script.md').exists():
            return p.resolve()
    key = Path(raw).name
    if re.fullmatch(r'\d{1,2}', key):
        key = f'{int(key):02d}_'
    hits = sorted(p for p in LESSONS.iterdir() if p.is_dir() and p.name.lower().startswith(key.lower()))
    if len(hits) == 1:
        return hits[0]
    sys.exit(f'Could not find lesson "{arg}" in {LESSONS}. Use 01 or 01_Hello_World.')


def parse_segments(folder, nscenes):
    f = folder / 'Segments.txt'
    if not f.exists():
        return [('explain', list(range(1, nscenes + 1)), ''), ('yourturn', [], '')]
    segs = []
    for l in f.read_text(encoding='utf-8').splitlines():
        l = l.split('#', 1)[0].strip() if not l.strip().startswith('code') else l.strip()
        if not l:
            continue
        head, _, title = l.partition('|')
        w = head.split()
        kind = w[0].lower()
        nums = []
        if len(w) > 1:
            a_, _, b_ = w[1].partition('-'); nums = list(range(int(a_), int(b_ or a_) + 1))
        segs.append((kind, nums, title.strip()))
    return segs


def quoted(path, head=None):
    if not path.exists():
        return []
    t = path.read_text(encoding='utf-8')
    if head:
        m = re.search(r'^## ' + head + r'[^\n]*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
        t = m.group(1) if m else ''
    return [q.strip() for q in re.findall(r'^> (.+)$', t, re.M)]


def find_visuals(folder):
    d = folder / 'images'; found, thumb = {}, None
    if d.exists():
        for p in sorted(d.iterdir()):
            ext = p.suffix.lower()
            if ext not in IMG_EXT + VID_EXT:
                continue
            if p.stem.lower().startswith('thumb') and ext in IMG_EXT:
                thumb = p; continue
            m = re.match(r'^(?:scene|sc|s)[\s_\-]*0*(\d{1,2})(?:\D.*)?$', p.stem, re.I)
            if m:
                i = int(m.group(1))
                # a video clip beats a still for the same scene; otherwise the newest file wins
                if i not in found or (ext in VID_EXT and found[i].suffix.lower() not in VID_EXT) or \
                        ((ext in VID_EXT) == (found[i].suffix.lower() in VID_EXT) and p.stat().st_mtime > found[i].stat().st_mtime):
                    found[i] = p
    return found, thumb


def find_voice(folder, stem, override):
    if override:
        p = Path(str(override).strip('"\'').replace('\\', '/'))
        for c in ([p] if p.is_absolute() else [Path.cwd() / p, folder / p, folder / 'voice' / p]):
            if c.exists():
                return c.resolve()
        sys.exit(f'--{stem} file not found: {override}')
    return next((p for p in sorted((folder / 'voice').glob(stem + '.*')) if p.suffix.lower() in
                 ('.m4a', '.mp3', '.wav', '.mp4', '.mov', '.aac', '.ogg', '.mkv')), None)


def placeholder(i, name, text, path):
    cols = [(72, 199, 142), (55, 118, 171), (251, 140, 0), (142, 68, 173), (229, 57, 53), (0, 150, 136)]
    c = cols[(i - 1) % len(cols)]
    im = Image.new('RGB', (W, H), c); d = ImageDraw.Draw(im)
    d.rounded_rectangle([120, 120, W - 120, H - 230], 50, fill=CREAM)
    d.text((W // 2, 230), f'PLACEHOLDER  •  Scene {i}', font=font(54), fill=c, anchor='mm')
    for k, l in enumerate(wrap(d, name, font(96), W - 400)[:2]):
        d.text((W // 2, 400 + k * 115), l, font=font(96), fill=NAVY, anchor='mm')
    for k, l in enumerate(wrap(d, noemoji(text), font(56, 'SemiBold'), W - 400)[:3]):
        d.text((W // 2, 650 + k * 70), l, font=font(56, 'SemiBold'), fill=(80, 80, 80), anchor='mm')
    im.save(path); return path


def lesson_thumb(folder, m):
    yt = pv.parse_youtube(folder / 'YouTube.md') if (folder / 'YouTube.md').exists() else {'thumb': '', 'title': folder.name}
    _, art = find_visuals(folder)
    text = yt['thumb'].split('"')[1] if '"' in yt['thumb'] else re.sub(r'\s*\|.*', '', yt['title'])
    return thumbnail(Image.open(art) if art else None, text, m, folder.name[:2])


# ---------------------------------------------------------------- main render
def render(arg, a):
    t0 = time.time()
    folder = resolve_lesson(arg); name = folder.name
    scenes = pv.parse_script(folder / 'Script.md')
    yt = pv.parse_youtube(folder / 'YouTube.md')
    out = folder / 'render'; work = out / '_work'
    shutil.rmtree(work, ignore_errors=True); work.mkdir(parents=True, exist_ok=True)
    size = (1280, 720) if a.quick else (W, H)
    PRESET[0], CRF[0] = ('ultrafast', '28') if a.quick else ('veryfast', '20')
    voice = Voice(a.voice, a.speed, ROOT / '.tts_cache')
    m = mascot()
    vis, _ = find_visuals(folder)
    if a.placeholder:
        vis = {**{i: placeholder(i, s['name'], s['onscreen'], work / f'ph_{i:02d}.png') for i, s in enumerate(scenes, 1)}, **vis}
        print(f'{name}: PLACEHOLDER mode - colour cards for every scene without a picture/clip')
    elif not vis:
        print(f'{name}: no images in {folder / "images"} - run tools/import_images.py, or use --placeholder'); return None
    miss = [i for i in range(1, len(scenes) + 1) if i not in vis]
    if miss:
        print('  missing scene visuals (previous picture reused): ' + ', '.join(f'scene_{i:02d}' for i in miss))
    first = next(iter(sorted(vis.items())))[1]
    first_still = Image.open(first) if first.suffix.lower() in IMG_EXT else None

    def speak(items):
        parts, caps, t = [], [], 0.0
        for s in items:
            if s is None:
                parts.append(silence(a.pause)); t += a.pause; continue
            clean = re.sub(r'\*\*?|\[[^\]]*\]', '', s).strip()
            if not clean:
                continue
            x = voice.say(clean); parts += [x, silence(.25)]
            caps.append((t, t + len(x) / SR, clean)); t += len(x) / SR + .25
        return (np.concatenate(parts) if parts else silence(.5)), caps

    def png(img, tag):
        p = work / f'{tag}.png'; img.convert('RGB').save(p); return p

    thumb = lesson_thumb(folder, m); thumb.save(out / f'{name}_thumb.jpg', quality=90)
    parts = []
    # ---- INTRO: your voice or AI voice, over this lesson's thumbnail
    it_text = ' '.join(quoted(folder / 'Intro_Outro.md', 'INTRO'))
    ot_text = ' '.join(quoted(folder / 'Intro_Outro.md', 'OUTRO'))

    def bookend(kind, pic, text, override):
        rec = None if a.ai_intro_outro else find_voice(folder, kind, override)
        if rec:
            aud, caps = load_audio(rec), [(0.2, max(.5, media_dur(rec) - .2), text)] if text else []
            print(f'  {kind}: your recording {rec.name} ({len(aud) / SR:.1f} s)')
        else:
            aud, caps = speak(sentences([text])) if text else (silence(2), [])
            print(f'  {kind}: AI voice ({len(aud) / SR:.1f} s)')
        p = slideshow([(png(pic, kind), np.concatenate([aud, silence(.4)]), True, None, caps)], work / f'{kind}.mp4',
                      work, size, burn=False, tag=kind)
        p.chapter = 'Intro' if kind == 'intro' else None; p.kind = kind
        return p

    if not a.no_intro_outro:
        parts.append(bookend('intro', thumb, it_text, a.intro))
    # ---- title card
    tt = re.sub(r'\s*\|.*', '', yt['title'])
    tp = slideshow([(png(title_card(tt, f'{SERIES}  •  Lesson {int(name[:2])}', first_still, m), 'title'),
                     silence(3.0), False, None, [])], work / 'title.mp4', work, size, False, 'title')
    tp.chapter = None if parts else 'Intro'
    parts.append(tp)
    # ---- body from Segments.txt
    ncode = 0; last = first; explain_parts = []
    for si, (kind, nums, title) in enumerate(parse_segments(folder, len(scenes))):
        if kind == 'explain':
            items = []
            for i in nums:
                if i > len(scenes):
                    print(f'  Segments.txt: scene {i} does not exist in Script.md, skipped'); continue
                s = scenes[i - 1]; v = vis.get(i, last); last = v
                lt = work / f'lt{i:02d}.png'; lower_third(s['onscreen']).save(lt)
                aud, caps = speak(sentences(s['lines']))
                items.append((v, np.concatenate([silence(.3), aud]), True, lt, [(c0 + .3, c1 + .3, t) for c0, c1, t in caps]))
            if items:
                p = slideshow(items, work / f'ex{si:02d}.mp4', work, size, not a.no_captions, f'ex{si:02d}')
                p.chapter = scenes[nums[0] - 1]['name']; p.kind = 'explain'; parts.append(p); explain_parts.append(p)
        elif kind == 'code':
            ncode += 1; k = nums[0] if nums else ncode
            task = title or f'Step {k}'
            say, caps = speak([f"Let's code! {task.rstrip('.!?')}."])
            cp = slideshow([(png(code_card(task, k, first_still, m), f'cc{k}'), np.concatenate([aud_pad(say), silence(.6)]), False, None, caps)],
                           work / f'cc{k:02d}.mp4', work, size, not a.no_captions, f'cc{k:02d}')
            cp.chapter = f"Let's code: {task}"; parts.append(cp)
            src = next((p for p in sorted((folder / 'live').glob(f'live_{k:02d}.*')) if p.suffix.lower() in VID_EXT), None)
            trims = {}
            if (folder / 'live' / 'trim.json').exists():
                trims = json.loads((folder / 'live' / 'trim.json').read_text(encoding='utf-8'))
            if src is None and a.placeholder:
                fp = work / f'fake{k}.png'; fake_code_png(code_for(folder, k), fp)
                tone = 0.15 * np.sin(np.linspace(0, 2 * np.pi * 220 * 6, 6 * SR)).astype(np.float32) * (np.arange(6 * SR) % SR < SR // 8)
                lp = slideshow([(fp, tone.astype(np.float32), False, None, [])], work / f'fake{k}.mp4', work, size, False, f'fake{k}')
                src = lp.path; print(f'  live_{k:02d}: missing -> dummy code screen (placeholder)')
            if src is None:
                lp = slideshow([(png(title_card(f'Record live_{k:02d} here', task, first_still, m), f'miss{k}'), silence(4), False, None, [])],
                               work / f'miss{k}.mp4', work, size, False, f'miss{k}')
                print(f'  live_{k:02d}: NOT FOUND in {folder / "live"} -> 4 s reminder card'); parts.append(lp); continue
            lp = live_part(src, work / f'live{k:02d}.mp4', size, trims.get(f'live_{k:02d}', {}))
            if a.whisper:
                lp.cues = whisper_cues(lp.path)
            print(f'  live_{k:02d}: {Path(src).name} -> {lp.dur:.1f} s'); parts.append(lp)
        elif kind == 'yourturn':
            ch = quoted(folder / 'Challenge.md') or ['Change the code and run it again.']
            aud, caps = speak(['Your turn!'] + ch + ['Pause the video and try it now.'])
            p = slideshow([(png(yourturn_card(ch, first_still, m), 'yt'), np.concatenate([aud, silence(2)]), False, None, caps)],
                          work / 'yourturn.mp4', work, size, not a.no_captions, 'yourturn')
            p.chapter = 'Your turn'; parts.append(p)
        elif kind == 'quiz' and (folder / 'Quiz.md').exists():
            qs = pv.parse_quiz(folder / 'Quiz.md'); items = []
            for n, q in enumerate(qs, 1):
                opts = [o for _, o in q['opts']]; ans = q['ans'][0]; qt = q['q'].split('. ', 1)[-1]
                aq, cq = speak([qt] + [f'{L}. {noemoji(o)}.' for L, o in q['opts']])
                items.append((png(quiz_card(n, len(qs), qt, opts, base=first_still), f'q{n}'), aq, False, None, cq))
                for c in range(5, 0, -1):
                    items.append((png(quiz_card(n, len(qs), qt, opts, count=c, base=first_still), f'q{n}c{c}'), silence(1), False, None, []))
                ar, cr = speak([f'The answer is {ans}. {noemoji(opts["ABCD".index(ans)])}!', q['why']])
                items.append((png(quiz_card(n, len(qs), qt, opts, ans=ans, why=q['why'], base=first_still), f'q{n}a'),
                              np.concatenate([ar, silence(.8)]), False, None, cr))
            if items:
                p = slideshow(items, work / 'quiz.mp4', work, size, not a.no_captions, 'quiz'); p.chapter = 'Quiz'; parts.append(p)
    # ---- OUTRO: next lesson's thumbnail + UP NEXT
    if not a.no_intro_outro:
        n = int(name[:2]) + 1
        nxt = next((p for p in sorted(LESSONS.iterdir()) if p.is_dir() and p.name.startswith(f'{n:02d}_')), None)
        pic = banner(lesson_thumb(nxt, m), 'UP NEXT') if nxt else banner(thumb, 'FULL COURSE PLAYLIST', (46, 125, 50))
        parts.append(bookend('outro', pic, ot_text, a.outro))
    # ---- join
    full = out / f'{name}_full.mp4'
    starts, total = concat_parts(parts, full, work)
    cues, chap = [], []
    for p, s in zip(parts, starts):
        cues += [(s + c0, s + c1, t) for c0, c1, t in p.cues]
        if p.chapter:
            chap.append((s, p.chapter))
    write_srt(cues, out / f'{name}_full.srt')
    merged = []
    for t, c in chap:   # YouTube: first chapter 0:00, each >= 10 s
        if merged and t - merged[-1][0] < 10:
            continue
        merged.append((t, c))
    if merged:
        merged[0] = (0.0, merged[0][1])
    (out / f'{name}_chapters.txt').write_text('\n'.join(f'{int(t // 60)}:{int(t % 60):02d} {c}' for t, c in merged), encoding='utf-8')
    (out / f'{name}_parts.json').write_text(json.dumps([dict(kind=p.kind or 'card', chapter=p.chapter, start=round(s, 2),
                                                             dur=round(p.dur, 2), file=Path(p.path).name) for p, s in zip(parts, starts)], indent=1))
    if not a.no_short and explain_parts:
        make_short(name, explain_parts[0], out, work)
    if not a.keep_work:
        shutil.rmtree(work, ignore_errors=True)
    secs = time.time() - t0
    print(f'{name}: {total / 60:.1f} min video ({len(parts)} parts) rendered in {secs / 60:.1f} min -> {full}')
    return dict(name=name, video_min=round(total / 60, 2), render_min=round(secs / 60, 2))


def aud_pad(x):
    return np.concatenate([silence(.3), x])


def code_for(folder, k):
    t = (folder / 'Live_Coding.md').read_text(encoding='utf-8') if (folder / 'Live_Coding.md').exists() else ''
    m = re.search(rf'^## live_{k:02d}.*?```python\n(.*?)```', t, re.M | re.S)
    return m.group(1) if m else 'print("Hello, World!")'


def whisper_cues(path):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print('  --whisper: pip install faster-whisper (skipped)'); return []
    model = WhisperModel('small.en', device='auto', compute_type='int8')
    segs, _ = model.transcribe(str(path), vad_filter=True)
    return [(s.start, s.end, s.text.strip()) for s in segs]


def make_short(name, part, out, work, maxs=45):
    """1080x1920 Short from the first explainer: blurred background + the 16:9 video in the middle + titles."""
    ov = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    outlined(d, (540, 300), 'Python', font(110), anchor='mm'); outlined(d, (540, 430), 'for Kids', font(110), fill=YEL, anchor='mm')
    outlined(d, (540, 1560), 'Full lesson + live coding', font(60, 'SemiBold'), anchor='mm', sw=6)
    outlined(d, (540, 1650), 'on the channel!', font(60, 'SemiBold'), anchor='mm', sw=6)
    ov.save(work / 'short_ov.png')
    fc = ('[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25[bg];'
          '[b]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2[m];[m][1:v]overlay=0:0,fps=30,format=yuv420p')
    run(['ffmpeg', '-y', '-v', 'error', '-t', str(min(maxs, part.dur)), '-i', Path(part.path).resolve(), '-loop', '1', '-i', 'short_ov.png',
         '-filter_complex', fc, '-t', str(min(maxs, part.dur)), *venc('veryfast', '21'), *AENC, (out / f'{name}_short.mp4').resolve()], cwd=work)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('lessons', nargs='*')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--voice', default='af_heart'); ap.add_argument('--speed', type=float, default=0.92)
    ap.add_argument('--pause', type=float, default=2.5)
    ap.add_argument('--quick', action='store_true', help='1280x720 ultrafast preview, no Short')
    ap.add_argument('--gpu', action='store_true', help='NVIDIA h264_nvenc, falls back to CPU')
    ap.add_argument('--placeholder', action='store_true', help='no Imagine pictures / live clips needed')
    ap.add_argument('--intro'); ap.add_argument('--outro')
    ap.add_argument('--ai-intro-outro', action='store_true', help='always use the AI voice for intro/outro')
    ap.add_argument('--no-intro-outro', action='store_true')
    ap.add_argument('--whisper', action='store_true', help='caption live clips with faster-whisper (optional)')
    ap.add_argument('--no-short', action='store_true'); ap.add_argument('--no-captions', action='store_true')
    ap.add_argument('--keep-work', action='store_true')
    a = ap.parse_args()
    if shutil.which('ffmpeg') is None:
        sys.exit('ffmpeg not found on PATH (Windows: winget install Gyan.FFmpeg, then open a new terminal)')
    if a.gpu:
        r = subprocess.run(['ffmpeg', '-v', 'error', '-f', 'lavfi', '-i', 'color=c=black:s=256x256:d=0.2',
                            '-c:v', 'h264_nvenc', '-f', 'null', '-'], capture_output=True, text=True)
        GPU[0] = r.returncode == 0
        print('GPU encoding on (h264_nvenc).' if GPU[0] else '--gpu: NVENC not available, using CPU.')
    if a.quick:
        a.no_short = True
    ls = a.lessons
    if a.all:
        ls = [p.name for p in sorted(LESSONS.iterdir()) if (p / 'Script.md').exists() and (a.placeholder or find_visuals(p)[0])]
    if not ls:
        ap.print_help(); sys.exit(1)
    res = [r for r in (render(x, a) for x in ls) if r]
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
