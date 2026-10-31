# M05 — Live-coding plan

| Step | Snippet | Type live | Point at |
|---|---|---|---|
| 1 | 01_attention_by_hand.py | `scores = Q @ K.T / ...` and `.softmax(dim=-1)` | row sums all 1.0 |
| 2 | 02_causal_mask.py | `torch.triu(..., diagonal=1)` | zeros in upper triangle |
| 3 | 03_multihead.py | the `.view(...).transpose(1, 2)` line, explained slowly | `torch.Size([2, 5, 32])` |
| 4 | same file | — | `matches SDPA: True` |
Tip: keep `03_multihead.py` — M06 imports it (`from m05.multihead import MultiHeadAttention`, or copy the class).
