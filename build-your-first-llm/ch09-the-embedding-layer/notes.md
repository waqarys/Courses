# Chapter 9 — The Embedding Layer (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch09.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch09.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
Token IDs are arbitrary labels. The embedding layer gives each token a learned vector and each position a learned vector, and their sum is what the transformer actually reads.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Embedding | A learned dense vector for a token |
| Lookup table | A matrix where row *i* is token *i*'s vector |
| `wte` / `wpe` | GPT-2's token table (50,257×768) / position table (1,024×768) |
| One-hot | A vocab-length vector with a single 1. A lookup equals one-hot × W |
| Cosine similarity | Similarity of direction: 1 = same, 0 = unrelated |
| Weight tying | Reusing `wte` as the output projection |

## 1. Why not raw IDs
- IDs come from BPE merge order. Numeric closeness means nothing (` cat` 3797, ` dog` 3290, ` kitten` 42143).
- One-hot vectors are huge and make all pairs equidistant. Dense vectors are small and can encode similarity.
- I checked in code that `one_hot @ W == W[id]`.

## 2. Token embeddings
- `W[token_ids]` maps shape (batch, seq) to (batch, seq, d).
- `nn.Embedding` is the same table, but trainable. GPT-2 initialises it with Normal(0, 0.02).
- 768 = 2⁸×3 = 12 heads × 64. `wte` holds 38.6M of GPT-2 small's 124.4M parameters.

## 3. Positions
- Attention is permutation-equivariant. I tested this: without positions, shuffling the input just shuffles the output. With position embeddings added, it doesn't.
- Options:
  - Learned absolute positions (GPT-2, BERT).
  - Sinusoidal positions (the 2017 Transformer).
  - RoPE (most current open models).
- `PositionalEmbedding` looks up `arange(seq_len)` on the input's device and broadcasts it over the batch.
- Past `max_seq_len`, `nn.Embedding` raises `IndexError: index out of range in self`. Learned positions can't extrapolate.

## 4. GPT2Embeddings
- `token_embed(ids) + pos_embed(positions)`. Addition keeps 768 dims, while concatenation would need 1,536.
- Pipeline: "The cat sat on the mat" → `[464, 3797, 3332, 319, 262, 2603]` → (1, 6, 768).
- Common mistakes:
  - Looking up token IDs in the position table.
  - Creating positions on the wrong device.
  - Skipping the length check.

## 5. Real GPT-2 embeddings (my experiments)
- Trained std: `wte` 0.144 and `wpe` 0.123. Both started at 0.02.
- **Use the space-prefixed token.** `encode("king")` gives a word-piece whose neighbours are 'ked', 'KING', 'kers'.
- Neighbours with the space-prefixed tokens:
  - ` king`: kings, King, queen, prince, monarch.
  - ` doctor`: doctors, physician.
  - ` fast`: faster, quick.
- Analogies:
  - ` king − man + woman` → ` queen` (0.709).
  - ` Paris − France + Germany` → ` Berlin` (0.666).
- Cosine similarity with ` cat`: ` kitten` 0.501, ` dog` 0.454, ` car` 0.381.
- `wpe`: nearby positions are similar and similarity fades with distance. The curves are smooth and learned purely from data.

## 6. Practical details
- Normal(0, 0.02) is a well-tested default, not a law.
- Create positions on `token_ids.device`. If the model and the inputs sit on different devices you get a RuntimeError.
- Weight tying saves 38.6M parameters in GPT-2 small (used in Ch 11).
- Embeddings are static. Attention (Ch 10) makes them contextual ("river bank" vs "savings bank").

## 7. Exercises (my answers)
1. `randn(10,8)` gives (10,8). IDs `[2,5,7]` have shape (3,), and the lookup gives (3,8). Notebook cell 32 is a `???` template and raises a SyntaxError until you fill it in.
2. TokenEmbedding: use `nn.Embedding` + `normal_(0, 0.02)` and assert `ids.dim()==2`.
3. Position 0's vector is identical whatever token sits there, because the lookup uses the index.
4. Pad the length-5 sequence to 8. The output is (2, 8, d). Mask the padding later.
5. Use ' Python', ' doctor', ' fast' (see above).
6. Move the IDs with `.to(next(model.parameters()).device)`.
7. Truncate with `ids[:, :max_seq_len]`.
8. JSONL record → `torch.tensor([ids])` → (1, n) → (1, n, d).

## 8. Book checks (errata)
- Example IDs:
  - dog is 3290, not 4273. 4273 is ' pet'.
  - kitten is 42143, not 28387. 28387 is ' WC'.
  - mat is 2603, not 21547.
  - `[314, 588, 4695, 345]` decodes to " I like animals you", not "I will help you".
- The similarity and analogy outputs printed in the book don't come from the code shown. The fix is a leading space.
- "Modern LLMs like GPT-2 prefer learned positions": current open models mostly use RoPE.

## 9. Review questions
1. Why do raw IDs fail?
2. Vocab 10k, d 512, batch 4×20: what are the shapes? (Table 10,000×512; output 4×20×512.)
3. Give two sentences with the same words but different meanings.
4. Why add instead of concatenate?
5. Why std 0.02?
6. What happens with a length-1,500 input when `max_seq_len=1024`?
7. Why did 'king' return 'ked'?

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
