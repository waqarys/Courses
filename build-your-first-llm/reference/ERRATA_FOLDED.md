# How the errata are folded into the new modules

Full verified list (67 rows): [ERRATA.md](ERRATA.md). The new modules teach the *correct* version directly — viewers never need to know a mistake existed.

| Errata topic (book ch) | Taught correctly in |
|---|---|
| `nn.LayerNorm(d_model=…)` / `nn.Embedding(vocab_size=…)` TypeErrors (8, 10) | M02 gotchas + snippet 04; M02 ex. 3 |
| String-length and char/vocab counts (5, 7, 8) | M02 snippet 01 ("spaces count"); M03 snippets print real counts |
| Tiny-data split rounding (7) | M03 S2/S3 + ex. 1 |
| SHA-1 collision odds (7) | M03 S2 ("fingerprint, not security") |
| Token IDs (` mat`=2603, ` cat`=3797 vs `cat`=9246, ` dog`=3290) (9, 10) | M03 snippet 04 + ex. 5; M04 S1 |
| BPE token-count examples, emoji counts (8) | M03 snippet 04 prints real counts |
| `king`/`queen` neighbours need the leading space (9) | M04 S4 + snippet 02 |
| BERT position embeddings are learned; modern open LLMs use RoPE (6, 9) | M02 gotcha 5; M04 S5 table |
| Bottleneck vs vanishing gradient (3) | M05 S2 + ex. 4 |
| Transformer base vs big training time (3) | not stated in the course (avoids the claim) |
| LayerNorm worked example `[0.52, -0.53, 1.32, -1.31]` (4) | M06 S3 + slide |
| LLaMA uses SwiGLU, GPT-4/Claude architectures unpublished (4) | M06 S3; course never claims unpublished details |
| MiniGPT `bias=False` → broken GPT-2 load; tanh GELU; 124,439,808 params (11) | M06 S4/S5, snippets 01–02 (diff 4e-4 with biases vs 46 without) |
| Weight-tying keys both in `state_dict` (11) | M06 S4 + ex. 3 |
| Training/fine-tune/prod chapters (12–17) numeric claims | M07–M10 only quote numbers measured by the snippets |

New finding during the refactor (not in the book list): with weight tying and PyTorch's default `nn.Embedding` init (std 1) the first loss is ~84 instead of ln V; GPT-2's std 0.02 init fixes it (M06 snippet 01, M07 S2).
