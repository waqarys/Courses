#!/usr/bin/env python3
"""make_lessons.py - build the lessons/NN_Topic/ folders for the Fast Pipeline from the existing course
material (slides/slides.source.md, notes/RECORDING-NOTES.md, code/).

    python tools/make_lessons.py            # create missing lesson folders (never overwrites your edits)
    python tools/make_lessons.py --force    # regenerate every generated file (careful!)

Per lesson it writes: Script.md, Segments.txt, Visual_Prompts.md, Live_Coding.md, Challenge.md,
Intro_Outro.md, YouTube.md and placeholder-ready images/ + live/ folders.
Lessons 02-23 are DRAFTS made from the slide bullets - read them once and polish the wording.
"""
import argparse, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / 'lessons'
CHAR = ("CHARACTER: Minty, an original cute cartoon python: friendly mint-green snake with a cream belly, big round "
        "dark-brown eyes with white sparkles, small happy smile, rosy cheeks, smooth rounded body with no fangs, "
        "wearing a tiny yellow-and-blue Python-logo-coloured scarf. Bright 2D vector cartoon, thick clean navy "
        "outlines, flat cheerful colours, kid-friendly, same design in every image.")
STYLE = ("STYLE: bright kids' educational cartoon, soft gradients, high saturation, simple uncluttered background, "
         "16:9 landscape 1920x1080, absolutely no text, no letters, no code on screen, no logos, no copyrighted characters.")


def slug(t):
    return re.sub(r'_+', '_', re.sub(r'[^A-Za-z0-9]+', '_', t)).strip('_')


def parse_slides():
    text = (ROOT / 'slides' / 'slides.source.md').read_text(encoding='utf-8')
    lessons = []
    for block in re.split(r'^# (?=\d\d \|)', text, flags=re.M)[1:]:
        head, body = block.split('\n', 1)
        n, title, code = [x.strip() for x in head.split('|')]
        if n == '00':
            continue
        slides = []
        for s in re.split(r'^## ', body, flags=re.M)[1:]:
            st, sb = s.split('\n', 1) if '\n' in s else (s, '')
            codes = re.findall(r'```\w*\n(.*?)```', sb, re.S)
            nocode = re.sub(r'```.*?```', '', sb, flags=re.S)
            bullets = [b[2:].strip() for b in nocode.splitlines() if b.startswith('- ')]
            tag = next((b[2:].strip() for b in nocode.splitlines() if b.startswith('@ ')), '')
            slides.append(dict(title=st.strip(), bullets=bullets, code=[c.rstrip() for c in codes], tag=tag))
        lessons.append(dict(n=n, title=title, codefile=code, slides=slides))
    return lessons


def notes_for(n):
    t = (ROOT / 'notes' / 'RECORDING-NOTES.md').read_text(encoding='utf-8')
    m = re.search(r'^## ' + n + r' — .*?(?=^## |\Z)', t, re.M | re.S)
    return m.group(0).strip() if m else ''


def sentence(b):
    b = b.strip().rstrip('.')
    b = b[0].upper() + b[1:] if b else b
    return b + ('' if b.endswith(('?', '!')) else '.')


def run_code(src):
    try:
        r = subprocess.run([sys.executable, '-c', src], input='Sam\n12\n5\nyes\n7\n3\n50\n',
                           capture_output=True, text=True, timeout=5)
    except subprocess.TimeoutExpired:
        return '(keeps running - stop it with the red Stop button)'
    out = r.stdout
    if r.returncode:
        out += r.stderr.strip().splitlines()[-1] if r.stderr.strip() else ''
    return out.rstrip()


def build(L, force):
    name = f"{L['n']}_{slug(L['title'])}"
    d = LESSONS / name
    for sub in ('images', 'live', 'voice'):
        (d / sub).mkdir(parents=True, exist_ok=True)
    draft = L['n'] != '01'
    files = {}
    scenes, segs, steps, done_code = [], [], [], ''
    challenge = []
    for s in L['slides']:
        if s['title'].lower().startswith('your turn'):
            challenge = s['bullets']; continue
        if s['bullets'] or not s['code']:
            scenes.append(s); segs.append(('explain', len(scenes)))
        for c in s['code']:
            prev = run_code(done_code) if done_code else ''
            full = run_code(done_code + '\n' + c)
            exp = full[len(prev):].strip('\n') if full.startswith(prev) else full
            is_mistake = 'mistake' in (s['title'] + s['tag']).lower()
            if not is_mistake:
                done_code += '\n' + c
            task = ('Spot the mistake' + ('' if 'mistake' in s['title'].lower() else ': ' + s['title'])) if is_mistake else s['title']
            steps.append(dict(task=task, code=c, out=exp, say=s['bullets'], mistake=is_mistake))
            segs.append(('code', len(steps)))
    # ---- Script.md (AI narration, Kokoro reads it)
    out = [f"# Lesson {L['n']} – {L['title']} | Python for Kids",
           f"**Narrator:** AI voice (Kokoro af_heart) · **Mascot:** Minty the Python · `[pause]` = 2–3 s silence."
           + ("  \n**DRAFT** – generated from the slide bullets. Read it once and make it sound like you." if draft else ''),
           '', '---', '']
    for i, s in enumerate(scenes, 1):
        out += [f"### Scene {i} – {s['title']} (0:00–0:00)", f"**On-screen text:** \"{s['title']}\"", '']
        lines = [sentence(b) for b in s['bullets']] or [f"Let's look at {s['title'].lower()}."]
        if i == 1:
            lines = [f"Hi friends! I'm Minty the Python. Today's lesson is: {L['title']}."] + lines
        out += [' '.join(lines), '']
    files['Script.md'] = '\n'.join(out)
    # ---- Segments.txt
    seg_lines = ['# Order of the video body (intro and outro are added automatically).',
                 '# explain N[-M]  = narrated scenes from Script.md (AI voice + Imagine pictures/clips)',
                 '# code N         = live/live_NN.mp4 (your OBS recording), with a "Let\'s code" card',
                 '# yourturn       = challenge card from Challenge.md   |   quiz = Quiz.md (optional)', '']
    for kind, k in segs:
        seg_lines.append(f'explain {k}' if kind == 'explain' else f"code {k} | {steps[k - 1]['task']}")
    # merge consecutive explains
    merged = []
    for l in seg_lines:
        m = re.match(r'explain (\d+)$', l)
        pm = re.match(r'explain (\d+)(?:-(\d+))?$', merged[-1]) if merged else None
        if m and pm and int(m.group(1)) == int(pm.group(2) or pm.group(1)) + 1:
            merged[-1] = f'explain {pm.group(1)}-{m.group(1)}'
        else:
            merged.append(l)
    merged.append('yourturn')
    files['Segments.txt'] = '\n'.join(merged) + '\n'
    # ---- Visual_Prompts.md
    vp = [f"# Visual Prompts – Lesson {L['n']} {L['title']}", '',
          'Grok Imagine. Attach `Character/Minty_reference.png` every time. 16:9. **No text or code in the images** – '
          'the render script adds titles and captions, and real code only ever appears in your live recording.',
          'Save stills as `images/scene_NN.jpg` (or .png). Scenes marked **🎬 VIDEO** look great as a 4–6 s Imagine '
          'clip: save it as `images/scene_NN.mp4` (it is looped/trimmed to the narration and muted). A still is always fine.', '',
          '**Character block (already inside every prompt):**', '```', CHAR, '```', '']
    for i, s in enumerate(scenes, 1):
        idea = ', '.join(s['bullets'][:3]) or s['title']
        video = i == 1 or i == (len(scenes) + 1) // 2 + (1 if len(scenes) > 2 else 0)
        vp += [f"## Scene {i} – {s['title']}" + ('  🎬 VIDEO' if video else ''), '', '**Image prompt:**', '```', CHAR,
               f"SCENE: Minty the Python in a cosy cartoon kids' coding classroom, acting out the idea \"{s['title']}\" "
               f"({idea}) with simple friendly props and visual metaphors; a laptop screen may glow but shows no readable text.",
               STYLE, '```']
        if video:
            vp += ['**Imagine video prompt (4–6 s, image-to-video from the still):**', '```',
                   'Gentle loop: Minty bobs happily and the props move playfully, slow camera push-in, '
                   'keep the character design exactly the same, no text.', '```']
        vp.append('')
    vp += ['## Thumbnail – thumb_art', '', '```', CHAR,
           f"SCENE: Minty the Python waving excitedly next to a big glowing laptop, theme: {L['title']}; empty space on the left for a title.",
           STYLE, '```', '']
    files['Visual_Prompts.md'] = '\n'.join(vp)
    # ---- Live_Coding.md
    lc = [f"# Live Coding – Lesson {L['n']} {L['title']}", '',
          'You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). '
          'Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … '
          '(any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.', '',
          f"Full lesson program for reference: `code/{L['codefile']}_*.py`.", '']
    for k, st in enumerate(steps, 1):
        lc += [f"## live_{k:02d} – {st['task']}", '',
               ('**This one is the deliberate mistake.** Type it, run it, read the red error out loud, then fix it.' if st['mistake']
                else '**Type this slowly, saying each part out loud:**'), '', '```python', st['code'], '```', '']
        if st['say']:
            lc += ['**What to say:**'] + [f'- {sentence(b)}' for b in st['say']] + ['']
        lc += ['**Expected output** (Run ▶ / F5):', '```', st['out'] or '(nothing printed)', '```', '']
        lc += ['**Kid tip to say:** "Pause the video and type it with me!"', '']
    nb = notes_for(L['n'])
    if nb:
        lc += ['---', '', '## Your original recording notes (unchanged, for reference)', '', nb, '']
    files['Live_Coding.md'] = '\n'.join(lc)
    ch = [sentence(b) for b in challenge if not b.lower().startswith('next')] or ['Change the code and run it again.']
    files['Challenge.md'] = '\n'.join([f"# Your turn – Lesson {L['n']}", '',
                                       'Shown on the "Your turn" card and read by the AI voice. Edit freely.', ''] +
                                      [f'> {c}' for c in ch]) + '\n'
    nxt = next((x for x in ALL if int(x['n']) == int(L['n']) + 1), None)
    files['Intro_Outro.md'] = '\n'.join([
        f"# Intro & Outro – Lesson {L['n']} {L['title']}", '',
        'If `voice/intro.*` / `voice/outro.*` exist (your CapCut recording) they are used; otherwise the AI voice reads '
        'the lines below. Either way the picture is this lesson\'s thumbnail (intro) and the next lesson\'s thumbnail with UP NEXT (outro).', '',
        '## INTRO (≈10 s)', '',
        f"> Hello, Happy Learners! Welcome to Python for Kids. Today we learn {L['title'].lower()}. Open Thonny and code along with me!",
        '', '## OUTRO (≈8 s)', '',
        (f"> Great coding today! Next time: {nxt['title'].lower()}. " if nxt else '> You finished the course, well done! ')
        + 'Ask a grown-up to like, share and subscribe. Happy Learning!', ''])
    files['YouTube.md'] = '\n'.join([
        f"# YouTube – Lesson {L['n']}", '', '## Title',
        f"{L['title']} | Python for Kids Lesson {int(L['n'])} | Code Along in Thonny", '', '## Thumbnail text', f'"{L["title"]}"', '',
        '## Description', '```',
        f"Lesson {int(L['n'])} of Python for Kids: {L['title']}! Minty the Python explains the idea with pictures, then we code it together live in Thonny. Pause, type along, and try the Your Turn challenge at the end.",
        '', '⏱️ Chapters: paste render/<lesson>_chapters.txt here', '',
        '📚 Playlist: Python for Kids – Full Course (ICSE Computer Applications friendly)',
        (f"▶️ NEXT: {nxt['title']}" if nxt else ''), '',
        'For kids 8–14. Works with Thonny (Windows/Mac) or Google Colab (Chromebook). Explanations use an AI voice and AI-made pictures (Grok Imagine); the coding is recorded live.',
        '', '#Python #PythonForKids #CodingForKids #LearnPython #ICSE #HappyLearnersICSE', '```', '',
        '## Tags', f"python for kids, {L['title'].lower()} python, learn python, coding for kids, thonny, icse computer applications, python lesson {int(L['n'])}, happy learners icse", '',
        '## Settings', '- Audience: **Yes, made for kids** (no comments/end screens/cards; the video itself says what is next).',
        '- Altered or synthetic content: No (cartoon mascot + AI voice narration). Category: Education. Language: English (India). Captions: upload the SRT.', ''])
    for fn, body in files.items():
        p = d / fn
        if force or not p.exists():
            p.write_text(body, encoding='utf-8')
    (d / 'live' / 'README.md').write_text('Drop your OBS recordings here: live_01.mp4, live_02.mp4 ... (order = Segments.txt).\n'
                                          'Optional trim.json: {"live_01": {"start": 2.5, "end": 95}}  (seconds; end may be omitted)\n', encoding='utf-8')
    (d / 'images' / 'README.md').write_text('scene_01.jpg ... (or scene_NN.mp4 Imagine clips) + optional thumb_art.jpg. '
                                            'Use tools/import_images.py to rename downloads.\n', encoding='utf-8')
    (d / 'voice' / 'README.md').write_text('Optional: intro.m4a / outro.m4a from CapCut. If missing, the AI voice reads Intro_Outro.md.\n', encoding='utf-8')
    return name, len(scenes), len(steps)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--force', action='store_true'); a = ap.parse_args()
    ALL = parse_slides()
    for L in ALL:
        print(*build(L, a.force))
