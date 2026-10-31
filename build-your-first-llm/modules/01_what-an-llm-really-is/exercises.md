# M01 — Exercises (with solutions)

**1. Spot the level.** Classify each as AI-but-not-ML, ML, deep learning, or LLM: (a) a 1997 chess engine with hand-tuned rules, (b) a spam filter trained on labelled email, (c) an image classifier with 50 layers, (d) a chatbot that writes code.
<details><summary>Solution</summary>(a) AI, not ML (rules written by people) · (b) ML · (c) deep learning · (d) LLM (deep learning trained for next-token prediction).</details>

**2. Trigram upgrade.** Change snippet 01 so it predicts from the *last two* words.
<details><summary>Solution</summary>

```python
follows = defaultdict(Counter)
for a, b, c in zip(words, words[1:], words[2:]):
    follows[(a, b)][c] += 1
print(follows[("the", "cat")])   # Counter({'sat': 1, 'ate': 1, '.': 1})
```
More context → sharper predictions, but many pairs are never seen. That sparsity is why we need learned vectors instead of counting tables.</details>

**3. Why does greedy loop?** Explain in one sentence.
<details><summary>Solution</summary>Greedy always picks the same successor for a given word, so once a word repeats, the whole sequence after it repeats.</details>

**4. Token vs letter.** Why might an LLM miscount the r's in "strawberry"?
<details><summary>Solution</summary>It receives a few token IDs (e.g. "str", "aw", "berry"), not 10 letters, so letter-level facts must be memorised rather than seen.</details>

**5. Chat memory.** A chatbot "remembers" your name from earlier in the conversation. Where is that memory stored?
<details><summary>Solution</summary>In the prompt: the app re-sends the conversation history each turn. The model weights don't change.</details>
