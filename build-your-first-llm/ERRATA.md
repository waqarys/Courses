# Errata — "Build Your First LLM" (Hasan Degismez, 2025)

Mistakes I found while verifying the book's text against running code (PyTorch 2.x, CPU; FirstLLM/code at commit d77f832). Each item is also flagged on the relevant slide and in the chapter notes. Please check the latest edition of the book — some may already be fixed.

| Ch | Location | Book says | Actually | How verified |
|---|---|---|---|---|
| 10 | §10.6.4 LayerNorm snippet | `nn.LayerNorm(d_model=768)` | Raises `TypeError` (parameter is `normalized_shape`); use `nn.LayerNorm(768)` | ran it |
| 10 | §10.1.3 / §10.9.2 pipeline | token IDs `[464, 3797, 3332, 319, 262, 21547]` for "The cat sat on the mat" | " mat" is **2603** in GPT-2 → `[464, 3797, 3332, 319, 262, 2603]` | GPT-2 tokenizer, notebook cell 30 |
| 3 | §3.7.2 "Why It Was Revolutionary" | 2-BLEU gain and "training took 12 hours instead of days" | 12 h (8 P100s) is the **base** model; the 28.4-BLEU **big** model trained **3.5 days** (Vaswani et al. 2017, §5.2) | paper |
| 3 | §3.1.1 Sequential bottleneck | RNN forgetting "is called the vanishing gradient problem" | Imprecise: forward forgetting = fixed-size state bottleneck; vanishing gradients = backward training-signal decay | conceptual |
| 4 | §4.4.2 LayerNorm example | `[102.5, 98.3, 105.7, 95.2]` → `[0.52, -0.31, 1.12, -0.78]` | → **`[0.52, -0.53, 1.32, -1.31]`** (book's output doesn't sum to 0) | `F.layer_norm` |
| 4 | §4.2.5 GELU note | "Most modern LLMs (GPT, Claude, LLaMA) use GELU or close variants" | LLaMA uses **SwiGLU** (gated FFN with SiLU); Claude's architecture is unpublished | model papers |
| 4 | §4.1.7 RoPE | "LLaMA, Mistral, and GPT-4 often use RoPE" | GPT-4's architecture is **not published** | — |
| 5 | §5.4.1 Variables | `print(len(output))  # 68` | **71** (60 letters + 11 spaces); the book's own notebook prints 71 | ran notebook |
| 6 | §6.12 Gotchas (embeddings) | "GPT-2 uses learned position embeddings; BERT uses sinusoidal (fixed)" | BERT uses **learned** absolute position embeddings (512×768); sinusoidal = 2017 Transformer | BERT config/paper |
| ch07 | §7.11 worked example | Printed split shows Train 1 / Val 1 / Test 1 | The code shown (seed, 80/10/10 on 3 docs) yields 1 / 0 / 2; notebook confirms |
| ch07 | String length example | `len('The bird flew over the house.')` given as 33 | It is 29 |
| ch07 | SHA-1 collision odds | "1 in 2^160" | Birthday bound ≈2^80 for any collision; SHA-1 is practically broken (fine for dedup, not security) |
