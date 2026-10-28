# Errata — "Build Your First LLM" (Hasan Degismez, 2025)

Mistakes I found while verifying the book's text against running code (PyTorch 2.x, CPU; FirstLLM/code at commit d77f832). Each item is also flagged on the relevant slide and in the chapter notes. Please check the latest edition of the book — some may already be fixed.

| Ch | Location | Book says | Actually | How verified |
|---|---|---|---|---|
| 10 | §10.6.4 LayerNorm snippet | `nn.LayerNorm(d_model=768)` | Raises `TypeError` (parameter is `normalized_shape`); use `nn.LayerNorm(768)` | ran it |
| 10 | §10.1.3 / §10.9.2 pipeline | token IDs `[464, 3797, 3332, 319, 262, 21547]` for "The cat sat on the mat" | " mat" is **2603** in GPT-2 → `[464, 3797, 3332, 319, 262, 2603]` | GPT-2 tokenizer, notebook cell 30 |
