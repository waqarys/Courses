# M06 — Live-coding plan
Prep: save snippet 01 as `m06/gpt_model.py`, snippet 02 as `m06/load_gpt2.py`. Run 02 once off-camera to download weights (~550 MB).

| Step | Do | Type live | Point at |
|---|---|---|---|
| 1 | paste `gpt_model.py`, scroll Block | the two residual lines in `Block.forward` | "discuss, think" |
| 2 | run it | — | `params: 124,439,808`, `both keys...: True` |
| 3 | run `load_gpt2.py` | — | diff ~1e-4, sensible continuation |
| 4 | Run config → program args `--no-bias`, run | — | big diff, degenerate text |
| 5 | Back on camera: "always compare with a reference" | | |
