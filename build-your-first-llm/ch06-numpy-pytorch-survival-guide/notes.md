# Chapter 6 — NumPy & PyTorch Survival Guide (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch06.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch06.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
Every number inside an LLM lives in a tensor, and most bugs are shape bugs. This chapter covers the tensor toolkit used in every later chapter: shapes, reshaping, broadcasting, matmul, attention in code, autograd, `nn.Module`, embeddings, and the training loop.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Tensor | An n-dimensional array with a shape, a dtype and a device |
| Shape | "How many of what", e.g. (batch, seq, d_model) |
| Broadcasting | Virtual expansion of size-1 or missing dims, aligned from the right |
| `@` | Matrix multiply (batched over leading dims) |
| Autograd | Records ops; `backward()` fills `.grad` |
| nn.Module | Parameters + `forward()`; `model(x)` calls forward |
| Loss | A scalar measure of wrongness that training minimises |
| Device | CPU or GPU; tensors in one op must share a device |

## 1. Tensors and the NumPy → PyTorch bridge
- **Shape ladder:** scalar () → vector (n,) → matrix → 3-D (B, S, d) → 4-D (B, H, S, S).
- **Differences from NumPy:** `torch.tensor` vs `np.array`; `.to(dtype/device)` vs `.astype`.
- **Default float:** NumPy uses **float64** and PyTorch **float32** (checked).
- **GPU:** `.to("cuda")`. Mixing CPU and GPU tensors raises a RuntimeError.
- **Zero-copy:** `torch.from_numpy` shares memory. Setting `np_arr[0]=999` gives the tensor `[999, 2, 3]` (I ran it). `torch.tensor(np_arr)` makes a copy.

## 2. Building up dimensions (notebook outputs)
`[2,3,4,6]` (4,) → batch (2, 4) → embeddings (2, 4, 768) → attention scores (2, 8, 4, 4). Naming: B, S/L, d_model, H.

## 3. Creation, seeds, dtype/device
`zeros/ones/rand/randn/randint/arange/linspace`. With `torch.manual_seed(42)` the tensors match → True. Set dtype and device deliberately.

## 4. Reshaping
- Shapes are contracts: (2, 4, 768) + (2, 4, 512) raises "size 768 must match 512 at dim 2".
- `reshape` (total element count unchanged, `-1` infers a dim), `unsqueeze(0)` (adds a batch-of-one dim), `squeeze`, `permute`.
- **view vs reshape:** `view` needs contiguous memory. After `.T` or `permute`, `view` fails (I triggered it), while `reshape` copies. Default to `reshape`.

## 5. Indexing, broadcasting, ops
- `x[0]`, `x[:, :, :-1]`, `...`, `torch.tril(ones)` for the causal mask.
- **Broadcasting rules (from the right):** dims must be equal or 1; a missing dim counts as 1. (3, 4) + (4,) → (3, 4).
- **Exercise 1 (ran):** (4, 3, 768) + (768,) ✓ and + (3, 768) ✓ (both give (4, 3, 768)); + (4, 768) fails (3 vs 4).
- **Ops:** `*` is element-wise and `@` is matmul. (32, 10, 64) @ (64, 128) → (32, 10, 128). `sum/mean(dim, keepdim)`, `cat` vs `stack`, `softmax(dim=-1)`.

## 6. Attention in code
Notebook cell 16 runs scores = Q@Kᵀ → /√64 → softmax → @V. The output has the same shape (2, 5, 64) and rows sum to 1. Token 2's weights: `[0.7634, 0.0332, 0.1282, 0.0501, 0.0251]`.

With the causal mask (`triu(..., 1).bool()` + `masked_fill(-inf)`), token 2 gives `[0.8256, 0.0359, 0.1386, 0, 0]`.

**My checks:**
- The manual version equals `F.scaled_dot_product_attention(..., is_causal=True)` → True.
- CPU timing (B4, H12, S512, d64): manual 166 ms vs fused 13.7 ms, about 12×. The book's "2–4× via FlashAttention" figure refers to GPUs.

## 7. Autograd, nn.Module, embeddings
- For x = [2, 3], z = Σx², `z.backward()` gives `x.grad = [4, 6]` (= 2x).
- `no_grad()` turns off tracking for a block; `.detach()` cuts out one tensor.
- `SimpleMLP(768, 3072, 768)` has **4,728,576** params (my count).
- **Embeddings:** `nn.Embedding(50257, 768)` = 38,597,376 params, plus positions `nn.Embedding(1024, 768)` = 786,432, for a total of **39,383,808** ✓. Token embeddings are ≈31% of GPT-2 small.
- Position ids: `arange(S).unsqueeze(0).expand(B, -1)`.

> ⚠️ **Errata.** §6.12 says "GPT-2 uses learned position embeddings; BERT uses sinusoidal (fixed)." **BERT also uses learned** absolute position embeddings (512×768 in BERT-base). Sinusoidal encodings come from the original 2017 Transformer.

## 8. Training loop
The steps are zero_grad → forward → loss → backward → **clip_grad_norm_(1.0)** → step. Gradients accumulate by default.
- **Notebook (3 epochs, random labels):** loss 0.6955 / 0.6925 / 0.6896, accuracy 0.56.
- **My experiment (300 steps):** loss 0.692 → 0.058 and train accuracy 1.00 **on random labels**. The model memorised noise, which is why you need a validation set.
- `train()`/`eval()` toggle dropout (and batch-norm stats); `zero_grad(set_to_none=True)` saves memory.

## 9. Exercises (my runs)
1. See §5.
2. (2, 5, 512) → reshape (2, 5, 8, 64) → permute (2, 8, 5, 64) → scores **(2, 8, 5, 5)** ✓. The permuted tensor is non-contiguous.
3. One Adam step (lr 1e-2, seed 0) moved the loss from 1.6769 to 1.6082. **Bonus:** `clip_grad_norm_` returns the pre-clip total norm. Mine was 0.555 < 1.0, so nothing was clipped.

## 10. Notebook run
`ch06.ipynb` ran on CPU (torch 2.15). **All 19 code cells passed, no errors.** The outputs match the book.

## 11. Key takeaways
1. Think in shapes.
2. PyTorch = NumPy + GPU + autograd, float32 by default.
3. (B, S) → (B, S, d) → (B, H, S, S).
4. Broadcasting aligns from the right.
5. `@` combines features; attention is 4 lines or one fused call.
6. zero_grad → forward → loss → backward → clip → step.

## 12. Review questions (my answers)
1. **float32 vs float64:** PyTorch defaults to float32 for speed and memory; NumPy uses float64 for scientific precision. It matters when you mix the two or need high precision.
2. **reshape vs view:** prefer `reshape` after transpose or permute, because `view` needs contiguous memory.
3. **Broadcasting:** align from the right; each pair must be equal or contain a 1.
4. **softmax dim:** the axis that sums to 1 (−1 for logits). The wrong dim is silently wrong.
5. **no_grad vs detach:** `no_grad` covers a block; `detach` covers one tensor.
6. **zero_grad:** gradients accumulate; `set_to_none` saves memory.
7. **train vs eval:** toggles dropout and batch-norm behaviour.

---
**Credits.** Based on *Build Your First LLM* by Hasan Degismez. Please buy the book: <https://leanpub.com/FirstLLM/>. Code shown verbatim: FirstLLM/code (MIT License), `notebooks/ch06.ipynb`. Notes, diagrams and experiments are my own adaptation (Waqar Shaikh Builds).
