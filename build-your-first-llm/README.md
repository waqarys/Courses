# Zero to LLM — build your own language model (Waqar Shaikh Builds)

A self-produced YouTube course kit: **11 modules**, each ready to record with OBS + IntelliJ and edit in CapCut in about three hours.
Start with **[PIPELINE.md](PIPELINE.md)**.

## Course map
| # | Module | You build | Length | Folder |
|---|---|---|---|---|
| M01 | What an LLM Really Is | a bigram "dumbest LM" | ~12 min | [01_what-an-llm-really-is](modules/01_what-an-llm-really-is) |
| M02 | The 20 % of Python & PyTorch You Need | tensors, autograd, `nn.Module` | ~14 min | [02_python-pytorch-toolkit](modules/02_python-pytorch-toolkit) |
| M03 | From Raw Text to Token IDs | clean/dedup/split + BPE from scratch | ~15 min | [03_text-to-tokens](modules/03_text-to-tokens) |
| M04 | Embeddings: a Map of Meaning | lookup tables, GPT-2 neighbours, positions | ~13 min | [04_embeddings-meaning-map](modules/04_embeddings-meaning-map) |
| M05 | Attention from Scratch | causal multi-head attention | ~16 min | [05_attention-from-scratch](modules/05_attention-from-scratch) |
| M06 | Assemble the GPT | full GPT-2 + load real weights | ~16 min | [06_assemble-the-gpt](modules/06_assemble-the-gpt) |
| M07 | Train Your Own Tiny GPT | a char-level GPT trained on CPU | ~15 min | [07_train-your-own](modules/07_train-your-own) |
| M08 | Fine-Tuning & LoRA | LoRA from scratch on GPT-2 | ~14 min | [08_fine-tuning-and-lora](modules/08_fine-tuning-and-lora) |
| M09 | Prompts, Sampling & RAG | RAG app in pure Python + Grok API | ~16 min | [09_prompts-rag-and-apps](modules/09_prompts-rag-and-apps) |
| M10 | Ship It: Fast, Small, Online | KV cache, int8, a web API | ~14 min | [10_ship-it-fast-and-cheap](modules/10_ship-it-fast-and-cheap) |
| M11 | What's Next + Capstone | "Ask My Notes" scaffold | ~12 min | [11_whats-next-and-capstone](modules/11_whats-next-and-capstone) |

Total ≈ 2 h 40 min of finished video.

## Every module folder
| File | What it is |
|---|---|
| `script.md` | teleprompter beats in segments `## S# · CAM/SLIDES/IDE · topic (≈time)` |
| `slides.md` / `slides.pdf` | Marp deck in the channel theme (bottom-right kept free for the webcam circle) |
| `livecode.md` | IntelliJ step plan: what to paste, what to type live, expected output |
| `snippets/*.py` | runnable code, verified on PyTorch 2.x CPU |
| `exercises.md` | exercises with collapsible solutions |
| `imagine.md` | Grok Imagine prompts: intro sting, thumbnail bg, b-roll, divider, outro |
| `grok_prompts.md` | Grok AI prompts: quiz, poll, extra exercises, script tighten, hooks, pinned comment, fact check |
| `youtube.md` | title, alt title, description, chapters, tags |

## Repo layout
```
PIPELINE.md            end-to-end production workflow + checklist + weekly cadence
modules/NN_slug/       the 11 modules (source of truth)
templates/             OBS scenes, CapCut template, thumbnail style, IntelliJ setup, Marp theme, webcam-circle assets
tools/prep_module.py   builds teleprompter/shot list/snippets/upload.json into build/ (stdlib only)
reference/             book ↔ module mapping, errata (67 verified) and where they're folded in, 18 study videos
archive/               v1 per-chapter study pack + automated video pipeline
```

## Quick start
```bash
python tools/prep_module.py 01        # → build/01_what-an-llm-really-is/
marp --theme-set templates/marp-theme.css modules/01_what-an-llm-really-is/slides.md -o build/01_what-an-llm-really-is/slides.html
```
Code setup: `pip install torch --index-url https://download.pytorch.org/whl/cpu && pip install numpy tiktoken transformers`.

## Credits
Recommended reading that inspired this series: **"Build Your First LLM" by Hasan Degismez** — <https://leanpub.com/FirstLLM/> (companion code: <https://github.com/FirstLLM/code>, MIT). Course scripts, analogies, code and visuals © Waqar Shaikh Builds.
