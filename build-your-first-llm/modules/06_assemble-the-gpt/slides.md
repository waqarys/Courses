---
marp: true
theme: zerotollm
paginate: true
size: 16:9
header: 'Zero to LLM · M06'
footer: 'Waqar Shaikh Builds'
---
<!-- _class: title -->
# Assemble the GPT
Module 6 · Zero to LLM

---
# A block = discuss, then think
```
x ─┬─ LayerNorm ─ Attention ─┐
   └──────────────(+)◄────────┘   discuss
x ─┬─ LayerNorm ─ MLP (768→3072→768, GELU) ─┐
   └──────────────(+)◄─────────────────────┘ think alone
```
Residual = notes in the margin · Pre-norm = calm breath first

---
# LayerNorm check
`[102.5, 98.3, 105.7, 95.2]` → `≈[0.52, −0.53, 1.32, −1.31]` — **sums to 0**
GELU (tanh approx) in GPT-2 · SwiGLU in Llama-style models

---
# The whole model
token emb + pos emb → 12 × Block → LayerNorm → lm_head (tied to token emb)
**124,439,808** parameters (= Hugging Face GPT-2)

---
# Verify against a reference
- HF stores 4 linear weights transposed (Conv1D)
- max logit diff ≈ 1e-4 → it *is* GPT-2
- `bias=False` on attention → biases silently skipped → "foxeseseses…"

---
# Same code, bigger numbers
| model | layers | d_model | heads | params |
|---|---|---|---|---|
| small | 12 | 768 | 12 | 124 M |
| medium | 24 | 1024 | 16 | 355 M |
| large | 36 | 1280 | 20 | 774 M |
| XL | 48 | 1600 | 25 | 1.5 B |

---
<!-- _class: title -->
# Next: M07 — train our own
