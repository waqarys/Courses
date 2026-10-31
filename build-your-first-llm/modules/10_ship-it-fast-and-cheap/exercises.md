# M10 — Exercises (with solutions)

**1. KV cache size.** GPT-2 small, 1024 tokens, fp16: cache size per sequence? (2 tensors × layers × tokens × d_model × 2 bytes)
<details><summary>Solution</summary>2·12·1024·768·2 = 37.7 MB.</details>

**2. Memory.** A 7 B-parameter model in fp16 vs 4-bit?
<details><summary>Solution</summary>~14 GB vs ~3.5 GB (+ small overhead for scales).</details>

**3. Harden the server.** Name three things snippet 03 lacks for production.
<details><summary>Solution</summary>Auth/rate limiting, request timeout & concurrency (threading/async), input validation & logging; also streaming responses.</details>

**4. Choose a deployment.** A school wants a private homework helper on 20 laptops with no internet. Option?
<details><summary>Solution</summary>Local: a small quantised GGUF model in Ollama or llama.cpp on each machine (or one LAN server).</details>

**5. Eval set.** Why rerun an eval set before swapping to a quantised model?
<details><summary>Solution</summary>Quantisation can degrade specific skills (maths, rare languages) silently; a fixed eval set catches regressions.</details>
