# YouTube upload — Chapter 9

**Title:** Build Your First LLM — Ch 9: The Embedding Layer (Full Walkthrough)

**Duration:** 17:10 · **Slides:** 41 · **Thumbnail:** thumbnail.png · **Captions:** captions.srt (English)

**Playlist:** Build Your First LLM (study series) · **Visibility:** set by Waqar at upload

## Description

Token IDs become vectors. We see why raw IDs can't be fed to a network, build token embeddings as a lookup table, show (with a real attention layer) why order is invisible without positions, implement GPT-2's learned positional embeddings and the complete GPT2Embeddings module, then open the real GPT-2: what wte and wpe learned, nearest neighbours, and king − man + woman ≈ queen — which only works once you use the space-prefixed token. CPU run of the book's ch09 notebook, my own experiments, solved exercises and book corrections.

This is part of my study series on the book "Build Your First LLM: A Hands-On Guide to Language Models" by Hasan Degismez. All slides, narration and diagrams are my own teaching adaptation. Please support the author and buy the book: https://leanpub.com/FirstLLM/

📌 Chapters
0:00 Intro & roadmap
1:38 Part 1 — Why not just use token IDs?
4:16 Part 2 — Token embeddings: a lookup table
5:37 Part 3 — Why position matters
7:59 Part 4 — Token + position = `GPT2Embeddings`
9:23 Part 5 — Inside the real GPT-2
12:09 Part 6 — Practical details
13:56 Part 7 — Exercises and review
16:13 Practice this
16:44 Credits

💻 Code (FirstLLM/code, MIT License)
- Notebook: https://github.com/FirstLLM/code/blob/main/notebooks/ch09.ipynb
- Run in Colab: https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch09.ipynb
- Slides + study notes: https://github.com/waqarys/Courses/tree/build-your-first-llm/build-your-first-llm

📚 Credit
Based on "Build Your First LLM" by Hasan Degismez — https://leanpub.com/FirstLLM/
Code: https://github.com/FirstLLM/code (MIT License)
Narration voice: synthetic (Kokoro TTS).

#LLM #Transformers #MachineLearning

## Tags
build your first llm, llm from scratch, transformers, attention mechanism, gpt-2, pytorch, deep learning, machine learning, large language models, hasan degismez, waqar shaikh builds, ai tutorial, the embedding layer
