# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter nine of my study series on Build Your First LLM by Hasan Degismez. Today token IDs become vectors. We'll build token embeddings and position embeddings from scratch, combine them into GPT-2's embedding layer, and then open up the real GPT-2 to see what its embeddings learned. I ran the notebook and some experiments of my own, and one of them shows why the book's similarity search returns odd results, and how a single space fixes it.

## Slide 2 — Where we are

We have clean data and token IDs. Today those IDs become vectors that also know their position. Next chapter, attention lets those vectors look at each other. Everything follows the chapter nine notebook, linked in the description.

## Slide 3 — Chapter 9 roadmap

Here's the plan. Why token IDs alone fail. Token embeddings as a lookup table. Why order is invisible without positions, and how learned position embeddings fix it. Putting both together into GPT-2's embedding layer. Then exploring the real thing, some practical details, and the review.

## Slide 4 — Key terms for this chapter

Some terms. An embedding is a learned dense vector for a token. The lookup table is a matrix with one row per token. In GPT-2 the token table is called w t e, and the position table is called w p e. One hot is the naive alternative: a huge vector of zeros with a single one. And cosine similarity measures how aligned two vectors are.

## Slide 5 — Part 1

Part one. Why can't we feed token IDs straight into the network?

## Slide 6 — IDs are labels, not quantities

Token IDs are labels, not quantities. In GPT-2, space cat is three seven nine seven, space dog is three two nine zero, space car is one zero nine seven, and space kitten is forty two thousand one hundred and forty three. Numerically cat is close to dog and far from kitten, but that means nothing: the IDs come from the order in which BPE merges were learned. If a network multiplied raw IDs, it would treat cat as roughly one point one six times dog. We need a representation where distance means something.

## Slide 7 — ⚠️ Book check: the example IDs

A book check on those IDs. Three seven nine seven is right for cat, but it's the version with a leading space. Without the space, cat is nine two four six. The book's dog, four two seven three, is actually the token space pet, and its kitten ID is the token space W C. The real IDs are three two nine zero and forty two thousand one hundred and forty three. In the full pipeline example, mat is two six zero three, and the notebook agrees. And the batch example labelled I will help you actually decodes to I like animals you. The point the book makes is right; the specific numbers aren't.

## Slide 8 — One-hot vs dense

The naive alternative is one hot: a vector fifty thousand long with a single one. It's huge, and every pair of words is exactly the same distance apart. A dense embedding uses seven hundred and sixty eight learned numbers, and similar words can be close. Here's a nice fact I verified in code: multiplying a one hot vector by the embedding matrix gives exactly the same result as picking row three seven nine seven. An embedding lookup is just a fast one hot matrix multiply.

## Slide 9 — Why 768?

Why seven hundred and sixty eight? It's two to the eighth times three, which splits cleanly into twelve attention heads of sixty four each. GPT-2's sizes go from seven sixty eight up to sixteen hundred, and the largest GPT-3 uses twelve thousand two hundred and eighty eight. More dimensions means more capacity but more parameters. In GPT-2 small, the token table alone is thirty eight point six million of the one hundred and twenty four point four million parameters, nearly a third, which I counted from the real model.

## Slide 10 — Part 2

Part two. Token embeddings are just a lookup table.

## Slide 11 — The lookup (my redraw)

Here's the whole idea in one picture. The embedding matrix has one row per token, fifty thousand two hundred and fifty seven rows, and seven hundred and sixty eight numbers per row. Token ID three seven nine seven, space cat, simply selects row three seven nine seven. No arithmetic, just indexing.

## Slide 12 — Manual lookup with fancy indexing (cells 8–12)

In code, it's fancy indexing. A random matrix of fifty thousand by seven sixty eight. Index it with three IDs and you get three rows, shape three by seven sixty eight. Index it with a batch of two sequences of four, and you get two by four by seven sixty eight. Remember this shape rule: batch by sequence becomes batch by sequence by embedding dimension.

## Slide 13 — `TokenEmbedding` (notebook cell 14)

The module version wraps nn dot Embedding, which is the same table but registered as a trainable parameter. It's initialised from a normal distribution with standard deviation zero point zero two, GPT-2's choice. Forward just looks up the IDs. On my run, one sequence of four becomes one by four by seven sixty eight, and the values are small, around plus or minus zero point zero two, exactly as initialised.

## Slide 14 — Part 3

Part three. Why position matters.

## Slide 15 — Order is invisible to attention (my experiment)

I tested this directly. I embedded the cat sat and sat cat the with the same table, and ran both through a real PyTorch attention layer. Without positions, the output for cat in the first sentence is exactly the output for cat in the second, just at a different index. Attention is permutation equivariant: shuffle the input, and the output shuffles the same way, and nothing else changes. Once I added position embeddings, the outputs differed. So without position information, dog bites man and man bites dog would mean the same thing to the model.

## Slide 16 — Two ways to add position

There are several ways to add position. Learned absolute embeddings, a trainable table with one vector per position, used by GPT-2 and BERT. Sinusoidal encodings, fixed waves from the original transformer paper. And rotary embeddings, RoPE, which rotate queries and keys by an angle that depends on position. The book describes GPT-2 as a modern LLM that prefers learned embeddings; GPT-2 is from twenty nineteen, and most current open models such as LLaMA, Mistral and Qwen use RoPE. I added that row myself. We'll implement learned positions, like GPT-2.

## Slide 17 — `PositionalEmbedding` (notebook cell 18, condensed)

The position module is another embedding table, indexed by position instead of token ID. Forward reads the sequence length, checks it against the maximum, creates positions zero to length minus one on the same device as the input, adds a batch dimension with unsqueeze, and expands it across the batch without copying memory. Then it looks them up. Note it never looks at the token values, only at the shape.

## Slide 18 — What happens past `max_seq_len`? (my run)

What if a sequence is longer than the table? I tried looking up fifteen hundred positions in a table of one thousand and twenty four, and got index error, index out of range in self. That's the cryptic error that the explicit check replaces with a clear message. And it's a real limitation of learned positions: there's no vector for position one thousand and twenty four, because it was never trained. The usual fixes are truncating or sliding a window over long text.

## Slide 19 — Part 4

Part four. Combining token and position embeddings.

## Slide 20 — Add, don't concatenate (my redraw)

We combine the two by simple element wise addition. The token vector says what, the position vector says where, and their sum carries both in the same seven sixty eight dimensions. Concatenating would double the width to fifteen thirty six and make every later layer bigger. Addition works because in a high dimensional space the network can learn to use somewhat different directions for content and for position.

## Slide 21 — `GPT2Embeddings` (notebook cell 20, condensed)

Here's the complete GPT-2 embedding layer. Two tables, both initialised with standard deviation zero point zero two. Forward builds the position indices exactly as before, looks up both, and adds them. Batch by sequence in, batch by sequence by seven sixty eight out. In the notebook, a batch of two sequences of six gives two by six by seven sixty eight.

## Slide 22 — Full pipeline: text → vectors (cell 22 — my run)

Now the full pipeline. The GPT-2 tokenizer turns the cat sat on the mat into six IDs, and our embedding layer turns them into one by six by seven sixty eight. The book lists three common mistakes worth remembering: passing token IDs to the position table instead of positions, creating positions on the CPU when the input is on the GPU, and forgetting the length check.

## Slide 23 — Part 5

Part five. Let's open up the real, trained GPT-2.

## Slide 24 — Loading `wte` and `wpe` (cell 24)

Hugging Face exposes the two tables as w t e and w p e: fifty thousand by seven sixty eight, and one thousand and twenty four by seven sixty eight. I measured their spread. The trained token table has a standard deviation of about zero point one four four, and the position table about zero point one two three. Both started at zero point zero two, so training spread them out by about seven times.

## Slide 25 — ⚠️ Book check: "similar words" (notebook cell 26)

Here's the book check. The book shows a beautiful list for king: prince, queen, kingdom, royal, throne. When I ran the notebook, the nearest neighbours of king were ked, KING in capitals, kers and ker. Why? Encoding king without a leading space gives the no space token, which is mostly used as a fragment inside other words, for example at the end of making. Its neighbours are other fragments. The function also assumes the top hit is always the word itself, which isn't guaranteed. The book's printed lists don't come from this code.

## Slide 26 — The one-space fix (my experiment)

The fix is one character. Use space king, the token for king in the middle of a sentence. Now the neighbours are kings, King, queen, prince and monarch. Space computer gives computers and laptop. Space doctor gives doctors and physician. Space fast gives faster and quick. Even so, notice that most top hits are case and plural variants of the same word. GPT-2's input embeddings encode spelling and form as much as meaning.

## Slide 27 — Analogies, fixed (my experiment)

Same story with analogies. The notebook's king minus man plus woman returns ked and KING. With the space prefixed tokens, the top answer is queen, at zero point seven one, followed by princess. And Paris minus France plus Germany gives Berlin, then Munich. So the classic analogy really does work in GPT-2's input embeddings, as long as you look up the right tokens. Note that the three input words are excluded from the results, which is standard practice and flatters these tests a little.

## Slide 28 — What did `wpe` learn? (my experiment)

And what did the position table learn? On the left, the cosine similarity between every pair of the first two hundred and fifty six positions. There's a bright diagonal band: nearby positions have similar vectors, and similarity fades with distance. On the right, a few individual dimensions plotted across all positions: smooth, slowly varying curves. Nobody told GPT-2 to do this; it learned a smooth sense of order purely from predicting the next token.

## Slide 29 — Part 6

Part six. Some practical details.

## Slide 30 — Initialization

Initialization. GPT-2 and BERT use a normal distribution with standard deviation zero point zero two. Too large and activations blow up early in training; too small and the signal is tiny and learning starts slowly. The book calls zero point zero two proven across billions of training runs. I'd call it a well tested default rather than a law: many newer models scale their initialization with the model width.

## Slide 31 — Devices and length checks

Devices and length checks. Creating positions with device equals token IDs dot device means they always follow the input. If the model is on the GPU and the IDs are on the CPU, you get a runtime error, so move the IDs first; that's exercise six. And validate the length with a clear error message.

## Slide 32 — Weight tying

Weight tying. On the way in, a token ID selects a row of the embedding matrix. On the way out, the final hidden state is multiplied by the transpose of that same matrix to get a score for every token. Sharing one matrix for both saves thirty eight point six million parameters in GPT-2 small, and it makes intuitive sense: if a hidden state points towards cat's embedding, cat should score highly. GPT-2 ties them, and we'll do the same in chapter eleven.

## Slide 33 — Embeddings are **static** — attention fixes that

One important limitation. These embeddings are static. Space bank has exactly the same vector in river bank and in savings bank. Attention, in chapter ten, lets each token look at its neighbours and update its vector, so after attention the two banks become different.

## Slide 34 — Part 7

Part seven. Exercises and review.

## Slide 35 — Exercises (my answers)

Exercise answers. Exercise one: a ten by eight matrix, three IDs, and the lookup gives three by eight. The notebook cell for this is a template with question marks, so it raises a syntax error until you fill it in; that's intended, not a bug. Exercise three: positions are looked up by index, so position zero gets the same vector whatever token is there. Exercise four: pad the shorter sequence to eight, giving two by eight by d, and later use an attention mask so padding is ignored. Exercise five: use the space prefixed tokens. Exercise seven: slice the IDs to the maximum length before embedding.

## Slide 36 — Key takeaways

Key takeaways. Token IDs are labels; embeddings give them geometry. An embedding layer is a lookup table, equivalent to a one hot matrix multiply. Attention can't see order, so we add position embeddings. GPT-2 adds token and learned position embeddings in seven sixty eight dimensions. Real GPT-2 embeddings do cluster related words, as long as you use the space prefixed token. And embeddings are static until attention makes them contextual.

## Slide 37 — Notebook run & book check

The notebook ran on my CPU; the only error is the exercise template, which is meant to be filled in. The book checks: several example token IDs are wrong, the printed similarity and analogy results don't come from the code shown, and the fix is a leading space, and current models mostly use RoPE rather than learned positions. All of these are in the errata file in the repo.

## Slide 38 — Review questions

Pause and try these. Why raw IDs fail. The shapes for a vocabulary of ten thousand, dimension five twelve, and a batch of four by twenty; the answer is a ten thousand by five twelve table and an output of four by twenty by five twelve. Two sentences with the same words but different meanings. Add versus concatenate. What the initialization does. What happens past the maximum length. And from our own experiment, why king returned ked.

## Slide 39 — Practice this

To practise: run the notebook, then add a leading space to the similarity queries and run it again. Plot the position similarity across all one thousand and twenty four positions. And compare cat with kitten, dog and car. I got cosine similarities of zero point five, zero point four five and zero point three eight, which is at least in the right order.

## Slide 40 — Up next: Chapter 10

Next time, chapter ten: self attention in code, where tokens finally look at each other.

## Slide 41 — Credits

This video is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams here are my own, but the book goes deeper, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. Thanks for watching, and see you in chapter ten.

