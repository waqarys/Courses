# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter eleven of my study series on Build Your First LLM by Hasan Degismez. Today we assemble everything into a complete GPT: a config object, a stack of transformer blocks, a final layer norm, a language modelling head and weight tying. Then we run five sanity checks and load the real GPT-2 weights into our own code. And that's where my run of the notebook turned up the most interesting bug in the series so far: the loaded model produces garbage, and I'll show you exactly why, and the two line fix that makes it match GPT-2 to four decimal places.

## Slide 2 — Where we are

We built embeddings in chapter nine and the transformer block in chapter ten. Today we stack the blocks into a complete model and load real GPT-2 weights into it. Next chapter we train it ourselves. Everything follows the chapter eleven notebook.

## Slide 3 — Chapter 11 roadmap

Here's the plan. What a single block is missing. The configuration pattern. The full model class. Weight tying. Five sanity checks. A forward pass with random weights. Loading GPT-2, including the bug and the fix. Then training versus evaluation mode, exercises and review.

## Slide 4 — Key terms for this chapter

A few terms. The language modelling head maps a seven sixty eight hidden state to a score for each of fifty thousand tokens. Those raw scores are logits. Weight tying reuses the embedding matrix for that head. Module list registers a list of layers properly. A config object holds every hyperparameter. And greedy decoding always picks the top token.

## Slide 5 — Part 1

Part one. From a single block to a full model.

## Slide 6 — The complete model (my redraw)

Here's the whole model. Token IDs go into the token and position embeddings, giving batch by sequence by seven sixty eight. Then twelve identical blocks, each with layer norm, attention and a residual, then layer norm, feed forward and a residual. The shape stays the same all the way through. A final layer norm, and then the head projects to fifty thousand two hundred and fifty seven scores per position. The dashed arrow is weight tying: the head reuses the embedding matrix.

## Slide 7 — Why stack identical blocks?

Why stack identical blocks? Every block has the same architecture but its own learned weights, and each one adds a refinement to the residual stream. Research that probes trained models finds a rough trend: earlier layers capture more local and syntactic patterns, later ones more semantic and task specific ones. The book uses a team of detectives as an analogy. It's a helpful picture, but the real division of labour is much messier.

## Slide 8 — Part 2

Part two. The configuration object.

## Slide 9 — A dataclass for hyperparameters (notebook cell 8)

All seven hyperparameters live in one dataclass, with GPT-2 small as the default. Post init runs right after construction and checks that the embedding dimension divides evenly by the number of heads. A tiny model for experiments is just a different set of arguments. And because it's a dataclass, a typo in a field name is an error, not a silently created new key as with a dictionary.

## Slide 10 — Part 3

Part three. The MiniGPT class.

## Slide 11 — `__init__` (notebook cell 10, condensed)

The constructor has the two embedding tables and dropout, a module list of transformer blocks, the final layer norm, and the head, a linear layer from seven sixty eight to the vocabulary with no bias. The last line ties the weights: the head's weight becomes the very same tensor as the token embedding.

## Slide 12 — Why `nn.ModuleList`, not a list?

Why a module list? A plain Python list hides the blocks from PyTorch. They don't appear in model dot parameters, they don't move with dot to device, and they aren't saved in the state dict. The optimizer would never update them, so training would appear to run while the blocks stay random. It's a classic silent bug.

## Slide 13 — `forward` (notebook cell 10, condensed)

The forward pass. Embed tokens and positions and add them; the position embeddings broadcast across the batch. Build a lower triangular causal mask. Run every block, final layer norm, and the head. The output is batch by sequence by vocabulary: a full set of next token scores at every position, which is what makes training so efficient.

## Slide 14 — Logits: a score for every token

Logits are a raw score for every token at every position. Softmax turns them into probabilities. During training, every position predicts its own next token, so one sequence gives many training examples at once. During generation, we only look at the last position.

## Slide 15 — Part 4

Part four. Weight tying.

## Slide 16 — One matrix, two jobs

The embedding matrix maps an ID to a vector. The head maps a vector to scores by multiplying with the transpose of a matrix of the same shape. Tie them, and you save thirty eight point six million parameters, about thirty one percent of GPT-2 small. In PyTorch, assigning the weight attribute makes both modules point at one tensor; an update through either path changes both.

## Slide 17 — ⚠️ Book check: weight-tying gotchas (my run)

The book lists four gotchas. Three are right. But it says lm head dot weight shouldn't appear in the state dict keys. In my run, it does: the state dict lists both keys. They share storage, so torch dot save writes the data only once and the file doesn't double in size. Also remember to tie only after both layers exist, and if you ever replace the tensor rather than copying into it, you have to tie again.

## Slide 18 — Part 5

Part five. Five sanity checks before any training.

## Slide 19 — The five checks (notebook cells 13–17 — my run)

The five checks all passed on my CPU. Shape: two by sixteen IDs become two by sixteen by fifty thousand two hundred and fifty seven logits. Parameter count. Causal masking: changing only the last token leaves the logits at earlier positions identical. Weight tying: the two weights are literally the same object. And gradient flow: every parameter receives a gradient. Keep an eye on that parameter count; it's a clue.

## Slide 20 — The causal-mask test (notebook cell 15)

The causal test is my favourite. Two inputs that differ only in the last token. Positions zero to two must produce identical logits, because they can't see the future, and position three must differ. If the mask were broken, the model could peek at the answer during training: the loss would look fantastic, and generation would be useless.

## Slide 21 — Parameter count: where do 124M go? (my redraw)

Here's where GPT-2 small's parameters live, from my own count, which matches Hugging Face exactly at one hundred and twenty four million four hundred and thirty nine thousand eight hundred and eight. The feed forward layers are the biggest share at forty five percent. The tied embedding is thirty one percent, attention twenty three percent, and positions and layer norms are tiny.

## Slide 22 — ⚠️ Book check: the parameter count

And here's the clue. The book prints one hundred and twenty four million four hundred and thirty nine thousand eight hundred and eight, the real GPT-2 number. But the notebook's model has thirty six thousand eight hundred and sixty four fewer parameters. That's exactly twelve layers times two thousand three hundred and four plus seven hundred and sixty eight: the query key value bias and the output projection bias. The notebook's attention is built without biases, but GPT-2's attention has them. Keep that in mind. As a small aside, the book's rough formula evaluates to one hundred and twenty four million three hundred and fifty six thousand eight hundred and sixty four, not the number printed.

## Slide 23 — Part 6

Part six. Our first forward pass, with random weights.

## Slide 24 — Random weights → random words (cells 19–20 — my run)

With random weights, the four token prompt gives a one by four by fifty thousand logits tensor, and the top predictions are random junk like RC and Abel, each with probability about one in ten thousand. An untrained model is close to uniform over fifty thousand tokens. That gives a useful number for chapter twelve: the starting loss should be about the natural log of fifty thousand, around ten point eight. If your first loss is far from that, something's wrong.

## Slide 25 — Part 7

Part seven. Loading GPT-2's weights, the bug, and the fix.

## Slide 26 — Name mapping and the transpose

To load GPT-2, we map names: w t e to token embed, h dot i dot l n one to our layer norms, c attn to our combined query key value projection, and so on. The projection weights must be transposed, because GPT-2's original code uses a Conv1D layer that stores weights as in by out, while nn dot Linear stores out by in. Notice what's missing from this table: there's no row for the attention biases.

## Slide 27 — ⚠️ Book check: "coherent text" (notebook cells 25–28)

Here's what the notebook actually generated after loading GPT-2. The quick brown foxeseseses. Artificial intelligence will be used to to to to. The capital of France is France is is is. The book shows a fluent continuation about the lazy dog, but this code cannot produce it. And notice: the weights loaded without errors, the shapes all matched, and every sanity check passed. The model is still broken. That's a lesson in itself.

## Slide 28 — Finding the bug (my experiment)

To debug, I compared our model's logits with Hugging Face's GPT-2 on the same input. The largest difference was fifty eight, which is not rounding; something is missing. Step two: I added the attention biases that the loader was silently dropping, and copied in GPT-2's values. The error fell to seven hundredths. Step three: GPT-2 uses the tanh approximation of GELU, while the notebook uses the exact version. Switching that brought the error down to six hundred thousandths. Now our model computes exactly what GPT-2 computes.

## Slide 29 — The fix in code (my patch)

Here's the patch, my own code on top of the notebook. Keep the biases in the attention projections. Copy them in the loader. And use the tanh GELU. With that, the parameter count becomes one hundred and twenty four million four hundred and thirty nine thousand eight hundred and eight, identical to Hugging Face.

## Slide 30 — After the fix (my run, greedy, 20 tokens)

After the fix, the same model with the same weights is fluent. Foxes are a great way to get a little bit of a kick out of your dog. Once upon a time, the world was a place of great beauty and great danger. It still repeats itself, but that's greedy decoding, which always picks the top token, not a bug; sampling comes in chapter fourteen. On my CPU, thirty tokens took about ten seconds, because this simple loop recomputes the whole prefix at every step.

## Slide 31 — The lesson: test against a reference

The lesson is bigger than this bug. All five sanity checks passed, and the model was still wrong. Those checks test wiring, not correctness. When a reference implementation exists, compare the actual numbers, as a maximum absolute difference. Typical silent mismatches are missing biases, the GELU variant, layer norm epsilon, transposes and tied weights. I'd add this as a sixth sanity check.

## Slide 32 — `train()` vs `eval()`, devices

A few practical details. Train mode enables dropout, eval mode disables it, so call eval before generating. Wrap generation in no grad to skip building the autograd graph. Move both the model and the inputs to the same device. And a preview of chapter twelve: weight decay is usually not applied to biases, layer norms and embeddings.

## Slide 33 — Part 8

Part eight. Exercises and review.

## Slide 34 — Exercises (my answers)

Exercise answers. The tiny checkpoint model has one hundred and thirty two thousand six hundred and eight parameters, not about one hundred and fifty thousand as the book says, or one hundred and thirty three thousand one hundred and twenty with attention biases. The full breakdown for GPT-2 small is on screen, with zero for the tied head. The causal mask is always a lower triangle. With the fixed model, def fibonacci produces return n in a loop: GPT-2 small is weak at code. And temperature only matters if you sample; argmax ignores it.

## Slide 35 — Key takeaways

Key takeaways. A GPT is embeddings, a stack of identical blocks, a final layer norm and a head. A config dataclass keeps experiments clean, and module list keeps parameters visible. Weight tying saves about a third of GPT-2 small. Sanity checks test wiring; comparing with a reference tests correctness. Loading GPT-2 needs the transposes, the attention biases and the tanh GELU. And a random model starts near a loss of ten point eight.

## Slide 36 — Notebook run & book check

The notebook ran completely on my CPU. The book checks: the loaded GPT-2 degenerates because of the missing attention biases and the GELU variant, which we fixed; the parameter count differs for the same reason; the lm head key does appear in the state dict; and the checkpoint model is about one hundred and thirty three thousand parameters. All in the errata file.

## Slide 37 — Review questions

Pause and try these. The four pieces. Why a dataclass. The output shape of the head. The savings from tying. Why earlier positions must be unchanged in the causal test. Why we transpose. And the big one: why could every sanity check pass while generation was garbage?

## Slide 38 — Practice this

To practise: run the notebook and reproduce the broken output. Apply the three line fix and verify the difference with Hugging Face is under one thousandth. Count parameters per component. And swap greedy decoding for temperature sampling.

## Slide 39 — Up next: Chapter 12

Next time, chapter twelve: training. The full loop, cross entropy, warmup, gradient clipping and perplexity, training a small MiniGPT on Shakespeare, on my CPU.

## Slide 40 — Credits

This video is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams here are my own, but the book goes deeper, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. Thanks for watching, and see you in chapter twelve.

