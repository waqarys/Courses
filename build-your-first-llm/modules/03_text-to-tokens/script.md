# M03 — From Raw Text to Token IDs (data + tokenizers)

Target length: **16 min** · Segments: 7 · Book chapters clubbed: data prep + tokenizer
Big idea: *A tokenizer is a LEGO sorting system: too few brick types and every model is huge; too many and you can't store the box. BPE learns the bricks that appear most often.*

## S1 · CAM · Hook (≈40s)
- Models can't read. They only eat numbers.
- So before any AI happens, someone has to turn "Hello world" into something like 15496, 995.
- How you cut text into pieces decides how much a model can read, how much it costs, and even why it's bad at spelling.
- Today: clean a dataset, then build three tokenizers — and watch the one GPT uses invent its own vocabulary.

## S2 · SLIDES · Garbage in, garbage out (≈2 min)
- Slide: the data pipeline — collect, clean, deduplicate, split.
- Clean: normalise whitespace and odd Unicode, strip boilerplate like navigation menus and licence footers.
- Deduplicate: if the same paragraph appears 500 times, the model memorises it. We hash each document and keep the first copy.
- A note on hashes: SHA-1 is fine as a fingerprint for dedup. It's not safe for security — real collisions have been produced.
- Split: train, validation, test. Validation is the quiz during the term; test is the final exam you only sit once.
- Tiny-data trap: with only 3 documents, an 80/10/10 split rounds weirdly — you can get one train, zero validation, two test. Always print your split sizes.

## S3 · IDE · Clean, dedup, split (≈2.5 min)
- Snippet 01. Our corpus has a duplicate and messy spacing.
- clean() squeezes whitespace. dedup() uses a hash set.
- Run it. Notice the printed split sizes — we check them, we don't trust them.

## S4 · SLIDES · Three ways to cut text (≈2.5 min)
- Slide: characters, words, subwords — the LEGO analogy.
- Characters: tiny vocabulary, maybe 100 bricks, but every sentence becomes a very long chain. Long chains cost compute.
- Words: short chains, but the vocabulary explodes and any new word — "ChatGPTing" — becomes unknown.
- Subwords: the sweet spot. Common words are one brick; rare words snap together from parts: "token" + "ization".
- Slide: GPT-2's quirk — the space belongs to the next word. " cat" with a space and "cat" without are different tokens with different IDs.

## S5 · IDE · Build char + word tokenizers, then BPE from scratch (≈5 min)
- Snippet 02: character tokenizer. Vocabulary = sorted set of characters. Encode, decode, round-trip check.
- Word tokenizer: split on spaces. Try a sentence with a new word — it hits unknown.
- Snippet 03: byte-pair encoding from scratch in 30 lines.
- Start with characters. Count every adjacent pair. Merge the most frequent pair into a new brick. Repeat.
- Run it and watch the merges print: first "a t" → "at", then "t h" → "th", then "th e" → "the", and soon whole words like "the_" with the end-of-word marker.
- That's the whole algorithm. GPT-2 did about fifty thousand merges on bytes.
- Snippet 04: compare with the real thing, tiktoken. Note " cat" vs "cat" have different IDs.
- Emoji cost: one emoji can be several tokens because they're multi-byte. Print it and see.

## S6 · SLIDES · Why tokenization explains LLM weirdness (≈1.5 min)
- Spelling and letter-counting: the model sees bricks, not letters.
- Non-English languages often need more tokens per word — more cost, less context.
- Numbers get chopped inconsistently — one reason arithmetic is shaky.
- Prices: APIs charge per token. Count them before you pay.

## S7 · CAM · Recap (≈40s)
- Clean, dedup, split — and print the sizes.
- Characters, words, subwords. BPE merges frequent pairs.
- Token IDs are just row numbers. Next module we give each row a meaning: embeddings.
