# M02 — Live-coding plan

Files under `m02/`. Use the course venv interpreter (PIPELINE.md §3).

| Step | Snippet | Type live | Point at | Expected |
|---|---|---|---|---|
| 1 | 01_python_basics.py | the `vocab = {...}` comprehension | `len(sentence)` | `... has 44 characters` |
| 2 | 02_tensors.py | `y = x @ W` | the printed shapes | `x @ W -> torch.Size([2, 4])` |
| 3 | 03_autograd.py | `loss.backward()` and `w.grad.zero_()` | w climbing to 4.0 | loss shrinks each step |
| 4 | 03 again, comment out `zero_()` and run | — | it overshoots/diverges | "that's why we zero grads" |
| 5 | 04_module.py | `self.layer1 = nn.Linear(...)` | params 58 | `params: 58` |
| 6 | In the Python Console, type `nn.LayerNorm(d_model=64)` | it | the TypeError | show the error on purpose |
