# YouTube upload — Chapter 12

**Title:** Build Your First LLM — Ch 12: Training Your Model (Full Walkthrough)

**Duration:** 14:42 · **Slides:** 43 · **Thumbnail:** thumbnail.png · **Captions:** captions.srt (English)

**Playlist:** Build Your First LLM (study series) · **Visibility:** set by Waqar at upload

## Description

We train MiniGPT on Shakespeare: the next-token shift, the five-step training loop, learning-rate warmup and gradient clipping, validation loss and perplexity, checkpoints and sampling. I ran the notebook unchanged on CPU (val loss 6.22 to 5.51, perplexity 246, far from the book's printed 42) and found that ignore_index=0 ignores GPT-2's '!' token instead of the padding, which is 22% of target positions. Then I trained the same model on a padding-free token stream: val loss 4.87, perplexity 130 after 1,200 steps.

This is part of my study series on the book "Build Your First LLM: A Hands-On Guide to Language Models" by Hasan Degismez. All slides, narration and diagrams are my own teaching adaptation. Please support the author and buy the book: https://leanpub.com/FirstLLM/

📌 Chapters
0:00 Intro & roadmap
1:43 Part 1 — Training as a feedback loop
2:10 Part 2 — The language-modelling objective
2:59 Part 3 — Cross-entropy loss
4:02 Part 4 — Data: Dataset, collate, DataLoader
5:36 Part 5 — The training loop
7:05 Part 6 — Validation, overfitting, perplexity
8:16 Part 7 — Checkpoints and generation
8:57 Part 8 — My CPU run vs the book
12:55 Part 9 — Exercises and review
14:01 Practice this
14:16 Credits

💻 Code (FirstLLM/code, MIT License)
- Notebook: https://github.com/FirstLLM/code/blob/main/notebooks/ch12.ipynb
- Run in Colab: https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch12.ipynb
- Slides + study notes: https://github.com/waqarys/Courses/tree/build-your-first-llm/build-your-first-llm

📚 Credit
Based on "Build Your First LLM" by Hasan Degismez — https://leanpub.com/FirstLLM/
Code: https://github.com/FirstLLM/code (MIT License)
Narration voice: synthetic (Kokoro TTS).

#LLM #Transformers #MachineLearning

## Tags
build your first llm, llm from scratch, transformers, attention mechanism, gpt-2, pytorch, deep learning, machine learning, large language models, hasan degismez, waqar shaikh builds, ai tutorial, training your model
