# M02 · snippet 03 — autograd: which way should w move?
import torch

w = torch.tensor(2.0, requires_grad=True)
x, target = torch.tensor(3.0), torch.tensor(12.0)

for step in range(5):
    pred = w * x
    loss = (pred - target) ** 2          # how wrong are we?
    loss.backward()                      # fills w.grad
    with torch.no_grad():
        w -= 0.05 * w.grad               # nudge downhill
    w.grad.zero_()                       # gradients accumulate otherwise!
    print(f"step {step}: w={w.item():.3f} loss={loss.item():.3f}")
