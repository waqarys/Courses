"""Regenerate the lesson table at the end of each series OUTLINE.md (python english/make_outline.py)."""
import pathlib
import re

import yaml

HERE = pathlib.Path(__file__).parent
for sdir in sorted(HERE.glob("0*_*")):
    out = sdir / "OUTLINE.md"
    if not out.exists():
        continue
    rows, nshorts = [], 0
    for f in sorted((sdir / "lessons").glob("*/lesson.md")):
        t = f.read_text(encoding="utf-8")
        m = yaml.safe_load(re.match(r"(?s)^---\n(.*?)\n---", t).group(1))
        items = len(re.findall(r"^@ (?:word|q|verb|phrase|fill|fix|[A-Z]) ", t, re.M))
        sh = len(m.get("shorts") or [])
        nshorts += sh
        rows.append(f"| {m['id']} | {m['youtube']['title'].replace('|', '&#124;')} | {items} | {sh} | `{f.parent.name}` |")
    head = out.read_text(encoding="utf-8").split("\n| # |")[0].rstrip()
    head = re.sub(r"\d+ Shorts", f"{nshorts} Shorts", head)
    out.write_text(head + "\n\n| # | YouTube title | Items | Shorts | Folder |\n|---|---|---|---|---|\n" + "\n".join(rows) + "\n",
                   encoding="utf-8")
    print(out, len(rows), "lessons", nshorts, "shorts")
