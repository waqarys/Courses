# Chapter 18 — What's Next (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch18.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch18.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
There's no new model code. The chapter consolidates the whole book, frames responsibility as part of engineering, and turns "what now?" into three paths and three sized capstone projects. The notebook (9 code cells, all ran on CPU) prints the journey, a 14-item skills checklist starting at 0/14, a learning-plan generator and two starter templates (a RAG API and a single-tool agent).

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| MLOps / LLMOps | Operating models in production: versioning, evaluation pipelines, monitoring |
| Quantization | Fewer bits per weight (e.g. 16 → 4) to save memory and compute |
| Structured outputs | Forcing JSON or function-call formats |
| Sparse attention | Attending to a subset of token pairs |
| Mixture of experts | A router sends each token to a few expert sub-networks |
| Interpretability | Explaining why a model produced an output |

## 1. The journey
Part I (ch1–4) theory → Part II (ch5–6) Python and tensors → Part III (ch7–12) data, tokenizer, embeddings, attention, MiniGPT, training → Part IV (ch13–15) LoRA, prompting, RAG and tools → Part V (ch16–17) FastAPI and Modal deployment.

## 2. Responsible building
Ask questions about **data** (source, licence, bias), **outputs** (harm, hallucination, validation and moderation) and **transparency** (disclosure, logging, traceability). Assume your next system will fail sometimes: set expectations, add guardrails, log, test for bias and give users an escape hatch.

## 3. Three paths (6–12 months)
| Path | For you if | Learn next | Builds on (corrected) |
|---|---|---|---|
| Research | You want *why* | evaluation science, sparse attention / MoE / SSMs, interpretability | Ch 10, 12, 15 |
| Builder | You want users | structured outputs, hybrid search + re-ranking, UX | Ch 14, 15 |
| Systems | You want scale | quantization, caching, batching, observability, LLMOps | Ch 16, 17 |

## 4. Capstones
1. **RAG with citations**: 50–100 docs, chunk and embed (Ch 15), cite sources, API (Ch 16), deploy (Ch 17), hand-grade 20 questions. Stretch: BM25 hybrid.
2. **Fine-tuned domain assistant**: 500–1,000 curated pairs, QLoRA on ~7B (PEFT + bitsandbytes), 20-question test against the generic model. Stretch: DPO.
3. **Single-tool agent**: one tool, a schema, structured selection, 20 tests (10 need the tool), target 19/20. The notebook's calculator uses `eval(expr, {"__builtins__": {}}, {})`, which still isn't a safe sandbox. Use a real parser (e.g. `ast` with whitelisted nodes).

My four-weekend plan: test set and baseline → core pipeline → API and guardrails → deploy and write-up.

## 5. Resources
Gentle: Hugging Face course, r/LocalLLaMA, a vendor prompt guide. Confident: Stanford CS324, the Transformer and LoRA papers, DeepLearning.AI short courses. Community: Hugging Face Discord, MLOps Community, small open-source PRs.

Paper reading: abstract and conclusion → figures → skip the maths first → experiments → related work last.

## 6. My lessons from the series
Running every notebook on a CPU found real issues (all in ERRATA.md). Examples:
- Ch 11's GPT-2 loader dropped attention biases.
- Ch 12's `ignore_index=0` ignores "!" instead of padding.
- The LoRA parameter counts and naming in Ch 13 don't match the code.
- vLLM on a T4 needs `dtype="half"` in Ch 17.

The habit to keep: trust your own logs over printed outputs.

## 7. Book checks (errata)
See ERRATA.md, ch18 rows: chapter cross-references for training/evaluation, RAG and audit trails.

## 8. Review questions (my answers)
1. Research, builder, systems.
2. Data, users and models change, and so do failure modes, so the checks have to be repeated.
3. RAG with citations, because it exercises the most chapters.
4. The LoRA paper and vLLM's docs.
5. How much behaviour hides in single arguments (`ignore_index`, `bias=False`, `dtype`).

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
