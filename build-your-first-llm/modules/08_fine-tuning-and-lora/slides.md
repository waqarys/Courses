---
marp: true
theme: zerotollm
paginate: true
size: 16:9
header: 'Zero to LLM · M08'
footer: 'Waqar Shaikh Builds'
---
<!-- _class: title -->
# Fine-Tuning & LoRA
Module 8 · Zero to LLM

---
# Three ways to adapt
| | trains | cost | risk |
|---|---|---|---|
| prompting | nothing | ~0 | low |
| **LoRA** | <1 % | low | low |
| full fine-tune | 100 % | high | forgetting |

---
# Instruction format
```
### Instruction: Explain attention in one line with an analogy.
### Response: Attention is a group chat where…<eos>
```
Loss **only** on the response (labels = −100 elsewhere)

---
# LoRA = sticky notes
`y = W x + (α/r) · B A x` · W frozen · A: d×r · B: r×d, **starts at 0**
768×2304 ≈ 1.77 M → r = 8 adds 24.6 k per layer

---
# Failure modes
memorising · forgetting (LR too high) · messy data · no held-out set

---
<!-- _class: title -->
# Next: M09 — prompts & apps
