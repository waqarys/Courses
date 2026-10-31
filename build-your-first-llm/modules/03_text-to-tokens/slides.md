---
marp: true
theme: zerotollm
paginate: true
size: 16:9
header: 'Zero to LLM · M03'
footer: 'Waqar Shaikh Builds'
---
<!-- _class: title -->
# From Raw Text to Token IDs
Module 3 · Zero to LLM

---
# The data pipeline
**collect → clean → dedup → split**
- clean: whitespace, Unicode, boilerplate
- dedup: hash each doc, keep first (SHA-1 OK as fingerprint, *not* for security)
- split: train / val (term quiz) / test (final exam)
- tiny data → splits round oddly → **print the sizes**

---
# Three ways to cut text (LEGO bricks)
| | vocab | sequence | unknown words |
|---|---|---|---|
| characters | ~100 | very long | never |
| words | 100k+ | short | often |
| **subwords (BPE)** | ~50k | medium | rare |

---
# BPE in one sentence
Start from characters (bytes); **merge the most frequent adjacent pair**; repeat ~50 000 times.

---
# GPT-2 quirk: the space rides with the word
`"cat"` ≠ `" cat"` — different IDs. Always check what you encode.

---
# Weirdness explained by tokens
- letter counting & spelling
- other languages cost more tokens
- numbers split inconsistently
- APIs bill per token

---
<!-- _class: title -->
# Next: M04 — giving IDs meaning (embeddings)
