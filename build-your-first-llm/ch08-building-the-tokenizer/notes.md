# Chapter 8 — Building the Tokenizer (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch08.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch08.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
Models only see integers. The tokenizer converts text to IDs on the way in and IDs back to text on the way out, and its choices affect sequence length, cost, multilingual fairness and even arithmetic.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Token | A unit of text with an integer ID |
| Vocabulary | Every token the tokenizer knows |
| Encode / decode | Text → IDs / IDs → text |
| `<PAD>` `<UNK>` `<BOS>` `<EOS>` | Structural tokens: padding, unknown, start, end |
| BPE | Learn subwords by repeatedly merging the most frequent adjacent pair |
| Byte-level BPE | BPE over UTF-8 bytes; spaces live inside tokens; never needs `<UNK>` |
| Round trip | `decode(encode(x)) == x`; the first test for any tokenizer |

## 1. Character tokenizer
- `fit`: `sorted(set(text))` gives deterministic IDs. Space and punctuation sort first.
- `encode`: a dictionary lookup per character. It raises KeyError on unseen characters.
- `decode`: `"".join(...)`.
- Tradeoff: a tiny vocabulary but sequences as long as the text. My run: the notebook sentence is 53 characters and 53 tokens, with a vocab of 22.

## 2. Word tokenizer
- Lowercase, `.split()`, `Counter.most_common(max_vocab-4)`. IDs 0–3 are reserved for specials.
- `encode` uses `.get(w, 1)`, so unknown words map to `<UNK>`. The round trip is lossy because of lowercasing and `<UNK>`.
- `.split()` keeps punctuation (`mat.`). A regex like `\b\w+\b` is cleaner.
- **Tie-breaking:** `Counter` orders equal counts by first appearance. On tiny corpora this decides the vocabulary.
- Quick-brown-fox comparison (my run): characters give vocab 28 and length 43; words give vocab 12 and length 9.

## 3. Subwords and BPE
- Start from characters (or bytes), count adjacent pairs, merge the most frequent, repeat.
- BPE comes from Gage (1994, compression) and Sennrich et al. (2015, NMT). GPT-2 popularised byte-level BPE.
- Toy corpus `low×3 lower newest×2`: (l,o)×4 → (lo,w)×4 → then a 4-way tie at ×2. Tie-break rules differ between implementations.
- Cousins: WordPiece (BERT), Unigram/SentencePiece (T5). LLaMA 1/2 use SentencePiece BPE.

## 4. Training BPE on TinyShakespeare (my run)
- 1,115,394 characters. vocab 1000 and min_frequency 2 trained in **0.4 s** on CPU.
- `"To be or not to be, that is the question."` gives 14 tokens (`que`,`st`,`ion`). The decoded text has spaces before punctuation, so **the round trip is False**.
- Fix: use a `ByteLevel` pre-tokenizer + `ByteLevel` decoder + the byte alphabet. The round trip becomes True (`Ġbe` tokens).
- The base alphabet is sorted. Merges follow in learned order. The longest tokens are speaker names (BOLINGBROKE, GLOUCESTER), because formatting gets learned too.
- Vocab sweep: 500 → 2.49, 1000 → 2.91, 2000 → 3.36, 5000 → 3.86 chars/token.
- Saved JSON: 59,956 bytes (this depends on the library version).

## 5. Production tokenizers
- **tiktoken `cl100k_base`** (GPT-4 / 3.5-turbo): 100,277 tokens. "Hello, world! How are you?" gives 8 tokens and a lossless round trip.
- **HF `AutoTokenizer("gpt2")`**: the same 8 pieces with different IDs, plus an `attention_mask`.
- GPT-2 has `<|endoftext|>` = 50256 as BOS/EOS and no PAD.
- Vocab sizes:
  - GPT-2/3: 50,257
  - cl100k: 100,277
  - o200k: ~200k
  - BERT: 30,522
  - LLaMA 1/2: 32,000
  - LLaMA 3: 128,256

## 6. Quirks (all measured with cl100k)
- Leading space: `Hello` is 9906, ` Hello` is 22691, `world` is 14957, ` world` is 1917.
- Numbers are chunked into groups of at most 3 digits: `1000` → `100|0`, `2024` → `202|4`. "…10000." takes 7 tokens and "…ten thousand." takes 6.
- Emoji: 😀 = 2, 🚀 = 3, 👍 = 3, 🔥🔥🔥 = 9. Inside "Hello 😀 world", ` 😀` is a single token.
- Other languages: café = 2, naïve = 3, 日本語 = 4, "Привет мир" = 5.

## 7. Connecting to Chapter 9
- Each JSONL record gets `token_ids` and `token_count`.
- `nn.Embedding(num_embeddings=50257, embedding_dim=768)` has ≈38.6M parameters.

## 8. Exercises (my answers)
1. "Artificial intelligence systems require careful data preparation and tokenization.":
   - Character tokenizer: vocab 23, length 82.
   - Word tokenizer: vocab 13, length 9, no `<UNK>`.
2. On a Gutenberg chapter, characters give the longest sequence, words the largest vocabulary, and cl100k the best balance.
3. Cost ≈ (input tokens + max output tokens) × current price.
4. The leading space changes the ID for every word tried. For rare words it can change the count too.
5. English is usually cheapest in cl100k.
6. Use the JSONL vocab inspector with `"ing" in token`, `max(key=len)` and `token.isdigit()`.

## 9. Book checks (errata)
- Character example: 53 characters / vocab 22, not 54 / 24. Quick brown fox: 43 / 28, not 44 / 20. Word vocab 12, not 13.
- Word vocab example: `'on':5, 'mat.':6 … 'was':9`, not `dog`, because ties go to first appearance.
- Coverage at vocab 10: 1/5 unknown, not 3/5.
- "tokenization" is 12 characters, not 13.
- Shakespeare BPE: 14 tokens and round trip **False**, not 12 / True.
- The modern sentence is 18 tokens, not 14.
- The low IDs are a sorted alphabet, not frequency-ordered.
- cl100k counts:
  - Hamlet line: 12, not 11.
  - Backprop sentence: 9, not 8.
  - The three prompts: 7/15/10, not 6/14/9.
- Emoji are 2–3 tokens each, not 1.
- `nn.Embedding(vocab_size=…)` raises TypeError. The parameter is `num_embeddings`.

## 10. Review questions
1. Give numbers for the vocab-size vs sequence-length tradeoff.
2. When are `<UNK>` and `<PAD>` used?
3. Explain BPE. Why do "-ing" and "un-" emerge?
4. Why do "Hello" and " Hello" differ?
5. Why can digits cost more than words?
6. Chinese chatbot: tiktoken or a custom tokenizer?
7. Why did our Shakespeare round trip fail, and how do you fix it?

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
