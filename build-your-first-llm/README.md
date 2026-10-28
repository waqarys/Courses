# Build Your First LLM — study course (Waqar Shaikh Builds)

A chapter-by-chapter study companion to **"Build Your First LLM: A Hands-On Guide to Language Models"** by **Hasan Degismez** (2025). Slides, study notes and narration are my own teaching adaptation. **Please buy the book:** <https://leanpub.com/FirstLLM/>.
Companion code: <https://github.com/FirstLLM/code> (MIT License).

Each chapter folder has:
- `slides.md` — Marp deck (16:9, dark theme; diagrams in `img/`)
- `notes.md` — long-form study notes with code references
- `script.md` — narration per slide
- `youtube.md` — title, description with timestamps, tags
- `captions.srt`, `timings.json`, `thumbnail.png`

Videos (MP4) are not stored in git; they are uploaded to YouTube.

## Chapters

| # | Chapter | Slides | Notes | Notebook | Status |
|---|---|---|---|---|---|
| 1 | What is AI, Really? | [slides](ch01-what-is-ai/slides.md) | [notes](ch01-what-is-ai/notes.md) | — (no notebook) | ✅ pilot |
| 2 | How Computers "Understand" Words | [slides](ch02-how-computers-understand-words/slides.md) | [notes](ch02-how-computers-understand-words/notes.md) | — | ✅ |
| 3 | The Attention Mechanism | [slides](ch03-the-attention-mechanism/slides.md) | [notes](ch03-the-attention-mechanism/notes.md) | — | ✅ |
| 4 | The Transformer Architecture | [slides](ch04-the-transformer-architecture/slides.md) | [notes](ch04-the-transformer-architecture/notes.md) | — | ✅ |
| 5 | Your First Python Program | [slides](ch05-your-first-python-program/slides.md) | [notes](ch05-your-first-python-program/notes.md) | [ch05](https://github.com/FirstLLM/code/blob/main/notebooks/ch05.ipynb) · [Colab](https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch05.ipynb) | ✅ |
| 6 | NumPy & PyTorch Survival Guide | [slides](ch06-numpy-pytorch-survival-guide/slides.md) | [notes](ch06-numpy-pytorch-survival-guide/notes.md) | [ch06](https://github.com/FirstLLM/code/blob/main/notebooks/ch06.ipynb) · [Colab](https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch06.ipynb) | ✅ |
| 7 | Preparing Your Data | [slides](ch07-preparing-your-data/slides.md) | [notes](ch07-preparing-your-data/notes.md) | [ch07](https://github.com/FirstLLM/code/blob/main/notebooks/ch07.ipynb) · [Colab](https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch07.ipynb) | ✅ |
| 8 | Building the Tokenizer | [slides](ch08-building-the-tokenizer/slides.md) | [notes](ch08-building-the-tokenizer/notes.md) | [ch08](https://github.com/FirstLLM/code/blob/main/notebooks/ch08.ipynb) · [Colab](https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch08.ipynb) | ✅ |
| 9 | The Embedding Layer | [slides](ch09-the-embedding-layer/slides.md) | [notes](ch09-the-embedding-layer/notes.md) | [ch09](https://github.com/FirstLLM/code/blob/main/notebooks/ch09.ipynb) · [Colab](https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch09.ipynb) | ✅ |
| 10 | Attention Is All You Need | [slides](ch10-attention-is-all-you-need/slides.md) | [notes](ch10-attention-is-all-you-need/notes.md) | [ch10](https://github.com/FirstLLM/code/blob/main/notebooks/ch10.ipynb) · [Colab](https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch10.ipynb) | ✅ pilot |
| 11 | Building the Transformer | [slides](ch11-building-the-transformer/slides.md) | [notes](ch11-building-the-transformer/notes.md) | [ch11](https://github.com/FirstLLM/code/blob/main/notebooks/ch11.ipynb) · [Colab](https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch11.ipynb) | ✅ |
| 12 | Training Your Model | | | [ch12](https://github.com/FirstLLM/code/blob/main/notebooks/ch12.ipynb) | planned |
| 13 | Fine-Tuning | | | [ch13](https://github.com/FirstLLM/code/blob/main/notebooks/ch13.ipynb) | planned |
| 14 | Prompt Engineering | | | [ch14](https://github.com/FirstLLM/code/blob/main/notebooks/ch14.ipynb) | planned |
| 15 | Building Applications | | | [ch15](https://github.com/FirstLLM/code/blob/main/notebooks/ch15.ipynb) | planned |
| 16 | Preparing for Production | | | [ch16](https://github.com/FirstLLM/code/blob/main/notebooks/ch16.ipynb) | planned |
| 17 | Deployment Options | | | [ch17](https://github.com/FirstLLM/code/blob/main/notebooks/ch17.ipynb) | planned |
| 18 | What's Next | | | [ch18](https://github.com/FirstLLM/code/blob/main/notebooks/ch18.ipynb) | planned |

## Errata
Book mistakes found while verifying the code: [ERRATA.md](ERRATA.md)

## Rebuilding a video
`_pipeline/` holds the build: Marp CLI renders slides to PNG, Kokoro TTS (voice `am_michael`) reads the `say:` notes in each slide, ffmpeg assembles a 1920×1080 30 fps H.264/AAC MP4 and writes `captions.srt` + `timings.json`.

```bash
npm i -g @marp-team/marp-cli
pip install kokoro-onnx soundfile numpy matplotlib torch transformers
python _pipeline/build.py ch10-attention-is-all-you-need
python _pipeline/youtube.py ch10-attention-is-all-you-need 10 "Attention Is All You Need" "<blurb>" ch10
```
(Kokoro model files `kokoro-v1.0.onnx` and `voices-v1.0.bin` from the kokoro-onnx releases; paths are set in `build.py`.)

## Credits
Based on "Build Your First LLM" by Hasan Degismez — <https://leanpub.com/FirstLLM/>. Code: <https://github.com/FirstLLM/code> (MIT). Course adaptation: Waqar Shaikh Builds.
