# M03 — Live-coding plan
Install once: `pip install tiktoken` (in the course venv).

| Step | Snippet | Type live | Point at |
|---|---|---|---|
| 1 | 01_clean_dedup_split.py | the `if h not in seen` line | printed split sizes (4 docs → 3/0/1) |
| 2 | 02_char_word_tokenizers.py | the `assert` round-trip | char vocab vs sequence length; `<unk>` = 0 |
| 3 | 03_bpe_from_scratch.py | the `most_common(1)` line | merges printing in order |
| 4 | change `range(8)` → `range(15)`, rerun | — | whole words like `the_` appear |
| 5 | 04_tiktoken_compare.py | — | `cat` vs ` cat` IDs; emoji token counts |
