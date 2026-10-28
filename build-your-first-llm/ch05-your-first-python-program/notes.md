# Chapter 5 — Your First Python Program (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch05.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch05.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt) · **Exercise solutions (mine):** [exercises_solution.py](exercises_solution.py)

---

## 0. Why this chapter matters
Part II moves from theory to code. This chapter covers just enough Python to build **stage 1 of every LLM: the tokenizer**, which converts text to integer IDs and back. It also introduces the slicing pattern (`tokens[:-1]` → inputs, `tokens[1:]` → targets) used in every training loop later on.

### Learning goals
1. Run GPT-2 with Hugging Face `pipeline` and explain each stage.
2. Use variables, strings, slicing, numbers and f-strings.
3. Build a vocabulary with lists and dictionaries, including `<PAD>` and `<UNK>`.
4. Handle unknown words with `if/else` and `dict.get`, and write loops and list comprehensions.
5. Package the code as functions, then as a `SimpleTokenizer` class with a Hugging Face-like interface.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Variable | A name bound to a value |
| String | Text (`str`) |
| List | An ordered, indexable collection |
| Dictionary | Key → value mapping (`dict`) |
| Function | Reusable code: `def name(params): ... return value` |
| Class | A blueprint bundling state and methods; objects are its instances |
| Tokenizer | text ↔ token IDs |
| Token | One unit of text (word, subword or character) |

---

## 1. The hook: run GPT-2
Notebook cell 3 (MIT) loads `pipeline('text-generation', model='gpt2')` and generates 20 new tokens from "The secret to building AI is" with `do_sample=True`.

**My CPU run:** "The secret to building AI is to know that people are not afraid to learn. / Conducted by the National Academy of". Your output will differ because sampling is random. Note that `max_new_tokens` counts **tokens**, not words.

**Why Python?** It is readable, and it has the ecosystem (NumPy, PyTorch, Hugging Face). Python orchestrates; the heavy maths runs in optimised C/CUDA.

## 2. Text and numbers
- `len(output)` counts characters; `type(output)` → `<class 'str'>`; `.lower().split()` (method chaining).
- **Slicing:** `s[0]`, `s[-1]`, `s[:3]`, `s[4:]`; `output[len(prompt):]` = the generated part.
- `ids[:-1]` = all but the last item (inputs); `ids[1:]` = all but the first (targets).
- f-strings: `{n:,}` → 124,000,000; `{lr:.2e}` → 1.00e-04; `{vocab_size // 2}` → 25128.

> ⚠️ **Errata.** §5.4.1 says `print(len(output))  # 68`. The string has 12 words, i.e. **60 letters + 11 spaces = 71**. The book's own notebook prints **71**.

## 3. Vocabulary
- "The secret to building AI is" → GPT-2 IDs **[464, 3200, 284, 2615, 9552, 318]** (verified ✓).
- Collect the words with `extend` (not `append`, which would nest the lists).
- `vocab = {'<PAD>': 0, '<UNK>': 1}`, then give each new word `len(vocab)`. That makes 14 unique words + 2 specials = **16**.
- `<PAD>` pads batches to equal length. `<UNK>` is the fallback for unseen words.

## 4. Edge cases, loops, comprehensions
- `vocab['neural']` raises `KeyError`. Use `vocab.get(word, vocab['<UNK>'])` instead → 1.
- "The neural network learns" → `[2, 1, 1, 1]` with either the loop or the comprehension. Three unknowns shows the weakness of word-level tokenizers (subwords fix this in Ch 8).

## 5. Functions and the class
- `tokenize` / `detokenize`: the reverse mapping is built with `{v: k for k, v in vocab.items()}`. "The secret to AI" ↔ `[2, 3, 4, 6]` ("the secret to ai", with case lost). GPT-2 gives `[464, 3200, 284, 9552]`.
- **Class basics:** `__init__` sets the starting state, `self` is this object, methods live on the object, and `__len__` enables `len(tok)`.
- `SimpleTokenizer` (notebook cell 15): `fit`, `encode`, `decode`, `__len__`. Same interface pattern as `GPT2Tokenizer` (create → fit/load → encode/decode).

| | SimpleTokenizer | GPT-2 BPE |
|---|---|---|
| unit | words | subwords/bytes |
| vocab | grows with data | fixed 50,257 |
| unknowns | `<UNK>` | never (falls back to pieces) |
| case/space | lowercased, split on whitespace | case-sensitive; leading space is part of the token |

> ℹ️ "understanding" → `['under', 'standing']` only **without** a leading space. `" understanding"` is a single GPT-2 token (`Ġunderstanding`).

## 6. Full circle
`pipeline()` runs 5 stages: (1) tokenize → (2) embed → (3) 12 Transformer layers → (4) sample → (5) decode, then loops with the new token appended. Today we built stage 1.

**Next-token training data:** for "The cat sat on the mat", inputs = `ids[:-1]` and targets = `ids[1:]`, which gives 5 prediction problems from one sentence.

## 7. Exercises (my solutions, run and verified)
See [exercises_solution.py](exercises_solution.py).
1. **Punctuation strip:** `text.lower().translate(str.maketrans("", "", string.punctuation)).split()`. "learning, data!" → "learning data".
2. **Count unknowns:** `sum(self.encode(s).count(1) for s in sentences)`. My test sentences ("AI systems learn quickly", "Neural networks learn from data") gave 3.
3. **Save/load:** JSON-dump `word_to_id` and rebuild `id_to_word` on load. *Gotcha:* JSON keys are always strings, so don't save `id_to_word` directly. The round-trip gave identical encodings ✓.

## 8. Notebook run
- `ch05.ipynb` ran end-to-end on CPU (torch 2.x, recent `transformers`; the notebook pins `transformers==4.46.1`). **All 9 code cells passed, no errors.**
- Outputs match the book (IDs, vocab size 16, `[2,1,1,1]`, `[2,3,4,6]`) except `len(output)` = 71 (see errata).

## 9. Key takeaways
1. Python orchestrates optimised code: ~10 lines run a 124M-parameter model.
2. LLMs see token IDs, not words.
3. A vocabulary is a dict, with `<PAD>` and `<UNK>`.
4. encode: text → IDs; decode: IDs → text.
5. `SimpleTokenizer` mirrors Hugging Face's interface.
6. `tokens[:-1]` / `tokens[1:]` are the inputs and targets for training.

## 10. Review questions (my answers)
1. **What does GPT-2 see?** Integer token IDs from a 50,257-entry vocabulary.
2. **Why `.get(w, UNK)`?** It avoids a `KeyError` on unseen words and returns a safe default.
3. **Function vs class?** A function is one operation. A class bundles state (the vocabulary) with methods that use it.
4. **`tokens[:-1]`?** All but the last token: the inputs. Paired with `tokens[1:]` as targets, it gives next-token prediction.
5. **Similarity to Hugging Face?** The same create → fit/load → encode/decode pattern. HF adds BPE, special tokens, save/load and batching.

---
**Credits.** Based on *Build Your First LLM* by Hasan Degismez. Please buy the book: <https://leanpub.com/FirstLLM/>. Code shown verbatim: FirstLLM/code (MIT License), `notebooks/ch05.ipynb`. Notes, diagrams and exercise solutions are my own adaptation (Waqar Shaikh Builds).
