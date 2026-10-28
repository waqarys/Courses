# Chapter 3 — The Attention Mechanism (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>. Companion code: <https://github.com/FirstLLM/code> (MIT). Chapter 3 has no notebook (they start at Chapter 5; attention is implemented in the Ch 10 notebook). **All code and GPT-2 experiments below are my own.**

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
Chapter 2 left us with static embeddings that cannot see word order or context. Attention fixes this. Each word looks at every other word, decides what is relevant, and builds a new, context-aware vector. This is the core of every Transformer.

### Learning goals
1. Explain the RNN sequential bottleneck.
2. Describe attention with the cocktail-party, spotlight and search-engine analogies.
3. Explain Query, Key and Value and where they come from.
4. Compute attention by hand: scores → softmax → weighted sum. Explain √d.
5. Explain multi-head attention, self vs cross attention, causal masking and the n² cost.
6. Explain why the 2017 Transformer paper mattered.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Attention | Weigh every position by relevance, then blend their information |
| Self-attention | Q, K and V come from the same sequence |
| Cross-attention | Q comes from one sequence; K and V from another |
| Query / Key / Value | What I'm looking for / what I advertise / what I hand over |
| Softmax | e^s / Σe^s: positive weights that sum to 1 |
| Scaled dot-product attention | softmax(QKᵀ/√d)·V |
| Multi-head attention | Several attentions in parallel, each with its own W_Q, W_K, W_V, then concatenated and projected |
| Weights / transformation | Learned numbers; multiplying by them maps an embedding to Q, K or V |
| Transformer | The 2017 attention-only architecture |

---

## 1. The problem with RNNs
An RNN reads one token at a time and carries a **fixed-size hidden state** forward, like a single sticky note that keeps being rewritten. In "The cat that the dog that the man owned chased ran away", the subject (*cat*) is overwritten by the time *ran* arrives. RNNs are also **sequential**: step t must wait for step t−1, which is poor for GPUs.

> ⚠️ **Precision note (errata).** The book calls this forgetting "the vanishing gradient problem: information degrades as it travels through a chain". Strictly, vanishing gradients describe the **training signal** shrinking as it flows *backward* through many steps, which makes long-range patterns hard to *learn*. The forward problem is the **fixed-size state bottleneck**. Both are real. LSTMs and GRUs mostly address the first.

Long text needs three things. In "The trophy didn't fit in the suitcase because **it** was too big", you have to keep both candidates available, use "too big" to choose between them, and link words that are far apart.

## 2. What attention is
- **Cocktail party:** selective focus. Irrelevant voices are dimmed, not deleted, so the weights are soft.
- **Spotlights:** any word can light up any other instantly (no single moving beam).
- **Search engine:** each word runs a query, ranks all words and blends the results.
- **Chain → web:** every pair connects directly, and all positions are computed in parallel.

## 3. Query, Key, Value
**Library:** the Query is your question, the Key is the spine label, the Value is the content. Matching is *soft*: every book gets a weight.

**Every word is both visitor and book.** For "The cat sat", *sat*'s query ("who's doing this?") matches *cat*'s key ("something that can act"), so *sat* absorbs much of *cat*'s value.

**Where Q, K and V come from:** three learned linear maps of the *same* embedding, Q = xW_Q, K = xW_K, V = xW_V. They are not stored separately. Book example: x = [2, 4, 1] with weight column [0.5, 0.25, 1.0] gives 1 + 1 + 1 = **3** (checked ✓).

**Open weights** means the learned numbers are published (e.g. Llama, Mistral), so you can run the model locally and fine-tune it.

## 4. The calculation
For the query *sat* in "The cat sat on the mat", the book's illustrative scores are `[0.1, 0.8, 0.4, 0.2, 0.1, 0.5]`.

Softmax: e^0.8 ≈ 2.23. The sum of all six exponentials ≈ 8.82, so w(cat) ≈ 0.25. Full result: `[0.126, 0.253, 0.170, 0.139, 0.126, 0.187]`, which matches the book's `[0.13, 0.25, 0.17, 0.14, 0.13, 0.19]` ✓.

Output = Σ wⱼ·V(j). It is a new vector for *sat*, with the same shape as the input, so layers can be stacked.

```python
scores  = Q @ K.T
weights = softmax(scores / sqrt(d))
output  = weights @ V
```

### Why √d (my experiment)
For random q, k ~ N(0, 1), std(q·k) ≈ √d. I measured **2.04 / 7.85 / 28.0** for d = 4 / 64 / 768. After dividing by √d it is **≈ 1.0** in every case. Unscaled at d = 768, softmax over 6 keys gave a max weight of 1.00 (one-hot); scaled, it gave 0.73. One-hot softmax makes gradients vanish, so scaling keeps learning healthy.

## 5. Multi-head attention
"The tall lawyer who argued the case **won** the trial": *won* needs its subject (lawyer), object (trial), modifier (tall) and the earlier action (argued). A single softmax must share one unit of weight among them. With multiple heads, each head has its own W_Q, W_K, W_V. You run attention per head, concatenate, then apply W_O. GPT-2 small uses 12 heads × 64 = 768.

Real GPT-2 heads (layer 5, `img/gpt2_heads.png`) look clearly different from one another: first-token, previous-token and diffuse patterns.

| Model | Heads | d_model |
|---|---|---|
| Transformer base (2017) | 8 | 512 |
| GPT-2 small | 12 | 768 |
| GPT-3 175B | 96 | 12,288 |
| Llama 3.1 405B | 128 (8 KV heads, GQA) | 16,384 |

*(Head counts come from the papers and model cards. The book's table lists GPT-2, GPT-3, Mistral Large, DeepSeek V3 and Llama 3 405B.)*

## 6. Self vs cross attention, masking, cost
- **Self:** used in GPT, BERT and single-document encoders. **Cross:** used in translation, captioning, QA and text-to-image. **Encoder–decoder** models use both.
- **Causal mask (GPT):** position i only sees positions ≤ i. Future scores are set to −∞ before the softmax.
- **Cost:** n² scores. 1,000 tokens → 10⁶ scores, and doubling the length means 4× the work. This is why context windows are limited.

## 7. The 2017 revolution
*Attention Is All You Need* (Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin): no recurrence, 6 encoder + 6 decoder layers, positional encodings. It reached 28.4 BLEU on WMT'14 En→De, more than 2 BLEU above the previous best.

> ⚠️ **Errata.** The book says "training took 12 hours instead of days". In the paper (§5.2), **12 h on 8 P100s is the base model**. The **big** model, which produced the 28.4 BLEU, trained for **3.5 days**. Its cost was still a small fraction of earlier state-of-the-art models.

Timeline: 2018 GPT-1 and BERT · 2019 GPT-2 · 2020 GPT-3 · 2022 ChatGPT · 2023+ rapid scaling.

## 8. Inside real GPT-2 (my experiments)
Setup: `transformers` GPT-2 small with `attn_implementation="eager"` and `output_attentions=True`.
- **"The cat sat on the mat"**, row *sat* averaged over layers 5–8 and all heads: The **0.78**, cat **0.14**, sat 0.08, and on/the/mat **0**, because they are masked as future tokens.
- **Attention sink:** many heads park most of their weight on token 0. It acts as a learned "no-op" because softmax weights must sum to 1.
- **Pronoun exercise in a causal model:** for "…cake in the freezer because **it** was warm/cold", attention *from "it"* is **identical** in both sentences (cake 0.040, freezer 0.054), because "warm" and "cold" come after "it". The book's pronoun exercises (and its illustrative sat→mat weight) assume a **bidirectional** view, so use BERT in BertViz to see the flip.
- "The cat chased the mouse because it was hungry": from *it*, cat 0.037 and mouse 0.056 (again before the adjective appears).

### Minimal attention (my own code)
```python
import torch
torch.manual_seed(0)
x  = torch.randn(6, 8)
Wq, Wk, Wv = (torch.randn(8, 8) / 8**0.5 for _ in range(3))
Q, K, V = x @ Wq, x @ Wk, x @ Wv
scores  = Q @ K.T / 8**0.5
mask    = torch.triu(torch.ones(6, 6), 1).bool()
weights = torch.softmax(scores.masked_fill(mask, float("-inf")), dim=-1)
out     = weights @ V          # (6, 8); each row of weights sums to 1
```

## 9. Exercises
- **Ex 0** ("The chef who prepared the meal forgot the salt"): forgot→chef and salt; prepared→chef and meal.
- **Ex 1:** cake/freezer, warm/cold (see §8 for the causal-model caveat).
- **Ex 2:** won→lawyer, argued→case, who→lawyer.
- **Ex 3:** does *stood* reach back to *cat* across the long clause?
- Look for syntax heads, previous-token heads, long-range heads, and differences between early and late layers. Tools: BertViz, Hugging Face Spaces.

## 10. Checkpoint (my answers)
1. **hungry** → *it* = cat; **scared** → *it* = mouse. The deciding word comes *after* "it", so a bidirectional reader is needed.
2. **Heads:** jumped→fox (subject), quick→fox (adjective→noun), dog→lazy (modifier) or →over.
3. **Reflection:** attention gives direct access to any word. Many heads give many relationship types at once. **Uniform** weights reduce to plain averaging, which is Chapter 2's problem.

## 11. Key takeaways
1. An RNN's fixed state along a chain makes long-range information fade.
2. Attention connects every pair of words directly.
3. Q, K and V are what I seek, what I offer and what I hand over.
4. softmax(QKᵀ/√d)·V
5. Multi-head attention captures many relationships in parallel.
6. Self vs cross attention; GPT uses a causal mask; the cost is n².
7. The 2017 Transformer removed recurrence.

## 12. Review questions (my answers)
1. **RNN problem:** the fixed-size state is rewritten every step (sticky note), so early words fade, and training is sequential.
2. **Cocktail party:** soft, relevance-based focus. Others are dimmed, not removed.
3. **Q, K, V:** search question, spine label, book contents.
4. **Steps:** scores = QKᵀ → softmax(scores/√d) → weighted sum of V.
5. **√d:** dot products grow like √d. Large scores make softmax one-hot, which kills gradients. Scaling keeps the variance ≈ 1.
6. **Many heads:** each learns a different relation, and one softmax can't focus on all of them.
7. **Self vs cross:** self takes Q, K, V from one sequence (GPT). Cross takes Q from one and K, V from another (translation, captioning).
8. **2017:** removed recurrence, giving parallel training, better BLEU and direct long-range links. It is the basis of all modern LLMs.

## 13. Notes on the book (verification)
| Item | Status |
|---|---|
| Softmax example | ✅ correct |
| Q-entry example (= 3) | ✅ correct |
| "12 hours instead of days" | ⚠️ 12 h = base model; the 28.4-BLEU big model took 3.5 days (paper §5.2) |
| RNN forgetting = vanishing gradients | ⚠️ imprecise (forward bottleneck vs backward gradient decay) |
| sat→mat weight; pronoun exercises | ℹ️ illustrative, and assume bidirectional attention; GPT is causal |

---
**Credits.** Based on *Build Your First LLM* by Hasan Degismez. Please buy the book: <https://leanpub.com/FirstLLM/>. Code: <https://github.com/FirstLLM/code> (MIT). GPT-2 weights: OpenAI via Hugging Face. Notes, diagrams and code are my own adaptation (Waqar Shaikh Builds).
