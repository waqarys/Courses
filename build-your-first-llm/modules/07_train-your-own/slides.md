---
marp: true
theme: zerotollm
paginate: true
size: 16:9
header: 'Zero to LLM · M07'
footer: 'Waqar Shaikh Builds'
---
<!-- _class: title -->
# Train Your Own Tiny GPT
Module 7 · Zero to LLM

---
# Shift by one
input `hello worl` → target `ello world` — every position is a mini-exam

---
# Loss & perplexity
- cross-entropy = surprise at the right answer
- random start ≈ **ln(V)** (88 chars → 4.48) — sanity check!
- perplexity = e^loss ≈ "choices it's torn between"

---
# Hiking downhill in fog
| part | why |
|---|---|
| AdamW | momentum + per-parameter step + weight decay |
| warmup → cosine | small steps, stride, slow down |
| clip grad 1.0 | no cliff jumps |
| validation | not lost / not memorising |
| checkpoints | survive crashes |

---
# Reading curves
- both ↓ → keep going
- val ↑ while train ↓ → overfitting
- spikes / NaN → LR too high

---
<!-- _class: title -->
# Next: M08 — fine-tuning
