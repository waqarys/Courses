# M07 · snippet 02 — train a tiny GPT on CPU (~10 min). Needs data.py + gpt_model.py (M06) in the same folder.
import math, time, torch
from data import get_batch, decode, chars
from gpt_model import GPT, GPTConfig

torch.manual_seed(1337)
cfg = GPTConfig(vocab_size=len(chars), max_len=128, d_model=128, n_layers=4, n_heads=4)
model = GPT(cfg)
print(f"params: {sum(p.numel() for p in model.parameters()):,}")

steps, warmup, lr_max = 2000, 100, 3e-3
opt = torch.optim.AdamW(model.parameters(), lr=lr_max, weight_decay=0.1)
def lr_at(s):                                   # warmup then cosine decay
    if s < warmup:
        return lr_max * (s + 1) / warmup
    p = (s - warmup) / (steps - warmup)
    return lr_max * (0.1 + 0.9 * 0.5 * (1 + math.cos(math.pi * p)))

@torch.no_grad()
def estimate(iters=20):
    model.eval()
    out = {s: torch.stack([model(*get_batch(s))[1] for _ in range(iters)]).mean().item() for s in ("train", "val")}
    model.train(); return out

print(f"initial loss ≈ {estimate(5)['train']:.2f} (expect ≈ ln({len(chars)}) = {math.log(len(chars)):.2f})")
t0 = time.time()
for step in range(steps + 1):
    for g in opt.param_groups:
        g["lr"] = lr_at(step)
    x, y = get_batch("train")
    _, loss = model(x, y)
    opt.zero_grad(set_to_none=True)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    opt.step()
    if step % 250 == 0:
        e = estimate()
        sample = decode(model.generate(torch.zeros((1, 1), dtype=torch.long), 120, 0.8)[0].tolist())
        print(f"\nstep {step} train {e['train']:.3f} val {e['val']:.3f} ({time.time()-t0:.0f}s)\n{sample}")
torch.save({"model": model.state_dict(), "cfg": cfg.__dict__, "chars": chars}, "tiny_gpt.pt")
print("saved tiny_gpt.pt")
