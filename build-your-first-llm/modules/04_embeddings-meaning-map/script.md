# M04 — Embeddings: Turning IDs into a Map of Meaning

Target length: **14 min** · Segments: 6
Big idea: *An embedding is a GPS coordinate for a word in "meaning space". Similar words live in the same neighbourhood; directions on the map carry meaning.*

## S1 · CAM · Hook (≈40s)
- Token 3290 and token 3797. Which one is "dog" and which is "cat"? The numbers don't tell you — and the model doesn't care.
- An ID is just a seat number in a stadium. Seat 3290 isn't more dog-like than seat 3291.
- So the model gives every seat a coordinate on a map of meaning. Today we draw that map.

## S2 · SLIDES · From seat numbers to coordinates (≈2.5 min)
- Slide: one-hot vs dense vectors.
- One-hot: a list of fifty thousand zeros with a single one. Every word is equally far from every other word. Useless for similarity.
- Dense: 768 numbers per token, learned. Words used in similar sentences drift close together during training.
- The famous idea: "you know a word by the company it keeps". Tea and coffee appear around "cup", "hot", "morning" — so they end up neighbours.
- Slide: the embedding table is literally a big matrix — vocab rows by 768 columns. Looking up a token = grabbing its row.

## S3 · IDE · Embedding lookup is just indexing (≈2.5 min)
- Snippet 01. nn.Embedding with num_embeddings and embedding_dim.
- Look up IDs — out comes a matrix of shape tokens × dim.
- Prove it's indexing: compare with emb.weight[ids]. Identical.
- Parameter count: vocab times dim. For GPT-2 that's 50257 × 768 — about 38.6 million, almost a third of the small model.

## S4 · IDE · Explore a real meaning map (≈3.5 min)
- Snippet 02 loads GPT-2's actual embedding table through Hugging Face.
- Cosine similarity: the angle between two arrows. 1 means same direction.
- Watch out — this is the trap: encode "king" without a space and you get a word-piece that's mostly used inside other words. Neighbours look like garbage.
- Encode " king" WITH the leading space — the way it appears mid-sentence — and the neighbours are kings, queen, prince, monarch.
- The analogy trick: king minus man plus woman. With space-prefixed tokens, " queen" comes out near the top.
- Lesson: always embed the token the model actually sees.

## S5 · SLIDES · Where am I in the sentence? Positions (≈2.5 min)
- Slide: "dog bites man" vs "man bites dog" — same tokens, opposite meaning.
- Attention, which we build next, has no built-in sense of order. So we add position information.
- Option A, learned: another table with one row per position. GPT-2 and BERT both do this.
- Option B, fixed sine waves — the original 2017 Transformer. Like a clock with many hands spinning at different speeds.
- Option C, rotary — RoPE: rotate the vectors by an angle that depends on position. Used by Llama, Mistral, Qwen and most current open models.
- In our build: token embedding plus position embedding, added together.

## S6 · CAM · Recap (≈40s)
- IDs are seat numbers; embeddings are coordinates.
- Lookup = indexing a learned table.
- Add position so order matters.
- Next: attention — how each word looks at the others. The heart of every LLM.
