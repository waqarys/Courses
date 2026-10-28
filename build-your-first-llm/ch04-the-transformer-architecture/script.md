# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter four of my study series on Build Your First LLM by Hasan Degismez. Attention is the star, but a star needs a stage. Today we assemble the complete transformer: positional encodings, feed forward networks, residual connections and layer normalisation, stacked into the architecture behind GPT, BERT and every modern language model. And as usual, I'll check everything against a real model, GPT-2 small, by counting its parameters, looking at its position vectors, and asking it a question.

## Slide 2 — Where we are

We have embeddings from chapter two and attention from chapter three. Today we build the whole transformer layer around them and stack it. This is the end of part one, the conceptual part. From chapter five, we start writing real code with the book's notebooks. As before, the snippets and GPT-2 experiments in this video are my own.

## Slide 3 — Chapter 4 roadmap

Here's the plan. First, the missing piece: position. Then feed forward networks and why they need an activation function. Then residual connections, the highway system, and layer normalisation, the thermostat. Then we assemble one complete layer and stack it. Then encoders versus decoders, and GPT versus BERT. Then training and inference, with real numbers from GPT-2. And we finish with exercises, the checkpoint and review questions.

## Slide 4 — Key terms for this chapter

The vocabulary. A position encoding is a set of numbers added to an embedding to say where the token sits. A feed forward network is a small neural network applied to each position separately: expand by four, apply an activation, contract back. An activation function is the nonlinearity, like GELU or ReLU, that makes depth worthwhile. A residual connection adds a layer's input to its output. LayerNorm and RMSNorm keep each vector in a stable range. An encoder lets every position see every other one, a decoder only lets positions look backward, and causal masking is how we enforce that.

## Slide 5 — Part 1

Part one. The missing piece, position.

## Slide 6 — Attention is blind to order

Here's the problem we skipped in chapter three. Attention compares every word with every word, all at once. There's no first word and no last word. So the dog chased the cat and the cat chased the dog look the same to it. I checked this in code: if you shuffle the input vectors, the attention outputs come out shuffled in exactly the same way, and nothing else changes. Mathematicians call that permutation equivariant. RNNs got order for free, because they read word one, then word two. We gave that up to gain parallelism, so we need another way to tell the model about order.

## Slide 7 — The fix: add a position vector

The fix is simple. Give every position its own vector, and add it to the word's embedding. Cat at position one becomes the embedding of cat plus position vector one. Cat at position five gets position vector five instead, so the two end up different. The embedding says what, the position says where. It's added once, at the input, and then carried through every layer. The book compares it to GPS coordinates on a message from a search party: the coordinates don't change what the message says, they tell you where it came from.

## Slide 8 — Sinusoidal encodings (2017)

The original transformer used sinusoidal encodings. Each pair of dimensions is a sine and cosine wave at a different frequency. On the left you can see the fast waves in the low dimensions and slow waves in the high ones. The book uses a clock analogy: the hour and minute hands turn at different rates, and together they give every time a unique reading, while times a minute apart look similar. Sinusoidal encodings work the same way with many hands, and because they come from a formula, they're defined for any position, even ones never seen in training.

## Slide 9 — Learned positions — real GPT-2 (my experiment)

Many models, including GPT-2, simply learn a position table instead. In GPT-2 that table is called wpe, and it's one thousand and twenty four rows by seven sixty eight. So GPT-2 can't handle position one thousand and twenty five, because there's no row for it. That's the trade-off the book describes. I compared the similarity of positions in both schemes. On the left, sinusoidal. On the right, GPT-2's learned table. GPT-2 discovered the same smoothness on its own: position ten and position eleven have a cosine of point nine nine eight, while position ten and position ninety are only at point two seven.

## Slide 10 — Rotary embeddings (RoPE)

Most recent models use rotary position embeddings, RoPE. Instead of adding a position vector, RoPE rotates the query and key vectors by an angle that depends on position. When you take the dot product of two rotated vectors, what's left depends on how far apart they are, so the model naturally sees relative distance. It's a fixed formula with no learned table, and it behaves better on long contexts. Llama, Mistral and most recent open models use it. One small correction: the book lists GPT-4 as using RoPE too, but OpenAI hasn't published GPT-4's architecture, so we can't know that.

## Slide 11 — Part 2

Part two. Feed forward networks.

## Slide 12 — Attention mixes; the FFN transforms

Why do we need anything after attention? Because attention is fundamentally a mixing operation. It takes weighted averages of value vectors, so it gathers the ingredients but doesn't cook the meal. The feed forward network does the cooking, transforming each position's vector. Every transformer layer follows this rhythm: attend, then process. The book compares it to a factory: attention is the mail room that sorts related letters together, and the feed forward network is the station that actually reads each letter.

## Slide 13 — Expand → activate → contract (my redraw)

The feed forward network has three steps. Expand the seven sixty eight numbers to three thousand and seventy two, four times as many. Apply a nonlinear activation to each one. Then contract back to seven sixty eight, so the output fits the next layer. I printed the shapes from real GPT-2: the expansion matrix is seven sixty eight by three oh seven two, and the contraction is the reverse. Crucially, every position goes through this independently. Cat, sat and the don't interact here. That was attention's job.

## Slide 14 — Why expand?

Why expand then contract? Expansion gives the model scratch space. The book's analogy is long multiplication. Twenty three times forty seven: twenty three times forty is nine twenty, twenty three times seven is one sixty one, add them to get one thousand and eighty one. The intermediate numbers don't appear in the answer, but you needed them. The wide hidden layer gives the model room for intermediate features like that. And as we'll see, the feed forward layers hold about two thirds of GPT-2's non embedding parameters.

## Slide 15 — Why we need a nonlinearity

Why do we need the activation function in the middle? Because without it, everything is linear: multiply and add. And a stack of linear operations collapses into a single linear operation. I checked it: B times A times v equals the matrix B A times v. So a hundred linear layers are no more expressive than one. The book's image is photocopying a photocopy: you'll never get a colour photograph out of it. Language is full of thresholds and reversals. Great job can be sincere or sarcastic depending on context. Capturing that needs a nonlinearity.

## Slide 16 — GELU vs ReLU (my plot)

Here are the two most common activations. ReLU passes positive values unchanged and zeroes the negatives. Its gradient there is zero, so units stuck in the negative region can stop learning. GELU is a smooth curve. It's close to the identity for large positive inputs and close to zero for large negatives, with a gentle dip in between. I computed the book's examples: GELU of two is one point nine five four, GELU of minus two is minus point zero four six, and GELU of minus a half is minus point one five four. They match the book. Think of thirty seventy two little judges, each deciding how much of its signal to let through.

## Slide 17 — ⚠️ Book check: "GPT, Claude, LLaMA use GELU"

One correction. The book says most modern LLMs, naming GPT, Claude and Llama, use GELU or close variants. GPT-2 and GPT-3 do use GELU. But Llama uses SwiGLU, a gated feed forward block built on the SiLU activation, and Claude's architecture isn't published. The book's broader point stands: modern models use smooth nonlinear activations, and many now use gated variants of the feed forward block.

## Slide 18 — Part 3

Part three. Residual connections.

## Slide 19 — The degradation problem

Stacking many layers creates a problem. Imagine a game of telephone through ninety six layers. Even if each layer keeps ninety nine percent of the signal, point nine nine to the power ninety six is point three eight one, so only thirty eight percent survives. The book's number is correct. The same thing happens to gradients flowing backward during training: they can vanish or explode, so the early layers barely learn.

## Slide 20 — The fix: add the input back (my redraw)

The fix is beautifully simple. Add the input back to the output: x plus f of x. Now the layer only has to learn the residual, the change to make, rather than rebuilding everything from scratch. If a layer has nothing useful to add, it can learn f close to zero and just pass x through. The book calls it a highway with optional exits. Information can cruise straight from early layers to late ones, and take an exit only where a layer adds value. And during training, gradients get the same highway back down.

## Slide 21 — Residuals in the Transformer

In a transformer layer there are two skip connections, one around the attention block and one around the feed forward block. People call the vector that flows along this highway the residual stream. Each sublayer reads from the stream, computes something, and adds its update back in. That's also why every sublayer has to output exactly the same size as its input, seven sixty eight in GPT-2 small.

## Slide 22 — Part 4

Part four. Layer normalisation.

## Slide 23 — The stability problem

Deep networks have a second problem: values can drift. If each layer amplifies its input by just one percent, after ninety six layers it's grown by two point six times, which again matches the book, and it can get much worse during training. LayerNorm resets the scale at every layer. For each vector, compute its mean and standard deviation across the dimensions, subtract the mean, divide by the standard deviation, and then apply a learned scale and shift so the network can undo it if it wants. The book calls it a thermostat.

## Slide 24 — ⚠️ Book check: the LayerNorm example

Let's check the book's LayerNorm example. The input is one oh two point five, ninety eight point three, one oh five point seven and ninety five point two. The book gives the output as point five two, minus point three one, one point one two, minus point seven eight. But those add up to point five five, and a normalised vector has to sum to zero. I ran PyTorch's layer norm with no scale or shift, and the correct output is point five two, minus point five three, one point three two, minus one point three one. The mean is one hundred point four two five and the standard deviation is about three point nine eight. The first value happens to match. A quick sanity check for any normalised vector: it should sum to zero and have a variance of one. This one is in the errata.

## Slide 25 — Pre-Norm vs Post-Norm (my redraw)

Where does LayerNorm go? The original 2017 transformer normalised after each residual addition. That's called post norm. GPT-2 and most modern models normalise the input to each sublayer instead, before attention and before the feed forward block. That's pre norm, and it trains more stably, especially in very deep stacks, because the residual highway itself is never normalised.

## Slide 26 — RMSNorm: the leaner cousin

Many recent models, including Llama and Mistral, use RMSNorm instead. It skips the mean subtraction and just divides by the root mean square of the vector, then applies a learned scale. It's slightly faster, uses less memory, and works about as well in practice. On the same input it gives one point oh two, point nine seven eight, one point oh five two and point nine four seven. Notice those aren't centred. They're just rescaled to a typical size of one.

## Slide 27 — Part 5

Part five. Putting it all together.

## Slide 28 — One Transformer layer (Pre-Norm, my redraw)

Here's one complete transformer layer, in the pre norm style that GPT-2 uses. Start with the input x. Normalise it, run multi head attention, and add the result back to x. That's the first residual. Then normalise again, run the feed forward network, and add that back. That's the second residual. The output has the same shape as the input, so it can go straight into the next layer.

## Slide 29 — The layer recipe

In two lines of pseudocode: h equals x plus attention of layer norm of x, then the output equals h plus the feed forward network of layer norm of h. Six steps: normalise, attend, add, normalise, process, add. Then you stack the layer. GPT-2 small has twelve layers, GPT-3 has ninety six, and big models today have eighty to a hundred and twenty or more.

## Slide 30 — What each floor does

The book compares the stack to a building. Every floor has the same layout, an attention room and a processing room, and the residual stream is the elevator. Researchers generally find that early layers capture local patterns and syntax, middle layers build phrases and semantic relationships, and late layers handle abstract structure and the final prediction. By the top floor, a simple word like sat carries who sat, where, and what's likely to come next.

## Slide 31 — The complete model

And here's the whole model. Token IDs go into the token embedding table, and position embeddings are added. The result flows through N transformer layers. A final layer norm, then a linear layer maps each vector back onto the vocabulary, producing a score, called a logit, for every possible next token. Softmax turns those into probabilities. That's GPT, end to end.

## Slide 32 — Where GPT-2's 124M parameters live (my count)

I counted every parameter in the real GPT-2 small. The total is a hundred and twenty four million, four hundred and thirty nine thousand, eight hundred and eight. The token embedding table, fifty thousand two hundred and fifty seven tokens by seven sixty eight, is thirty eight point six million on its own. Each layer has two point three six million parameters in attention and four point seven two million in the feed forward network, twice as many. Across twelve layers, that's fifty seven million in the feed forward networks and twenty eight million in attention. Layer norms are tiny. GPT-2 also reuses the token embedding matrix as its output layer, which is called weight tying, so it isn't counted twice.

## Slide 33 — Part 6

Part six. Encoders versus decoders.

## Slide 34 — Encoder vs decoder attention

An encoder lets every position attend to every other position, so it has full, bidirectional visibility. A decoder uses a causal mask: each position can see itself and earlier positions, but nothing later. In the grid, the ticks below the diagonal are allowed and the crosses above it are blocked. When you're generating, you can't look at words you haven't written yet. That would be cheating.

## Slide 35 — Three families (my redraw)

That gives three families. Encoder only models, like BERT, see everything, which makes them great for classification, entity extraction and retrieval, but they don't naturally generate text. Decoder only models, like GPT, Llama and Claude, are causal and generate text one token at a time. Encoder decoder models, like the original transformer and T5, read the source fully with an encoder, then generate with a decoder that cross attends to it. That's natural for translation and summarisation.

## Slide 36 — GPT vs BERT — who won?

The two famous lineages are BERT and GPT, both from 2018. BERT is encoder only and bidirectional, built for understanding. GPT is decoder only and causal, built for generation. As models scaled up, the decoders turned out to be good at understanding too, just by predicting what comes next, and they won the scaling race. ChatGPT, Claude and Llama are all decoder only. That's what we'll build in part three of this book. And GPT stands for generative pre-trained transformer: it generates, it's pre-trained on lots of text, and it's a transformer.

## Slide 37 — Part 7

Part seven. From architecture to application.

## Slide 38 — Training vs inference

Training and inference use the same architecture in different ways. In training, we feed a sequence and ask the model to predict the next token at every position at once, measure how wrong it was with a loss, run the backward pass, and update every weight: embeddings, attention, feed forward networks, norms, everything. Billions of times. In inference, we feed a prompt, read the probabilities at the last position, pick a token, append it, and run again. One forward pass per new token, which is why long outputs take time.

## Slide 39 — Real inference: "The capital of France is" (my experiment)

The book's inference example uses the capital of France is, with the model picking Paris. So I asked real GPT-2 small. Its top choice is not Paris but the word the, at eight and a half percent, followed by now, a, and France. Paris is only fifth, at three point two percent. If we always pick the most likely token, it continues the capital of the French Republic, and so on. That's a nice lesson about scale. A hundred and twenty four million parameter model, trained only to predict web text, knows Paris is relevant but doesn't answer like an assistant. Bigger models and instruction tuning, which come later in the book, change that.

## Slide 40 — Scale: same architecture, more of it

Here's how the same architecture scales. GPT-2 small: twelve layers, width seven sixty eight, twelve heads, a hundred and twenty four million parameters. GPT-2 large: thirty six layers, width twelve eighty, twenty heads, about seven seventy four million. GPT-3: ninety six layers, width twelve thousand two hundred and eighty eight, ninety six heads, a hundred and seventy five billion. Llama three point one four oh five B: a hundred and twenty six layers, width sixteen thousand three hundred and eighty four, a hundred and twenty eight heads. These figures come from the published papers and model cards. The design is the same; the scale changes, and with scale come abilities nobody fully understands yet.

## Slide 41 — Everything you now know

Let's take stock. You now know every major part of a transformer. Embeddings turn words into vectors. Position encodings add location. Attention gathers context. Feed forward networks transform each position. Residual connections preserve the signal. Layer norm keeps the values stable. And stacking builds depth. Every response from a modern chatbot flows through exactly this design.

## Slide 42 — Part 8

Part eight. Hands on.

## Slide 43 — Exercise 1 & 2: trace "The cat sat"

Exercises one and two ask you to trace the cat sat through the model. Tokenise it: in GPT-2 that's three tokens, with IDs four six four, three seven nine seven and three three three two. Look up embeddings, giving a three by seven sixty eight matrix. Add position vectors zero, one and two. In layer one's attention, sat queries for its subject and finds cat. The feed forward network transforms each row on its own. More layers refine the picture, and at the top we get a distribution over the next token, with words like on or down likely. And through it all, the residual stream keeps the original signal for cat alive.

## Slide 44 — Exercise 3 & 4: design and choose

Exercise three: design a tiny transformer for predicting the last letter of a word. My choice would be two layers, width sixty four, four heads, and learned positions, because words are short and have a fixed maximum length. Exercise four asks which architecture fits each task. Sentiment classification: an encoder. Translation: classically an encoder decoder, though big decoders do it well too. Continuing a story: a decoder. Extracting entities: an encoder. Question answering over a passage: an encoder if you're extracting a span, a decoder if you're generating an answer.

## Slide 45 — Part 9

Part nine. The checkpoint exercise.

## Slide 46 — Checkpoint (25–30 min)

The checkpoint has four parts. First, draw one transformer layer from memory, with both layer norms, attention, the feed forward network and both residual paths. Second, pick a word from the quick brown fox jumps and trace it through two layers. Third, answer four design questions. And fourth, pick the architecture for a document question answerer, an essay writer and a translator. Pause the video and try it before you look at my answers.

## Slide 47 — My answers to the design questions

My answers. Without residuals, a deep stack degrades and the gradients vanish, so the early layers barely learn. Without layer norm, activations drift and blow up or shrink, and training becomes unstable. Positions have to be added before attention, because attention is blind to order: the position information needs to be inside the queries and keys when the scores are computed. More layers give more capacity and more refinement, but they cost compute, are harder to optimise, and can overfit small data sets. And for part four: a document question answerer is naturally an encoder, an essay writer a decoder, and a translator an encoder decoder.

## Slide 48 — Part 10

Part ten. Wrapping up.

## Slide 49 — Key takeaways

The key takeaways. One: attention is blind to order, so we add position information, with sinusoidal, learned or rotary encodings. Two: the feed forward network expands by four, applies GELU, and contracts, separately at each position. Three: residual connections, x plus f of x, are the highway through depth. Four: LayerNorm or RMSNorm keeps values in a stable range, and modern models normalise before each sublayer. Five: a layer is norm, attend, add, norm, feed forward, add, stacked N times. Six: encoders are bidirectional, decoders are causal, and GPT is decoder only.

## Slide 50 — Notes on the book (checked)

My notes on the book for this chapter. The compounding numbers, the GELU values and the feed forward shapes are all correct. Three items go into the errata. The LayerNorm example output is wrong, and the correct values are point five two, minus point five three, one point three two and minus one point three one. Llama uses SwiGLU rather than GELU, and Claude's architecture isn't published. And GPT-4's architecture, including its position scheme, isn't public. Finally, the Paris example is illustrative: real GPT-2 small ranks Paris fifth.

## Slide 51 — Review questions 1

Review questions, with my answers. One: why position encodings? Because attention treats its inputs as an unordered set, so without them dog bites man equals man bites dog. Two: the two main approaches are sinusoidal, a formula that extrapolates, and learned, a table that often works better within range but stops at the maximum length. RoPE is the modern relative variant. Three: the feed forward network is a per position network that expands for scratch space, applies a nonlinearity, and contracts to fit the next layer. Four: residuals are a highway with exits. Adding x back preserves both the signal and the gradients through depth.

## Slide 52 — Review questions 2

Five: layer norm stops values drifting by normalising each vector to mean zero and variance one, then applying a learned scale and shift. Modern models apply it before each sublayer. Six: one layer is layer norm, multi head attention, add x, layer norm, feed forward, add again. Seven: encoders use full attention and suit understanding, like BERT. Decoders use causal attention and suit generation, like GPT. Eight: the causal mask sets future scores to minus infinity before the softmax, so they get zero weight. It's needed so that a model trained to predict the next token can't simply look at it.

## Slide 53 — Practice this

Your practice list. Draw the pre norm layer from memory and check it against the slide. Verify the LayerNorm correction by hand. Load GPT-2 and count its parameters with one line of Python. Do exercises three and four and the checkpoint design questions. And get your Python environment ready, because the book's chapter five notebook is next. The code in this video is my own, since part one has no book notebook.

## Slide 54 — Up next: Chapter 5 — Part II begins

That's chapter four, and the end of part one. You understand what AI is, how words become numbers, how attention works, and how the transformer puts it all together. Part two is hands on. In chapter five we set up Python and start writing real code with the book's notebooks. The theory is in place. Time to build.

## Slide 55 — Credits

This video is based on the book Build Your First LLM by Hasan Degismez. Everything here is my own adaptation for study, so please support the author and buy the book at leanpub dot com slash First LLM. The companion code is at github dot com slash First LLM slash code, under the MIT license. Thanks for watching, and see you in chapter five.

