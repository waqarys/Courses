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
| ch08 | §8.2.4 char tradeoff | "Tokenization is the first step…" = 54 chars, vocab 24 | 53 chars, vocab 22 (notebook) |
| ch08 | §8.3.4 word vocab | `'mat.':5, 'on':6 … 'dog':9` | `'on':5, 'mat.':6 … 'was':9` — Counter ties go to first appearance (notebook) |
| ch08 | §8.3.6 coverage | Vocab 10 → 3/5 unknown (40%) | 1/5 unknown (80%) |
| ch08 | §8.3.7 comparison | char vocab 20, length 44; word vocab 13 | char vocab 28, length 43; word vocab 12 (notebook) |
| ch08 | §8.4 "tokenization" | 13 characters (in 8.2) | 12 characters (book's own table says 12) |
| ch08 | §8.5.5 Shakespeare BPE | 12 tokens, `question` whole, round trip True | 14 tokens (`que`,`st`,`ion`), decoded `'… be , that … que st ion .'`, round trip **False** (no decoder with Whitespace pre-tokenizer) |
| ch08 | §8.5.5 modern text | "ChatGPT generates amazing responses" → 14 tokens | 18 tokens |
| ch08 | §8.5.6 vocab order | IDs 4+ are most-frequent chars (e, t, o, a…) | Base alphabet is sorted (`!`, `$`, …, `A`…, `a`…); only merges are in learned order |
| ch08 | §8.5.8 cl100k counts | Hamlet line 11 tokens; backprop sentence 8 (`propagation` whole) | 12; 9 (`back`,`prop`,`agation`) |
| ch08 | §8.6.2 prompt counts | 6 / 14 / 9 tokens | 7 / 15 / 10 (notebook) |
| ch08 | §8.7.3 emoji | 😀🚀👍 1 token each; 🔥🔥🔥 3; "Hello 😀 world" 4 | 2 / 3 / 3; 9; 3 (notebook) |
| ch08 | §8.8 embedding | `nn.Embedding(vocab_size=…, embedding_dim=…)` | TypeError — parameter is `num_embeddings` |
| ch09 | §9.1.1 example IDs | dog 4273, kitten 28387 | ` dog`=3290, ` kitten`=42143 (4273=` pet`, 28387=` WC`); 3797 is ` cat` with space (`cat`=9246) |
| ch09 | §9.2.3 batch example | "I will help you" = [314, 588, 4695, 345] | Those IDs decode to " I like animals you"; "I will help you" = [40, 481, 1037, 345] |
| ch09 | §9.4.3 pipeline | "mat" = 21547 | 2603 (notebook) |
| ch09 | §9.5.2 similarity output | king → King, prince, Queen, kingdom…; happy → glad, pleased… | Notebook code gives king → 'ked','KING','kers'… because `encode("king")` is the no-space word-piece; with ' king' → kings, King, queen, prince, monarch |
| ch09 | §9.5 analogy | king − man + woman ≈ queen (implied) | Notebook returns 'ked'; with space-prefixed tokens ' queen' is top (0.709) |
| ch09 | §9.3.2 positions | "modern LLMs like GPT-2 prefer learned embeddings" | Most current open LLMs (LLaMA, Mistral, Qwen) use RoPE |
| ch11 | §11.3.4 / notebook MiniGPT | Attention uses `bias=False`; loading GPT-2 "generates coherent text" | GPT-2's `c_attn`/`c_proj` biases are silently dropped → loaded model degenerates ("foxeseseses…", "to to to…"); max logit error 58. Adding the biases (and tanh GELU) matches HF to 6e-5 |
| ch11 | §11.4.2 param count | "Total parameters: 124,439,808" from this code | This code gives 124,402,944 (no attention biases); 124,439,808 is HF GPT-2. The formula estimate is 124,356,864, not 124,354,560 |
| ch11 | §11.6.4 generation | "The quick brown fox jumps over the lazy dog. The dog is…" | Notebook: "The quick brown foxeseseses…"; with fixed loader: "…foxes are a great way to get a little bit of a kick out of your dog." |
| ch11 | Weight-tying gotcha 4 | `lm_head.weight` shouldn't appear in `state_dict()` keys | It does appear (both keys, shared storage); `torch.save` stores the storage once |
| ch11 | §11.12 checkpoint | "Parameter count: ~150,000" | 132,608 with the book's config (133,120 with attention biases) |
