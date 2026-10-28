# Chapter 15 — Building Applications (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch15.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch15.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt) · **My Llama run:** [ch15_real.py](ch15_real.py) (+ [nb_defs.py](nb_defs.py), notebook code)

---

## 0. Why this chapter matters
From model trainer to application builder: a chat loop, RAG with citations, a tool-calling preview, and automatic evaluation.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| RAG | Retrieve relevant text, add it to the prompt, generate |
| Sentence embedding | One vector per passage, trained for meaning similarity |
| Chunking | Splitting documents into retrievable windows |
| Context window | Max tokens visible at once (prompt + reply) |
| Tool calling | Model asks your code to run a whitelisted function |
| Citation | [n] marker linking a claim to a source |

## 1. Patterns
Prompting → add RAG for missing knowledge → add tools for actions or exact computation.

## 2. Chat loop
Memory = resending history. `ChatSession` keeps ≤ 20 messages (counts messages, not tokens). Leave ~20% of the window for the reply.
- Llama 3.2 3B supports **131,072** tokens (book: ~8,192); Ollama ran it with `-c 4096` on my box. Set `num_ctx`.
- The logging snippet calls `count_history_tokens()` / `count_tokens()`, which don't exist. Use a tokenizer or Ollama's `prompt_eval_count` / `eval_count`.

## 3. RAG
- `all-MiniLM-L6-v2` → 384-d vectors. Book example cosine: **0.657** (book ~0.65) ✔.
- Chunk 200 words with 50 overlap; normalised vectors → dot product = cosine; top-k with `min_score=0.3`.
- Prompt: numbered sources, "only use these", permission to say not found.
- Embeddings/cosine were **Ch 9**, not Ch 6.

## 4. Tools
`<tool>name(arg)</tool>` → parse → run whitelisted function → send result back.
- **Security:** `eval(expr, {"__builtins__": {}}, {})` is *not* a sandbox. My test expression reached the `os` module via `().__class__.__base__.__subclasses__()` → `BuiltinImporter.load_module('os')`. Use an `ast` whitelist or `simpleeval`.
- Rules: whitelist, validate, read-only first, log every call.

## 5. Testing and production
Trait checks (keywords, citations, refusal, length); temperature per task (RAG ~0.2–0.3, tools 0, creative ~0.8; the book's `gpt-3.5-turbo` client snippet doesn't match the chapter's Ollama helper); streaming; embedding cache; a layered debugging checklist.

## 6. My runs
**Notebook:** chat memory ✔; one chunk passes `min_score` per query (0.712, 0.546); RAG answers cite [1] ✔; Llama 3.2 3B ignored the `<tool>` format ("calculate 15% of 847") so no tool ran; two calls timed out at the helper's 120 s (busy CPU); streaming ✔.

**My Llama 3.2 3B run** ([ch15_real.py](ch15_real.py), raw [ch15_real.json](ch15_real.json)):
- Retrieval: vacation 0.791 (+ remote 0.360), remote 0.420, carry-over 0.668; "meaning of life" retrieves nothing ≥ 0.3.
- Book eval set: **5/8 traits** — vacation 3/3; expense process 2/3 (correct list, no [n]); meaning of life 0/2: the empty-retrieval prompt offers general knowledge, so the model wrote about Aristotle and **cited a non-existent [1]**. Fix: skip the LLM when retrieval is empty.
- Tools: 0/2 real tool calls ("calculate 15% of 847" without tags; `<get_date> </get_date>`); "capital of France" correctly used none. Use native tool calling, a format example, or a larger model.

## 7. Book checks (errata)
See ERRATA.md, ch15 rows.

## 8. Review questions (my answers)
1. RAG supplies facts the model never saw (private/recent).
2. Token embeddings: per token, inside the model. Sentence embeddings: one vector per passage, for retrieval.
3. Chunking fits the context and sharpens matching; too small loses context, too big blurs it.
4. Filter by `min_score` and let the prompt say "not in sources".
5. Whitelisting stops calls to arbitrary code (e.g. a file-deleting function).
6. Trait-based eval set + reading samples; track citation and correctness rates.
7. Request id, prompt/response tokens, retrieved sources + scores, latency, errors, tool calls.

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
