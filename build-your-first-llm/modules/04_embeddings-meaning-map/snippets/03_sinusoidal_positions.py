# M04 · snippet 03 — fixed sine-wave positions (2017 Transformer) for comparison
import math, torch

def sinusoidal(n_pos, d):
    pe = torch.zeros(n_pos, d)
    pos = torch.arange(n_pos).unsqueeze(1)
    div = torch.exp(torch.arange(0, d, 2) * (-math.log(10000.0) / d))
    pe[:, 0::2] = torch.sin(pos * div)   # fast "clock hands" in early dims
    pe[:, 1::2] = torch.cos(pos * div)   # slow ones in later dims
    return pe

pe = sinusoidal(6, 8)
print(pe.round(decimals=2))
