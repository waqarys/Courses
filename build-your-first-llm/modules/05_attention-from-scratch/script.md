# M05 — Attention from Scratch: How Words Look at Each Other

Target length: **18 min** · Segments: 7
Big idea: *Attention is a group chat where every word posts a question (query), wears a name-tag (key) and carries a message (value). Each word reads the messages of the words whose name-tags best match its question.*

## S1 · CAM · Hook (≈45s)
- "The trophy didn't fit in the suitcase because it was too big." What is "it"?
- You know instantly: the trophy. Change "big" to "small" — now "it" is the suitcase.
- To understand one word, you have to look at the others. That's attention.
- Today we build it with plain matrix maths, then the masked, multi-head version GPT uses.

## S2 · SLIDES · Why older models struggled (≈2 min)
- Before 2017, the go-to was the recurrent network: read one word at a time, keep a running summary.
- Problem one — the bottleneck. Everything you've read is squashed into one fixed-size summary. Long sentences overflow it.
- Problem two — a separate one during training: the learning signal fades as it travels back through many steps. That's the vanishing gradient. Two different problems, often mixed up.
- Problem three — it's sequential, so it can't use a GPU's parallel power.
- Attention fixes all three: every word looks directly at every other word, all at once.

## S3 · SLIDES · The group chat analogy: Q, K, V (≈3 min)
- Slide: each word makes three vectors from its embedding, using three learned matrices.
- Query: "what am I looking for?" — "it" is looking for a noun that could be big.
- Key: "what do I offer?" — trophy's name-tag says "object, can be big".
- Value: the actual message to pass on.
- Score = query dot key. Big dot product = good match.
- Divide by the square root of the key size — keeps scores from getting so large that softmax becomes all-or-nothing.
- Softmax turns scores into percentages that add to 100.
- Output = weighted average of values.
- One formula: softmax of Q K-transpose over root d, times V.

## S4 · IDE · Attention with numbers you can check (≈3.5 min)
- Snippet 01. Three tokens, 4-dimensional, small random weights.
- Compute Q, K, V. Print shapes — 3 by 4 each.
- Scores: 3 by 3 — every token against every token.
- Softmax row-wise. Each row sums to one. Print it.
- Output: 3 by 4 — same shape as input, but now each row is "informed" by the others.
- Snippet 02: the causal mask. A writer can't peek at words not written yet.
- We fill the upper triangle with minus infinity before softmax — those become exactly zero.
- Row one only sees itself. Row three sees everything before it.

## S5 · IDE · Multi-head attention as a module (≈4 min)
- One head = one kind of question. Grammar, coreference, topic — different heads specialise.
- Snippet 03: MultiHeadAttention class. One big linear layer makes Q, K and V together — that's what GPT-2 calls c_attn.
- Split 768 into 12 heads of 64. Attend in each head in parallel. Glue back. Project with c_proj.
- Keep the biases on these layers — GPT-2 has them, and in Module 6 we'll see what breaks if you drop them.
- Run: input batch 2 × 5 × 32, output same shape. Check.
- Bonus: compare with PyTorch's built-in scaled_dot_product_attention — the numbers match.

## S6 · SLIDES · Cost and context (≈1.5 min)
- Scores are n by n. Double the context, four times the work. That's why context windows are expensive.
- Tricks you'll hear about: FlashAttention (same maths, smarter memory use), KV cache for generation — Module 10.

## S7 · CAM · Recap (≈40s)
- Query, key, value. Dot, scale, softmax, mix.
- Mask the future. Split into heads.
- Next: we wrap attention with a few more parts and get the full GPT block.
