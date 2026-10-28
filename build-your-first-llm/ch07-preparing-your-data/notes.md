# Chapter 7 — Preparing Your Data (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>.
> **Code: FirstLLM/code (MIT License).** Notebook: <https://github.com/FirstLLM/code/blob/main/notebooks/ch07.ipynb> · Colab: <https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch07.ipynb>

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
A model can only learn what its data shows it. Leftover HTML, duplicates and leaked test text can quietly ruin training, so this chapter builds a small, repeatable pipeline: **source → clean → dedup → split → chunk → store (JSONL) → check**.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Corpus | The whole collection of training text |
| Cleaning | Removing markup and normalising whitespace and Unicode |
| Deduplication | Dropping repeated documents (exact: by hash; near: e.g. MinHash) |
| Split | Train / validation / test, by **document**, with a fixed seed |
| Chunk | A fixed-size window of text; overlap keeps context across edges |
| JSONL | One JSON object per line; easy to stream and append |
| Provenance | A record of where each file came from and its licence |

## 1. Sourcing text
- Use text you have the right to use. Public-domain books (e.g. Project Gutenberg) are ideal for learning.
- Check robots.txt and terms of service, strip personal data, and keep a provenance README.

## 2. Python tools used
- Files (`open`, `with`), `set` for seen-hashes, `json.dumps` per line.
- `re.sub(r'<[^>]+>', '', s)` to strip tags; `\s+` → single space.
- `hashlib.sha1(text.encode()).hexdigest()`. I checked that `sha1("hello world")` = `2aae6c35…` and that the book's digest example is right.

## 3. Cleaning
- Remove HTML, normalise Unicode (NFKC), collapse whitespace, strip.
- Decisions: keep case? keep punctuation? drop very short pieces? Usually keep case and punctuation for a generative model, and drop near-empty fragments.

## 4. Deduplication
- Exact dedup: hash the cleaned text and keep the first copy.
- Near-duplicates (boilerplate, small edits) need MinHash/LSH; exact hashing will miss them.
- **Order matters: dedup *before* split**, otherwise the same text can land in train and test (leakage).

## 5. Splitting
- Shuffle documents with a fixed seed, then cut by ratio (e.g. 80/10/10).
- Split by **document**, not by chunk, so neighbouring chunks don't straddle train and test.
- With only 3 documents, rounding makes ratios odd: the notebook gives **1 / 0 / 2** (see errata).

## 6. Chunking and storage
- Sliding window: size 800 characters, overlap 200 (stride 600).
- Store each chunk as a JSONL record: `text`, `source`, `split`, `length`.
- Sanity checks after every stage: count, average/min/max length, HTML leakage, duplicate rate, top words.

## 7. My experiment — three Wells novels
- Corpus: *The Time Machine*, *The War of the Worlds*, *The Invisible Man* (Gutenberg, public domain).
- GPT-2 tokenizer: about **4.3 characters per token**, so "4 chars ≈ 1 token" is a fair rule of thumb for English prose.
- 800-character chunks average **≈187 tokens**.
- Paragraph duplicate rate **0.38%**; **338** short paragraphs dropped.
- Chunk counts: 298 / 558 / 446.
- Top words in *The Time Machine*: the, and, **I** (first-person narrator), of.

## 8. Exercises (my answers)
1. Add a minimum-length filter: drop cleaned texts under 40 characters before dedup.
2. Near-duplicate detection: shingle into 5-word sets and compare with Jaccard similarity, or use MinHash for scale.
3. Change chunk size/overlap and watch the chunk count: smaller stride means more chunks and more repeated text.

## 9. Book checks (errata)
- §7.11 worked example: the printed split (1/1/1) can't come from the code shown. Running it gives **1 / 0 / 2**.
- `len('The bird flew over the house.')` is **29**, not 33.
- SHA-1 collision odds: "1 in 2^160" ignores the birthday bound (≈2^80 for any collision), and SHA-1 is cryptographically broken. It's fine for dedup, but don't call it collision-proof.

## 10. Review questions
1. Why deduplicate before splitting?
2. Why split by document and not by chunk?
3. What does overlap buy you, and what does it cost?
4. Why is JSONL convenient for big corpora?
5. Name three sanity checks to run after cleaning.

---
**Credit:** Based on *Build Your First LLM* by Hasan Degismez. Buy the book: <https://leanpub.com/FirstLLM/> · Code: <https://github.com/FirstLLM/code> (MIT). Notes, slides and narration are my own study materials.
