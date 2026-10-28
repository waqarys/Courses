# YouTube upload — Chapter 13

**Title:** Build Your First LLM — Ch 13: Fine-Tuning Your Model (Full Walkthrough)

**Duration:** 14:02 · **Slides:** 46 · **Thumbnail:** thumbnail.png · **Captions:** captions.srt (English)

**Playlist:** Build Your First LLM (study series) · **Visibility:** set by Waqar at upload

## Description

Instruction data, loss masking, and LoRA adapters built from scratch. The chapter's notebook can't show any improvement (a randomly initialised base model and an empty test split: 69 FAQ examples, not 80+20), so I ran the same recipe on a pretrained GPT-2 small with LoRA on every attention projection and a real 55/14 split. Masked training loss fell from 3.15 to 0.73 and held-out word overlap rose from 5% to 18.5%, but exact match stayed at 0%: the adapter learned the company's voice and invented facts it never saw. I also check the 48x claim (it depends on layer shape), the swapped A/B naming versus the LoRA paper, and the file sizes.

This is part of my study series on the book "Build Your First LLM: A Hands-On Guide to Language Models" by Hasan Degismez. All slides, narration and diagrams are my own teaching adaptation. Please support the author and buy the book: https://leanpub.com/FirstLLM/

📌 Chapters
0:00 Intro & roadmap
1:26 Part 1 — Fine-tune, or just prompt better?
2:49 Part 2 — Instruction data
4:03 Part 3 — Supervised fine-tuning with loss masking
5:21 Part 4 — LoRA: low-rank adaptation
8:47 Part 5 — Evaluating the fine-tune
11:41 Part 6 — Shipping adapters
13:23 Practice this
13:36 Credits

💻 Code (FirstLLM/code, MIT License)
- Notebook: https://github.com/FirstLLM/code/blob/main/notebooks/ch13.ipynb
- Run in Colab: https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch13.ipynb
- Slides + study notes: https://github.com/waqarys/Courses/tree/build-your-first-llm/build-your-first-llm

📚 Credit
Based on "Build Your First LLM" by Hasan Degismez — https://leanpub.com/FirstLLM/
Code: https://github.com/FirstLLM/code (MIT License)
Narration voice: synthetic (Kokoro TTS).

#LLM #Transformers #MachineLearning

## Tags
build your first llm, llm from scratch, transformers, attention mechanism, gpt-2, pytorch, deep learning, machine learning, large language models, hasan degismez, waqar shaikh builds, ai tutorial, fine-tuning your model
