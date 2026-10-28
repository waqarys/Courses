# YouTube upload — Chapter 17

**Title:** Build Your First LLM — Ch 17: Deployment Options (Full Walkthrough)

**Duration:** 11:24 · **Slides:** 40 · **Thumbnail:** thumbnail.png · **Captions:** captions.srt (English)

**Playlist:** Build Your First LLM (study series) · **Visibility:** set by Waqar at upload

## Description

We take the LLM API from chapter 16 to a public HTTPS URL on a cloud GPU with Modal: Hello Modal, adding a GPU, container images, FastAPI web endpoints, then a vLLM + Qwen2.5-1.5B service with lazy loading, concurrency, secrets and volumes. I check the prices against Modal's pricing page (Oct 2026) and fix what the book's code needs: T4 GPUs can't run bfloat16 in vLLM, instruct models need the chat template, and the API-key header returns 422 for any request that doesn't send it, even when no key is configured.

This is part of my study series on the book "Build Your First LLM: A Hands-On Guide to Language Models" by Hasan Degismez. All slides, narration and diagrams are my own teaching adaptation. Please support the author and buy the book: https://leanpub.com/FirstLLM/

📌 Chapters
0:00 Intro & roadmap
1:34 Part 1 — Why serverless?
2:41 Part 2 — Hello Modal → GPU → dependencies
3:51 Part 3 — Web endpoints
4:47 Part 4 — The full LLM service
6:54 Part 5 — Secrets and volumes
7:31 Part 6 — GPUs, costs, cold starts
8:47 Part 7 — Security basics
10:00 Part 8 — Review
10:43 Practice this
10:59 Credits

💻 Code (FirstLLM/code, MIT License)
- Notebook: https://github.com/FirstLLM/code/blob/main/notebooks/ch17.ipynb
- Run in Colab: https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch17.ipynb
- Slides + study notes: https://github.com/waqarys/Courses/tree/build-your-first-llm/build-your-first-llm

📚 Credit
Based on "Build Your First LLM" by Hasan Degismez — https://leanpub.com/FirstLLM/
Code: https://github.com/FirstLLM/code (MIT License)
Narration voice: synthetic (Kokoro TTS).

#LLM #Transformers #MachineLearning

## Tags
build your first llm, llm from scratch, transformers, attention mechanism, gpt-2, pytorch, deep learning, machine learning, large language models, hasan degismez, waqar shaikh builds, ai tutorial, deployment options
