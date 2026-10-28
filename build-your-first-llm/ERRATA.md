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
| ch17 | §17.3.1 llm_service.py | Qwen2.5-1.5B-Instruct on `gpu="T4"` with vLLM 0.6.4 | T4 (cc 7.5) has no bfloat16; vLLM 0.6.x refuses bf16 models on it (vllm issue #9990). Add `dtype="half"` or use L4/A10 |
| ch17 | §17.5.4 API key | `x_api_key: str = Header()`, check skipped if no API_KEY | Header is required: missing header → 422 even with no key configured (tested). Use `Header(default=None)` |
| ch17 | §17.1.2 free tier | "you will get an email warning before any charges" | Modal pricing: Starter usage beyond the $30 included is pay-as-you-go; set a workspace budget to cap spend |
| ch18 | §18.3.1 Path 1 | "build on: Chapter 6 (training and evaluation)" | Ch 6 is NumPy & PyTorch; training is Ch 12, evaluation is in Ch 15 |
| ch18 | §18.3.2, §18.4.1 (+ notebook cell 8/14) | RAG = "Chapter 14" | Ch 14 is Prompt Engineering; RAG and tool use are both Ch 15 (Building Applications) |
| ch18 | §18.4.2 Capstone 2 | "Revisit … Ch6 (evaluation)" | Evaluation material is Ch 15 (and Ch 12 for val loss/perplexity) |
| ch18 | §18.2.1 | "In Chapter 17, you set up audit trails" | Ch 17 has no audit-trail section; JSONL logging is Ch 16 |
| ch12 | §12.4.5 train_epoch / §12.5.1 evaluate | `ignore_index=0  # Ignore padding (token ID 0)` | GPT-2 token 0 is "!" (0.62% of tokens); pad = eos = 50256 is *not* ignored (22% of target positions in padded batches, my count). Mask with `attention_mask` → -100 |
| ch12 | §12.2.3 create_lm_labels | default `pad_token_id=0` | Same issue: GPT-2 has no id-0 pad; use `tokenizer.pad_token_id` (50256 here) |
| ch12 | §12.3.4 / §12.7 output | "312 batches" per epoch | Notebook (256-char chunks): 3,921 train chunks → 123 batches/epoch, 369 steps total |
| ch12 | §12.7 output | "Parameters: 10,789,121" | 16,054,016 with the chapter's config (embed 256, 4 layers, vocab 50,257) |
| ch12 | §12.7 output | Val 4.22 → 3.89 → 3.75, perplexity 42.3 | My unchanged CPU run: val 6.22 → 5.66 → 5.51, perplexity 504.9 → 287.1 → 246.2 |
| ch12 | §12.8.3 output | "The king is a man of great virtue and honour…" | Actual 3-epoch output: "The king'd / proto imports, theolute. / Buteb: …" (play-shaped, not sentences) |
| ch17 | §17.3.3, §17.5.4 | "same pattern as Chapter 16's environment variables" / "API Keys: Use the pattern from Chapter 16" | Ch 16 covers no environment variables, .env files or API keys |
| ch16 | §16.7 complete app.py | `SUSPICIOUS_PATTERNS = [..., r"act as"]` | No word boundary: "In fact as a beginner, how do I learn Python?" → 400 Invalid input (tested). Use `r"\bact as\b"` |
| ch16 | §16.5.1 | `MAX_PROMPT_LENGTH = 4000  # Maximum prompt length (tokens, roughly)` | The check is `len(text)` → characters, as the error message itself says |
| ch16 | §16.3.3, §16.6.4 | Kubernetes restarts "more on this in Chapter 17"; canary "infrastructure we build in Chapter 17" | Ch 17 covers neither (Modal deploy is a rolling update) |
| ch13 | §13.2.2 / notebook | "80 examples for training and 20 for evaluation" | Notebook `FAQ_DATA` has 69 examples; `train_data = FAQ_DATA[:80]` takes all 69 → test set empty → ZeroDivisionError (cell 27), NameError (cell 28) |
| ch13 | §13.4.4–13.4.5 LoRA naming | B is the (in, r) "down" matrix (random init), A the (r, out) "up" matrix (zeros) | Reversed vs the LoRA paper / PEFT: A is the down projection (random), B the up projection (zeros). Maths still works, but names won't match PEFT checkpoints |
| ch13 | §13.4.4 / §13.7 "48× efficiency" | 768×768 layer: 12,288 vs 589,824 | True only for a hypothetical 768×768 layer. MiniGPT's `qkv_proj` is 256→768: 196,608 vs 8,192 = 24× (notebook demo on 256×256: 65,536 vs 4,096 = 16×) |
| ch13 | §13.4.7 output | "Trainable: 24,576 / 10,789,121 (0.23%)" | Notebook: 32,768 / 16,086,784 (0.20%): 4 layers × (256×8 + 8×768) |
| ch13 | §13.4.7 | LoRA on combined `qkv_proj` "primarily affects Q and V" | A LoRA on the fused projection adapts Q, K and V alike; targeting only Q and V needs separate layers or a sliced update |
| ch13 | §13.5.2–13.5.3 | `model.generate(input_ids, max_new_tokens=50, do_sample=False)` | MiniGPT has no `.generate()` with these kwargs; the notebook needs its own greedy loop |
| ch13 | §13.6.1 output | LoRA 0.10 MB vs full 41.2 MB, "400× smaller" | Notebook: 131.6 KB vs 61.4 MB (478×) |
| ch13 | §13.11 checkpoint | "Exact match accuracy improves from ~0% to 50%+" | Notebook base is randomly initialised (no Ch 12 weights loaded): loss 10.86 → 10.74, outputs gibberish before and after |
