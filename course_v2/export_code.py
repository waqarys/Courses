#!/usr/bin/env python3
"""Copy every program from the lesson scripts into course_v2/code/ so learners can download them.

    python course_v2/export_code.py

Each ```python block under a '## CODE | name.py' or '## ANSWER | name.py' heading becomes
code/<lesson folder>__<name>.py. Blocks are exported exactly as written in the script (for the bug-hunt
lessons that is the version WITH the bugs, which is the point of the exercise).
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "code"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    n = 0
    for f in sorted((HERE / "lessons").glob("*/lesson.md")):
        text = re.sub(r"(?s)<!--.*?-->", "", f.read_text(encoding="utf-8"))
        for m in re.finditer(r"^##\s+(CODE|ANSWER)\s*\|\s*(\S+)\s*\n+```python\n(.*?)\n```", text, re.M | re.S):
            kind, name, code = m.groups()
            stem = name[:-3] if name.endswith(".py") else name
            tag = "_answer" if kind == "ANSWER" else ""
            dst = OUT / f"{f.parent.name}__{stem}{tag}.py"
            dst.write_text(f"# {f.parent.name} - {name}\n{code}\n", encoding="utf-8")
            n += 1
    print(f"{n} programs -> {OUT}")


if __name__ == "__main__":
    main()
