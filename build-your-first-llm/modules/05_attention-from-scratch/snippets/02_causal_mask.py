# M05 · snippet 02 — causal mask: no peeking at future tokens
import torch

torch.manual_seed(0)
T = 4
scores = torch.randn(T, T)
mask = torch.triu(torch.ones(T, T, dtype=torch.bool), diagonal=1)   # above diagonal = future
weights = scores.masked_fill(mask, float("-inf")).softmax(dim=-1)
print(weights.round(decimals=2))           # upper triangle is exactly 0
