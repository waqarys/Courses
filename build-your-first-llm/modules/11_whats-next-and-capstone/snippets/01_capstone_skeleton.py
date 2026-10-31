# M11 · snippet 01 — scaffold the "Ask My Notes" capstone
import csv, pathlib

root = pathlib.Path("ask_my_notes")
for d in ("data/raw", "data/chunks", "src", "eval"):
    (root / d).mkdir(parents=True, exist_ok=True)
files = {
    "src/chunk.py": "# M03: clean + chunk files from data/raw into data/chunks\n",
    "src/retrieve.py": "# M09: embed chunks, retrieve top-k for a question\n",
    "src/tone_lora.py": "# M08: LoRA tone adapter trained on eval-style Q&A pairs\n",
    "src/serve.py": "# M10: load once, POST /ask -> answer + sources\n",
    "README.md": "# Ask My Notes\nCapstone for Zero to LLM (Waqar Shaikh Builds).\n",
}
for name, body in files.items():
    p = root / name
    if not p.exists():
        p.write_text(body, encoding="utf-8")
with open(root / "eval/questions.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["id", "question", "expected_answer", "score_before", "score_after"])
    for i in range(1, 16):
        w.writerow([i, "", "", "", ""])
print("\n".join(sorted(str(p) for p in root.rglob("*"))))
