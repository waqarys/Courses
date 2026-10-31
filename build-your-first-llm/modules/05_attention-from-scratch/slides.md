---
marp: true
theme: zerotollm
paginate: true
size: 16:9
header: 'Zero to LLM · M05'
footer: 'Waqar Shaikh Builds'
---
<!-- _class: title -->
# Attention from Scratch
Module 5 · Zero to LLM

---
# "It was too big"
The trophy didn't fit in the suitcase because **it** was too *big* / *small*.
Meaning depends on the other words.

---
# Why recurrent nets struggled
1. **Bottleneck** — one fixed-size summary (forward problem)
2. **Vanishing gradients** — training signal fades backwards (different problem!)
3. **Sequential** — no GPU parallelism

---
# The group chat
| | asks | example |
|---|---|---|
| **Query** | what am I looking for? | "it" wants a big noun |
| **Key** | what do I offer? | "trophy: object, big" |
| **Value** | what I pass on | trophy's meaning |

---
# One formula
$$\text{Attention}(Q,K,V)=\text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$
dot → scale → softmax → weighted mix

---
# Causal mask
Future positions → `-inf` → weight 0.
Lower-triangular attention.

---
# Multi-head
768 = 12 heads × 64 · each head asks a different question
GPT-2 names: `c_attn` (QKV, with bias) → heads → `c_proj`

---
# Cost
Scores are **n × n** → 2× context = 4× attention work
FlashAttention = same maths, smarter memory

---
<!-- _class: title -->
# Next: M06 — assemble the GPT block
