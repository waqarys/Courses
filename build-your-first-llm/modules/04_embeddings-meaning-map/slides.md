---
marp: true
theme: zerotollm
paginate: true
size: 16:9
header: 'Zero to LLM · M04'
footer: 'Waqar Shaikh Builds'
---
<!-- _class: title -->
# Embeddings: a Map of Meaning
Module 4 · Zero to LLM

---
# IDs are seat numbers
Seat 3290 isn't "more dog" than seat 3291.
We need **coordinates**.

---
# One-hot vs dense
| one-hot | dense embedding |
|---|---|
| 50 257 numbers, one `1` | 768 learned numbers |
| all words equally far | similar words are neighbours |

"A word is known by the company it keeps."

---
# The table
`vocab × d_model` matrix → lookup = take a row
GPT-2: 50 257 × 768 ≈ **38.6 M** parameters

---
# Cosine similarity = angle between arrows
⚠ `"king"` (no space) ≠ `" king"` — embed the token the model really sees

---
# Order matters: positions
| method | used by |
|---|---|
| learned table | GPT-2, BERT |
| fixed sinusoids | 2017 Transformer |
| rotary (RoPE) | Llama, Mistral, Qwen… |

`x = token_emb + pos_emb`

---
<!-- _class: title -->
# Next: M05 — Attention
