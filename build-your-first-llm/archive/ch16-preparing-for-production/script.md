# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter sixteen of my study series on Build Your First LLM by Hasan Degismez. Today we turn a working notebook into software other people can use: a versioned config, a FastAPI service, JSON lines logging, metrics, input validation, rate limiting and tests. I ran the notebook, and then I ran the book's complete app against a real local Llama 3.2 through Ollama, with all four of the book's tests plus two of my own. One of mine found a false positive in the injection filter.

## Slide 2 — Where we are

Chapter fifteen gave us an app that works when we're watching. Today we make it reliable for other people, and next chapter we deploy it. The chapter sixteen notebook uses a mock chat function, so it runs without any model.

## Slide 3 — Chapter 16 roadmap

The plan. What changes in production. Packaging. Serving with FastAPI. Logs and metrics. Validation and rate limits. Testing. Then the complete app, which I ran against a real model. Then review.

## Slide 4 — Key terms for this chapter

Key terms. Production is code running for real users without you watching. An endpoint is a URL and method. A health check reports whether you're alive. Rate limiting caps requests per client. Graceful degradation means failing helpfully. And JSON lines logs are one object per line.

## Slide 5 — Part 1

Part one. A different world.

## Slide 6 — Two different worlds

In development you are the only user, errors are lessons, you debug with print and you can rerun a cell. In production many people use it at once, errors mean frustrated users, you debug by reading last night's logs, and the system has to recover on its own.

## Slide 7 — What goes wrong (it will)

The book lists the classic failures. A huge prompt, a sudden crowd, a prompt injection, a failure at night with no logs, and a fix that breaks something else. The principle: fail gracefully. Don't crash, tell the user something useful, log it and keep serving everyone else.

## Slide 8 — Part 2

Part two. What exactly are we shipping?

## Slide 9 — Save the config, with a version

For an Ollama based app, the model is really the model tag plus your system prompt and settings. The book saves them as a versioned JSON file with a timestamp. My run wrote config version one point zero point zero exactly as printed.

## Slide 10 — Semantic versioning + a changelog

Use semantic versioning. A bug fix bumps the patch number, a compatible feature the minor number, and a behaviour change the major number. My opinion: changing the system prompt or the model is a behaviour change, so version it like code and keep a changelog.

## Slide 11 — Why Ollama models fit on a laptop

Why does a three billion parameter model fit on a laptop? Quantization. The copy I use is a four bit build of about two gigabytes, against about six point four in sixteen bit. You lose a little quality and gain a lot of memory.

## Slide 12 — Part 3

Part three. Making it reachable over HTTP.

## Slide 13 — HTTP in one slide

HTTP in one slide. An endpoint plus a method. Get reads, post sends data. Every response has a status code: two hundred OK, four hundred bad request, four twenty two failed the schema, four twenty nine too many requests, and five hundred means we broke.

## Slide 14 — A minimal FastAPI service

Here's the minimal service. A Pydantic request model with a validator that rejects empty messages, a response model, and a chat endpoint that times the call. FastAPI validates both directions automatically and generates docs at slash docs.

## Slide 15 — The health check

A good health check also checks its dependencies. The book's version calls the model with "say OK". My caution: that's a full generation every time a monitor polls, which can be every few seconds. On my CPU one generation took over twenty seconds. Cheaper: ask Ollama for its model list, and cache the result briefly.

## Slide 16 — Running and calling it

Run it with uvicorn, then call it with curl, with Python requests, or from the interactive docs page.

## Slide 17 — The request path

Here's my redrawing of the request path. Each stage can stop a bad request with its own status code: the rate limiter with four twenty nine, Pydantic with four twenty two, our validator with four hundred, and a failed generation with five hundred. Everything is logged at the end.

## Slide 18 — Part 4

Part four. Knowing what it's doing.

## Slide 19 — Structured JSONL logs

Logs are a flight recorder. The book logs metadata only: lengths, latency, success and errors, never the prompt itself, for privacy. Here's a real line from my run: a twenty eight character prompt, a four character answer, twenty six seconds of latency on a busy CPU.

## Slide 20 — Simple in-memory metrics

For metrics, a dictionary is enough to start: requests, errors and latency, exposed at slash metrics. It resets on restart and counts per process. Real dashboards add percentiles, because averages hide pain. One thirty second request in a hundred barely moves the mean, but P ninety nine shows it.

## Slide 21 — Why LLMs are slow (and that's OK)

LLMs generate one token per forward pass, so a hundred tokens means a hundred passes. The book estimates five to fifteen seconds on a CPU. On my busy eight core box a short reply took twenty six seconds. So set generous timeouts, show progress, and stream when you can.

## Slide 22 — Part 5

Part five. Expect bad input.

## Slide 23 — Input validation

The validator rejects long inputs and a few injection phrases with regular expressions, returns a generic error and logs the attempt. One small inconsistency: the comment says the limit is in tokens, roughly, but the code compares string length, so it's characters.

## Slide 24 — My test: the filter blocks innocent input

Here's what my own test found. The complete app shortens one pattern to just "act as", with no word boundaries. I sent: in fact as a beginner, how do I learn Python? It was rejected with four hundred, because the letters "act as" appear inside "fact as". Contact as soon as possible would be blocked too. Add word boundaries, and remember keyword filters only stop casual attacks.

## Slide 25 — Rate limiting

The rate limiter keeps a list of recent timestamps per IP and returns four twenty nine past twenty a minute. My test confirmed it. Two caveats. It lives in one process's memory. And behind a proxy or a cloud platform, the client host may be the proxy's address, so every user shares one limit unless you read the forwarded header carefully.

## Slide 26 — Part 6

Part six. Insurance.

## Slide 27 — pytest + TestClient

FastAPI's test client calls your app in process, no server needed. Test the happy path, but also the error paths: empty input gets four twenty two, long input gets four hundred. Add unicode, the rate limit and what happens when the model is down.

## Slide 28 — My results

My results. The notebook's three mock tests all pass. Against the real model, the book's four tests pass, including the long input test, which the notebook leaves out. My rate limit test passes. My false positive test fails, which is exactly what tests are for.

## Slide 29 — Canary deployments (concept)

Canary deployments send a new version to a small slice of traffic first, then ramp up or roll back. The book says chapter seventeen builds the infrastructure for this, but chapter seventeen only uses Modal's rolling deploy. There's no canary step.

## Slide 30 — Timeouts and fallbacks

Graceful degradation in practice. Give every model call a timeout, so a stuck generation can't hold a worker forever. On timeout return a five oh three with a friendly message, not a stack trace. Optionally fall back to a smaller model or a cached answer. Keep the user message generic and put the details in the log.

## Slide 31 — Config from the environment (my addition)

One thing I'd add. Read settings like the model name, rate limit and any API key from environment variables, never from code in git. The book's chapter seventeen refers back to chapter sixteen's environment variable and API key pattern, but chapter sixteen doesn't actually cover it, so here it is.

## Slide 32 — Part 7

Part seven. The complete app.

## Slide 33 — The complete `app.py`, in one picture

The complete app puts it all together: config, logger, rate limiter, validator, models and three endpoints. Chat goes rate limit, validate, call the model, then log and count. And around it all sits the production loop: detect, diagnose, fix with a regression test, and monitor.

## Slide 34 — Small fixes I'd make

Small fixes I'd make. Word boundaries. A cheap health check. Count rejected requests in the metrics too, because right now validation failures never reach the counters. Say characters, or count tokens. Use the forwarded header for the rate limit key, but only from a proxy you trust. And for the bonus cache, include the model and system prompt in the key.

## Slide 35 — My "ready to share" checklist

My checklist before sharing. Tests are green, including the error paths. Logs exist, you can read them, and they hold no prompts or personal data. Health is cheap and metrics count rejects. Every limit is set: length, rate, max tokens and timeouts. And the version in slash health matches your changelog.

## Slide 36 — Part 8

Part eight. Review.

## Slide 37 — Review questions: short answers

Short answers. Development is you, production is many users without you. Health proves liveness and should check dependencies cheaply. Log metadata, not content. Rate limiting protects capacity and your bill. And test error paths, because that's where production actually lives.

## Slide 38 — Checkpoint exercise

The checkpoint: health and chat endpoints, validation with word boundaries, content free logs, a metrics endpoint and at least four tests. Add my false positive test. The bonus is a five minute cache for identical prompts.

## Slide 39 — Practice this

Practice: run the complete app against Ollama with pytest. Add my false positive test, watch it fail, fix the regular expression and watch it pass. Then plot latency from your log and compare the median with the ninety ninth percentile.

## Slide 40 — Credits

This video is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams are my own, but the book goes deeper, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. Thanks for watching, and see you in chapter seventeen.

