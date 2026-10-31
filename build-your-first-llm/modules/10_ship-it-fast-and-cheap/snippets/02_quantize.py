# M10 · snippet 02 — dynamic int8 quantisation of Linear layers (CPU)
import os, torch
from torch.ao.quantization import quantize_dynamic

# GPT-2 (HF) uses Conv1D, which quantize_dynamic skips, so we demo on a GPT-2-sized MLP block
mlp = torch.nn.Sequential(torch.nn.Linear(768, 3072), torch.nn.GELU(), torch.nn.Linear(3072, 768)).eval()
q = quantize_dynamic(mlp, {torch.nn.Linear}, dtype=torch.qint8)
torch.save(mlp.state_dict(), "fp32.pt"); torch.save(q.state_dict(), "int8.pt")
x = torch.randn(4, 768)
print(f"fp32 {os.path.getsize('fp32.pt')/1e6:.1f} MB  int8 {os.path.getsize('int8.pt')/1e6:.1f} MB")
print("max abs diff:", (mlp(x) - q(x)).abs().max().item())
