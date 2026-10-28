# Chapter 17 — Deployment Options (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch17.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch17.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
Chapter 16 gave us a production-style FastAPI app. This chapter puts an LLM behind a public HTTPS URL on a cloud GPU using Modal, with no Dockerfile and no server to manage.

**About the notebook:** it only prints the `.py` files to save (`hello.py`, `gpu_test.py`, `with_deps.py`, `simple_api.py`, `llm_service.py`). Deploying needs `modal setup` with your own account, and I didn't deploy anything from this course box. All 10 code cells ran on my CPU without errors.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Serverless | The platform runs, scales and bills machines per second |
| Container | A packaged OS + Python + libraries, created per function |
| Cold start | Boot + weights download + load to GPU on the first request |
| Volume | Persistent storage shared across container restarts |
| Secret | A named set of environment variables stored by Modal |
| `scaledown_window` | Idle seconds before a container stops |

## 1. Serverless economics (checked on modal.com/pricing, 28 Oct 2026)
- GPU list prices per second: T4 $0.000164 (≈$0.59/h), L4 $0.000222 (≈$0.80/h), A10 $0.000306 (≈$1.10/h), A100-40GB ≈$2.10/h, A100-80GB ≈$2.50/h, H100 ≈$3.95/h.
- The Starter plan includes $30/month of compute. That's ~50 T4-hours **only if the GPU were the sole cost**, because CPU and memory are billed too.
- Beyond $30, Starter is pay-as-you-go. Set a **workspace budget** if you want a hard cap. The book says you'll get an email warning before any charges, and the pricing page doesn't promise that.

## 2. Building up
1. `modal.App` + `@app.function()` + `.remote()` runs code in the cloud.
2. `gpu="T4"` attaches a GPU. Import heavy libraries *inside* the function.
3. `modal.Image.debian_slim(...).pip_install(...)` builds the image, which is cached. Pin versions.
4. `@modal.asgi_app()` returning a FastAPI app gives you a web endpoint. Use `modal deploy` for persistence, `modal run` for one-offs and `modal serve` for hot-reload development.

## 3. The LLM service
- vLLM + `Qwen/Qwen2.5-1.5B-Instruct`, lazy-loaded once per container through a global.
- `@modal.concurrent(max_inputs=10)` lets one container (one model copy) handle 10 requests at once, and vLLM batches them.
- `scaledown_window=300` keeps it warm for 5 minutes after the last request.

### Fixes I'd make
1. **T4 + bfloat16.** Qwen2.5 weights are bf16. The T4 is compute capability 7.5 and has no bf16, so vLLM 0.6.x raises `ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0` (see vllm-project/vllm issue #9990, Qwen2.5 on a T4 with 0.6.3). Use `LLM(..., dtype="half", max_model_len=4096)` or pick `gpu="L4"`.
2. **Chat template.** `model.generate([message])` sends raw text to an *Instruct* model. Use `model.chat([{"role":"user","content":message}], params)` so the template is applied.
3. **Mount the volume and attach the secret to `serve`**, not only to the separate demo functions. Otherwise the endpoint re-downloads weights on every cold start and never sees `API_KEY`.
4. **API-key header.** `x_api_key: str = Header()` makes the header *required*. I tested it with FastAPI's TestClient: no header gives **422** even with no key configured. Use `x_api_key: str | None = Header(default=None)`.
5. Cap `max_tokens` (e.g. `Field(256, le=512)`) so one request can't keep a GPU busy for minutes.
6. Ch 16's in-memory rate limiter counts **per container**. With autoscaling, the limits multiply.

## 4. Choosing a GPU
Weights in fp16 take about 2 bytes per parameter: a 1.5B model is ~3 GB, a 7B ~14 GB, plus KV cache. The T4 (16 GB) works in fp16. The L4 (24 GB, bf16) is often the better small-model default at about $0.21/h more.

## 5. Operating it
- `modal app logs <app>` or the dashboard. Ch 16's JSONL logs appear unchanged.
- Redeploy with `modal deploy` (rolling update).
- Cold starts take tens of seconds for LLMs. Cache weights in a volume, keep a warm window and accept the occasional slow first call.

## 6. Alternatives (book's Appendix E and others)
Docker on a VPS (full control, 24/7 cost), Hugging Face Spaces / Inference Endpoints, or a local Ollama plus a tunnel. The FastAPI app stays the same in every case.

## 7. Book checks (errata)
See ERRATA.md, ch17 rows: vLLM + T4 + bf16, the required API-key header and the "email warning before any charges" claim.

## 8. Review questions (my answers)
1. Serverless: per-second billing and scale-to-zero fit spiky, low-volume LLM traffic.
2. A GPU: `@app.function(gpu="T4")`.
3. Cold start: container boot + weight download + GPU load. Reduce it with volumes, `scaledown_window` and smaller models.
4. Volumes: keep model weights between containers so they aren't downloaded again.
5. With no traffic, the app scales to zero after the window and costs no GPU time.

## 9. Checkpoint exercise (my plan)
Hello World → GPU check on L4 → the LLM service with `dtype="half"` (T4) or bf16 (L4), a volume, `model.chat` → test `/health` and `/chat` from a phone → add the secret to `serve` plus the header fix → set a budget → share the URL.

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
