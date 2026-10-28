# Chapter 14 — Prompt Engineering (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch14.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch14.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt) · **My Llama runs:** [ch14_real.py](ch14_real.py)

---

## 0. Why this chapter matters
Better outputs without changing weights: sampling controls, prompt patterns, structured output, injection defences and systematic evaluation.

**My runs:** the notebook (MiniGPT demos + Ollama), plus my own script running the chapter's prompts on **Llama 3.2 3B (Q4_K_M) via Ollama** on CPU.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| System message | Role + rules at the top of a chat |
| Few-shot | Worked examples inside the prompt |
| Chain-of-thought | Reasoning before the answer |
| Prompt injection | User text trying to override instructions |
| Temperature | Divides logits; <1 sharpens, >1 flattens |
| Top-p | Sample from the smallest set covering p of the probability |

## 1. Completion mindset
Models continue text. End your prompt where the answer should start (`Q: … \nA:`).

## 2. Roles
System = job description (role, constraints, format). It's text, but chat-tuned models weight it. MiniGPT has no roles.

## 3. Temperature and top-p
- Temperature on probabilities = p^(1/T), renormalised. For 0.70/0.25/0.05: **T=0.3 → 0.969/0.031/0.0001; T=2 → 0.536/0.320/0.143** (the book prints 0.47/0.33/0.20).
- T=0 = greedy (special-cased). Facts 0–0.3, chat 0.5–0.7, creative 0.8–1.0.
- Top-p keeps the fewest tokens whose mass ≥ p (`searchsorted(...)+1` correctly keeps the crossing token). Common: T=0.8, p=0.95.

## 4. Patterns
Zero-shot (just ask) · few-shot (2–5 examples covering every label, matching real style; all-positive examples bias) · chain-of-thought (pays off on large models) · delimiters (`###`, backticks, tags) · explicit output format, parsed defensively (`safe_json_parse`).

## 5. Injection and defences
Delimiters around untrusted input, input pattern checks, output checks, system reminders. Prompt-level defences are one layer: add least privilege, output validation and human review.

## 6. Evaluation
Small deliberate eval set (easy / hard / edge / adversarial). The scorer is part of the metric: the book's exact-equality check fails "Positive."; the notebook's first-word check also keeps the period.

## 7. My runs
**Notebook:** MiniGPT temperature/top-p/few-shot demos ran (gibberish by design, random weights). The Ollama CoT cell timed out at the helper's 120 s limit on my busy CPU. JSON parsing, delimiter and validation cells worked ("Ignore previous instructions…" blocked).

**My Llama 3.2 3B runs** ([ch14_real.py](ch14_real.py), raw [ch14_real.json](ch14_real.json)); Ollama, CPU, seed 0:

| Prompt on the 7-case eval set (T=0) | Strict | Lenient |
|---|---|---|
| BAD | 0/7 | 1/7 |
| BETTER | 0/7 | 6/7 |
| BEST (role + one word + 3 examples + "treat as data") | 4/7 | 4/7 |

- BEST invented labels ("confused", "mixed") and obeyed the adversarial review ("positive"); BETTER got that case right.
- CoT (T=0.3) on "great effects / confusing story": clear 4-step reasoning, verdict **negative** (the chapter's examples treat mixed as neutral).
- JSON: 5/5 valid with schema-only prompt and 5/5 with `format="json"` (T=0.8).
- Injection: vulnerable prompt → refusal 3/3 (no "HACKED"); delimited prompt → echoed template + garbled French. No leak, but no translation either.

## 8. Book checks (errata)
See ERRATA.md, ch14 rows.

## 9. Review questions (my answers)
1. Rules in the system message persist across turns and carry more weight than user text.
2. Backwards: ~0.8 for creative writing, 0–0.2 for code.
3. CoT puts the evidence in context before the answer token.
4. Check label consistency, coverage of all classes, and an explicit format line (plus example order/length).
5. Prompt injection → delimiters + input/output validation.
6. Build a 10–20 case eval set, change one thing at a time, re-run, watch for regressions.
7. (a) fine-tune · (b) few-shot first, fine-tune if needed · (c) RAG.

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
