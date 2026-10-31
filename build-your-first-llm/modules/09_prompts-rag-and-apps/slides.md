---
marp: true
theme: zerotollm
paginate: true
size: 16:9
header: 'Zero to LLM · M09'
footer: 'Waqar Shaikh Builds'
---
<!-- _class: title -->
# Prompts, Sampling & RAG
Module 9 · Zero to LLM

---
# The knobs
| knob | effect | use for |
|---|---|---|
| temperature ↓ | plain, safe | extraction, code |
| temperature ↑ | bold, risky | brainstorming |
| top-k | keep k best | trim nonsense |
| top-p | keep 90 % mass | adaptive trimming |

---
# Prompt patterns
1. role + task + format + constraints
2. few-shot examples
3. reason, then `Final answer:` line
4. delimiters around user text (injection defence)
5. JSON + validate in code

---
# RAG = brief the intern with the right pages
chunk → embed → retrieve nearest → prompt "use only this context"

---
<!-- _class: title -->
# Next: M10 — ship it
