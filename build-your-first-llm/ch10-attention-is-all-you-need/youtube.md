# YouTube upload — Chapter 10

**Title:** Build Your First LLM — Ch 10: Attention Is All You Need (Full Walkthrough)

**Duration:** 49:20 · **Slides:** 84 · **Thumbnail:** thumbnail.png · **Captions:** captions.srt (English)

**Playlist:** Build Your First LLM (study series) · **Visibility:** set by Waqar at upload

## Description

We build attention from scratch in PyTorch with every tensor shape tracked: Q/K/V projections, scaled dot-product attention (and why we divide by √d_k, measured), causal masking, efficient multi-head attention with the reshape trick, and a complete pre-norm Transformer block (FFN, GELU, LayerNorm, residuals) — 7,084,800 parameters, verified. Every notebook cell was run; outputs shown are real. Plus experiments with pretrained GPT-2: how "bank" changes meaning across layers, and what real attention heads look like.

This is part of my study series on the book "Build Your First LLM: A Hands-On Guide to Language Models" by Hasan Degismez. All slides, narration and diagrams are my own teaching adaptation. Please support the author and buy the book: https://leanpub.com/FirstLLM/

📌 Chapters
0:00 Intro & roadmap
2:33 10.1 Why Static Embeddings Aren't Enough
6:20 10.2 What IS Attention?
10:23 10.3 Building Self-Attention Step by Step
20:08 10.4 Causal Masking
23:52 10.5 From One Head to Many
29:51 10.6 The Complete Transformer Block
38:29 10.7 Visualising Attention
41:35 10.8 Practical Considerations
43:09 10.9 Key Takeaways
44:25 Review questions 1–3
47:34 Practice this (notebook ch10.ipynb)
48:53 Credits

💻 Code (FirstLLM/code, MIT License)
- Notebook: https://github.com/FirstLLM/code/blob/main/notebooks/ch10.ipynb
- Run in Colab: https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch10.ipynb
- Slides + study notes: https://github.com/waqarys/Courses/tree/build-your-first-llm/build-your-first-llm

📚 Credit
Based on "Build Your First LLM" by Hasan Degismez — https://leanpub.com/FirstLLM/
Code: https://github.com/FirstLLM/code (MIT License)
Narration voice: synthetic (Kokoro TTS).

#LLM #Transformers #MachineLearning

## Tags
build your first llm, llm from scratch, transformers, attention mechanism, gpt-2, pytorch, deep learning, machine learning, large language models, hasan degismez, waqar shaikh builds, ai tutorial, attention is all you need
