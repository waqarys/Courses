# M02 — Exercises (with solutions)

**1. Shape prediction.** What is the shape of `torch.randn(8,16,768) @ torch.randn(768, 50257)`?
<details><summary>Solution</summary>`(8, 16, 50257)` — one score per vocabulary entry for every token of every sequence.</details>

**2. Parameter count.** How many parameters in `nn.Linear(768, 3072)`?
<details><summary>Solution</summary>768×3072 + 3072 = 2,362,368.</details>

**3. Fix the bug.** `emb = nn.Embedding(vocab_size=100, dim=8)` fails. Fix it.
<details><summary>Solution</summary>`nn.Embedding(num_embeddings=100, embedding_dim=8)` or positionally `nn.Embedding(100, 8)`.</details>

**4. Autograd by hand.** For loss = (3w − 12)², what is d(loss)/dw at w = 2?
<details><summary>Solution</summary>2·(3w−12)·3 = 2·(−6)·3 = −36. Negative → increase w. Check: run snippet 03 and print `w.grad` before the update.</details>

**5. Decode.** Extend `Tokenizer` so unknown words map to an `<unk>` ID instead of crashing.
<details><summary>Solution</summary>

```python
self.vocab = {"<unk>": 0, **{w: i + 1 for w, i in vocab.items()}}
def encode(self, text):
    return [self.vocab.get(w, 0) for w in text.lower().split()]
```
</details>
