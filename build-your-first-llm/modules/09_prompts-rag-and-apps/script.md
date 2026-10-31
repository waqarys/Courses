# M09 — Prompts, Sampling, RAG: Building Real Apps on an LLM

Target length: **17 min** · Segments: 7
Big idea: *An LLM is a brilliant new intern with no memory of your company. A prompt is the briefing; RAG is handing the intern the right pages from the filing cabinet before they answer.*

## S1 · CAM · Hook (≈40s)
- Most LLM apps you use don't train anything. They're a prompt, some retrieved text, and a loop.
- Today: the knobs that control generation, prompt patterns that actually work, and a retrieval-augmented app built from scratch — no frameworks.

## S2 · SLIDES · The sampling knobs (≈2.5 min)
- Temperature: the spice knob. Divide the scores before softmax. Low — plain, safe, repetitive. High — bold, creative, sometimes nonsense.
- Top-k: only consider the k most likely tokens.
- Top-p, nucleus: take the smallest set of tokens whose probabilities add up to p, say 0.9.
- Greedy is temperature zero. Good for extraction and code; bad for stories.
- Repetition penalties exist because greedy loves loops — remember our Module 1 bigram.

## S3 · IDE · Turn the knobs (≈2.5 min)
- Snippet 01 with GPT-2. Same prompt, temperature 0.2, 0.8, 1.5.
- Print the top-5 next-token probabilities at each temperature — the distribution flattens as it heats up.

## S4 · SLIDES · Prompt patterns that work (≈2.5 min)
- One: role + task + format + constraints. "You are a Class 10 tutor. Explain X. Use three bullets. No jargon."
- Two: few-shot — show two examples of the exact output you want.
- Three: think step by step, then give a final answer on its own line — easy to parse.
- Four: delimiters — put user text inside triple quotes or tags so instructions and data don't mix. Basic defence against prompt injection.
- Five: ask for JSON with a schema, and validate it in code.
- Token counts matter: every example costs tokens, and you pay per token.

## S5 · SLIDES · RAG: hand the intern the right pages (≈2 min)
- Step one: split your documents into chunks.
- Step two: embed each chunk — a meaning vector, like Module 4 but for whole passages.
- Step three: at question time, embed the question and fetch the nearest chunks.
- Step four: paste them into the prompt with "answer using only this context, say I don't know otherwise".
- This is how you fix the knowledge-cutoff and hallucination limits from Module 1.

## S6 · IDE · RAG from scratch + Grok (≈4.5 min)
- Snippet 02. Pure Python retrieval with a word-count vector and cosine similarity — so you see every step.
- Our "company docs" are a few lines about this course.
- Ask "How long is the training run in module 7?" — it retrieves the right chunk. Print the scores.
- Build the prompt with delimiters.
- Then send it to Grok through the xAI API — key read from the environment variable, never hard-coded.
- No key? The script prints the prompt so you can paste it into Grok chat.
- In production you'd swap the word-count vectors for a real embedding model and a vector database. Same four steps.

## S7 · CAM · Recap (≈40s)
- Temperature, top-k, top-p.
- Role-task-format-constraints, few-shot, delimiters, JSON.
- RAG: chunk, embed, retrieve, prompt.
- Next: making it fast and cheap enough to ship.
