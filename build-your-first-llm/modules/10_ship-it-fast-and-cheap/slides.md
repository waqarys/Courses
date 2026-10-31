---
marp: true
theme: zerotollm
paginate: true
size: 16:9
header: 'Zero to LLM · M10'
footer: 'Waqar Shaikh Builds'
---
<!-- _class: title -->
# Ship It: Fast, Small, Online
Module 10 · Zero to LLM

---
# The kitchen
| trick | kitchen | effect |
|---|---|---|
| KV cache | prep ahead | reuse past keys/values |
| quantisation | smaller pans | 4–8× less memory |
| batching | batch orders | more users per GPU |

---
# Quantisation formats
int8 dynamic (CPU) · GPTQ / AWQ (4-bit GPU) · **GGUF** (llama.cpp, Ollama)
Always re-measure quality.

---
# Where to deploy
| option | cost model | control | ops |
|---|---|---|---|
| local / Ollama | hardware | full | you |
| cloud GPU container | per second | high | you |
| managed API (e.g. Grok) | per token | low | none |
| edge / browser | free | tiny models | low |

---
# Production checklist
rate limits · timeouts · responsible logging · filtering · cost alerts · **eval set before every change**

---
<!-- _class: title -->
# Next: M11 — what's next + capstone
