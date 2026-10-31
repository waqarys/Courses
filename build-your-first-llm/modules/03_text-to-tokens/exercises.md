# M03 — Exercises (with solutions)

**1. Split sanity.** With 3 documents and `int(0.8n)`, `int(0.1n)`, what sizes do you get?
<details><summary>Solution</summary>train 2, val 0, test 1. `int()` rounds down — always print sizes, and for tiny data split by tokens rather than documents.</details>

**2. Round trip.** Why must `decode(encode(x)) == x` for a tokenizer used in training? Which of our tokenizers fails it?
<details><summary>Solution</summary>Otherwise generated IDs can't be turned back into the exact text. The word tokenizer fails (case, punctuation, unknown words); char and byte-level BPE pass.</details>

**3. BPE by hand.** Corpus: `aaab aab`. What is the first merge?
<details><summary>Solution</summary>Pairs: (a,a)×3, (a,b)×2, (b,_)×2 → merge `aa`.</details>

**4. Token budget.** Use snippet 04 to count tokens for the same sentence in English and in Hindi (e.g. "मुझे चाय पसंद है"). What do you notice?
<details><summary>Solution</summary>The Hindi text needs many more GPT-2 tokens per word (multi-byte UTF-8 + English-heavy merges) — higher cost and shorter effective context.</details>

**5. Space matters.** Encode "dog" and " dog" with tiktoken GPT-2. Are the IDs equal?
<details><summary>Solution</summary>No: `dog` = 9703, ` dog` = 3290. Mid-sentence words almost always carry the leading space.</details>
