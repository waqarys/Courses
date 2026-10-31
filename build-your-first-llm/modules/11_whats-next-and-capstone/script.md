# M11 — Where LLMs Are Heading + Your Capstone

Target length: **12 min** · Segments: 6
Big idea: *You now own the whole map. The frontier is the same map with four new roads: bigger context, mixture-of-experts, multimodal input, and agents that use tools.*

## S1 · CAM · Hook (≈40s)
- Ten modules ago an LLM was magic. Now you've built the tokenizer, attention, the block, trained one, fine-tuned one and served one.
- Today: what's changing at the frontier, how to keep learning, and a capstone you can finish in a weekend.

## S2 · SLIDES · Four roads at the frontier (≈3 min)
- Longer context: RoPE scaling and efficient attention push windows from a thousand tokens to hundreds of thousands.
- Mixture of experts: many feed-forward "specialists", a router picks two per token. Big total size, small cost per token.
- Multimodal: images and audio become tokens too, through their own encoders. Same transformer underneath.
- Agents and tools: the model writes a function call, code runs it, the result goes back into the prompt. The loop from Module 1, with hands.
- Plus reasoning models that spend more tokens thinking before answering.

## S3 · SLIDES · How to keep learning without drowning (≈2 min)
- Read one paper a week, but run its code.
- Rebuild before you read the next thing — your Module 6 model is your lab.
- Recommended reading: the book that inspired this series — "Build Your First LLM" by Hasan Degismez — linked below.

## S4 · SLIDES · Capstone: "Ask My Notes" (≈3 min)
- Goal: a small app that answers questions about your own notes, in your voice.
- Step one: collect 20 pages of your notes — clean and chunk them, Module 3.
- Step two: retrieval, Module 9.
- Step three: a LoRA tone adapter with 30 of your own Q&A pairs, Module 8.
- Step four: serve it behind a tiny API, Module 10. Bonus: quantise it.
- Step five: an eval sheet with 15 questions and your expected answers. Score before and after every change.
- Share a screen recording and tag the channel.

## S5 · IDE · Capstone starter (≈2 min)
- Snippet 01: a project skeleton generator — makes the folders and an eval CSV for you.
- Run it. You get ask_my_notes with data, src and eval folders.

## S6 · CAM · Thank you + next (≈40s)
- You went from "what is a token" to shipping a model.
- Comment what you'd like next: a deeper dive into mixture of experts, agents, or building a Hindi/Urdu tokenizer.
- Subscribe, and see you in the next build.
