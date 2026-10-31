# M10 — Live-coding plan
Folder `m10/`: copy `gpt_model.py` and `tiny_gpt.pt` from m07.

| Step | Do | Type live | Point at |
|---|---|---|---|
| 1 | run 01_kv_cache_timing.py | `use_cache=cache` | the two timings |
| 2 | run 02_quantize.py | `quantize_dynamic(...)` | MB sizes, tiny diff |
| 3 | run 03 as serve.py (Run window) | `n = min(..., 500)` | "serving on…" |
| 4 | IntelliJ Terminal (Alt+F12): the curl line in the header comment | — | JSON response |
Windows note: in PowerShell use `curl.exe` and single-quote the JSON: `curl.exe -X POST localhost:8000/generate -d '{"prompt":"Holmes","n":120}'`.

Note: PyTorch 2.9+ prints a deprecation warning for `torch.ao.quantization` (moving to `torchao`). It still works; mention it on camera or filter it with `-W ignore`.
