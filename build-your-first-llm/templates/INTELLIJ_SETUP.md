# IntelliJ IDEA for recording (Python)

1. Install the **Python** plugin (Community: "Python Community Edition"; Ultimate: "Python"). Settings → Plugins.
2. One project for the whole course: `D:\ZeroToLLM\code\zero-to-llm` with folders `m01 … m11`.
3. Interpreter: File → Project Structure → SDK → Add Python SDK → **Virtualenv** → new at `.venv`, Python 3.11/3.12. Then in the terminal:
   `pip install torch --index-url https://download.pytorch.org/whl/cpu` and `pip install numpy tiktoken transformers`
   (use the CUDA wheel instead if you have an NVIDIA GPU — see pytorch.org.)
4. Pre-download models off camera once: run `m04/02_gpt2_meaning_map.py` (caches GPT-2 in `%USERPROFILE%\.cache\huggingface`).
5. Recording look:
   - Theme: **Dark** (Darcula / New UI Dark) to match slides.
   - Editor font JetBrains Mono **20**, line spacing 1.2 · Settings → Editor → Font.
   - View → Appearance → **Presentation Mode** for full-screen talk-throughs, or **Zen Mode** while typing.
   - Hide: tool window bars, breadcrumbs, inlay hints (Settings → Editor → Inlay Hints → off), "Code With Me", notifications (Do Not Disturb).
   - Run tool window docked at bottom, font 16 (Settings → Editor → Color Scheme → Console Font).
   - Install the **Presentation Assistant** plugin so shortcuts you press appear on screen — viewers love it, and you never have to explain keys.
6. Snippets for "pasted live" code:
   - Simplest: keep `build/<module>/snippets/` open in a second IntelliJ tab group or Scratch file and copy blocks.
   - Faster: **Live Templates** (Settings → Editor → Live Templates → `+` group "ztl"): abbreviation `m05a` → paste the snippet body. Typing `m05a` + Tab inserts the whole file on camera — looks like magic, zero typos.
7. Shortcuts you'll use on camera: Run current file **Ctrl+Shift+F10**, Rerun **Shift+F10**, Terminal **Alt+F12**, Python Console (Tools → Python Console).
8. Before each IDE segment: close other tabs, clear the Run window, set zoom to 100 %, Do Not Disturb on Windows (Win+N → Do not disturb).
