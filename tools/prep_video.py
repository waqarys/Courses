#!/usr/bin/env python3
"""prep_video.py - parsers for Script.md / Visual_Prompts.md / Quiz.md / YouTube.md (shared with the Science Olympiad pipeline).

Usage (Windows / macOS / Linux, Python 3.8+, standard library only):
    python tools/prep_video.py 02_Plants
    python tools/prep_video.py 02_Plants 03_Animals          # several folders
    python tools/prep_video.py --all                          # every NN_* folder
    python tools/prep_video.py 02_Plants --tts                # OPTIONAL offline AI voice WAVs

Writes <folder>/build/:
    voiceover_by_scene.txt  clean narration, one numbered block per scene (cues stripped)
    prompts_batch.txt       every scene image prompt (+motion) and the thumbnail prompt
    onscreen_text.txt       on-screen text per scene, with timings
    quiz_cards.txt          question / options / answer / explanation for each quiz card
    upload_metadata.txt     title, description, tags, playlists, thumbnail text, end screen
    shot_list.csv           scene, time, narration snippet, prompt, on-screen text, SFX
    audio/SNN.wav           only with --tts (needs `pip install pyttsx3`; uses the Windows
                            built-in SAPI voices offline). Skipped with a message if missing.
"""
import argparse, csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCENE_RE = re.compile(r'^### (Scene (\S+)) – (.+?) \((\d+:\d+)–(\d+:\d+)\)\s*$')


def read(p):
    return Path(p).read_text(encoding='utf-8')


def clean_line(line):
    line = re.sub(r'\[pause[^\]]*\]', '(pause)', line, flags=re.I)
    line = re.sub(r'\[SFX:[^\]]*\]', '', line)
    line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
    line = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'\1', line)
    return line.strip()


def parse_script(path):
    scenes, cur = [], None
    for raw in read(path).splitlines():
        m = SCENE_RE.match(raw)
        if m:
            cur = dict(id=m.group(2), name=m.group(3), start=m.group(4), end=m.group(5),
                       onscreen='', sfx=[], lines=[])
            scenes.append(cur)
            continue
        if cur is None or raw.startswith('---') or raw.startswith('#'):
            continue
        s = raw.strip()
        if not s:
            continue
        om = re.match(r'\*\*On-screen text:\*\*\s*"(.*)"', s)
        if om:
            cur['onscreen'] = om.group(1)
            continue
        cur['sfx'] += re.findall(r'\[SFX:\s*([^\]]+)\]', s)
        if re.fullmatch(r'\*\(.*\)\*', s):           # editor directions like *(Read the quiz...)*
            cur['lines'].append('[EDIT NOTE: ' + s.strip('*()') + ']')
            continue
        c = clean_line(s)
        if c:
            cur['lines'].append(c)
    return scenes


def parse_prompts(path):
    text = read(path)
    out, thumb = {}, ''
    for sec in re.split(r'\n## ', text)[1:]:
        head = sec.split('\n', 1)[0]
        blocks = re.findall(r'```\n(.*?)\n```', sec, flags=re.S)
        mo = re.search(r'\*\*Image-to-video motion[^*]*\*\*\s*(.+)', sec)
        if head.startswith('Thumbnail'):
            ov = re.search(r'\*\*Text overlay[^*]*\*\*\s*(.+)', sec)
            thumb = (blocks[0] if blocks else '') + ('\nTEXT OVERLAY: ' + ov.group(1) if ov else '')
            continue
        m = re.match(r'Scene (\S+)', head)
        if m and blocks:
            out[m.group(1)] = dict(prompt=blocks[0], motion=mo.group(1).strip() if mo else '')
    return out, thumb


def parse_quiz(path):
    qs = []
    for sec in re.split(r'\n### ', read(path))[1:]:
        if not re.match(r'Q\d+\.', sec):
            continue
        q = sec.split('\n', 1)[0]
        opts = re.findall(r'^- ([A-D])\. (.+)$', sec, flags=re.M)
        am = re.search(r'\*\*Answer: (.+?)\*\*\s*[–-]\s*(.+)', sec)
        qs.append(dict(q=q, opts=opts, ans=am.group(1) if am else '?', why=am.group(2).strip() if am else ''))
    return qs


def parse_youtube(path):
    t = read(path)
    def sect(name):
        m = re.search(r'^## ' + re.escape(name) + r'[^\n]*\n(.*?)(?=^## |\Z)', t, flags=re.M | re.S)
        return m.group(1).strip() if m else ''
    desc = re.search(r'```\n(.*?)\n```', sect('Description'), flags=re.S)
    return dict(title=sect('Title'), description=desc.group(1) if desc else '', tags=sect('Tags'),
                playlist=sect('Playlist'), thumb=sect('Thumbnail text'), settings=sect('Settings'),
                endscreen=sect('Up next') or sect('End screen'), cards=sect('Made for Kids limits') or sect('Cards'))


def tts(scenes, outdir):
    try:
        import pyttsx3
    except ImportError:
        print('  --tts skipped: pyttsx3 not installed (pip install pyttsx3).')
        return
    eng = pyttsx3.init()
    eng.setProperty('rate', 150)
    outdir.mkdir(exist_ok=True)
    for i, s in enumerate(scenes, 1):
        txt = ' '.join(l for l in s['lines'] if not l.startswith('[EDIT')).replace('(pause)', '... ... ...')
        eng.save_to_file(txt, str(outdir / f'S{i:02d}.wav'))
    eng.runAndWait()
    print(f'  wrote {len(scenes)} WAV files to {outdir}')


def build(folder, want_tts=False):
    import render_video as rv            # same folder; shared folder + image name rules
    folder = rv.resolve_folder(folder)
    need = ['Script.md', 'Visual_Prompts.md', 'Quiz.md', 'YouTube.md']
    missing = [n for n in need if not (folder / n).exists()]
    if missing:
        print(f'{folder.name}: missing {missing}, skipped'); return False
    scenes = parse_script(folder / 'Script.md')
    prompts, thumb = parse_prompts(folder / 'Visual_Prompts.md')
    quiz = parse_quiz(folder / 'Quiz.md')
    yt = parse_youtube(folder / 'YouTube.md')
    b = folder / 'build'; b.mkdir(exist_ok=True)
    found, _ = rv.find_images(folder, None)
    if len(found) < len(scenes):
        rv.report_missing(folder, folder / 'images', scenes, found)
    else:
        print(f'{folder.name}: all {len(scenes)} scene images found in {(folder / "images").resolve()}')

    vo = [f'VOICEOVER – {yt["title"]}', 'Read slowly and smile. (pause) = stay silent 2–3 seconds.', '']
    for i, s in enumerate(scenes, 1):
        vo += [f'=== {i:02d}. Scene {s["id"]} – {s["name"]} ({s["start"]}–{s["end"]}) ===', *s['lines'], '']
    (b / 'voiceover_by_scene.txt').write_text('\n'.join(vo), encoding='utf-8')

    pb = [f'PROMPTS – {yt["title"]}', 'Attach Character/Ojas_the_Owl_Character_Sheet.jpg as reference for EVERY prompt.', '']
    for i, s in enumerate(scenes, 1):
        p = prompts.get(s['id'], {})
        pb += [f'----- {i:02d}. Scene {s["id"]} – {s["name"]} -----', p.get('prompt', '(no prompt found)'),
               f'MOTION: {p.get("motion", "")}', '']
    pb += ['----- THUMBNAIL (1280x720) -----', thumb, '']
    (b / 'prompts_batch.txt').write_text('\n'.join(pb), encoding='utf-8')

    ot = [f'{i:02d}  {s["start"]}–{s["end"]}  {s["onscreen"]}' for i, s in enumerate(scenes, 1)]
    (b / 'onscreen_text.txt').write_text('\n'.join(ot) + '\n', encoding='utf-8')

    qc = [f'QUIZ CARDS – {yt["title"]}', '']
    for i, q in enumerate(quiz, 1):
        qc += [f'CARD {i}', f'Q: {q["q"].split(". ", 1)[-1]}', *[f'   {l}) {o}' for l, o in q['opts']],
               '   [5-second countdown]', f'ANSWER: {q["ans"]}', f'WHY: {q["why"]}', '']
    (b / 'quiz_cards.txt').write_text('\n'.join(qc), encoding='utf-8')

    um = ['TITLE', yt['title'], '', 'DESCRIPTION', yt['description'], '', 'TAGS', yt['tags'], '',
          'PLAYLISTS', yt['playlist'], '', 'THUMBNAIL TEXT', yt['thumb'], '', 'SETTINGS', yt['settings'], '',
          'UP NEXT', yt['endscreen'], '', 'MADE FOR KIDS LIMITS', yt['cards'], '']
    (b / 'upload_metadata.txt').write_text('\n'.join(um), encoding='utf-8')

    with open(b / 'shot_list.csv', 'w', newline='', encoding='utf-8-sig') as f:   # utf-8-sig opens cleanly in Excel
        w = csv.writer(f)
        w.writerow(['#', 'scene', 'start', 'end', 'narration_snippet', 'on_screen_text', 'sfx', 'motion', 'prompt'])
        for i, s in enumerate(scenes, 1):
            narr = ' '.join(l for l in s['lines'] if not l.startswith('[EDIT'))
            p = prompts.get(s['id'], {})
            w.writerow([i, f'Scene {s["id"]} – {s["name"]}', s['start'], s['end'],
                        (narr[:140] + '…') if len(narr) > 140 else narr, s['onscreen'], '; '.join(s['sfx']),
                        p.get('motion', ''), p.get('prompt', '').split('SCENE: ', 1)[-1].split('\n')[0]])

    words = sum(len(' '.join(s['lines']).split()) for s in scenes)
    warn = '' if len(prompts) == len(scenes) else f'  WARNING: {len(scenes)} scenes but {len(prompts)} prompts'
    print(f'{folder.name}: {len(scenes)} scenes, ~{words} spoken words (~{words/130:.1f} min at 130 wpm), '
          f'{len(quiz)} quiz cards -> {b}{warn}')
    if want_tts:
        tts(scenes, b / 'audio')
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('folders', nargs='*', help='video folder(s), e.g. 02_Plants')
    ap.add_argument('--all', action='store_true', help='process every NN_* folder')
    ap.add_argument('--tts', action='store_true', help='OPTIONAL: offline AI voice WAV per scene (pyttsx3)')
    a = ap.parse_args()
    folders = sorted(p.name for p in ROOT.iterdir() if p.is_dir() and re.match(r'\d\d_', p.name)) if a.all else a.folders
    if not folders:
        ap.print_help(); sys.exit(1)
    ok = all([build(f, a.tts) for f in folders])
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
