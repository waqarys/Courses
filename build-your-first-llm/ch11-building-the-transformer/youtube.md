# YouTube upload — Chapter 11

**Title:** Build Your First LLM — Ch 11: Building the Transformer (Full Walkthrough)

**Duration:** 14:57 · **Slides:** 40 · **Thumbnail:** thumbnail.png · **Captions:** captions.srt (English)

**Playlist:** Build Your First LLM (study series) · **Visibility:** set by Waqar at upload

## Description

We assemble a complete GPT: a GPTConfig dataclass, a ModuleList of Transformer blocks, the final LayerNorm, the language-modelling head and weight tying, then verify it with five sanity checks. Then we load real GPT-2 weights into our own code — and the book's notebook produces 'The quick brown foxeseseses…'. I trace the bug (dropped attention biases plus the GELU variant), fix it in three lines, and match Hugging Face GPT-2 to 6e-5. CPU run of the ch11 notebook, my own experiments, parameter breakdown, solved exercises and book corrections.

This is part of my study series on the book "Build Your First LLM: A Hands-On Guide to Language Models" by Hasan Degismez. All slides, narration and diagrams are my own teaching adaptation. Please support the author and buy the book: https://leanpub.com/FirstLLM/

📌 Chapters
0:00 Intro & roadmap
1:46 Part 1 — From block to model
2:53 Part 2 — `GPTConfig`
3:24 Part 3 — `MiniGPT`
4:54 Part 4 — Weight tying
5:50 Part 5 — Five sanity checks
7:58 Part 6 — First forward pass
8:35 Part 7 — Loading GPT-2 — the bug and the fix
12:00 Part 8 — Exercises and review
14:02 Practice this
14:32 Credits

💻 Code (FirstLLM/code, MIT License)
- Notebook: https://github.com/FirstLLM/code/blob/main/notebooks/ch11.ipynb
- Run in Colab: https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch11.ipynb
- Slides + study notes: https://github.com/waqarys/Courses/tree/build-your-first-llm/build-your-first-llm

📚 Credit
Based on "Build Your First LLM" by Hasan Degismez — https://leanpub.com/FirstLLM/
Code: https://github.com/FirstLLM/code (MIT License)
Narration voice: synthetic (Kokoro TTS).

#LLM #Transformers #MachineLearning

## Tags
build your first llm, llm from scratch, transformers, attention mechanism, gpt-2, pytorch, deep learning, machine learning, large language models, hasan degismez, waqar shaikh builds, ai tutorial, building the transformer
