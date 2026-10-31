# M05 · snippet 01 — single-head attention with small, checkable numbers
import torch

torch.manual_seed(0)
x = torch.randn(3, 4)                      # 3 tokens, 4 dims each
Wq, Wk, Wv = (torch.randn(4, 4) * 0.5 for _ in range(3))

Q, K, V = x @ Wq, x @ Wk, x @ Wv
scores = Q @ K.T / K.shape[-1] ** 0.5      # (3,3): every token vs every token
weights = scores.softmax(dim=-1)           # rows sum to 1
out = weights @ V                          # (3,4): informed tokens
print("weights:\n", weights.round(decimals=3))
print("row sums:", weights.sum(-1))
print("out shape:", out.shape)
