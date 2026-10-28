# Chapter 11 — Building the Transformer (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch11.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch11.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
This chapter assembles the Ch 9 embeddings and Ch 10 blocks into a full GPT, checks the wiring, and loads real GPT-2 weights. My CPU run exposed a silent loading bug, which is the most useful lesson here.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| LM head | Linear map from d_model to vocab_size that produces logits |
| Logits | Raw scores before softmax |
| Weight tying | The LM head reuses the token-embedding matrix |
| `nn.ModuleList` | A list that registers its submodules' parameters |
| GPTConfig | A dataclass holding all hyperparameters, with validation in `__post_init__` |
| Greedy decoding | Always take the argmax |

## 1. Architecture
- token + position embeddings → dropout → N × block (pre-norm: LN→attn→+, LN→FFN→+) → `ln_f` → `lm_head`.
- The shape stays (B, T, d) until the head, which produces (B, T, vocab).
- Every position predicts its next token in training. Generation uses only the last position.

## 2. Config and ModuleList
- The defaults match GPT-2 small (12 layers, 12 heads, 768, 3072, 1024, 50257).
- A plain list hides the blocks from `parameters()`, `.to()` and `state_dict()`, so the blocks never train.

## 3. Weight tying
- `self.lm_head.weight = self.token_embed.weight` makes both modules share the same tensor. This saves 38,597,376 parameters (≈31%).
- `parameters()` counts the shared tensor once.
- `state_dict()` **does** list `lm_head.weight` (shared storage, saved once).
- Tie after creating both layers, and re-tie if you replace tensors.

## 4. Sanity checks (all passed on my CPU)
1. Shape: (2,16) → (2,16,50257).
2. Parameter count: 124,402,944 with the notebook code.
3. Causal mask: changing token 4 leaves logits 0–2 unchanged.
4. Tying: `is` identity, and an edit propagates.
5. Gradient flow: every parameter gets `.grad`.

Parameter breakdown for HF GPT-2 small:

| Component | Parameters | Share |
|---|---|---|
| wte | 38,597,376 | 31.0% |
| wpe | 786,432 | 0.6% |
| attention ×12 | 28,348,416 | 22.8% |
| FFN ×12 | 56,669,184 | 45.5% |
| LayerNorms | 38,400 | — |
| **Total** | **124,439,808** | |

## 5. Random forward pass
- Top predictions are junk (' RC', ' Abel', …), each with p ≈ 1e-4. A random model is near uniform, so the expected initial loss is ln(50257) ≈ 10.8.

## 6. Loading GPT-2 (the bug)
- The mapping is wte/wpe/h.i.ln_1/... GPT-2's Conv1D weights are (in, out), so they must be transposed for `nn.Linear`.
- **The notebook's output is degenerate:** "The quick brown foxeseseses…", "…will be used to to to…", "France is is is…".
- Diagnosis (my experiment), comparing logits with HF GPT-2 on the same input:
  - max |Δ| = **58** for the notebook code.
  - After adding the attention biases (`c_attn.bias`, `c_proj.bias`, which the notebook's `bias=False` layers drop): **0.075**.
  - After also using `F.gelu(..., approximate="tanh")`: **6e-5**.
- After the fix, the output is fluent: "The quick brown foxes are a great way to get a little bit of a kick out of your dog." The parameter count becomes 124,439,808.
- Lesson: sanity checks test wiring. **Compare against a reference** to test correctness.
- Speed: 30 greedy tokens took 10.1 s on CPU (no KV cache).

## 7. Practical details
- `train()` turns dropout on and `eval()` turns it off. Use `@torch.no_grad()` for generation, and keep the model and inputs on the same device.
- Ch 12 preview: no weight decay on biases, LayerNorms or embeddings.

## 8. Exercises (my answers)
1. Tiny/checkpoint model (vocab 500, seq 16, d 64, h 2, L 2, ff 256): **132,608** parameters (133,120 with attention biases). The book says ~150,000.
2. Breakdown for the notebook code: wte 38,597,376; wpe 786,432; blocks 85,017,600 (+36,864 attention biases in real GPT-2); ln_f 1,536; lm_head 0 (tied).
3. The causal mask is a lower-triangular heatmap at every length.
4. Prompts with the fixed model:
   - "Once upon a time, the world was a place of great beauty and great danger…"
   - "The capital of France is the capital of the French Republic…"
   - "def fibonacci(n):" gives `return n` loops.
5. Temperature only matters with sampling (`multinomial`).
6. Top-k: renormalise the top 5 and sample. The output is more varied than greedy.

## 9. Book checks (errata)
- MiniGPT attention drops biases, so loaded GPT-2 degenerates, while the book shows fluent text. Fix: biases + tanh GELU.
- The printed parameter count (124,439,808) is HF's. This code gives 124,402,944. The book's formula evaluates to 124,356,864, not 124,354,560.
- `lm_head.weight` does appear in `state_dict()`.
- The checkpoint model is ≈132.6k parameters, not ~150k.

## 10. Review questions
1. What four pieces turn a block into a model?
2. Why use a dataclass config?
3. What output shape does the LM head give?
4. How many parameters does tying save?
5. Why must positions 0–2 be unchanged in the causal test?
6. Why transpose when loading?
7. Why can all five checks pass while generation is garbage?

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
