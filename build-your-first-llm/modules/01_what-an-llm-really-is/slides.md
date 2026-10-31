---
marp: true
theme: zerotollm
paginate: true
size: 16:9
header: 'Zero to LLM · M01'
footer: 'Waqar Shaikh Builds'
---

<!-- _class: title -->
# What an LLM Really Is
### The autocomplete that read the internet
Module 1 · Zero to LLM

---
# The ladder
- **AI** — any behaviour we'd call "smart"
- **Machine learning** — learn rules from examples
- **Deep learning** — many stacked layers learn their own features
- **LLM** — deep learning aimed at *one* job: **predict the next token**

> Spam filter: you don't write rules, you show 10 000 labelled emails.

---
# Why "large"?
| Model | Parameters (approx.) |
|---|---|
| Our bigram toy | a few hundred counts |
| GPT-2 small (we rebuild it) | ~124 million |
| Frontier models | reported 100s of billions |

Parameters = adjustable numbers. Training = nudging them.

---
# The one loop
```
text → tokens → numbers → model → scores → probabilities → pick → append ↺
```
1. Chop text into **tokens**
2. Look each token up as a **vector** (M04)
3. **Mix** information between tokens — attention (M05)
4. Score **every** vocabulary entry (~50k for GPT-2)
5. **Pick** one (greedy vs sampling) and repeat

---
# A chat is just the loop
- Your message + history is pasted in front
- No memory between chats unless the app re-sends it
- No fact database — learned patterns

---
# Live: the dumbest LM
Bigram counting in 20 lines → `snippets/01_bigram_counts.py`

---
# Four honest limits
| Limit | Falls out of… |
|---|---|
| Hallucination | the loop *always* emits a fluent token |
| Letter counting / maths | it sees tokens, not letters |
| Knowledge cutoff | frozen training data |
| Context limit | fixed window |

---
<!-- _class: title -->
# Recap
Next-token predictor **+ scale**.
Next: **M02 — the 20 % of Python & PyTorch you need**
