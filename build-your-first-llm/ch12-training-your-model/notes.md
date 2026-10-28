# Chapter 12 — Training Your Model (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch12.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch12.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
This is where MiniGPT's random weights become learned weights. I ran the notebook **unchanged on CPU for the full 3 epochs** (about 35 minutes on a shared 8-core box). Then I ran my own fixed training pipeline on the same model and compared the two.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Cross-entropy | −ln(probability given to the correct next token), averaged |
| Learning rate | Step size of each update |
| Warmup | A linear ramp of the LR from ~0 over the first N steps |
| Epoch | One pass over the training set |
| Perplexity | e^(mean loss), "how many tokens it's torn between" |
| Overfitting | Train loss falls while validation loss rises |
| Checkpoint | Model + optimizer + scheduler state + metadata |

## 1. The objective
- `inputs = ids[:, :-1]`, `targets = ids[:, 1:]`: one sequence of T tokens gives T−1 next-token examples, kept fair by the causal mask.
- Cross-entropy only looks at p(correct). Scale: p=0.9 → 0.11, p=0.1 → 2.30, p=0.01 → 4.61, uniform over 50,257 → **10.82**.
- Flatten to `(B*T, V)` and `(B*T,)`. Use `reshape` for the sliced targets (they aren't contiguous).

## 2. Data
- TinyShakespeare: 1,115,394 chars → **338,025 GPT-2 tokens** (my count).
- `TextDataset(text, chunk_size=256)` cuts **characters**, giving 4,357 chunks. A 90/10 `random_split` (seed 42) gives **3,921 / 436**.
- `collate_fn` tokenizes, pads to the longest item in the batch and truncates at 128. `pad_token = eos_token`, so **pad id = 50256**.
- Batch size 32 → **123 batches per epoch** (the book prints 312).

## 3. The loop
zero_grad → forward → loss → backward → clip(1.0) → optimizer.step → scheduler.step. AdamW lr 3e-4, wd 0.01, 100 warmup steps then linear decay over 369 total steps, `model.train()` at the start of each epoch.

## 4. Evaluation
`@torch.no_grad()` with `model.eval()`: sum the loss over the counted tokens, divide, exponentiate. Early stopping with patience 3 can't trigger in a 3-epoch run.

## 5. My CPU run vs the book
| | Book (printed) | My run (notebook unchanged) |
|---|---|---|
| Parameters | 10,789,121 | **16,054,016** |
| Batches/epoch | 312 | **123** |
| Epoch 1 train/val/ppl | 4.82 / 4.22 / 67.8 | **8.38 / 6.22 / 504.9** |
| Epoch 2 | 3.98 / 3.89 / 49.0 | **5.90 / 5.66 / 287.1** |
| Epoch 3 | 3.62 / 3.75 / 42.3 | **5.54 / 5.51 / 246.2** |

Sample ("To be or not to be", T=0.8): *"To be or not to be breathed by / The already, you you hathAM. / But me in Ty her, of thee,CA: …"*. It has the shape of a play, but no sentences.

## 6. The padding bug (my main finding)
- `F.cross_entropy(..., ignore_index=0)`, with the comment "Ignore padding (token ID 0)". In GPT-2, **token 0 is `!`**, a real character and 0.62% of Shakespeare's tokens.
- The real pad (50256) is **not** ignored. Padded batches average ~100 positions while chunks average ~78 tokens. I counted **22% of target positions** as pad→pad predictions, which are easy. That also flatters the reported validation loss.
- The `create_lm_labels(..., pad_token_id=0)` helper has the same default.
- Fix: `targets = input_ids[:,1:].masked_fill(attention_mask[:,1:]==0, -100)` and `ignore_index=-100`.

## 7. A better pipeline (my experiment, `_src/exp/ch12_mine.py`)
Same 16M MiniGPT (with the Ch 11 bias fix), same AdamW/lr/warmup/clipping, but:
- Tokenize the whole text once and split by token position (first 90% train, last 10% val).
- Sample random 128-token windows: no padding at all, and every position is real text.
- Log every 50 steps on 10 fixed validation batches.

Result: after 1,200 steps (≈1.5 h on a shared CPU) val loss **4.87, perplexity 130** (notebook after 3 epochs: 5.51 / 246). At step 350 mine was already 5.37, vs the notebook's 5.51 at step 369, on a stricter no-padding metric. Sample for `KING HENRY:` → "It should said long: / A saved before, my lord. / QUEEN MARGARET: / I tell me not it, and knee, …": real names and verse shape, no sense. Log and samples: [ch12_mine.json](ch12_mine.json), script [ch12_mine.py](ch12_mine.py).

## 8. Exercises (my answers)
1. Custom data: under ~1 MB it overfits fast, so watch val loss per step.
2. LR sweep: 1e-5 barely moves; 3e-4 is healthy; 1e-2 spikes or diverges even with clipping.
3. Temperature: 0.3 loops, 1.0 varies, 2.0 is soup.
4. Resume: reload model + optimizer + scheduler. The curves match apart from dropout and shuffle RNG unless you also restore the RNG states.
5. Early stopping: needs more epochs than patience. Reload `best_model.pt` at the end.
6. Perplexity table: improvement = 1 − ppl_final/ppl_epoch1 (my run: 1 − 246.2/504.9 = **51%**).

## 9. Book checks (errata)
See ERRATA.md, ch12 rows: `ignore_index=0`, the `pad_token_id=0` default, 312 vs 123 batches, the parameter count, the printed losses/perplexity, and the sample output.

## 10. Review questions (short)
1. `zero_grad`, forward, loss, `backward`, `step`.
2. Shifting makes each position predict its successor. Without it the model copies its input.
3. `-100` positions are skipped in the loss, but only if you actually map padding to it.
4. LR is the step size: too high diverges, too low crawls.
5. Warmup: early gradients from random weights are unreliable.
6. Overfitting: val turns up while train falls. Stop early or add data/regularisation.
7. Perplexity 50 ≈ choosing among 50 equally likely tokens.
8. Save model, optimizer, scheduler, epoch and losses. Weights only means AdamW's moments and the LR schedule reset.
9. `train()` turns dropout on; `eval()` turns it off. Use eval for validation and generation.
10. 10,000/32 = 312.5 → 313 batches (312 if `drop_last=True`); 5 epochs → 1,565 updates.

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
