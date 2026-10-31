# M02 — The 20 % of Python & PyTorch You Actually Need

Target length: **15 min** · Segments: 6
Big idea: *A tensor is a spreadsheet that can have any number of dimensions and remembers how it was calculated, so it can tell every number which way to move.*

## S1 · CAM · Hook (≈40s)
- You don't need to be a Python expert to build an LLM.
- You need about six ideas. Lists, functions, classes, and three PyTorch ideas: tensors, shapes, and gradients.
- If you already code in Java or JavaScript, this will feel familiar in ten minutes.
- If you've never coded, follow along in Colab — link below — and pause as often as you like.
- Let's set up the toolkit.

## S2 · IDE · Python in five moves (≈3 min)
- IntelliJ, file m02/python_basics.py. Paste snippet 01.
- Move one: variables and f-strings. Python figures out types for you.
- Move two: lists and the list comprehension — "make a new list by doing this to each item". We'll use it for tokens constantly.
- Move three: dictionaries — word to ID. This is literally what a vocabulary is.
- Move four: functions with def.
- Move five: a class. A class bundles data and the functions that act on it. Every model we build will be a class.
- Run it. Note the length of the sentence: count the characters, spaces included. Python counts spaces — beginners always forget that.

## S3 · SLIDES · Tensors: spreadsheets with more dimensions (≈3 min)
- Slide: scalar, vector, matrix, 3D tensor.
- A single number is a scalar. A row of numbers is a vector. A grid is a matrix.
- Stack grids and you have a 3D tensor. In our LLM the standard shape is batch × tokens × features.
- Analogy: a batch of essays; each essay is a list of tokens; each token is described by 768 numbers.
- The one habit that saves hours: print the shape. Always. Shape bugs are 80 percent of deep-learning bugs.
- Slide: matrix multiply as "every row asks every column a question". Inner sizes must match: (2×3) @ (3×4) gives 2×4.

## S4 · IDE · PyTorch hands-on (≈4 min)
- Snippet 02. Make tensors, check .shape, .dtype.
- Matrix multiply with the @ operator. Watch the shapes.
- Broadcasting: add a 4-number bias to a 2×4 matrix — PyTorch copies it down each row for you.
- Snippet 03: autograd. We make w with requires_grad=True.
- Compute a loss — how wrong we are — then call backward.
- w.grad tells us which way to nudge w to be less wrong. That's the whole idea of training, in one line.
- Snippet 04: a tiny nn.Module. A Linear layer is just "multiply by a matrix, add a bias".
- Count its parameters: in × out + out.

## S5 · SLIDES · Gotchas I hit so you don't (≈2 min)
- Gotcha one: wrong keyword names. nn.Embedding takes num_embeddings and embedding_dim. nn.LayerNorm takes normalized_shape — just pass the number. Writing a made-up keyword raises a TypeError.
- Gotcha two: forgetting to zero gradients — they add up across steps.
- Gotcha three: dtype mixups — integer token IDs vs float weights.
- Gotcha four: device mismatch — model on GPU, data on CPU.
- Gotcha five: position embeddings. GPT-2 and BERT both *learn* theirs. The fixed sine-wave version is from the original 2017 Transformer, and most new open models use rotary embeddings.

## S6 · CAM · Recap (≈40s)
- Python: lists, dicts, functions, classes.
- PyTorch: tensors, shapes, autograd, nn.Module.
- Print the shape. Zero the grads.
- Next: turning raw text into token IDs — data and tokenizers.
