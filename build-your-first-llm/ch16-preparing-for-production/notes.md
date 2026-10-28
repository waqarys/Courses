# Chapter 16 — Preparing for Production (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch16.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch16.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt) · **My test run:** [book_app.py](book_app.py) + [test_book_app.py](test_book_app.py)

---

## 0. Why this chapter matters
It turns a notebook prototype into a small, reliable service: versioned config, a FastAPI API, JSONL logs, metrics, validation, rate limiting and tests.

**My runs:**
- **Notebook:** 8 code cells, all pass. It uses a *mock* `chat()`, so no LLM is needed.
- **The book's complete `app.py`:** I ran it against a **real Llama 3.2 3B (Q4_K_M) through Ollama** on my CPU box, with the book's 4 tests plus 2 of my own.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Production | Running for real users without you watching |
| Endpoint | URL + HTTP method the service answers |
| Health check | "Alive?" endpoint for monitors and load balancers |
| Rate limiting | Max requests per client per window (429 past it) |
| Graceful degradation | Controlled, helpful failure |
| JSONL logging | One JSON object per line, append-only |

## 1. The production mindset
Expect long inputs, crowds, injection, night-time failures and regressions. Fail gracefully: don't crash, tell the user something useful, log it, and keep serving others.

## 2. Packaging
- Save `{model_name, version, system_prompt, ollama_model, created_at}` to `config_v{version}.json`.
- Semantic versions plus a changelog. A system-prompt or model change is a **major** behaviour change.
- Quantization explains why Ollama models fit on a laptop. My `llama3.2` GGUF (Q4_K_M) is **2.02 GB**, against ~6.4 GB in fp16 for 3.2B params.

## 3. Serving
- Pydantic `ChatRequest` with a `field_validator` (empty → **422**). `ChatResponse(response, latency_ms)`.
- `/health`. The book's dependency check calls `chat("Say OK")`, which is a **full generation per probe**. I'd ping `GET /api/tags` and cache it.
- Status codes: 200 / 400 (our validation) / 422 (schema) / 429 (rate) / 500 (us).

## 4. Logs and metrics
- Log metadata only: timestamp, lengths, latency, success, error. A real line from my run: `{"prompt_length": 28, "response_length": 4, "latency_ms": 26260.41, "success": true}`.
- In-memory metrics reset on restart and are per-process. Prefer P50/P99 to the mean.
- Latency: the book says 5–15 s on CPU. Mine was ~26 s on a contended 8-core box. Use timeouts ≥ 30 s and streaming.

## 5. Safety
- Length limit 4000 (**characters**, though the comment says "tokens, roughly").
- Regex injection filter: the full `app.py` uses `r"act as"` with no word boundary, so **"In fact as a beginner…" is rejected with 400** (my test). Use `\b…\b`, and treat keyword filters as a weak first layer.
- Rate limiter: per-IP timestamps in a 1-minute window. My test sent 21 quick requests and the last got **429**. It's per-process, and behind a proxy `request.client.host` is the proxy's IP. Use `X-Forwarded-For` only from a trusted proxy.

## 6. Testing (my results)
| Test | Notebook (mock) | Book app.py + real Llama 3.2 |
|---|---|---|
| health 200 "healthy" | ✓ | ✓ |
| valid chat 200 | ✓ | ✓ (26.3 s) |
| empty → 422 | ✓ | ✓ |
| 10,000 chars → 400 "too long" | (not in notebook) | ✓ |
| mine: 21 requests → 429 | — | ✓ |
| mine: "In fact as a beginner…" → 200 | — | **✗ 400** |

## 7. Fixes I'd make
1. `\b` word boundaries.
2. A cheap, cached health check.
3. Count rejected requests in `/metrics`.
4. Call the length limit "characters", or count tokens.
5. Use a trusted forwarded-for header as the rate-limit key behind proxies.
6. Timeouts → 503 with a friendly message.
7. Read config and API keys from environment variables. Ch 17 refers to a "Ch 16 pattern" for these that the chapter doesn't contain.
8. Bonus cache key: `(model, system_prompt, message)`, TTL 5 minutes.

## 8. Book checks (errata)
See ERRATA.md, ch16 rows: the `act as` false positive, tokens vs characters, and the forward references to Kubernetes and canary infrastructure in Ch 17.

## 9. Review questions (my answers)
1. Development has one user and you watching. Production has many users and must recover alone.
2. `/health` proves liveness to monitors and load balancers. Check dependencies cheaply.
3. Log timestamps, lengths, latency, status and error types. Don't log raw prompts or PII.
4. Rate limiting protects capacity and cost from floods and abuse.
5. Error paths are where production failures happen. Each bug fix gets a regression test.

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
