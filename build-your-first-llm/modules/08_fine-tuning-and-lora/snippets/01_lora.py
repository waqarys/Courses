# M08 · snippet 01 — LoRA wrapper: frozen layer + trainable low-rank "sticky note" B·A
import torch
from torch import nn

class LoRA(nn.Module):
    def __init__(self, base, d_in, d_out, r=8, alpha=16):
        super().__init__()
        self.base = base
        for p in self.base.parameters():
            p.requires_grad = False                  # the textbook stays frozen
        self.A = nn.Parameter(torch.randn(d_in, r) * 0.01)
        self.B = nn.Parameter(torch.zeros(r, d_out)) # zero => starts identical to base
        self.scale = alpha / r
    def forward(self, x):
        return self.base(x) + (x @ self.A @ self.B) * self.scale

if __name__ == "__main__":
    base = nn.Linear(768, 2304)
    lora = LoRA(base, 768, 2304)
    x = torch.randn(2, 768)
    print("identical at start:", torch.allclose(base(x), lora(x)))
    print("trainable:", sum(p.numel() for p in lora.parameters() if p.requires_grad))  # 24,576
