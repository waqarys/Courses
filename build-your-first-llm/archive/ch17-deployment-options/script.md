# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter seventeen of my study series on Build Your First LLM by Hasan Degismez. This is the chapter where the project leaves your laptop. We deploy an LLM API to Modal, a serverless GPU platform, using a few decorators and one command. I'll walk through every step, check the prices against Modal's pricing page as of today, and point out two problems in the book's code that would trip you up on a T4 GPU.

## Slide 2 — Where we are

In chapter sixteen we built a production style FastAPI service. Today we put it on a cloud GPU with a public URL. The chapter seventeen notebook doesn't deploy anything itself. It prints the files you save and then run with the modal command line tool.

## Slide 3 — Chapter 17 roadmap

The plan. What serverless means. Three small Modal programs that build up to a GPU. Web endpoints. The full LLM service. Secrets and volumes. Choosing a GPU, logs, costs and cold starts. Security. Then the fixes the book's code needs, and review.

## Slide 4 — Key terms for this chapter

Key terms. Serverless means you ship code and the platform handles machines. A container packages the operating system, Python and your libraries. A cold start is the time to boot one and load the model. A volume is storage that survives restarts. A secret holds keys safely. And the scale down window is how long an idle container stays alive.

## Slide 5 — Part 1

Part one. Why serverless at all?

## Slide 6 — Owning a car vs taking a taxi

The book's analogy is a car versus a taxi. A traditional server is rented around the clock, you pay while it sits idle and you maintain it. Serverless runs only when a request arrives, bills per second and scales down to zero.

## Slide 7 — The cost picture (list prices, Oct 2026)

I checked Modal's pricing page today. A T4 is about fifty nine cents an hour, an A10 about a dollar ten and an H100 about three ninety five, which matches the book. The starter plan includes thirty dollars of compute a month. That's about fifty T4 hours if the GPU were the only cost. In practice CPU and memory are billed too, so expect a bit less. For a demo used a few hours a month, serverless is far cheaper than a server rented all month.

## Slide 8 — Getting set up

Setup is three commands. Install the package, run modal setup, which opens a browser and stores a token on your machine, and check the version. Treat that token like a password.

## Slide 9 — Part 2

Part two. Building up in small steps.

## Slide 10 — Hello Modal

The smallest Modal app. Create an app, decorate a function, and call it with dot remote from a local entry point. Modal run starts a container in the cloud, runs the function there and prints the result on your laptop.

## Slide 11 — What actually happened

Four ideas. The app is a named group of functions. The function decorator marks code to run remotely. Dot remote calls it in the cloud, and dot local would run it on your machine. Behind the scenes Modal built a container, ran your code, sent back the value and shut it down.

## Slide 12 — One parameter for a GPU

Adding a GPU is one argument. The function imports torch inside its body, because torch only needs to exist inside the container, not on your laptop. On a T4 it reports a Tesla T4.

## Slide 13 — Defining the container image

The image says what to install, in Python instead of a Dockerfile. The first run builds and caches it, and later runs reuse it. My tip: pin versions, so a rebuild next month doesn't quietly pull a different torch.

## Slide 14 — Part 3

Part three. Giving it a URL.

## Slide 15 — FastAPI on Modal

Any FastAPI app can be served by returning it from a function decorated with asgi app. Modal deploy, not modal run, keeps it running and prints a public HTTPS URL built from your workspace, app and function names.

## Slide 16 — `run` vs `deploy`

Run is ephemeral and stops when your terminal does. Deploy is persistent and is what you share. There's also modal serve, which gives you a temporary URL that reloads as you edit, handy while developing.

## Slide 17 — The deploy flow

Here's the whole flow, redrawn. A Python file on your laptop, modal deploy, an image build and a container on a GPU, and a public URL with your health, chat and docs routes. The docs page is the same Swagger interface you used locally in chapter sixteen.

## Slide 18 — Part 4

Part four. A real model behind the URL.

## Slide 19 — The image and the model loader

The service installs FastAPI and vLLM, a fast inference engine. A global holds the model, and get model loads Qwen two point five, one point five billion, the first time it's called, then reuses it. That's lazy loading.

## Slide 20 — The endpoints

The chat endpoint takes a validated request, generates with vLLM and returns a validated response, the same Pydantic pattern as chapter sixteen. Exceptions become an HTTP five hundred.

## Slide 21 — The function decorators

The decorators set the image, the GPU, a five minute timeout and a five minute scale down window. Concurrent with ten inputs lets one container, and one loaded model, serve ten requests at once. vLLM batches them together on the GPU.

## Slide 22 — Fix 1: T4 can't do bfloat16

Here's the first fix the book's code needs. Qwen two point five is stored in bfloat sixteen, and a T4 doesn't support that format. vLLM version zero point six refuses to start with an error saying bfloat sixteen needs compute capability eight. There's a public vLLM issue showing exactly this with Qwen two point five on a T4. The fix is dtype half. I'd also cap the context length so the cache fits in sixteen gigabytes. Or choose an L4 or A10, which support bfloat sixteen.

## Slide 23 — Fix 2: prompts need the chat template

The second issue is quality rather than a crash. The service passes the raw message to an instruct model with no chat template, so it tends to ramble or just continue your sentence. vLLM's chat method applies the model's template for you. I'd use that.

## Slide 24 — Testing the deployment

Test with curl: the health route, then a chat post with a JSON body. Expect the first call after the app has been idle to take a while. That's a cold start. Or use the docs page.

## Slide 25 — Part 5

Part five. Keys and caches.

## Slide 26 — Secrets: never hard-code keys

Create a secret once from the command line or the dashboard. Attach it to a function, and it appears as an environment variable. One detail: to protect the chat endpoint, attach the secret to the serve function itself, otherwise the API key check never sees a key.

## Slide 27 — Volumes: cache the weights

A volume mounted at the Hugging Face cache folder means the weights download once and every later cold start reads them from the volume. Mount it on the serve function too, not only a demo function.

## Slide 28 — Part 6

Part six. Running it sensibly.

## Slide 29 — Choosing a GPU

Here's my table from the current pricing page. The T4 is cheapest but lacks bfloat sixteen. An L4 costs a little more, supports it and is faster, which makes it a good default for small models. A rough memory rule: two bytes per parameter in half precision, plus room for the KV cache. A one and a half billion model needs about three gigabytes for weights.

## Slide 30 — Cold starts

A cold start is boot time, plus downloading weights, plus loading them onto the GPU. This is my sketch, not a measurement. A volume removes the download, and a longer scale down window keeps a container warm between requests, at a cost. For a hobby project, an occasional slow first request is fine.

## Slide 31 — Logs, updates, cost control

Logs stream from the command line or the dashboard, and your chapter sixteen JSON logs appear there unchanged. Updating is just deploying again. For cost, let it scale to zero and start small. One correction: the book says you'll get an email before any charges. Modal's pricing page says usage beyond the thirty dollars is pay as you go, so set a workspace budget if you want a hard cap.

## Slide 32 — Part 7

Part seven. Your API is public.

## Slide 33 — The API-key check, and a subtle bug

The book's API key check has a small trap. Header with no default makes the header required, so any request without it gets a four twenty two validation error, even when no key is set. I tested it with FastAPI's test client. Give it a default of None, and then the code behaves as the book describes.

## Slide 34 — The rest of the checklist

The rest. HTTPS is automatic. Reuse your rate limiter and validation. Put an upper limit on max tokens, so a single request can't run your GPU for minutes. And remember that an in memory rate limiter counts per container, so if Modal scales to three containers, each has its own count.

## Slide 35 — Not Modal? Other routes

Modal isn't the only route. The book's appendix covers Docker on a rented server, which gives full control but costs money around the clock. Hugging Face Spaces and inference endpoints are good for demos. And a local model plus a tunnel is free but only works while your machine is on. The nice thing is that your FastAPI app is the same everywhere. Only the wrapper changes.

## Slide 36 — Part 8

Part eight. Review.

## Slide 37 — Review questions: short answers

Short answers. Serverless bills per second and scales to zero, perfect for spiky traffic. A GPU is one argument. A cold start is boot plus model load, reduced by volumes and warm windows. Volumes keep weights between containers. And with no traffic, the app scales to zero and costs nothing.

## Slide 38 — Checkpoint exercise, my version

My version of the checkpoint. Deploy hello world, then a GPU function. Deploy the service with half precision or on an L4, a volume and the chat method. Test from your phone. Add the API key secret with the header fix. And set a budget before you share the link.

## Slide 39 — Practice this

Practice: deploy the simple API and time a cold versus a warm request. Swap in your own chapter twelve model behind the same routes. And compare tokens per second per dollar on a T4 and an L4.

## Slide 40 — Credits

This video is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams are my own, but the book goes deeper, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. Thanks for watching, and see you in the final chapter.

