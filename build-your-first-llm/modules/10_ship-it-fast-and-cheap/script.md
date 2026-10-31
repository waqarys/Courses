# M10 — Ship It: Fast, Small, and Online

Target length: **16 min** · Segments: 7
Big idea: *Serving an LLM is running a restaurant kitchen: prep ahead (KV cache), use smaller pans (quantisation), batch orders (batching), and choose between a food truck (local), a rented kitchen (cloud GPU), or ordering in (an API).*

## S1 · CAM · Hook (≈40s)
- A model that works in a notebook isn't a product.
- Users want answers in under a second, and you want a bill that doesn't make you cry.
- Today: the three speed tricks, a real web API around our tiny GPT, and how to choose where to deploy.

## S2 · SLIDES · Why generation is slow (≈2 min)
- Every new token reruns the model over the whole context. Naively, token 500 redoes the work of tokens 1 to 499.
- KV cache: keep each layer's keys and values from earlier tokens; only compute the new token's. Prep ahead.
- Cost: memory. The cache grows with context length × layers × width.

## S3 · IDE · See the KV cache speed-up (≈2 min)
- Snippet 01: GPT-2 generate 100 tokens with use_cache on, then off.
- Time both. On the test box it was about twice as fast for 100 tokens — and the gap grows with longer outputs. Same text out.

## S4 · SLIDES · Smaller pans: quantisation (≈2 min)
- Weights are usually 32-bit or 16-bit floats. Store them as 8-bit or 4-bit integers with a scale.
- 4× to 8× less memory, often little quality loss.
- Formats you'll meet: int8 dynamic for CPU, GPTQ / AWQ / GGUF for 4-bit — GGUF is what llama.cpp and Ollama run.
- Always measure quality after quantising — perplexity on a held-out set, plus a few eyeball prompts.

## S5 · IDE · Quantise + serve (≈4 min)
- Snippet 02: dynamic int8 quantisation of the Linear layers. Compare size on disk and the output.
- Snippet 03: a tiny web API with Python's standard library — POST a prompt, get text back. It loads our Module 7 tiny_gpt.pt.
- Run it, then call it with curl from the IntelliJ terminal.
- For real products you'd use FastAPI or a serving engine like vLLM, Text Generation Inference, or Ollama — same shape: load once, handle requests, stream tokens.

## S6 · SLIDES · Where to deploy (≈2.5 min)
- Table: four options.
- Local / Ollama on your machine: free per request, private, limited by your hardware.
- Serverless or container on a cloud GPU: scales, pay per second, you manage the model.
- Managed API like Grok or others: zero ops, pay per token, least control.
- Edge or in-browser for tiny models: offline, but small.
- Production checklist: rate limits, timeouts, logging prompts responsibly, content filtering, cost alerts, and an eval set you rerun before every model change.

## S7 · CAM · Recap (≈40s)
- KV cache, quantisation, batching.
- Wrap in an API; choose local, cloud, or managed.
- Last module next: where LLMs are heading and your capstone project.
