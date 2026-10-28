# YouTube upload — Chapter 8

**Title:** Build Your First LLM — Ch 8: Building the Tokenizer (Full Walkthrough)

**Duration:** 21:55 · **Slides:** 51 · **Thumbnail:** thumbnail.png · **Captions:** captions.srt (English)

**Playlist:** Build Your First LLM (study series) · **Visibility:** set by Waqar at upload

## Description

How text becomes token IDs and back. We build a character tokenizer and a word tokenizer with <UNK> from scratch, work through Byte-Pair Encoding step by step, train our own BPE tokenizer on TinyShakespeare (and fix its broken round trip), then use the production tools: tiktoken (GPT-4's cl100k_base) and Hugging Face. We finish with the quirks that change token counts and costs — leading spaces, numbers, emoji and other languages. Every output was checked against a real CPU run of the book's ch08 notebook; this chapter has a dozen printed outputs that don't match, all flagged on the slides.

This is part of my study series on the book "Build Your First LLM: A Hands-On Guide to Language Models" by Hasan Degismez. All slides, narration and diagrams are my own teaching adaptation. Please support the author and buy the book: https://leanpub.com/FirstLLM/

📌 Chapters
0:00 Intro & roadmap
1:45 Part 1 — Why tokenize?
2:51 Part 2 — Character-level tokenization
4:52 Part 3 — Word-level tokenization
7:30 Part 4 — Subwords and BPE
9:52 Part 5 — Training BPE on Shakespeare
13:35 Part 6 — Production tokenizers
15:55 Part 7 — Quirks and gotchas
18:08 Part 8 — To Chapter 9, exercises and review
21:00 Practice this
21:27 Credits

💻 Code (FirstLLM/code, MIT License)
- Notebook: https://github.com/FirstLLM/code/blob/main/notebooks/ch08.ipynb
- Run in Colab: https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch08.ipynb
- Slides + study notes: https://github.com/waqarys/Courses/tree/build-your-first-llm/build-your-first-llm

📚 Credit
Based on "Build Your First LLM" by Hasan Degismez — https://leanpub.com/FirstLLM/
Code: https://github.com/FirstLLM/code (MIT License)
Narration voice: synthetic (Kokoro TTS).

#LLM #Transformers #MachineLearning

## Tags
build your first llm, llm from scratch, transformers, attention mechanism, gpt-2, pytorch, deep learning, machine learning, large language models, hasan degismez, waqar shaikh builds, ai tutorial, building the tokenizer
