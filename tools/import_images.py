"""import_images.py - copy your newest Imagine downloads into a video's images/ folder with the right names.

Usage (from the repo root or from tools/):
    python tools/import_images.py "%USERPROFILE%\\Downloads" 01          # newest N images/clips -> lessons/01_*/images/scene_01..N
    (Imagine video clips .mp4 are copied as scene_NN.mp4 and used instead of a still.)
    python tools/import_images.py ~/Downloads 02_Plants --thumb            # newest N+1: the LAST one is thumb_art
    python tools/import_images.py D:\\imgs 02 --count 6 --start 5           # only scenes 05..10
    add --yes to skip the confirmation question, --move to move instead of copy

How it works: N = number of scenes in <video>/Script.md. It takes the N newest image files
(png/jpg/jpeg/webp, any case) in the folder, sorts them OLDEST -> NEWEST (the order you made them),
shows the mapping, asks y/n, then copies them to <video>/images/scene_01.png ... (converted to PNG,
or kept as .jpg if --keep-format). So: generate scene 1 first, then scene 2 ..., download each as you go.
"""
import argparse, shutil, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import prep_video as pv          # noqa: E402
import render_video as rv        # noqa: E402

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('downloads'); ap.add_argument('video', help="e.g. 02_Plants or 02")
    ap.add_argument('--count', type=int, help='how many scene images (default: all scenes from --start)')
    ap.add_argument('--start', type=int, default=1, help='first scene number (default 1)')
    ap.add_argument('--thumb', action='store_true', help='one extra image (the newest) becomes thumb_art')
    ap.add_argument('--yes', action='store_true'); ap.add_argument('--move', action='store_true')
    ap.add_argument('--keep-format', action='store_true', help='keep original extension instead of PNG')
    a = ap.parse_args()
    folder = rv.resolve_lesson(a.video)
    scenes = pv.parse_script(folder / 'Script.md')
    src = Path(a.downloads).expanduser()
    if not src.is_dir():
        sys.exit(f'Downloads folder not found: {src.resolve()}')
    n = a.count or (len(scenes) - a.start + 1)
    if n < 1 or a.start + n - 1 > len(scenes):
        sys.exit(f'{folder.name} has {len(scenes)} scenes; --start {a.start} --count {n} does not fit.')
    files = [p for p in src.iterdir() if p.is_file() and p.suffix.lower() in rv.IMG_EXT + rv.VID_EXT]
    need = n + (1 if a.thumb else 0)
    if len(files) < need:
        sys.exit(f'Need {need} images but found only {len(files)} in {src.resolve()}')
    pick = sorted(sorted(files, key=lambda p: p.stat().st_mtime)[-need:], key=lambda p: p.stat().st_mtime)
    dst = folder / 'images'; dst.mkdir(exist_ok=True)
    plan = []
    for k, p in enumerate(pick):
        i = a.start + k
        stem = 'thumb_art' if (a.thumb and k == need - 1) else f'scene_{i:02d}'
        ext = p.suffix.lower() if (a.keep_format or p.suffix.lower() in rv.VID_EXT) else '.png'
        label = 'thumbnail art' if stem == 'thumb_art' else scenes[i - 1]['name']
        plan.append((p, dst / (stem + ext), label))
    print(f'Video: {folder.name}  ({len(scenes)} scenes)\nFrom:  {src.resolve()}\nTo:    {dst.resolve()}\n')
    for p, d, label in plan:
        t = time.strftime('%d %b %H:%M:%S', time.localtime(p.stat().st_mtime))
        warn = '   (will REPLACE existing)' if any(dst.glob(d.stem + '.*')) else ''
        print(f'  {t}  {p.name[:45]:45s} -> {d.name:16s} {label}{warn}')
    if not a.yes and input('\nCopy these? [y/N] ').strip().lower() != 'y':
        sys.exit('Cancelled, nothing copied.')
    from PIL import Image
    for p, d, _ in plan:
        for old in dst.glob(d.stem + '.*'):
            old.unlink()
        if d.suffix == '.png' and p.suffix.lower() != '.png':
            Image.open(p).convert('RGB').save(d)
        else:
            shutil.copy2(p, d)
        if a.move:
            p.unlink()
    print(f'Done: {len(plan)} images in {dst.resolve()}\nNext: python tools/render_video.py {folder.name[:2]} --quick')

if __name__ == '__main__':
    main()
