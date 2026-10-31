# M06 · snippet 01 — the full GPT-2 architecture in ~60 lines
import math, torch
from torch import nn
import torch.nn.functional as F
from dataclasses import dataclass

@dataclass
class GPTConfig:
    vocab_size: int = 50257
    max_len: int = 1024
    d_model: int = 768
    n_layers: int = 12
    n_heads: int = 12
    attn_bias: bool = True          # GPT-2 HAS attention biases. False => broken loading.

class MultiHeadAttention(nn.Module):           # same as M05 snippet 03
    def __init__(self, c):
        super().__init__()
        self.h, self.dh = c.n_heads, c.d_model // c.n_heads
        self.c_attn = nn.Linear(c.d_model, 3 * c.d_model, bias=c.attn_bias)
        self.c_proj = nn.Linear(c.d_model, c.d_model, bias=c.attn_bias)
    def forward(self, x):
        B, T, C = x.shape
        q, k, v = (t.view(B, T, self.h, self.dh).transpose(1, 2) for t in self.c_attn(x).split(C, 2))
        y = F.scaled_dot_product_attention(q, k, v, is_causal=True)
        return self.c_proj(y.transpose(1, 2).reshape(B, T, C))

class MLP(nn.Module):                          # "think alone": widen 4x, GELU, narrow
    def __init__(self, c):
        super().__init__()
        self.c_fc = nn.Linear(c.d_model, 4 * c.d_model)
        self.c_proj = nn.Linear(4 * c.d_model, c.d_model)
    def forward(self, x):
        return self.c_proj(F.gelu(self.c_fc(x), approximate="tanh"))   # GPT-2 uses tanh GELU

class Block(nn.Module):
    def __init__(self, c):
        super().__init__()
        self.ln_1, self.attn = nn.LayerNorm(c.d_model), MultiHeadAttention(c)
        self.ln_2, self.mlp = nn.LayerNorm(c.d_model), MLP(c)
    def forward(self, x):
        x = x + self.attn(self.ln_1(x))        # discuss (pre-norm + residual)
        return x + self.mlp(self.ln_2(x))      # think alone

class GPT(nn.Module):
    def __init__(self, c: GPTConfig):
        super().__init__()
        self.c = c
        self.wte = nn.Embedding(c.vocab_size, c.d_model)
        self.wpe = nn.Embedding(c.max_len, c.d_model)
        self.h = nn.ModuleList(Block(c) for _ in range(c.n_layers))
        self.ln_f = nn.LayerNorm(c.d_model)
        self.lm_head = nn.Linear(c.d_model, c.vocab_size, bias=False)
        self.lm_head.weight = self.wte.weight  # weight tying
        self.apply(self._init)                 # GPT-2 init: small weights => sane starting loss
    @staticmethod
    def _init(m):
        if isinstance(m, (nn.Linear, nn.Embedding)):
            nn.init.normal_(m.weight, mean=0.0, std=0.02)   # PyTorch's default Embedding init is std=1 -> loss ~80!
        if isinstance(m, nn.Linear) and m.bias is not None:
            nn.init.zeros_(m.bias)
    def forward(self, idx, targets=None):
        T = idx.shape[1]
        x = self.wte(idx) + self.wpe(torch.arange(T, device=idx.device))
        for b in self.h:
            x = b(x)
        logits = self.lm_head(self.ln_f(x))
        loss = None if targets is None else F.cross_entropy(logits.flatten(0, 1), targets.flatten())
        return logits, loss
    @torch.no_grad()
    def generate(self, idx, n_new, temperature=1.0, top_k=None):
        for _ in range(n_new):
            logits = self(idx[:, -self.c.max_len:])[0][:, -1] / max(temperature, 1e-6)
            if top_k:
                v, _ = logits.topk(top_k)
                logits[logits < v[:, [-1]]] = -float("inf")
            idx = torch.cat([idx, torch.multinomial(logits.softmax(-1), 1)], dim=1)
        return idx

if __name__ == "__main__":
    m = GPT(GPTConfig())
    print(f"params: {sum(p.numel() for p in m.parameters()):,}")   # 124,439,808 (tied, with biases)
    print("both keys in state_dict:", {"wte.weight", "lm_head.weight"} <= set(m.state_dict()))
