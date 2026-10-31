# Chapter 13 — Fine-Tuning Your Model (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch13.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch13.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt) · **My experiment:** [lora_gpt2.py](lora_gpt2.py)

---

## 0. Why this chapter matters
Pretraining gives broad language skill; fine-tuning specialises it. The chapter covers instruction data, loss masking and LoRA adapters built from scratch.

**My runs:**
- **Notebook (unchanged, CPU):** runs top to bottom until evaluation, but the base MiniGPT is randomly initialised and the test split is empty, so it can't show improvement (details in §6).
- **My fix:** the same recipe on a pretrained **GPT-2 small** with LoRA on every `c_attn`, the book's 69 FAQ pairs split 55 train / 14 held out.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| SFT | Supervised fine-tuning on input → output pairs |
| Loss masking | Label prompt tokens -100 so only answers are graded |
| LoRA | Frozen W plus a trainable low-rank update ΔW = down·up·(α/r) |
| Adapter | Small trainable add-on module |
| Rank r | Bottleneck width of the LoRA update |
| Freezing | `requires_grad=False` |

## 1. Fine-tune or prompt?
Try 5–10 prompt variants first. Fine-tune if at least two hold: 100+ good examples; strict vocabulary/format needed; task far from pretraining. Prompting costs tokens per request; fine-tuning costs compute once plus an artifact to version.

## 2. Data
- Records become `{"instruction": …, "response": …}` in JSONL (one object per line).
- Quality beats quantity: each example is seen many times, so mistakes and contradictions are amplified.
- **Notebook:** `FAQ_DATA` has **69** pairs, and `train_data = FAQ_DATA[:80]` uses all of them → empty test set.

## 3. Loss masking
- Format: `[INST] question [/INST] answer`; labels = input ids with the prompt part set to **-100**; `F.cross_entropy(..., ignore_index=-100)` after the usual one-token shift.
- Notebook example: 115 masked positions (prompt + padding), 13 trained.
- Add an end-of-text token after the answer so the model learns to stop (the chapter doesn't).

## 4. LoRA
- `out = x@W + (x@down@up)·(α/r)`. One factor random, the other zero → starts as a no-op.
- **Naming:** the book calls the down matrix `lora_B` and the up matrix `lora_A`; the LoRA paper and PEFT use the opposite names.
- **Savings depend on shape:** 768×768 → 48×; MiniGPT's `qkv_proj` (256→768) → 24×; the notebook's 256×256 demo → 16×.
- Notebook model: **32,768 trainable / 16,086,784 total (0.20%)**.
- A LoRA on the fused qkv projection adapts Q, K and V alike (not "primarily Q and V").
- QLoRA = 4-bit frozen base + LoRA (bitsandbytes + PEFT).

## 5. Evaluation
Exact match (strict), word overlap, and reading outputs, always on held-out examples. The book's `model.generate(…, do_sample=False)` is Hugging Face's API; MiniGPT needs a small greedy loop.

## 6. My runs
**Notebook:** random base → loss 10.8632 → 10.7390 (−1.1%); gibberish before and after; evaluation cell 27 `ZeroDivisionError` (empty test set), cell 28 `NameError`. Adapter 131.6 KB vs full model 61.4 MB (478×).

**My GPT-2 + LoRA run** ([lora_gpt2.py](lora_gpt2.py), results [lora_gpt2.json](lora_gpt2.json)): GPT-2 small, LoRA r=8 α=16 on all 12 `c_attn` (294,912 trainable / 124,734,720 = 0.24%), AdamW lr 1e-3, batch 8, 12 epochs, masked loss + EOS, shuffled 55/14 split (seed 0), greedy decoding.

| Metric | Before | After |
|---|---|---|
| Masked train loss | — | 3.15 → 0.73 |
| Held-out exact match | 0% | 0% |
| Held-out word overlap | 5.3% | 18.5% |
| Train-set overlap / exact | — | 53.4% / 21% |

Held-out answers have the right voice but invented facts (a made-up support email and phone number; a vague uptime answer). Facts already present in other training answers (Amsterdam) come back right. **Lesson:** small-data SFT teaches style and format; unseen facts need RAG. The book's "50%+ exact match" isn't realistic on genuinely held-out questions. Adapter file: 1.16 MB.

## 7. Shipping adapters
Save only `lora_*` tensors; load into the same structure with `strict=False` (on the same base weights). Keep adapters separate to swap tasks; merge (`W += (down@up·scale)ᵀ`, then zero the adapter) for one simple file.

## 8. Book checks (errata)
See ERRATA.md, ch13 rows: 69 vs 80/20 examples, A/B naming, the 48× claim, trainable counts, "primarily Q and V", `model.generate`, file sizes, and the 50%+ checkpoint claim.

## 9. Review questions (my answers)
1. 200 Q&A pairs + strict format → fine-tune (after trying prompts).
2. Masking avoids wasting signal on the question and stops the model learning to parrot it.
3. Task changes are low-rank; larger shifts may need a higher rank.
4. Freezing protects pretrained skills (catastrophic forgetting).
5. More noisy data isn't better for fine-tuning: every example is repeated and errors amplify.
6. Keep adapters separate for multi-task swapping; merge for a single-purpose deployment.
7. The medical fine-tune overwrote general weights; LoRA keeps them frozen.

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
