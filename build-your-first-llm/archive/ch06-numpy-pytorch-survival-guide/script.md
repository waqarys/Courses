# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter six of my study series on Build Your First LLM by Hasan Degismez. This is the survival guide to tensors. Every number inside a language model lives in a tensor, and almost every bug you'll hit is a shape bug. So today we learn to think in shapes: creating tensors, reshaping them, slicing, broadcasting, matrix multiplication, attention in four lines, autograd, nn dot Module, embeddings, and the five step training loop. I ran the book's chapter six notebook on a CPU for this video, and I'll show the real outputs plus a few experiments of my own.

## Slide 2 — Where we are

In chapter five we turned text into a list of token IDs. Today those IDs become tensors, then embeddings, then we run attention on them and write a training loop. From chapter seven, part three of the book, we build the model itself. Everything today follows the chapter six notebook, linked in the description.

## Slide 3 — Chapter 6 roadmap

Here's the plan. Why tensors, and what changes moving from NumPy to PyTorch. Then building up dimensions from one to four. Creating tensors, seeds, data types and devices. Reshaping, including the view versus reshape puzzle. Indexing, broadcasting and the essential operations. Attention in four lines of code. Then autograd, nn dot Module and embeddings. And finally the five step training loop, the exercises and the review.

## Slide 4 — Key terms for this chapter

The vocabulary. A tensor is a multi-dimensional array with a shape and a data type. The shape lists its dimensions, like batch, sequence and features. Broadcasting virtually expands a smaller tensor to match a bigger one. The at sign is matrix multiplication, the core of attention and feed forward layers. Autograd records operations and computes gradients, and a gradient tells you how much the loss changes when you nudge a parameter. nn dot Module is PyTorch's building block that bundles parameters with a forward method. The loss measures how wrong we are, and the device is where a tensor lives, on the CPU or the GPU.

## Slide 5 — Part 1

Part one. Why tensors?

## Slide 6 — Shapes: "how many of what" (my redraw)

Python lists are like loose pages on a desk: fine for scribbles, terrible for maths. Tensors are organised stacks of numbers that the computer can optimise. Every tensor is just how many of what. A scalar is one number. A vector is a row of numbers. A matrix is rows by columns. A three dimensional tensor is a stack of matrices, and a four dimensional tensor is a cabinet of stacks. In LLM code you'll mostly see three shapes: token IDs as batch by sequence, embeddings as batch by sequence by model width, and attention scores as batch by heads by sequence by sequence.

## Slide 7 — NumPy → PyTorch: what changes

The good news is that PyTorch feels like NumPy with extras. Creating an array becomes creating a tensor. Matrix multiplication is the at operator in both. Changing type uses dot astype in NumPy and dot to in PyTorch, and dot to also moves tensors between devices. Defaults differ: NumPy floats are float sixty four, PyTorch floats are float thirty two. I checked both. For deep learning float thirty two is what you want: half the memory and faster. And PyTorch adds the two superpowers: GPUs and automatic gradients.

## Slide 8 — Devices and the zero-copy bridge

Two practical things. Devices: you move a tensor to the GPU with dot to cuda, and you can't mix CPU and GPU tensors in one operation, or you get a runtime error. GPUs are often ten to a hundred times faster for this kind of work, although everything in this video ran on a CPU. And the zero copy bridge: torch dot from numpy shares memory with the NumPy array, so changing one changes the other. I ran it: set element zero of the NumPy array to nine nine nine, and the tensor shows nine nine nine too. If you want an independent copy, use torch dot tensor.

## Slide 9 — Part 2

Part two. Building up dimensions.

## Slide 10 — From token IDs to 4-D (my redraw)

Let's connect to chapter five. Our tokenizer gave us two, three, four, six: a one dimensional tensor with shape four. Add a second sentence and we have a batch, a two by four matrix: two sentences, four tokens each. Replace every ID with its seven sixty eight dimensional embedding and we get a three dimensional tensor, two by four by seven sixty eight. The book's filing cabinet analogy fits well: the drawer is the sentence, the folder is the token, and the page is one feature. And multi head attention adds a fourth dimension: two by eight by four by four, one four by four score grid per head.

## Slide 11 — The notebook confirms each step

Here's the notebook's real output for those steps. Shape four, then two by four, then two by four by seven sixty eight, where a single token's embedding is seven sixty eight numbers, then the four dimensional attention tensor. Get used to the names, because they're everywhere in transformer code: B for batch, S or L for sequence length, d model for features, and H for heads.

## Slide 12 — Part 3

Part three. Creating tensors.

## Slide 13 — Four ways to fill the box

There are four ways to fill a tensor. From existing data with torch dot tensor. With a fill rule: zeros, ones, uniform random with rand, normally distributed with randn, or random integers with randint. As evenly spaced number lines, with arange and linspace, which are handy for positions and masks. And by choosing the kind of number and where it lives, with the dtype and device arguments. Set those deliberately rather than relying on defaults.

## Slide 14 — Seeds: reproducible randomness

Computers don't make truly random numbers. They run a formula from a starting point called the seed. Set the same seed and you get exactly the same random numbers, which is essential for debugging and comparing experiments. The notebook checks it and prints true. Why forty two? It's a nod to the Hitchhiker's Guide to the Galaxy. Any integer works.

## Slide 15 — Part 4

Part four. Shapes and reshaping.

## Slide 16 — Shapes are contracts

Shapes are contracts between your code and the operations you call. Try to add a tensor ending in seven sixty eight to one ending in five twelve, and PyTorch refuses with a clear error: size seven sixty eight must match size five twelve at dimension two. Read shapes from left to right like nested containers: two batches, each of four tokens, each of seven sixty eight features. And print shapes all the time. Half of all deep learning bugs live here.

## Slide 17 — reshape, -1, squeeze, unsqueeze, permute

The reshaping toolkit. reshape rearranges the same numbers into a new shape, and the total must stay the same: twelve can be three by four, but not three by five. Minus one means infer this dimension for me. unsqueeze adds a dimension of size one, typically to make a single example into a batch of one. squeeze removes size one dimensions. And permute reorders dimensions, for example swapping heads and sequence. Below is the notebook's real output, walking a tensor through view, reshape, squeeze, permute and flatten.

## Slide 18 — view vs reshape: contiguity (my redraw)

Why does view sometimes fail? Think of memory as numbered boxes in a row. A freshly created tensor is contiguous, stored in order, so view can just relabel the boxes without moving anything. After a transpose or permute, the logical order jumps around memory: zero, four, eight, one, five, nine. view refuses to move data and raises an error. I triggered it on the permuted heads tensor from exercise two. reshape is happy to make a copy when it needs to. So the book's advice is right: default to reshape.

## Slide 19 — Part 5

Part five. Indexing, broadcasting, and the essential operations.

## Slide 20 — Indexing & slicing a 4-D tensor (notebook)

Indexing works like Python lists, one dimension at a time. x zero takes the first batch. A colon keeps a whole dimension, and colon minus one drops the last element, here the last token. Three dots, the ellipsis, means all the remaining dimensions. And torch dot tril, lower triangle, builds the causal mask from chapter three in one line. The outputs here are from the notebook.

## Slide 21 — Broadcasting (my redraw)

Broadcasting lets you combine tensors of different shapes without copying. Add a three by four matrix and a vector of four. PyTorch virtually repeats the vector for each row, the dashed cells, and adds element by element. Eleven, twenty two, thirty three, forty four, and so on. The rules, read from the right: two dimensions are compatible if they're equal or if one of them is one, and missing dimensions count as one. Otherwise it fails.

## Slide 22 — Broadcasting in LLMs (my Exercise 1 run)

Here's exercise one, which I ran. A four by three by seven sixty eight tensor plus a bias of seven sixty eight broadcasts across batch and sequence: that's how every linear layer adds its bias. The exercise asks what happens with a three by seven sixty eight tensor. It works too. Aligning from the right, three matches three and the batch dimension is missing, so it's treated as one. But four by seven sixty eight fails, because it lines up four against three. And the causal mask, shape one by one by S by S, broadcasts across every batch and head.

## Slide 23 — Essential operations

The operations you'll use ninety percent of the time. Star is element-wise, while at is matrix multiplication. A thirty two by ten by sixty four tensor times a sixty four by one twenty eight matrix gives thirty two by ten by one twenty eight. That's how a linear layer mixes features at every position. Reductions like sum and mean take a dim argument, and keepdim keeps the reduced dimension as size one. cat joins along an existing dimension, while stack creates a new one. And softmax with dim minus one normalises each row. The two classic bugs are confusing star with at, and running softmax over the wrong dimension.

## Slide 24 — Part 6

Part six. Attention in four lines.

## Slide 25 — Scaled dot-product attention (notebook cell 16)

Here's chapter three's attention as real code, from the notebook. Q, K and V are random two by five by sixty four tensors. Step one: Q times K transposed over the last two dimensions gives a five by five score grid per batch. Step two: divide by the square root of sixty four, which is eight. Step three: softmax over the last dimension, so each row sums to one. Step four: multiply by V to blend the values. The output has the same shape as the input. In my run, token two put seventy six percent of its attention on token zero.

## Slide 26 — + causal mask, then the one-liner

Add the causal mask. The notebook builds an upper triangle of trues above the diagonal, the future, and fills those scores with minus infinity, which becomes zero after softmax. Token two's weights now end in two zeros: it can only see tokens zero, one and two. In practice, PyTorch does all of this in one call: F dot scaled dot product attention, with is causal equals true. I checked that my manual version and the one liner give the same result. And I timed them on my CPU, with four sequences, twelve heads, five hundred and twelve tokens: the manual version took a hundred and sixty six milliseconds and the fused one under fourteen. About twelve times faster, even without a GPU.

## Slide 27 — Part 7

Part seven. Autograd, nn dot Module, and embeddings.

## Slide 28 — Autograd (my redraw + notebook cell 30)

A gradient tells you how much the output changes when you nudge an input. Mark x as requires grad, and PyTorch records every operation on it. Here y is x squared and z is the sum of y, which is thirteen. Call z dot backward, and PyTorch walks the graph in reverse and fills in x dot grad. The derivative of x squared is two x, so at two and three we get four and six. The notebook prints exactly that. To stop tracking, for example during inference, use torch dot no grad for a whole block, or dot detach for a single tensor.

## Slide 29 — nn.Module: the building block

Every network in PyTorch inherits from nn dot Module. You define layers in init, after calling super init, and you define the data flow in forward. Calling model of x runs forward. The module automatically tracks every parameter, moves them all to a device at once, and saves and loads them. This is the book's example MLP, condensed onto one line in forward, with GPT-2's feed forward shapes: seven sixty eight to three oh seven two and back. I counted its parameters: four million seven hundred and twenty eight thousand, five hundred and seventy six.

## Slide 30 — Token + position embeddings (notebook cell 18)

An embedding layer is just a lookup table: row i is the vector for token i. GPT-2 has fifty thousand two hundred and fifty seven rows of seven sixty eight, thirty eight point six million parameters. Position embeddings are a second table, one thousand and twenty four by seven sixty eight. Position IDs are just arange of the sequence length, given a batch dimension and expanded across the batch. Add the two lookups, and that's what goes into the first transformer block. The notebook confirms the totals: thirty nine million, three hundred and eighty three thousand, eight hundred and eight. Token embeddings are about thirty one percent of GPT-2 small, which is why vocabulary size matters so much for small models.

## Slide 31 — ⚠️ Book check: "BERT uses sinusoidal (fixed)"

One correction. A gotcha box in the book says GPT-2 uses learned position embeddings, while BERT uses sinusoidal, fixed ones. The GPT-2 part is right. But BERT also uses learned absolute position embeddings, a five hundred and twelve by seven sixty eight table in BERT base. Sinusoidal encodings belong to the original 2017 transformer. That's in the errata.

## Slide 32 — Part 8

Part eight. The training loop.

## Slide 33 — The 5-step recipe (my redraw)

Training is always the same five steps. One: zero the gradients, because PyTorch adds new gradients to old ones by default. Two: the forward pass, to get predictions. Three: compute the loss. Four: the backward pass, to fill every parameter's gradient. For LLMs, clip the gradients here, between backward and step, to prevent explosive updates. A max norm of one is a safe default. Five: the optimizer step updates the weights. Then repeat.

## Slide 34 — The loop in code (notebook cell 19, condensed)

Here's the notebook's loop, condensed. A small MLP, the Adam optimizer, cross entropy loss, and sixty four random examples with random labels. Each epoch: train mode, zero the gradients, forward, loss, backward, clip, step. Then evaluation mode and no grad to measure accuracy. My run printed losses of point six nine five, point six nine two and point six eight nine, and an accuracy of fifty six percent. Basically chance, because the labels are random and we only took three steps.

## Slide 35 — What happens if we keep going? (my experiment)

I wondered what happens if you keep going, so I ran the same loop for three hundred steps. The loss falls from point six nine two to point zero five eight, and training accuracy reaches a hundred percent. On random labels! There's nothing to learn, so the model has simply memorised sixty four random examples. That's a powerful lesson for later: a falling training loss alone proves nothing. You always need a separate validation set, which we'll use when we train our LLM.

## Slide 36 — train() vs eval(), no_grad vs detach

A few switches that confuse everybody. model dot train turns dropout on, and model dot eval turns it off for deterministic behaviour. torch dot no grad stops building the computation graph for a whole block of code, saving memory during inference. dot detach cuts a single tensor out of the graph. And zero grad with set to none equals true sets the gradients to None instead of filling them with zeros, which saves memory and is slightly faster.

## Slide 37 — Part 9

Part nine. The exercises, with my solutions.

## Slide 38 — Exercise 2: split into heads (my run)

Exercise two simulates splitting into attention heads. Take a two by five by five twelve tensor, reshape the last dimension into eight heads of sixty four, then permute so heads come before sequence: two by eight by five by sixty four. Now a batched matmul with its own transpose gives scores of two by eight by five by five, one score grid per head, as expected. And note that after permute the tensor isn't contiguous, so view would fail. This exact reshape and permute is how multi head attention splits the model width, which we'll see in chapter ten.

## Slide 39 — Exercise 3: one step + clipping (my run)

Exercise three: one training step on a tiny network. My loss went from one point six seven seven to one point six oh eight after a single step, with a learning rate of point zero one. For the bonus question, how do you know whether gradients were actually clipped? clip grad norm returns the total gradient norm before clipping. Mine was point five five five, which is below the max norm of one, so nothing was clipped this time. Log that number in real training runs. It's one of the best early warnings of trouble.

## Slide 40 — Part 10

Part ten. Wrapping up.

## Slide 41 — Key takeaways

The key takeaways. One: tensors are arrays with shapes, so think how many of what. Two: PyTorch is NumPy plus GPUs plus autograd, with float thirty two by default. Three: the LLM shapes go from batch by sequence, to batch by sequence by model width, to batch by heads by sequence by sequence. Four: broadcasting aligns shapes from the right, expanding dimensions of size one or missing ones. Five: matrix multiplication combines features, and attention is four lines of code, or one fused call. Six: the training recipe is zero grad, forward, loss, backward, clip, step.

## Slide 42 — Notebook run & book check

My notebook run and book check. The chapter six notebook ran end to end on a CPU, all nineteen code cells, with no errors, and the shapes, parameter counts and gradients all match the book. My own checks of the default data types, zero copy sharing and fused attention all agree with the text. One erratum: BERT uses learned positions, not sinusoidal ones. And a note: the book's two to four times speed-up refers to FlashAttention on GPUs. On my CPU, the fused call was about twelve times faster than the manual version, mostly from avoiding all those separate operations.

## Slide 43 — Review questions 1

Review questions, with my answers. One: why the different default floats? NumPy targets scientific precision, so sixty four bits. PyTorch targets speed and memory, so thirty two bits. It matters when you mix them, which can cause dtype errors, and for calculations that need high precision. Two: view needs contiguous memory, while reshape copies when needed, so prefer reshape after a transpose or permute. Three: broadcasting aligns shapes from the right, and each pair must be equal or contain a one, with missing dimensions counting as one. Four: the dim in softmax is the axis that sums to one, usually minus one for logits. Pick the wrong one and you normalise across the batch or across positions, and it's silently wrong.

## Slide 44 — Review questions 2

Five: torch dot no grad disables gradient tracking for a whole block, while detach returns a single tensor with no history. Six: why zero the gradients first? Because gradients accumulate, so without clearing them each step would add the old gradients to the new ones. Set to none also saves memory. Seven: switching from train to eval turns off dropout and changes batch norm to use stored statistics, so evaluation and inference become deterministic.

## Slide 45 — Practice this

Your practice list. Run the chapter six notebook in Colab, and try a GPU runtime to compare timings. Print the shape after every line of the attention cell. Break broadcasting on purpose, and read the error carefully. Run the training loop for three hundred steps and watch it memorise noise. And solve the three exercises plus the clipping bonus.

## Slide 46 — Up next: Chapter 7 — Part III begins

That's chapter six. You can now read and write the tensor code at the heart of every modern LLM. Next, part three begins: we wire these pieces into a real data pipeline and start building the model itself. Same maths, aimed at real text.

## Slide 47 — Credits

This video is based on the book Build Your First LLM by Hasan Degismez. Everything here is my own adaptation for study, so please support the author and buy the book at leanpub dot com slash First LLM. The code shown comes from the companion repository at github dot com slash First LLM slash code, under the MIT license. Thanks for watching, and see you in chapter seven.

