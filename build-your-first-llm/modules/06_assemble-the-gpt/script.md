# M06 — Assemble the GPT: Blocks, LayerNorm, and Loading Real Weights

Target length: **18 min** · Segments: 7
Big idea: *A transformer block is a two-step study routine repeated 12 times: discuss with classmates (attention), then think alone (feed-forward) — with notes kept in the margin (residual) and a calm-down breath before each step (LayerNorm).*

## S1 · CAM · Hook (≈40s)
- Last module we built attention. Alone it's not a language model.
- Today we add four small parts and get the exact architecture of GPT-2.
- Then the fun bit: we pour OpenAI's real GPT-2 weights into OUR code — and make it talk.
- And I'll show you a tiny bug that turns it into a babbling mess.

## S2 · SLIDES · The block: discuss, then think (≈3 min)
- Slide: block diagram.
- Step one, discuss: LayerNorm, then attention. Tokens share information.
- Step two, think alone: LayerNorm, then a feed-forward network — two linear layers with GELU in the middle. It widens to 4× — 3072 — then narrows back to 768.
- Residuals: the input skips around each step and is added back. Like writing notes in the margin instead of erasing the page. It also gives gradients a highway during training.
- GPT-2 puts LayerNorm before each step — "pre-norm". More stable for deep stacks.

## S3 · SLIDES · LayerNorm and GELU, quickly (≈2 min)
- LayerNorm: for each token, subtract its mean, divide by its spread, then scale and shift with learned numbers.
- Worked example: 102.5, 98.3, 105.7, 95.2. Mean 100.425. After normalising: about 0.52, −0.53, 1.32, −1.31. It sums to zero — a quick sanity check whenever you see a LayerNorm example.
- GELU: a smooth version of "keep positives, zero negatives". GPT-2 uses the tanh approximation.
- Note: Llama-style models swap this for SwiGLU, a gated variant. Same slot, different flavour.

## S4 · IDE · Build the model (≈4 min)
- Snippet 01: Block and GPT classes. Reuse our attention from Module 5.
- GPT = token embedding + position embedding, 12 blocks, final LayerNorm, and lm_head — a linear layer back to 50257 scores.
- Weight tying: lm_head shares its matrix with the token embedding. Saves 38 million parameters.
- Note: both names still appear in state_dict — they just point at the same storage.
- Initialisation: we set every weight to small random numbers, standard deviation 0.02, like GPT-2. PyTorch's default embedding init is much bigger, and with weight tying your first loss would be around 80 instead of 4. I hit this myself.
- Count parameters: 124,439,808 with tying and attention biases — this matches Hugging Face's GPT-2 exactly.

## S5 · IDE · Load GPT-2 weights and generate (≈4 min)
- Snippet 02. Download GPT-2 from Hugging Face and copy tensors into our model by name.
- One gotcha: Hugging Face stores those linear weights transposed — it uses a Conv1D class. We transpose four of them.
- Compare logits with Hugging Face: max difference around 1e-4 or smaller. Our code IS GPT-2.
- Generate: "The quick brown fox" … and it continues sensibly.
- Now the bug demo: set bias=False on attention, as some tutorials do. The biases get silently skipped, and the output turns into "foxeseseses". One flag, total collapse. Always compare against a reference.

## S6 · SLIDES · What scales (≈1.5 min)
- Table: GPT-2 small, medium, large, XL — layers, width, heads.
- Same code, bigger numbers. That's the scaling story in one slide.

## S7 · CAM · Recap (≈40s)
- Block = norm → attention → add, norm → MLP → add.
- Twelve blocks plus embeddings plus a head = GPT-2.
- Verified against the real thing.
- Next: we train our own small one from scratch.
