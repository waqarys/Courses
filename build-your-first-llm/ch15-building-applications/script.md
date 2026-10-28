# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter fifteen of my study series on Build Your First LLM by Hasan Degismez. We stop training and start building: a chat loop with memory, a retrieval augmented generation system with citations, a first look at tool calling, and simple automatic evaluation. I ran the whole pipeline against a real Llama 3.2 3B on my own machine, and I also found that the calculator tool's sandbox isn't a sandbox at all.

## Slide 2 — Where we are

We've changed weights and we've changed prompts. Today we build an application around the model: memory, documents and tools. Then chapters sixteen and seventeen make it production ready and deploy it. The notebook uses Ollama and sentence transformers.

## Slide 3 — Chapter 15 roadmap

The plan. The mindset shift. The three application patterns. A chat loop. RAG, step by step. Tool calling and its safety. Evaluation with my real model run. And production tips.

## Slide 4 — Key terms for this chapter

Key terms. RAG means retrieve, then generate. A sentence embedding is one vector for a whole passage. Chunking splits documents. The context window is how much the model can see. Tool calling lets the model ask your code to run a function. And a citation ties a claim to its source.

## Slide 5 — Part 1

Part one. A change of role.

## Slide 6 — Your training skills transfer

Nearly every training skill has an application twin. Token embeddings become sentence embeddings. Chunking data becomes chunking documents. Data quality becomes validation. Seeds and logs become debugging. Loss becomes evaluation. One correction: the book says embeddings and cosine similarity were chapter six. They were chapter nine.

## Slide 7 — Three application patterns

Three patterns, each adding capability and complexity. Pure prompting uses only what the model knows. RAG adds documents it has never seen. Tools let it fetch live data or take actions.

## Slide 8 — Choosing a pattern

Start simple. Prompt first. Add retrieval when the model lacks knowledge. Add tools when it needs to act or calculate exactly. This chapter goes deep on RAG and previews tools.

## Slide 9 — Part 2

Part two. The chat loop.

## Slide 10 — The basic loop

A chat loop. Read input, append it to history, send the whole history, append the reply. The model has no memory of its own; memory is just resending the conversation every turn. Which means the history grows forever.

## Slide 11 — The context window

Every model has a context window covering prompt plus reply. The book says Llama 3.2's is about eight thousand. The model actually supports a hundred and thirty one thousand. But Ollama runs it with a much smaller window by default; on my machine the server ran with four thousand ninety six. So the practical limit is whatever you configure, using num ctx.

## Slide 12 — ChatSession: trim old turns

The ChatSession class keeps at most twenty messages, dropping the oldest and keeping user and assistant turns paired. It counts messages, not tokens, which is simple but rough. And leave about twenty percent of the window for the reply.

## Slide 13 — Logging, and a missing method

The logging version calls count history tokens and count tokens, but neither method exists anywhere, so it crashes. Use a tokenizer, or read Ollama's prompt eval count and eval count from the response, which are the real token numbers.

## Slide 14 — Part 3

Part three. The heart of the chapter.

## Slide 15 — The problem RAG solves

Models have frozen training data and finite context. RAG turns the test into an open book exam: a retriever finds the right pages, like a librarian, and the model reads them and answers.

## Slide 16 — RAG by hand

Here's RAG done by hand: paste the policy into the prompt, then ask. That's the whole idea. The engineering is in finding the right text automatically.

## Slide 17 — Sentence embeddings

A sentence embedding model turns a whole passage into one vector, here three hundred and eighty four numbers, trained so that passages with similar meaning land close together. I ran the book's example: the cosine similarity is point six five seven, matching the book.

## Slide 18 — Why not GPT-2's embeddings?

Why not reuse our own embeddings? Token embeddings are trained for predicting the next word. Sentence encoders are trained for matching meaning. Different objectives give different geometry, so use a purpose built encoder for retrieval.

## Slide 19 — Chunking with overlap

Chunking splits text into windows of two hundred words that overlap by fifty, so a fact sitting on a boundary appears whole in at least one chunk. Too small and chunks lack context; too big and retrieval gets fuzzy. Two hundred to five hundred words is a good start.

## Slide 20 — The RAG pipeline

The full pipeline. Offline, chunk and embed your documents. Online, embed the question, find the most similar chunks, build a prompt with numbered sources, and let the model answer with citations.

## Slide 21 — Retrieval = a dot product

Retrieval is one matrix product. Normalise every vector to length one, and the dot product equals cosine similarity. Sort, take the top k, and drop anything below a minimum score.

## Slide 22 — Prompting with citations

The prompt numbers each source and names it, tells the model to cite by number, to use only these sources, and gives it permission to say the answer isn't there. That last line is what keeps hallucination down.

## Slide 23 — Notebook knowledge base

The notebook's knowledge base is three short policies: vacation, expenses and remote work. Each is under two hundred words, so each becomes one chunk.

## Slide 24 — My RAG run: retrieval + answers

My real run. Retrieval works well on in-scope questions: the vacation policy scores point seven nine, the remote work policy point four two, and the answers are correct and mostly cited. The interesting failure is the out of scope question, the meaning of life. Nothing passed the minimum score, so the book's fallback prompt was sent, which offers to answer from general knowledge. The model did exactly that, wrote about Aristotle, and cited a source one that doesn't exist.

## Slide 25 — My RAG run: the book's evaluation

Scoring with the book's evaluation set gives five out of eight traits. The vacation case passes everything. The expense case is correct but forgot the citation marker. The out of scope case fails both checks: it didn't refuse, and it cited a source that wasn't there. The fix is simple: if retrieval comes back empty, don't call the model at all. Return a fixed reply saying it isn't in your documents.

## Slide 26 — Part 4

Part four. Tools.

## Slide 27 — How tool calling works

Tool calling is a two turn dance. You describe the tools. The model writes a tool request in an agreed format. Your code parses it, runs the function, and sends the result back so the model can write the final answer. The model never runs anything itself.

## Slide 28 — The book's tools

Two tools: a calculator built on eval with empty builtins, and a date tool. A regular expression pulls out the tool name and argument.

## Slide 29 — ⚠ Empty `__builtins__` is not a sandbox

Important. The book says eval with empty builtins prevents arbitrary code execution. It doesn't. From any Python object you can walk to every loaded class. In my test, a single calculator expression reached the os module and printed the working directory, which means it could run anything. The book does mention simpleeval for production, but treat this code as unsafe. Parse with the ast module and allow only numbers and arithmetic.

## Slide 30 — My tool-calling run

Tool calling, on my real run. For fifteen percent of eight four seven, the model just wrote calculate fifteen percent of eight four seven, with no tool tags, so nothing ran. For the date, it invented its own tag format. Only the capital of France went well: it correctly used no tool. So zero out of two tool calls. A three billion parameter model doesn't reliably follow an invented text format. Use the runtime's native tool calling, show the format with an example, or use a bigger model.

## Slide 31 — Tool safety rules

Tool safety. Whitelist names. Validate arguments and never eval anything a user can influence. Start with read only tools and add write tools only with confirmation. Log every call. A tool that can send email, delete files or spend money is a security boundary.

## Slide 32 — Part 5

Part five. Testing and production.

## Slide 33 — Trait-based evaluation

LLM answers vary, so test traits. Does it contain the key words, cite a source, refuse when it should, and say enough? The checker uses a phrase list for refusals, which misses natural wordings like I couldn't find.

## Slide 34 — Temperature per task

Temperature by task. Low for RAG, zero for tool calls, higher for creative work. The book's snippet here uses an OpenAI client with GPT three point five that the chapter never sets up; with Ollama you just pass temperature to chat.

## Slide 35 — Streaming and caching

Two production tips. Stream tokens as they arrive; users feel it's faster even when it isn't. And cache embeddings keyed by a hash of the text, so you only embed what changed.

## Slide 36 — Debugging checklist

When it misbehaves, go layer by layer. Input: what exactly was sent. Retrieval: which chunks, what scores. Generation: temperature and prompt. And reproducibility: can you replay the exact input?

## Slide 37 — Notebook run summary

My notebook run. Memory works: asked what it just asked, the model answered correctly. Retrieval passes one chunk per question, with scores of point seven one and point five five. The RAG answers cite source one. Tool calling did not work: the three billion parameter model ignored the tool format and replied with plain text, so no tool ran. Two calls timed out at the helper's two minute limit because my CPU was busy, so I reran those in my own script. Streaming worked.

## Slide 38 — Key takeaways

Takeaways. An application is a model plus memory, knowledge, actions and checks. RAG is chunk, embed, retrieve, cite, and retrieval quality decides everything. Your code runs the tools, so you own their safety. Evaluate traits automatically and read the answers too. And check the context limit your runtime actually uses.

## Slide 39 — Review questions: short answers

Short answers. RAG adds facts the model never saw. Token embeddings live inside the model; sentence embeddings represent whole passages for retrieval. Chunking keeps things focused. A minimum score plus permission to say not found handles bad retrieval. And whitelisting stops the model calling functions you never meant to expose.

## Slide 40 — Review 6–7 + checkpoint

Evaluate accuracy with an eval set and by reading samples. Log request ids, lengths, which sources were retrieved with their scores, tokens, latency and errors. The checkpoint is a personal knowledge assistant over your own files, with a ten question evaluation.

## Slide 41 — Practice this

Practice. Add questions your documents can't answer and check the app admits it. Replace the eval calculator with an ast based one and confirm the escape no longer works. And log real token counts from Ollama.

## Slide 42 — Credits

This video is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams are my own, but the book goes deeper, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. Thanks for watching, and see you in chapter sixteen.

