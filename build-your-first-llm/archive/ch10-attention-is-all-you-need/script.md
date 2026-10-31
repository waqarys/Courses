# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter ten of my study series on Build Your First LLM by Hasan Degismez. This is the chapter I've been waiting for, because it's the heart of every transformer. We are going to build attention from scratch in PyTorch, tracking every tensor shape, then turn it into multi-head attention, and finally into a complete transformer block, the exact unit GPT two stacks twelve times. Every piece of code in this video comes from the book's companion notebook, which I actually ran on my machine, so the outputs you see are real.

## Slide 2 — Run along with the notebook

Open the notebook alongside this video. The links are on screen and in the description. You can run it in Colab with no setup. I executed every code cell on a plain CPU and all of them ran without errors. When I mention a cell number, I'm counting cells in the notebook file from zero, including markdown cells, so you can jump straight to it. All code shown is from the FirstLLM code repository, which is MIT licensed.

## Slide 3 — Chapter 10 roadmap

Here's the plan. First, the problem: why the embeddings from chapter nine aren't enough. Then three analogies that build intuition for queries, keys and values. Then the core: self-attention in five steps, with shapes at every line. Then causal masking, which stops the model from cheating. Then we go from one head to twelve heads with the reshape trick. Then we assemble a full transformer block with the feed forward network, layer normalisation and residual connections. We'll count parameters, visualise attention, talk about the quadratic memory cost, trace the whole pipeline, and finish with takeaways, all ten review questions with answers, and a practice list.

## Slide 4 — Notation used throughout

Let's fix our notation, because shapes are everything in this chapter. Batch is how many sequences we process at once, two in the examples. Seq, or n, is the number of tokens, six for the cat sat on the mat. D model is the embedding width, seven hundred sixty eight for GPT two small. Num heads is twelve. D head, also called d k, is d model divided by the number of heads, which is sixty four. And d f f, the hidden size of the feed forward network, is four times d model, three thousand seventy two. Keep these numbers in your head: seven sixty eight, twelve, sixty four, three oh seven two.

## Slide 5 — 10.1 Why Static Embeddings Aren't Enough

Section one. Why static embeddings aren't enough.

## Slide 6 — The "bank" problem

In chapter nine we built embeddings. Each token ID looks up a row in a table, and we add a position vector. So in, I went to the river bank, and, I deposited money at the bank, the token bank, which is ID three three three one in GPT two's vocabulary, fetches exactly the same row both times. The position vectors differ a little because bank sits at a different position, but nothing in the embedding layer knows about river or money. It's a pure lookup. The meaning of bank depends on its neighbours, and the embedding layer can't see the neighbours.

## Slide 7 — Recap: what Chapter 9 gives us

Here's the chapter nine forward pass as a reminder. Token embedding, shape batch by seq by seven sixty eight. Position embedding, same shape. Add them. So the input to this chapter is a tensor of shape batch, seq, seven sixty eight, which encodes what each token is and where it is. What's missing is what each token means in this particular sentence. That's the job of attention.

## Slide 8 — Dictionary definition vs sentence meaning

A helpful analogy from the book. A static embedding is like a dictionary entry that lists every sense of bank at once: river edge, financial institution, to rely on. You get all of them blended and don't know which applies. Attention is like a smart reader who reads the whole sentence and highlights the right sense. In river bank, bank looks at river and moves towards the first meaning. In savings bank, it looks at savings and moves toward the second. Crucially, the shape doesn't change. Six by seven sixty eight goes in, six by seven sixty eight comes out. Only the values change.

## Slide 9 — Evidence from real GPT-2 (my experiment)

I wanted to see this for real, so I ran the pretrained GPT two model on four sentences and took the hidden vector for bank at every layer. Then I compared them with cosine similarity. At layer zero, before any attention, they're nearly identical, around zero point nine nine eight. As we go up the layers, the pink line, river bank versus money bank, drops to about zero point seven five, while the gold line, two financial uses, stays around zero point nine five. So the representation genuinely separates by meaning. The jump back up at the last layer is a known quirk of GPT two's final layer, where all vectors become very similar. The lesson: attention layers are where context gets mixed in.

## Slide 10 — Not just ambiguous words

And it's not only about words with two meanings. Attention handles coreference: in Alice went to the store, she bought milk, the word she needs information from Alice. Long-range agreement: in the keys to the cabinet are, the verb are must agree with keys, not with the nearer word cabinet. Syntax: in the cat that chased the mouse sat, the subject of sat is cat, several words back. Semantics: capital should pull in information about Paris. All of these are one mechanism: tokens exchanging information with each other.

## Slide 11 — Where we are in the pipeline

Here is the whole pipeline. Text goes into the tokenizer from chapter eight, giving token IDs of shape one by six. The embedding layer from chapter nine turns them into static vectors, one by six by seven sixty eight. This chapter adds the transformer block, which keeps the shape but makes the vectors context aware. Chapter eleven stacks twelve of these blocks and adds the language model head, which produces logits over all fifty thousand two hundred fifty seven tokens, and then we sample the next token.

## Slide 12 — 10.2 What IS Attention?

Section two. What is attention? Three analogies, then the maths in plain English.

## Slide 13 — Analogy 1: the committee meeting

First analogy, a committee meeting. Every token is a member. When it's sat's turn, it first listens to everyone, including itself. Then it decides how relevant each input is. Cat is very relevant, because it answers who sat. On is somewhat relevant, it hints where. The is barely relevant. Finally it updates its own position by blending everyone's input, weighted by relevance. After this, the vector for sat encodes something like, an action performed by the cat, at some location.

## Slide 14 — Analogy 2: the search engine → Q, K, V

Second analogy, a library search. Your search text is the query. Each book has index terms, its keys. And each book has contents, its value. The search compares your query to every key, books tagged animals, pets, felines score high, books on history or dogs score low, and you get back the contents weighted by relevance. Attention is exactly this. Each token produces a query, what am I looking for, a key, how can I be found, and a value, what information do I hand over if someone attends to me.

## Slide 15 — Why three separate vectors?

Why three different vectors instead of one? Because the roles really are different. The way cat advertises itself, its key, might say, I'm a subject noun, which attracts verbs looking for their subject. But what cat actually hands over, its value, is its semantic content, animal, feline, pet. Separating them lets the model learn what to look for, what to be found by, and what to pass on, independently. And each one is simply a learned linear projection of the same input embedding.

## Slide 16 — Analogy 3: the spotlight

Third analogy, a spotlight. Each token shines a spotlight over all the tokens, with different brightness on each. These brightnesses are the attention weights, and they add up to one. For sat, maybe seventy percent on cat, twenty percent on on, and ten percent spread over the rest. The new representation of sat is then zero point seven times cat's value, plus zero point two times on's value, plus zero point one times the others. These numbers are illustrative, but the formula is exactly what the code computes.

## Slide 17 — The math in plain English

Now the maths in plain words. Start with X, six tokens by seven sixty eight. Step one, project X with three weight matrices to get Q, K and V, each six by sixty four. Step two, score every pair: the dot product of query i with key j. That gives a six by six table. Step three, divide by the square root of sixty four, which is eight. Step four, apply softmax to each row so the weights are positive and sum to one. Step five, each output is the weighted sum of value vectors. All of that compresses into the famous formula: softmax of Q K transpose over root d k, times V.

## Slide 18 — The full flow, with shapes

Here's the same thing as a diagram. X, six by seven sixty eight, branches into three projections. Each produces a six by sixty four matrix. Q and K meet to form the six by six score table, scaled by root sixty four. That goes through masking and softmax, still six by six. Then the weights multiply V to give the output, six by sixty four. Notice V doesn't take part in the scoring at all. It only gets mixed at the end.

## Slide 19 — Self-attention vs cross-attention

One more term. What we're building is self-attention: queries, keys and values all come from the same sequence, so the sentence attends to itself. The original transformer for translation also used cross-attention, where the decoder's queries look at the encoder's keys and values, which come from a different sentence, the source language. GPT is a decoder only model, so we only need self-attention, with a causal mask, which we'll add shortly.

## Slide 20 — 10.3 Building Self-Attention Step by Step

Section three. Building self-attention, step by step, every line, every shape.

## Slide 21 — Step 0 · setup (notebook cells 2 & 4)

Step zero, the setup. We import torch, the neural network module nn, the functional module F, which gives us softmax and gelu, and math for the square root. Then we fake the output of chapter nine: torch dot randn creates random numbers of shape two by six by seven sixty eight. Two sentences, six tokens each, seven sixty eight numbers per token. When I ran it, the print confirmed torch size two, six, seven sixty eight. In a real model these would be the embeddings, here they're random because we only care about the mechanics.

## Slide 22 — Step 1 · Q, K, V projections (cell 6)

Step one, the projections. d model is seven sixty eight, d k is sixty four. We create three linear layers, each mapping seven sixty eight numbers to sixty four. Bias equals false, in GPT two style, because the layer norm before attention already handles centring. Then we apply each to the embeddings. A linear layer acts on the last dimension only, so two by six by seven sixty eight becomes two by six by sixty four. Every one of the twelve tokens across both sentences now has a sixty four number query, key and value. These three weight matrices are learned during training. Right now they're random.

## Slide 23 — What `nn.Linear` does to shapes

A quick zoom into nn dot Linear, since it's everywhere. Linear seven sixty eight to sixty four stores a weight matrix of shape sixty four by seven sixty eight, and computes x times W transpose on the last dimension. All the leading dimensions, batch and seq, just come along for the ride. So two by six by seven sixty eight times seven sixty eight by sixty four gives two by six by sixty four. Each projection has seven sixty eight times sixty four, which is forty nine thousand one hundred fifty two parameters. Why sixty four? It's what each head will get later, when we split seven sixty eight across twelve heads.

## Slide 24 — Step 2 · scores = Q·Kᵀ (cell 8)

Step two, the scores. We want the dot product of every query with every key. For matrix multiplication the inner dimensions must match, so we transpose K's last two dimensions with transpose minus two, minus one. K goes from two by six by sixty four to two by sixty four by six. Now Q, two by six by sixty four, times K transpose, two by sixty four by six, gives two by six by six. The leading two is a batch dimension, handled automatically. Entry i j of the six by six matrix is query i dotted with key j.

## Slide 25 — Reading the 6×6 score matrix

How do we read this matrix? Rows are queries, the token doing the looking. Columns are keys, the token being looked at. So scores zero, two, four is how strongly token two matches token four in the first sentence. A dot product is the sum of sixty four element-wise products, large and positive when the query and key point in similar directions. Here's the real first row from my notebook run: minus two point six, two point four nine, minus four point four two, minus zero point one seven, two point six, three point nine four. These are spread out over about plus or minus five, and that's a problem the next step fixes.

## Slide 26 — Worked example by hand (notebook exercise 1)

Let's do one completely by hand. This is exercise one from the notebook, and I checked every number in PyTorch. Two tokens, three dimensions. Query zero is one, zero, one. Key zero is one, one, zero. Their dot product is one. Query zero with key one, zero one one, is also one. Query one, zero one one, with key zero gives one, with key one gives two. Divide by root three, about one point seven three, giving zero point five seven seven and one point one five five. Softmax of two equal numbers is a half and a half. Softmax of zero point five seven seven and one point one five five is zero point three six and zero point six four. Finally mix the values: row zero is half of two, zero, one plus half of one, two, zero, which is one point five, one, zero point five. Row one is zero point three six times the first value plus zero point six four times the second, giving one point three six, one point two eight, zero point three six.

## Slide 27 — Step 3 · scale by √d_k (cell 10)

Step three, scaling. One line: divide the scores by the square root of d k. With d k equal to sixty four, that's dividing by eight. The shape stays two by six by six. But why the square root? Let's actually look at the maths, because the notebook just says a proof shows this keeps variance stable.

## Slide 28 — Why √d_k? The variance argument

Here's the argument. Suppose the entries of q and k are independent with mean zero and variance one. The dot product is a sum of d products, each with variance one, so the total variance is d and the standard deviation is root d. I measured it with twenty thousand random pairs. At d equals sixty four the standard deviation was seven point nine four, almost exactly eight. At seven sixty eight it was about twenty eight. Divide by root d, and the green line sits right at one regardless of dimension. That's the whole justification: scaling keeps the scores at a consistent size no matter how wide the heads are.

## Slide 29 — Why big scores hurt: softmax saturates

And why do large scores matter? Because softmax exaggerates differences. Scores of one, two and three give weights of about nine percent, twenty four percent and sixty six percent. Multiply those scores by eight, roughly what happens without scaling at d equals sixty four, and you get essentially zero, zero, and one. All the attention collapses onto one token. Worse, in that saturated regime the gradients of softmax are nearly zero, so the query and key weights barely learn. Scaling keeps softmax in its sensitive range.

## Slide 30 — Step 4 · softmax → attention weights (cell 12)

Step four, softmax. F dot softmax with dim equals minus one normalises along the last dimension, the keys. So each row, one query, becomes a probability distribution over the keys. In my run, token zero's weights were zero point one one, zero point two oh, zero point oh nine, zero point one five, zero point two one, zero point two five, and they sum to exactly one. The dim argument matters enormously. Softmax over dim zero would normalise across the batch, which is meaningless. Always minus one here.

## Slide 31 — Step 5 · weighted sum of values (cell 14)

Step five, mix the values. Attention weights are two by six by six, V is two by six by sixty four. Multiply, and we get two by six by sixty four. Look at a single sentence: a six by six matrix times a six by sixty four matrix. Row i of the result is the sum over j of weight i j times value j. A weighted average of value vectors. If token two gave seventy percent to token one and twenty percent to token three, its output is mostly token one's value, with some of token three's. Each token's output now carries information from the tokens it attended to.

## Slide 32 — The five steps on real numbers (my run)

Here are those steps on real numbers from a run I did with the tokens of the cat sat on the mat. Left: raw scores, spanning about plus or minus six. Middle: the same after dividing by eight, now within about plus or minus one. Right: after softmax. Every row sums to one, and with random untrained weights the attention is fairly spread out, which is what you'd expect. Training is what will make these patterns meaningful.

## Slide 33 — All together: `scaled_dot_product_attention` (cell 16)

Now we package everything into one function, scaled dot product attention. It takes Q, K, V, and an optional mask. Line one reads d k from the last dimension of Q, so the function works for any head size. Then scores equals Q times K transpose, shape batch, seq, seq. Divide by root d k. If a mask is provided, masked fill replaces every score where the mask is zero with minus infinity. We'll see why in a moment. Softmax along the last dimension gives the weights. Multiply by V for the output, and return both the output and the weights, so we can visualise them later. About ten lines of real logic. This is the core of every transformer.

## Slide 34 — Shape tracking summary

Here is the shape table to memorise. Projection: two six seven sixty eight to two six sixty four. Transpose K: two sixty four six. Q times K transpose: two six six. Scale, mask, softmax keep two six six. Weights times V: back to two six sixty four. And the three classic bugs: forgetting the transpose, which crashes with a shape error, or worse, silently works when d k happens to equal seq. Softmax on the wrong dimension. And a mask with a shape that doesn't broadcast. When learning, print shapes after every line.

## Slide 35 — 10.4 Causal Masking

Section four. Causal masking, no peeking at the future.

## Slide 36 — The cheating problem

Why do we need a mask? In training, one sentence gives us several lessons at once. After the, predict cat. After the cat, predict sat, and so on. All positions are processed in parallel. But the attention we built lets every token see every other token. So while the model is supposed to predict what comes after cat, cat can attend to sat, which is the answer. In this illustrative row, more than half the attention goes to future tokens. That's like sitting an exam with the answer key on the desk. The model learns to copy, and then fails completely at generation time, when the future doesn't exist yet.

## Slide 37 — The rule: token *i* sees only positions 0…i

The rule is simple. The token at position i can attend to positions zero through i, itself and the past, never the future. So sat at position two can look at the, cat and itself. If you draw allowed cells in a grid with queries as rows and keys as columns, you get a lower triangle. The book's analogy: reading a mystery novel, you can remember every page you've read, but you can't flip ahead.

## Slide 38 — Creating the mask (cell 18)

Building the mask is one line. Torch dot ones makes a six by six matrix of ones, and torch dot tril keeps the lower triangle including the diagonal, zeroing everything above. This is the real output. Row zero has a single one: token zero sees only itself. Row two has three ones: tokens zero, one and two. Row five is all ones: the last token sees everything. One small note: the docstring calls this a boolean tensor, but it's actually float ones and zeros. That works fine because the attention function compares mask equals zero.

## Slide 39 — Applying it: −∞ before softmax (cell 20)

Now we use it. Random Q, K and V of shape two by six by sixty four, the mask, and call our function with mask equals causal mask. Inside, masked fill sets every blocked score to minus infinity before softmax. Since e to the minus infinity is zero, those positions get exactly zero weight, and the remaining weights in each row still sum to one. Here's my real output. Token zero puts all its weight, one point zero, on itself. Token one splits zero point four and zero point six. Token two splits across three tokens. And the upper triangle is exactly zero. Notice also that the six by six mask broadcasts automatically across the batch of two.

## Slide 40 — Mask → masked scores → weights (my run)

Here is the masking pipeline visually, from my run. On the left, the mask, ones in the lower triangle. In the middle, the scaled scores after masked fill: every future cell is minus infinity. On the right, after softmax: the first row is a single one, and every future cell is exactly zero. Why minus infinity and not just zero? Because a score of zero still gets e to the zero, which is one, a real chunk of weight. Only minus infinity gives exactly nothing.

## Slide 41 — Training vs inference

Let's be clear about training versus inference. In training we feed the whole sequence at once for efficiency, so the future tokens are physically present and must be hidden by the mask. During generation we produce one token at a time, so the future simply doesn't exist, and the restriction is automatic. The mask is what makes training conditions match generation conditions. That's why a decoder model like GPT can learn from every position of a sentence in one parallel pass.

## Slide 42 — 10.5 From One Head to Many

Section five. From one head to many.

## Slide 43 — Why one head isn't enough

A single head has one set of attention weights per token, one probability distribution. But language has many simultaneous relationships. Subject verb agreement, coreference, syntax, semantic links, and plain positional patterns like look at the previous word. One distribution can't do all of those at once. If it focuses on the subject, it can't simultaneously focus on the previous word. So we run several attention heads in parallel, each free to learn its own pattern.

## Slide 44 — Multi-head = several perspectives, same budget

The neat part is that multi-head attention costs no extra parameters. Instead of one head with seven sixty eight dimensions, we use twelve heads with sixty four dimensions each. Twelve times sixty four is seven sixty eight. Each head gets its own slice of Q, K and V, computes its own attention pattern, and produces a sixty four dimension output. Concatenate the twelve and you're back at seven sixty eight, and a final output projection blends them. I verified that the attention module has two million three hundred fifty nine thousand two hundred ninety six parameters whether you configure one head or twelve.

## Slide 45 — MultiHeadAttention · `__init__` (cell 22)

Here's the constructor. The assert checks that d model divides evenly by the number of heads, seven sixty eight by twelve is sixty four, fine. We store d head. Then the first efficiency trick: instead of three separate linear layers, one linear layer maps seven sixty eight to three times seven sixty eight, two thousand three hundred and four outputs, producing Q, K and V for all heads in a single matrix multiply. Then an output projection, seven sixty eight to seven sixty eight, which mixes the heads after concatenation. And a dropout layer that we'll apply to the attention weights during training.

## Slide 46 — `forward` part 1 · project and split (cell 22)

The forward pass, part one. Unpack batch, seq and d model from x. Project: two by six by seven sixty eight becomes two by six by two thousand three hundred and four. Now the reshape trick. Reshape the last dimension, two thousand three hundred four, into three by twelve by sixty four: which of Q, K, V, which head, and which of the sixty four dimensions. Then permute the axes into the order three, batch, heads, seq, d head. That's what the indices two, zero, three, one, four mean: take old axis two first, then old axis zero, and so on. Finally index zero, one, two to split out Q, K and V, each of shape two by twelve by six by sixty four. Heads now sit next to batch, like an extra batch dimension.

## Slide 47 — The reshape trick, visualised

Let's slow down on this trick, because it's the hardest part of the chapter. After the projection, each token's two thousand three hundred four numbers are laid out as all the Q's for the twelve heads, then all the K's, then all the V's. Reshape doesn't move any data, it just labels each number: this one is Q, head five, dimension thirty. Permute then rearranges the axes so the head axis sits before the sequence axis. The result: for each of the two sentences, twelve independent six by sixty four problems. And since matrix multiply in PyTorch only works on the last two dimensions and broadcasts over the rest, Q times K transpose computes all twenty four attention maps in a single call. No Python loop over heads.

## Slide 48 — `forward` part 2 · attention per head (cell 22)

Part two is the same five steps as before, just with an extra head axis. Scores are now two by twelve by six by six: a six by six table per head per sentence. Scale by root sixty four. For the mask, if it's two dimensional, we unsqueeze twice to make it one by one by six by six, so it broadcasts across batch and heads. Masked fill with minus infinity, softmax on the last dimension, then dropout on the attention weights, which randomly zeroes some weights during training as regularisation. Then weights times V gives two by twelve by six by sixty four.

## Slide 49 — `forward` part 3 · concatenate and project (cell 22)

Part three undoes the split. Transpose axes one and two, so we have batch, seq, heads, d head: two by six by twelve by sixty four. Now for each token, the twelve head outputs sit next to each other. Reshape to two by six by seven sixty eight, which concatenates the twelve sixty four dimension outputs into one seven sixty eight vector per token. Finally the output projection mixes information across heads. We return the output and the attention weights.

## Slide 50 — Testing it (cell 22) · real output

Testing it: twelve heads, random input of two by six by seven sixty eight, a causal mask. My real output: input two six seven sixty eight, output two six seven sixty eight, and attention weights two by twelve by six by six, one six by six map for each of the twelve heads. The fact that the output shape equals the input shape is what lets us stack these layers as deep as we like.

## Slide 51 — Why `.reshape()` and not `.view()`?

A practical PyTorch detail the book highlights. Transpose and permute don't actually move numbers in memory, they just change the strides, the recipe for walking through memory. The result is called non contiguous. View requires contiguous memory, so calling view after a transpose throws a runtime error. Reshape handles both cases: it returns a view when it can and makes a copy when it must. The alternative is contiguous then view. Rule of thumb: after transpose or permute, use reshape. The small snippet here is mine, you can paste it into the notebook to see the error yourself.

## Slide 52 — 10.6 The Complete Transformer Block

Section six. The complete transformer block.

## Slide 53 — What attention alone is missing

Attention alone isn't enough. First, it's mostly linear: projections, then a weighted average. Stacking linear operations just gives another linear operation, so we need a non-linearity to learn complex functions. Second, deep stacks are hard to train, so we need residual connections and normalisation. Third, attention moves information between tokens, but we also want to process that information inside each token. The book's picture is an assembly line: each station adds something, but the original item always travels alongside, thanks to the residual connections.

## Slide 54 — Component 1 · Feed-forward network (cell 24)

The feed forward network. Two linear layers. fc1 expands seven sixty eight to three thousand seventy two, four times wider. Then GELU, the non-linearity. Then dropout. Then fc2 projects back down to seven sixty eight. It's called position wise because the same network is applied independently to every token. Position zero gets FFN of x zero, position one gets FFN of x one, same weights. No information moves between tokens here. That's attention's job. In my run the shapes went two six seven sixty eight, to two six three oh seven two inside, and back to two six seven sixty eight.

## Slide 55 — GELU vs ReLU

GELU, the Gaussian error linear unit, is x times phi of x, where phi is the cumulative distribution of a standard normal. Compared to ReLU, which is a hard zero for negatives, GELU is smooth. At x equals minus one it outputs about minus zero point one six instead of zero, and at plus one it gives about zero point eight four. The smooth curve gives gradients everywhere, which tends to train a bit better. GPT two, BERT, and most transformers use it.

## Slide 56 — FFN parameters & why bias here

Parameters. fc1 has seven sixty eight times three oh seven two weights, about two point three six million, plus three thousand seventy two biases. fc2 is the same size the other way, plus seven sixty eight biases. Total about four point seven two million, roughly two thirds of a whole block. Notice the FFN keeps the default bias equals true, while our attention uses bias false. That's a simplification common in educational code. The original GPT two actually does have attention biases, and the book's chapter eleven weight loading code deals with that difference.

## Slide 57 — Component 2 · LayerNorm

Layer normalisation. For each token separately, compute the mean and variance across its seven sixty eight features, subtract the mean, divide by the standard deviation, then apply a learned scale gamma and shift beta. This keeps the activations in a healthy range as data flows through many layers. Note it normalises across features for each token, unlike batch norm, which normalises across the batch. Parameters: gamma and beta, seven sixty eight each, one thousand five hundred thirty six. One catch I hit: the book's printed snippet writes LayerNorm with a keyword d model equals seven sixty eight, and that raises a type error, because the parameter is actually called normalized shape. Just pass the number positionally, as the notebook's classes do.

## Slide 58 — Component 3 · Residual (skip) connections

Residual connections. Instead of replacing x with attention of x, we add: x plus attention of x. The layer only has to learn a refinement, a delta, rather than rebuilding the representation from scratch. The book's piano analogy: each lesson adds improvements to what you already know. And there's a training benefit. The derivative of x plus f of x with respect to x includes a plain one from the skip path, so gradients can flow straight back. Without it, as in the book's example, if every layer scales the gradient by zero point eight, after twelve layers a gradient of zero point five shrinks to about zero point oh three. With the skip, there's always an unimpeded path. That's how GPT three can stack ninety six blocks.

## Slide 59 — Component 4 · Pre-norm vs post-norm

Where does layer norm go? The original 2017 paper used post norm: add the residual, then normalise. GPT two and most modern models use pre norm: normalise the input to the sub-layer, then add the result back to the untouched x. The difference matters. In pre norm, the residual stream from input to output is pure addition, it never passes through a normalisation. That clean highway makes deep networks train more stably and often without the learning rate warm up that post norm needs. We'll use pre norm.

## Slide 60 — The block, top to bottom

Here is the whole block. Input x, batch by seq by seven sixty eight. Layer norm one, then multi-head attention, then add the result back to the original x. That sum goes through layer norm two, then the feed forward network, and the result is added back again. The dashed lines are the residual skips. Two sub-layers, each wrapped in norm, then add. That's the entire transformer block.

## Slide 61 — `TransformerBlock` (cell 26)

And the code, which reads exactly like the diagram. The constructor creates two layer norms, the multi-head attention, the feed forward network, and a dropout. In forward: normalise x with ln1, run attention with the mask, apply dropout to the output and add it to x. Then normalise with ln2, run the feed forward network, dropout, add to x. Return x and the attention weights. Two residual lines, that's the whole block in about ten lines, built from pieces we've already written.

## Slide 62 — Testing the block · real output

Running the block on random input. Shapes in and out are both two six seven sixty eight, attention weights two twelve six six. The notebook also prints means: input mean zero point oh one oh eight, output zero point oh one two two, and the average absolute difference is about zero point two six. That's the residual design in action: the output is the input plus a moderate refinement, not a completely new vector. Your exact numbers will differ, since the weights are random.

## Slide 63 — Parameter count for one block (verified)

How many parameters in one block? The QKV projection is seven sixty eight times two three oh four, one point seven seven million. The output projection, five hundred ninety thousand. fc1 and fc2 about two point three six million each including biases. Two layer norms, three thousand seventy two. Total seven million eighty four thousand eight hundred, and I confirmed it by summing the parameters of the actual module. Twelve blocks gives about eighty five million. GPT two small has about a hundred twenty four million in total, the rest mostly being the token and position embeddings.

## Slide 64 — Information flow through one block

Let's trace it once more as a summary. Input two six seven sixty eight. Layer norm. Multi-head attention splits into two by twelve by six by sixty four, attends per head, and concatenates back. Add the residual. Layer norm. Feed forward expands to three oh seven two with GELU and comes back to seven sixty eight. Add the residual. Output, same shape. A useful mental model: attention is communication between tokens, the feed forward network is computation within each token. A block does one round of each.

## Slide 65 — From block to model (Ch 11 preview)

And here's a preview of chapter eleven. A GPT two model is the embedding layer, twelve transformer blocks in a module list, a final layer norm, and a language model head, a linear layer from seven sixty eight to fifty thousand two hundred fifty seven vocabulary logits. The forward pass embeds, loops through the blocks, normalises, and projects to logits. This is a condensed sketch from the book, and the mask is created from the sequence length in the real chapter eleven code. Everything inside the loop, you now understand completely.

## Slide 66 — 10.7 Visualising Attention

Section seven. Visualising attention.

## Slide 67 — `visualize_attention` (cell 28)

The visualisation helper. It takes the attention weights, a list of token strings, and a head index. It picks the first sentence and that head, giving a seq by seq matrix. Detach removes it from the autograd graph, cpu and numpy convert it for matplotlib. imshow draws it as a heatmap with values fixed between zero and one. Then it labels the axes: keys, attended to, along the bottom, queries, attending from, down the side, and adds a colour bar.

## Slide 68 — Running it on a real sentence (cell 28)

Then the notebook runs a real sentence. The GPT two tokenizer turns the quick brown fox jumps over the lazy dog into nine tokens. Notice the leading spaces, GPT two's tokenizer attaches the space to the start of each word. A fresh, untrained embedding layer and a fresh transformer block process them, and we get attention weights of one by twelve by nine by nine. Then it plots the first four heads in a two by two grid. Important: this block is untrained, so the patterns will be the causal triangle with fairly random weights inside.

## Slide 69 — Untrained block (notebook figure, my run)

Here's the figure the notebook produced on my machine. You can see the causal structure: everything above the diagonal is dark, exactly zero. The first token always puts all its weight on itself, so the top left cell is bright. But inside the triangle, the patterns are essentially random, because nothing has been trained. That's still useful: it verifies the mask works.

## Slide 70 — Trained GPT-2 heads (my experiment)

To see what trained heads look like, I loaded pretrained GPT two and plotted three heads for the sentence, the cat sat on the mat because it was tired. Layer zero, head one, attends mostly to the token itself, a bright diagonal. Layer four, head eleven, is a previous token head: each token looks at the one right before it, a diagonal shifted by one. And layer five, head one, dumps nearly all its attention on the very first token. You might hope the word it would attend to cat, but in this head, it puts zero point nine eight on the first token, the. That's a well known pattern often called an attention sink, where the first token acts as a place to park attention. Which leads directly to the next slide.

## Slide 71 — Attention ≠ explanation

The book is careful here, and so should we be. From heatmaps you can conclude that masking works, and that heads behave differently, some local, some long range. You cannot conclude that a head encodes syntax or semantics, or that attention weights explain a decision. The feed forward layers, residual stream and norms carry a lot of the computation, heads interact with each other, and a weight tells you where a head reads from, not what it does with what it read. The attention sink we just saw is a perfect example: high weight, almost no meaning. Use visualisations for intuition, not explanation.

## Slide 72 — 10.8 Practical Considerations

Section eight. Practical considerations.

## Slide 73 — Memory is O(n²) in sequence length

Attention's big cost is memory that grows with the square of the sequence length, because the score tensor is batch by heads by n by n. At n equals five twelve, that's two hundred sixty two thousand scores per head. At two thousand forty eight, about four million. With a batch of eight and twelve heads at two thousand forty eight tokens, that's eight times twelve times two thousand forty eight squared, about four hundred million floats, times four bytes, roughly one point six gigabytes, for just one layer's scores. Double the context, quadruple the memory. GPT two used ten twenty four tokens. Longer contexts need more efficient techniques, which the book returns to in chapter sixteen.

## Slide 74 — The full pipeline in code (cell 30) · real output

The notebook ends by running everything end to end. Tokenise the cat sat on the mat into six IDs, embed them to one by six by seven sixty eight, build a causal mask of size six, and push them through one transformer block. Output one by six by seven sixty eight, context aware vectors. In my run the token IDs were four sixty four, three seven nine seven, three three three two, three nineteen, two sixty two, and two six oh three. Small detail: the book's text lists mat as two one five four seven, but the real GPT two tokenizer gives two six oh three, so trust the notebook output.

## Slide 75 — 10.9 Key Takeaways

Let's wrap up with the key takeaways.

## Slide 76 — What we built

What did we build? Scaled dot product attention, softmax of Q K transpose over root d k, times V. Causal masking with tril and masked fill minus infinity. Multi-head attention, twelve heads of sixty four, one fused projection, and the reshape and permute trick. A complete pre norm transformer block with attention, a GELU feed forward network and two residual connections, about seven point one million parameters. And attention heatmaps, which are great for checking the mask and dangerous for over-interpretation.

## Slide 77 — Core concepts to remember

The core concepts. Static embeddings become context aware vectors with the same shape. Query is what I seek, key is how I'm found, value is what I give. We scale by root d k because the dot product's spread grows like root d k. Multi-head attention gives different perspectives at no extra parameter cost. Residuals and layer norm make deep stacks trainable. And this exact mechanism powers GPT four, BERT, vision transformers and even AlphaFold, applied to different kinds of sequences.

## Slide 78 — Review questions 1–3

Review questions. Pause and answer each one before I do. Question one: why aren't static embeddings enough? Because bank gets the same vector in river bank and money bank. The lookup can't see neighbours, attention mixes in context so the vectors diverge, as we saw with real GPT two. Question two: the roles of Q, K and V, and why the dot product measures relevance. The query is what a token seeks, the key is what it advertises, the value is what it passes on. The dot product is large when query and key point the same way. Question three: why scale by root d k? Because the dot product's standard deviation grows like root d k, about eight for sixty four. Without scaling softmax saturates, the weights become nearly one hot and the gradients vanish.

## Slide 79 — Review questions 4–6

Question four: what is causal masking? A lower triangular mask that sets future scores to minus infinity, so their weights become zero. That makes training match generation, where the future doesn't exist yet. Question five: how do multiple heads give different perspectives without more parameters? We split seven sixty eight into twelve heads of sixty four, which is still seven sixty eight. The fused projection is still seven sixty eight by two three oh four. Each head just gets its own slice and learns its own pattern. Question six: the reshape trick. We reshape to separate Q, K, V and heads, then permute so heads act like a batch dimension, and one batched matrix multiply handles all heads at once on optimised kernels, instead of a slow Python loop.

## Slide 80 — Review questions 7–8

Question seven: the four components of a block. Attention, for exchanging information between tokens. The feed forward network, for non-linear processing within each token. Residual connections, which preserve the original signal and give gradients a highway. And layer norm, which keeps activations in a stable range. Question eight: pre norm versus post norm. Post norm is layer norm of x plus f of x, as in the original paper. Pre norm is x plus f of layer norm of x, used by GPT two, because the residual path stays pure addition and deep models train more stably.

## Slide 81 — Review questions 9–10

Question nine: memory for batch four, twelve heads, sequence two thousand forty eight. Four times twelve times two thousand forty eight squared is about two hundred one million floats. At four bytes each, that's about zero point eight gigabytes for one layer's scores. Double the length and memory quadruples. Question ten: why be cautious with heatmaps? They show where a head reads, not what it computes. Feed forward layers and residuals matter too, heads interact, and attention sinks get huge weight with little meaning. You can confirm masking and see diversity. You can't claim a head does syntax or that weights explain a decision.

## Slide 82 — Practice this (notebook ch10.ipynb)

Your practice list, all in the chapter ten notebook. Run cells two through thirty in Colab and print shapes after every line. Then the exercises. Cell thirty two, exercise one: manual attention, you should get one point five, one, zero point five, and one point three six, one point two eight, zero point three six. Cell thirty four: with and without the mask, assert the upper triangle is zero. Cell thirty six: trace shapes for d model five twelve with eight heads and sequence ten. The projection gives fifteen thirty six, heads give eight by ten by sixty four. Cell thirty eight: compare one head and twelve heads, both should have two million three hundred fifty nine thousand two hundred ninety six attention parameters. Cell forty: visualise heads for your own sentence. Cells forty two to forty six: stack three blocks, write a post norm block, and count the block parameters, seven million eighty four thousand eight hundred.

## Slide 83 — Up next: Chapter 11

In chapter eleven, we complete the picture. We stack twelve of these blocks, add the final layer norm and the language model head, load real GPT two weights into our own code, and generate text. See you there.

## Slide 84 — Credits

This video is based on the book Build Your First LLM by Hasan Degismez. The code is from the FirstLLM code repository under the MIT license, and the diagrams, narration and extra experiments are my own adaptation for study. If this helped you, please buy the book at leanpub dot com slash First LLM, it has much more detail than I could fit here. Thanks for watching.

