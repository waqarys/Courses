# M05 · snippet 03 — causal multi-head self-attention (GPT-2 layout: c_attn + c_proj, with biases)
import torch
from torch import nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_heads, max_len=1024):
        super().__init__()
        assert d_model % n_heads == 0
        self.h, self.dh = n_heads, d_model // n_heads
        self.c_attn = nn.Linear(d_model, 3 * d_model)   # Q,K,V in one go (bias=True like GPT-2)
        self.c_proj = nn.Linear(d_model, d_model)
        self.register_buffer("mask", torch.tril(torch.ones(max_len, max_len)).bool())

    def forward(self, x):
        B, T, C = x.shape
        q, k, v = self.c_attn(x).split(C, dim=2)
        q, k, v = (t.view(B, T, self.h, self.dh).transpose(1, 2) for t in (q, k, v))  # (B,h,T,dh)
        att = (q @ k.transpose(-2, -1)) / self.dh ** 0.5
        att = att.masked_fill(~self.mask[:T, :T], float("-inf")).softmax(-1)
        y = (att @ v).transpose(1, 2).contiguous().view(B, T, C)                    # glue heads
        return self.c_proj(y)

if __name__ == "__main__":
    torch.manual_seed(0)
    mha = MultiHeadAttention(d_model=32, n_heads=4)
    x = torch.randn(2, 5, 32)
    y = mha(x)
    print(y.shape)
    # same maths as PyTorch's fused kernel:
    q, k, v = (t.view(2, 5, 4, 8).transpose(1, 2) for t in mha.c_attn(x).split(32, dim=2))
    ref = F.scaled_dot_product_attention(q, k, v, is_causal=True).transpose(1, 2).reshape(2, 5, 32)
    print("matches SDPA:", torch.allclose(y, mha.c_proj(ref), atol=1e-6))
