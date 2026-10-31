# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to the final chapter of my study series on Build Your First LLM by Hasan Degismez. There's no new model code here. Instead we look back at what we built, talk about building responsibly, and map out three paths and three concrete capstone projects for the next six to twelve months. I'll also share what this series taught me from running every notebook on a plain CPU, including the bugs we found along the way.

## Slide 2 — Where we are

We've gone from what is AI all the way to a deployed API. Today we consolidate and choose what to build next. The chapter eighteen notebook is a skills checklist, a learning plan and two starter templates.

## Slide 3 — Chapter 18 roadmap

The plan. The journey in five parts. A skills checklist. Responsible building. Three paths. Three capstones. Communities and how to read a paper. My own lessons from this series. And a final checklist.

## Slide 4 — Key terms for this chapter

Some terms for the road. MLOps and LLMOps mean running models in production. Quantization stores weights with fewer bits. Structured outputs force JSON or function calls. Sparse attention skips most token pairs. Mixture of experts routes each token to a few specialists. And interpretability asks why the model did what it did.

## Slide 5 — Part 1

Part one. Look how far we've come.

## Slide 6 — The journey

Here's the journey, redrawn in five parts. Understanding in chapters one to four. Python and tensors in five and six. Data, tokenizer, embeddings, attention, the transformer and training in seven to twelve. Fine tuning, prompting and applications in thirteen to fifteen. Production and deployment in sixteen and seventeen.

## Slide 7 — Part by part

Part one gave us the why. Part two the tools. Part three the model itself, built piece by piece and trained. Part four made it useful with LoRA, prompting, retrieval and tools. And part five shipped it behind a validated, logged API on a cloud GPU.

## Slide 8 — Skills checklist

The checklist, in three columns: theory, building and production. The notebook starts you at zero out of fourteen and asks you to flip each one honestly. If you followed the exercises, most should be true. If one isn't, that tells you which chapter to revisit.

## Slide 9 — These are the real skills

These aren't toy skills. Frontier labs use the same fundamentals at a much bigger scale. And you understand them because you built them. Sometimes you fixed them too, as we'll see in a moment.

## Slide 10 — Part 2

Part two. Building responsibly.

## Slide 11 — Responsibility is good engineering

The author frames responsibility as good engineering, and I agree. Asking what could go wrong before you deploy is the same habit as writing tests. There are three areas to question: your data, your outputs and your transparency.

## Slide 12 — Questions to ask every time

Here they are as a grid. For data: where did it come from, is it licensed, what biases does it carry. For outputs: could it cause harm, what if someone believes a hallucination, are you validating and moderating. For transparency: do users know it's AI, are you logging, can you trace a failure.

## Slide 13 — Where we practised this

We practised these along the way. Data sourcing in chapter seven. Guardrails in fifteen. Validation, logging and rate limits in sixteen. Secrets and keys in seventeen. The book says ethics is a practice you maintain, not a checklist you complete. One small correction: it credits chapter seventeen with audit trails, but logging was really chapter sixteen.

## Slide 14 — Your next system *will* fail sometimes

Whatever you build next will fail sometimes. Retrieval will grab the wrong passage. Fine tunes will inherit bias. Agents will call the wrong tool. So set expectations, add guardrails, log everything, test on diverse inputs and let users report problems or override the AI. The goal is failing gracefully, not perfection.

## Slide 15 — Part 3

Part three. Where to go from here.

## Slide 16 — Pick a direction for 6–12 months

Three directions for the next six to twelve months. Research, builder and systems. It's not a permanent career choice, and many people move between them.

## Slide 17 — Path 1 · Deeper technical (research)

Path one is research. Learn evaluation beyond loss and perplexity, architecture variants like sparse attention, mixture of experts and state space models, and interpretability. The book says this builds on chapter six, but six is the NumPy and PyTorch chapter. Training is chapter twelve and evaluation is in chapter fifteen. Start with the original transformer paper, which you can now actually read.

## Slide 18 — Path 2 · Product and applications (builder)

Path two is the builder. Reliable JSON and function calls, better retrieval with hybrid search and re ranking, and the user experience of streaming and graceful failure. The book points to chapter fourteen for RAG and fifteen for tools. In fact, both RAG and tool use are in chapter fifteen, and fourteen is prompting.

## Slide 19 — Path 3 · Production and infrastructure (systems)

Path three is systems. Make inference cheap with quantization, caching and batching. Make it observable with dashboards and tracing. And run it like software with prompt versioning, A B tests and evaluation pipelines. This builds on chapters sixteen and seventeen.

## Slide 20 — Combine them

Real projects need all three: technical depth, product sense and production skill. Pick one to go deep on and stay competent in the other two.

## Slide 21 — Part 4

Part four. Stop reading, start building.

## Slide 22 — Three capstones

The book offers three capstones, each sized for a few weekends. RAG with citations. A fine tuned domain assistant. And a single tool agent.

## Slide 23 — Capstone 1 · RAG with citations

Capstone one: a RAG system over your own documents. Collect a corpus, chunk and embed it using chapter fifteen's RAG section, which the book labels chapter fourteen, return sources with every answer, wrap it in the API and deploy it. Then grade twenty questions by hand. The stretch goal is hybrid search with BM25.

## Slide 24 — Capstone 2 · Fine-tuned domain assistant

Capstone two: a domain assistant. Curate five hundred to a thousand clean examples, QLoRA tune a seven billion model using chapter thirteen's ideas with the PEFT library, test on twenty questions the base model fails, compare and deploy. The stretch is DPO, which learns from preferred versus rejected answers.

## Slide 25 — Capstone 3 · Single-tool agent

Capstone three: an agent with exactly one tool. Define its schema, decide with structured outputs, and test twenty cases, half needing the tool. Aim for nineteen out of twenty. One warning from the notebook's own starter: its calculator uses eval with empty built ins. That still isn't safe, so use a proper math parser.

## Slide 26 — How to choose

How to pick. To consolidate, do the RAG system. To learn something new, do fine tuning. For fun, build the agent. The only wrong choice is analysis paralysis.

## Slide 27 — A four-weekend plan (any capstone)

Here's a plan I'd use for any of the three. Weekend one: data and a twenty question test set, so you have a baseline score. Weekend two: the core pipeline, beating the baseline. Weekend three: the API, logging and guardrails. Weekend four: deploy and write it up with real numbers.

## Slide 28 — Measure it like Ch 15

Measure it the way chapter fifteen taught. Freeze the test set before tuning. Report accuracy, citation correctness, latency and cost per thousand requests. Keep a log of every failure and its cause. And always compare against a baseline without the feature.

## Slide 29 — Make it portfolio-ready

Make it portfolio ready. A README that goes from problem to approach to numbers to limitations. A short demo video. A live URL with a budget cap. And an honest section on what didn't work, which is often the most impressive part.

## Slide 30 — Part 5

Part five. You don't have to learn alone.

## Slide 31 — Where to keep learning

Resources by comfort level. Start with the Hugging Face course and the local LLaMA community. When you're confident, Stanford's CS324 and the original papers. Then join the Hugging Face Discord or MLOps community, and contribute small things to open source: docs, bug reports, examples.

## Slide 32 — How to read an ML paper

The book's method for reading papers. Abstract and conclusion first. Then the figures. Skip the maths the first time. Focus on what the experiments actually tested. And read related work last.

## Slide 33 — Part 6

Part six. What running every notebook taught me.

## Slide 34 — Run the code, and read your logs

My biggest lesson: run the code and read your own logs. In chapter eleven, loaded GPT-2 wrote foxes es es es, because of missing attention biases and the wrong GELU. In chapter twelve, the loss ignored the exclamation mark instead of padding. In thirteen, the LoRA counts and naming didn't match the code. In seventeen, a T4 can't run bfloat sixteen. Every one of these is in the errata file in my repository. None of it takes away from the book. Finding these is how I actually learned the material.

## Slide 35 — Where your MiniGPT sits

Here's where our own model sits. Our sixteen million parameter MiniGPT, trained on a third of a million Shakespeare tokens, writes Shakespeare shaped noise. GPT-2 small, which we loaded in chapter eleven, is fluent but unreliable. Llama three point two, three billion parameters, which we ran locally through Ollama for chapters fourteen to sixteen, is a genuinely useful assistant. It's the same family of architecture. The difference is scale, data and tuning.

## Slide 36 — The series by the numbers

The series by the numbers. Eighteen chapters, and fourteen notebooks run on an ordinary CPU. The first seventeen videos add up to about five hours and fifty minutes. Along the way I logged sixty seven errata, every one checked by running code. That's not a criticism of the book: checking a book against running code is the best way to learn from it, and I'd encourage you to do the same.

## Slide 37 — What I'd do next

What I'd do next myself. Retrain MiniGPT with the chapter twelve fixes on a bigger corpus such as TinyStories, for about an hour of GPU. LoRA tune Llama three point two on my own FAQ and evaluate it properly. And deploy it on an L4 with a small budget cap.

## Slide 38 — Review questions: my answers

My answers to the review questions. The three paths are research, builder and systems. Responsibility is ongoing because data, users and models all change. My capstone is the RAG system. My next reads are the LoRA paper and vLLM's documentation. And what surprised me most is how much behaviour hides in a single argument.

## Slide 39 — Final checklist

Before you close the book: score the fourteen skills, choose one capstone and start this week, bookmark one resource, and share your deployed URL. The author ends with a personal note. He's a backend developer who wrote the book to teach himself how LLMs work, and his closing line is "now go build something".

## Slide 40 — Credits and thank you

This series is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams are my own, but the book is the real thing, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. All my slides, notes and the errata for the series are in my Courses repository. Thank you for watching the whole series. Now go build something.

