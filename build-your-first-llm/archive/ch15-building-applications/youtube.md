# YouTube upload — Chapter 15

**Title:** Build Your First LLM — Ch 15: Building Applications (Full Walkthrough)

**Duration:** 12:20 · **Slides:** 42 · **Thumbnail:** thumbnail.png · **Captions:** captions.srt (English)

**Playlist:** Build Your First LLM (study series) · **Visibility:** set by Waqar at upload

## Description

From model trainer to application builder: a chat loop with memory, retrieval-augmented generation (sentence embeddings, chunking, cosine retrieval, citations), a tool-calling preview, and trait-based evaluation. I ran the full pipeline on a real Llama 3.2 3B: retrieval and cited answers work, the book's eval set scores 5/8 (the empty-retrieval fallback makes the model answer anyway with a fake citation), and the 3B model never used the invented tool format. I also show that eval() with empty __builtins__ is not a sandbox, and that Llama 3.2's context window is 131,072 tokens, not ~8,192.

This is part of my study series on the book "Build Your First LLM: A Hands-On Guide to Language Models" by Hasan Degismez. All slides, narration and diagrams are my own teaching adaptation. Please support the author and buy the book: https://leanpub.com/FirstLLM/

📌 Chapters
0:00 Intro & roadmap
1:23 Part 1 — From trainer to builder
2:19 Part 2 — A chat loop with memory
3:37 Part 3 — RAG: retrieval-augmented generation
6:55 Part 4 — Tool calling
8:50 Part 5 — Testing and production tips
11:39 Practice this
11:54 Credits

💻 Code (FirstLLM/code, MIT License)
- Notebook: https://github.com/FirstLLM/code/blob/main/notebooks/ch15.ipynb
- Run in Colab: https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch15.ipynb
- Slides + study notes: https://github.com/waqarys/Courses/tree/build-your-first-llm/build-your-first-llm

📚 Credit
Based on "Build Your First LLM" by Hasan Degismez — https://leanpub.com/FirstLLM/
Code: https://github.com/FirstLLM/code (MIT License)
Narration voice: synthetic (Kokoro TTS).

#LLM #Transformers #MachineLearning

## Tags
build your first llm, llm from scratch, transformers, attention mechanism, gpt-2, pytorch, deep learning, machine learning, large language models, hasan degismez, waqar shaikh builds, ai tutorial, building applications
