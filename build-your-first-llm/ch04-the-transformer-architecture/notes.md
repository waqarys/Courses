# Chapter 4 — The Transformer Architecture (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>. Companion code: <https://github.com/FirstLLM/code> (MIT). Chapter 4 has no notebook; the notebooks start at Chapter 5. **All code and GPT-2 measurements below are my own.**

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
Attention mixes information between positions, but it is not a complete model. This chapter adds four supporting pieces: **position**, the **feed-forward network**, **residual connections** and **normalisation**. Together they make the repeating Transformer layer that GPT stacks N times. Part III of the book builds exactly this, as a decoder-only model.

### Learning goals
1. Explain why attention needs position information, and compare sinusoidal, learned and RoPE encodings.
2. Explain the FFN's expand → activate → contract structure and why a nonlinearity is required.
3. Explain residual connections and the residual stream.
4. Explain LayerNorm and RMSNorm, and Pre-Norm vs Post-Norm.
5. Write out one Transformer layer and the full model.
6. Distinguish encoder, decoder and encoder–decoder models.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Position encoding | A vector added to a token embedding that encodes *where* the token is |
| FFN | A per-position MLP: Linear(d→4d) → activation → Linear(4d→d) |
| Activation function | A nonlinearity (GELU, ReLU, SiLU…) |
| Residual connection | `out = x + f(x)` |
| LayerNorm | Per-vector (x−μ)/σ, then learned γ, β |
| RMSNorm | x / RMS(x) · γ (no mean subtraction) |
| Encoder / decoder | Bidirectional attention / causal attention |
| Causal mask | Future attention scores set to −∞ |

---

## 1. Position
**The problem.** Attention is *permutation-equivariant*: if you shuffle the inputs, the outputs are shuffled the same way. I checked this with a random attention layer: `torch.allclose(att(x)[p], att(x[p]))` → **True**. So "The dog chased the cat" and "The cat chased the dog" look identical to it.

**The fix.** final = E(token) + P(position). Position is added once, at the input, and carried through every layer. The book compares it to GPS coordinates attached to a message.

| Scheme | How | Pros / cons | Used by |
|---|---|---|---|
| Sinusoidal | sin/cos at geometric frequencies (clock hands) | unique, smooth, defined for any position | 2017 Transformer |
| Learned | a trainable table `max_len × d` | flexible; no positions beyond max_len | GPT-2 (`wpe`: **1024 × 768**) |
| RoPE | rotate Q, K by a position-dependent angle | relative distance, fixed formula, good on long contexts | Llama, Mistral, most recent open models |

**My GPT-2 check.** The learned positions came out smooth: cos(wpe[10], wpe[11]) = **0.998**, cos(wpe[10], wpe[90]) = **0.27** (`img/pos_similarity.png`).

> ⚠️ **Errata.** The book lists GPT-4 among RoPE users. GPT-4's architecture has not been published.

```python
# my own: sinusoidal encodings
import numpy as np, math
def sinusoidal(n, d):
    pe = np.zeros((n, d)); pos = np.arange(n)[:, None]
    div = np.exp(np.arange(0, d, 2) * (-math.log(10000.0) / d))
    pe[:, 0::2] = np.sin(pos * div); pe[:, 1::2] = np.cos(pos * div)
    return pe
```

## 2. Feed-forward networks
- **Attention mixes, the FFN transforms.** Attention gathers the ingredients and the FFN cooks them. In the book's factory analogy, attention is the mail room and the FFN is the processing station.
- **Shape:** 768 → 3072 → 768. Real GPT-2: `c_fc` 768×3072 and `c_proj` 3072×768. It is applied **independently per position**.
- **Why expand:** scratch space for intermediate features (book analogy: 23×47 = 920 + 161 = 1081).
- **Why a nonlinearity:** stacked linear maps collapse into one, because B(Av) = (BA)v (checked). Language needs thresholds and reversals, like a sincere vs sarcastic "Great job!".
- **GELU vs ReLU.** ReLU zeroes negative inputs, so their gradient is 0 ("dead" units). GELU is smooth. My values: GELU(2) = **1.954**, GELU(−2) = **−0.046**, GELU(−0.5) = **−0.154** (the book's ≈1.96 / −0.04 / −0.15 are fine to rounding).

> ⚠️ **Errata.** The book says "Most modern LLMs (GPT, Claude, LLaMA) use GELU or close variants." GPT-2 and GPT-3 do use GELU. **LLaMA uses SwiGLU**, a gated FFN with SiLU/Swish. **Claude's architecture is not public.**

## 3. Residual connections
- **Degradation:** 0.99⁹⁶ = **0.381** ✓. Gradients vanish or explode through depth.
- `out = x + f(x)`, so f only learns the *residual* (the change). If f ≈ 0, the layer is an identity.
- **Highway with exits:** information and gradients bypass layers that don't help.
- A Transformer layer has two skips (around attention and around the FFN). The vector carried along is the **residual stream**. Every sublayer must output d_model.

## 4. Normalisation
- **Drift:** 1.01⁹⁶ = **2.60** ✓.
- **LayerNorm** (per vector): subtract the mean, divide by the std, then apply learned γ and β. The book calls it a thermostat.

> ⚠️ **Errata, the LayerNorm example.** Input `[102.5, 98.3, 105.7, 95.2]`. The book's output `[0.52, −0.31, 1.12, −0.78]` sums to 0.55, but a normalised vector must sum to 0. The correct values (μ = 100.425, σ ≈ 3.98, via `F.layer_norm` with γ=1, β=0) are **`[0.52, −0.53, 1.32, −1.31]`**.

- **Pre-Norm vs Post-Norm.** The 2017 paper used Post-Norm (LN after the residual add). GPT-2 and most modern LLMs use Pre-Norm (LN on each sublayer's input), which is more stable for deep models.
- **RMSNorm:** x / √(mean(x²)) · γ, with no centring. It is faster and uses less memory (Llama, Mistral). The same input gives `[1.020, 0.978, 1.052, 0.947]`.

## 5. Putting it together
```text
h   = x + Attention(LayerNorm(x))
out = h + FFN(LayerNorm(h))
```
Stack the layer N times: GPT-2 small 12, GPT-3 96, large models 80–120+.

Full model: ids → wte + wpe → N layers → final LN → unembedding (tied to wte in GPT-2) → logits → softmax.

Rough layer roles: early layers handle syntax and local patterns, middle layers phrases and semantics, late layers abstraction and the prediction.

**GPT-2 small parameter count (my measurement)**
| Part | Params |
|---|---|
| total | **124,439,808** |
| token embedding (50,257 × 768) | 38,597,376 |
| position embedding (1,024 × 768) | 786,432 |
| attention, per layer | 2,362,368 (× 12 = 28.3M) |
| FFN, per layer | 4,722,432 (× 12 = 56.7M) |
| LayerNorms, per layer | 3,072 |

The FFNs hold about ⅔ of the non-embedding parameters.

```python
# my own
from transformers import GPT2LMHeadModel
m = GPT2LMHeadModel.from_pretrained("gpt2")
print(sum(p.numel() for p in m.transformer.parameters()))    # 124439808
print(m.transformer.h[0].mlp.c_fc.weight.shape)              # (768, 3072)
```

## 6. Encoder vs decoder
- **Encoder** (BERT): full, bidirectional attention. Used for classification, NER and retrieval.
- **Decoder** (GPT, Llama, Claude): causal mask. Used for generation, and at scale for understanding too.
- **Encoder–decoder** (2017 Transformer, T5): the encoder reads the source; the decoder uses masked self-attention plus cross-attention. Used for translation and summarisation.
- GPT = Generative Pre-trained Transformer. Part III of the book builds a decoder-only model.

## 7. Training, inference, scale
- **Training:** predict the next token at *every* position, compute the loss, run backprop, update all weights. This is repeated billions of times.
- **Inference:** prompt → probabilities at the last position → sample → append → repeat (one forward pass per token).
- **My experiment, "The capital of France is":** GPT-2 small's top-6 next tokens are " the" 0.085, " now" 0.048, " a" 0.046, " France" 0.032, " Paris" 0.032, " in" 0.027. Greedy decoding continues "…is the capital of the French Republic, and". The book's "Paris" example is illustrative. A small base model knows Paris is relevant but does not answer like an assistant (instruction tuning comes later in the book).

| Model | Layers | d_model | Heads | Params |
|---|---|---|---|---|
| GPT-2 small | 12 | 768 | 12 | 124M |
| GPT-2 large | 36 | 1,280 | 20 | 774M |
| GPT-3 | 96 | 12,288 | 96 | 175B |
| Llama 3.1 405B | 126 | 16,384 | 128 | 405B |

(Sources: the papers and model cards.)

## 8. Exercises (my answers)
1–2. **Trace "The cat sat".** GPT-2 IDs [464, 3797, 3332] → (3×768) embeddings + wpe[0..2] → L1 attention (sat→cat) → per-row FFN → more layers → P(next) (e.g. " on", " down"). The residual stream keeps the original "cat" signal alive.
3. **Tiny transformer for a word's last letter:** 2 layers, d=64, 4 heads, learned positions (short, fixed length).
4. **Architecture choice:** sentiment → encoder; translation → encoder–decoder (or a large decoder); story continuation → decoder; NER → encoder; QA → encoder (extractive) or decoder (generative).

## 9. Checkpoint (my answers)
- **No residuals:** depth degrades and gradients vanish, so early layers barely learn.
- **No LayerNorm:** activations drift and blow up or vanish, so training is unstable.
- **Position before attention:** attention is order-blind, so position must already be inside Q and K when the scores are computed.
- **More layers:** more capacity and refinement, but more compute, harder optimisation and overfitting on small data.
- **Part 4:** document QA → encoder; essay writer → decoder; translator → encoder–decoder.

## 10. Key takeaways
1. Attention is order-blind, so add position (sinusoidal, learned or RoPE).
2. FFN: ×4 expand → GELU → contract, applied per position.
3. Residuals: x + f(x).
4. LayerNorm / RMSNorm, applied Pre-Norm in modern models.
5. One layer = LN → Attn → +x → LN → FFN → +h, stacked N times.
6. Encoders are bidirectional and decoders causal. GPT is decoder-only.

## 11. Review questions (my answers)
1. **Why positions?** Attention is permutation-equivariant, so without them "dog bites man" = "man bites dog".
2. **Two approaches?** Sinusoidal (a formula, extrapolates) vs learned (a table, often better within range, capped at max_len). RoPE is the modern relative-position variant.
3. **FFN?** Per-position processing: expand for scratch space, apply a nonlinearity, contract to fit the next layer.
4. **Residuals?** A highway: x + f(x) preserves the signal and the gradients through depth.
5. **LayerNorm?** Prevents drift by normalising each vector and applying γ, β. Modern models apply it before each sublayer.
6. **One layer:** LN → MHA → +x → LN → FFN → +h.
7. **Encoder vs decoder:** full vs causal attention. Encoders suit understanding (BERT); decoders suit generation (GPT).
8. **Causal mask:** future scores are set to −∞ before the softmax, so they get zero weight. This stops a next-token model from peeking ahead.

## 12. Notes on the book (verification)
| Item | Status |
|---|---|
| 0.99⁹⁶ ≈ 0.38; 1.01⁹⁶ ≈ 2.6 | ✅ |
| GELU(2, −2, −0.5) | ✅ (to rounding) |
| 768 → 3072 → 768 | ✅ (GPT-2 shapes) |
| LayerNorm example output | ⚠️ should be [0.52, −0.53, 1.32, −1.31] |
| "GPT, Claude, LLaMA use GELU" | ⚠️ LLaMA uses SwiGLU; Claude unpublished |
| "GPT-4 uses RoPE" | ⚠️ GPT-4's architecture is not public |
| "Paris" inference example | ℹ️ illustrative; GPT-2 small ranks " Paris" 5th (3.2%) |

---
**Credits.** Based on *Build Your First LLM* by Hasan Degismez. Please buy the book: <https://leanpub.com/FirstLLM/>. Code: <https://github.com/FirstLLM/code> (MIT). GPT-2 weights: OpenAI via Hugging Face. Notes, diagrams and code are my own adaptation (Waqar Shaikh Builds).
