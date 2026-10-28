---
marp: true
theme: llmdark
paginate: true
size: 16:9
footer: "Build Your First LLM · Ch 10: Attention Is All You Need · Waqar Shaikh Builds · Code: FirstLLM/code (MIT)"
---

<!-- _class: lead -->
<!-- _paginate: false -->
# Build Your First LLM
## Chapter 10 — Attention Is All You Need
Full walkthrough: Q, K, V · scaling · causal mask · multi-head · Transformer block
**Waqar Shaikh Builds**

<!-- say: Welcome to chapter ten of my study series on Build Your First LLM by Hasan Degismez. This is the chapter I've been waiting for, because it's the heart of every transformer. We are going to build attention from scratch in PyTorch, tracking every tensor shape, then turn it into multi-head attention, and finally into a complete transformer block, the exact unit GPT two stacks twelve times. Every piece of code in this video comes from the book's companion notebook, which I actually ran on my machine, so the outputs you see are real. -->

---

# Run along with the notebook

- Notebook: **github.com/FirstLLM/code/blob/main/notebooks/ch10.ipynb**
- Colab (no setup): **colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/ch10.ipynb**
- I ran every code cell on CPU (PyTorch 2.x): **all cells pass**
- Cell numbers below = cell index in the notebook file, counting from 0 (markdown included)

<small>Code shown verbatim from FirstLLM/code (MIT License).</small>

<!-- say: Open the notebook alongside this video. The links are on screen and in the description. You can run it in Colab with no setup. I executed every code cell on a plain CPU and all of them ran without errors. When I mention a cell number, I'm counting cells in the notebook file from zero, including markdown cells, so you can jump straight to it. All code shown is from the FirstLLM code repository, which is MIT licensed. -->

---

# Chapter 10 roadmap

1. Why static embeddings aren't enough — "bank"
2. Intuition: committee, search engine, spotlight
3. Self-attention step by step (5 steps, every shape)
4. Causal masking — no peeking at the future
5. One head → many heads (the reshape trick)
6. The Transformer block: FFN, LayerNorm, residuals, pre-norm
7. Parameter counts · visualising attention · O(n²) memory
8. Full pipeline · takeaways · 10 review questions · practice list

<!-- say: Here's the plan. First, the problem: why the embeddings from chapter nine aren't enough. Then three analogies that build intuition for queries, keys and values. Then the core: self-attention in five steps, with shapes at every line. Then causal masking, which stops the model from cheating. Then we go from one head to twelve heads with the reshape trick. Then we assemble a full transformer block with the feed forward network, layer normalisation and residual connections. We'll count parameters, visualise attention, talk about the quadratic memory cost, trace the whole pipeline, and finish with takeaways, all ten review questions with answers, and a practice list. -->

---

# Notation used throughout

| Symbol | Meaning | GPT-2 small |
|---|---|---|
| `batch` | sequences processed together | 2 in examples |
| `seq` / n | tokens per sequence | 6 ("The cat sat on the mat") |
| `d_model` | embedding size | 768 |
| `num_heads` / h | attention heads | 12 |
| `d_head` = `d_k` | per-head size = d_model / h | 64 |
| `d_ff` | feed-forward hidden size = 4·d_model | 3072 |

<!-- say: Let's fix our notation, because shapes are everything in this chapter. Batch is how many sequences we process at once, two in the examples. Seq, or n, is the number of tokens, six for the cat sat on the mat. D model is the embedding width, seven hundred sixty eight for GPT two small. Num heads is twelve. D head, also called d k, is d model divided by the number of heads, which is sixty four. And d f f, the hidden size of the feed forward network, is four times d model, three thousand seventy two. Keep these numbers in your head: seven sixty eight, twelve, sixty four, three oh seven two. -->

---

<!-- _class: divider -->
# 10.1 Why Static Embeddings Aren't Enough

<!-- say: Section one. Why static embeddings aren't enough. -->

---

# The "bank" problem

```python
text1 = "I went to the river bank"
text2 = "I deposited money at the bank"
# After GPT2Embeddings (Ch 9): both "bank" tokens get
# THE SAME 768-number token vector (+ a position vector)
```

- Chapter 9's embedding = **lookup table**: token ID → fixed row
- Token ID for " bank" in GPT-2 is **3331** — same row every time
- Different positions add different position vectors, but **no context**

<!-- say: In chapter nine we built embeddings. Each token ID looks up a row in a table, and we add a position vector. So in, I went to the river bank, and, I deposited money at the bank, the token bank, which is ID three three three one in GPT two's vocabulary, fetches exactly the same row both times. The position vectors differ a little because bank sits at a different position, but nothing in the embedding layer knows about river or money. It's a pure lookup. The meaning of bank depends on its neighbours, and the embedding layer can't see the neighbours. -->

---

# Recap: what Chapter 9 gives us

```python
class GPT2Embeddings(nn.Module):
    def forward(self, token_ids):
        token_emb = self.token_embed(token_ids)  # (batch, seq, 768)
        pos_emb = self.pos_embed(position_ids)   # (batch, seq, 768)
        embeddings = token_emb + pos_emb         # (batch, seq, 768)
        return embeddings
```

**Input to this chapter:** `(batch, seq, 768)` — *what* each token is + *where* it is.
**Missing:** what each token *means here*.

<!-- say: Here's the chapter nine forward pass as a reminder. Token embedding, shape batch by seq by seven sixty eight. Position embedding, same shape. Add them. So the input to this chapter is a tensor of shape batch, seq, seven sixty eight, which encodes what each token is and where it is. What's missing is what each token means in this particular sentence. That's the job of attention. -->

---

# Dictionary definition vs sentence meaning

- Static embedding ≈ a dictionary entry: *bank: 1) river edge 2) financial institution 3) to rely on*
- Attention ≈ a reader who sees the sentence and highlights the right sense
- "river bank" → look at *river* → emphasise sense 1
- "savings bank" → look at *savings* → emphasise sense 2
- **Same shape in and out**, different values: `(seq, 768) → (seq, 768)`

<!-- say: A helpful analogy from the book. A static embedding is like a dictionary entry that lists every sense of bank at once: river edge, financial institution, to rely on. You get all of them blended and don't know which applies. Attention is like a smart reader who reads the whole sentence and highlights the right sense. In river bank, bank looks at river and moves towards the first meaning. In savings bank, it looks at savings and moves toward the second. Crucially, the shape doesn't change. Six by seven sixty eight goes in, six by seven sixty eight comes out. Only the values change. -->

---

# Evidence from real GPT-2 (my experiment)

![w:1250](img/bank_gpt2.png)

<small>Hidden state of " bank" in 4 sentences, pretrained GPT-2 (HF `gpt2`), cosine similarity per layer.</small>

<!-- say: I wanted to see this for real, so I ran the pretrained GPT two model on four sentences and took the hidden vector for bank at every layer. Then I compared them with cosine similarity. At layer zero, before any attention, they're nearly identical, around zero point nine nine eight. As we go up the layers, the pink line, river bank versus money bank, drops to about zero point seven five, while the gold line, two financial uses, stays around zero point nine five. So the representation genuinely separates by meaning. The jump back up at the last layer is a known quirk of GPT two's final layer, where all vectors become very similar. The lesson: attention layers are where context gets mixed in. -->

---

# Not just ambiguous words

| Phenomenon | Example | What attends to what |
|---|---|---|
| Coreference | Alice went to the store. **She** bought milk. | She → Alice |
| Long-range agreement | The **keys** to the cabinet **are** | are → keys (not cabinet) |
| Syntax | The **cat** that chased the mouse **sat** | sat → cat |
| Semantics | **Paris** is the **capital** of | capital → Paris |

Attention = a general way for tokens to **exchange information**.

<!-- say: And it's not only about words with two meanings. Attention handles coreference: in Alice went to the store, she bought milk, the word she needs information from Alice. Long-range agreement: in the keys to the cabinet are, the verb are must agree with keys, not with the nearer word cabinet. Syntax: in the cat that chased the mouse sat, the subject of sat is cat, several words back. Semantics: capital should pull in information about Paris. All of these are one mechanism: tokens exchanging information with each other. -->

---

# Where we are in the pipeline

![w:1700](img/pipeline.png)

<!-- say: Here is the whole pipeline. Text goes into the tokenizer from chapter eight, giving token IDs of shape one by six. The embedding layer from chapter nine turns them into static vectors, one by six by seven sixty eight. This chapter adds the transformer block, which keeps the shape but makes the vectors context aware. Chapter eleven stacks twelve of these blocks and adds the language model head, which produces logits over all fifty thousand two hundred fifty seven tokens, and then we sample the next token. -->

---

<!-- _class: divider -->
# 10.2 What IS Attention?
Three analogies, then the math in plain English

<!-- say: Section two. What is attention? Three analogies, then the maths in plain English. -->

---

# Analogy 1: the committee meeting

Each token is a committee member. When "**sat**" speaks it:
1. **Listens** to everyone: The, cat, sat, on, the, mat
2. **Weighs relevance**: *cat* very (who sat?), *on* somewhat (where?), *The* little
3. **Updates** its own position using a weighted blend of their input

Result: "sat" now encodes *an action done by the cat, somewhere*.

<!-- say: First analogy, a committee meeting. Every token is a member. When it's sat's turn, it first listens to everyone, including itself. Then it decides how relevant each input is. Cat is very relevant, because it answers who sat. On is somewhat relevant, it hints where. The is barely relevant. Finally it updates its own position by blending everyone's input, weighted by relevance. After this, the vector for sat encodes something like, an action performed by the cat, at some location. -->

---

# Analogy 2: the search engine → Q, K, V

| Library search | Attention |
|---|---|
| What you type: "books about cats" | **Query** — what am I looking for? |
| Index terms on each book | **Key** — what do I offer / how can I be found? |
| The book's contents | **Value** — the information I pass on |

Compare query to every key → relevance scores → return values weighted by relevance

<!-- say: Second analogy, a library search. Your search text is the query. Each book has index terms, its keys. And each book has contents, its value. The search compares your query to every key, books tagged animals, pets, felines score high, books on history or dogs score low, and you get back the contents weighted by relevance. Attention is exactly this. Each token produces a query, what am I looking for, a key, how can I be found, and a value, what information do I hand over if someone attends to me. -->

---

# Why three separate vectors?

- **Query**: what to look for · **Key**: what to be found by · **Value**: what to pass on
- They can differ! For "cat":
  - Key ≈ "I'm a subject noun" → attracts verbs looking for a subject
  - Value ≈ "animal, feline, pet" → the content verbs receive
- Each is a **learned linear projection** of the same embedding

<!-- say: Why three different vectors instead of one? Because the roles really are different. The way cat advertises itself, its key, might say, I'm a subject noun, which attracts verbs looking for their subject. But what cat actually hands over, its value, is its semantic content, animal, feline, pet. Separating them lets the model learn what to look for, what to be found by, and what to pass on, independently. And each one is simply a learned linear projection of the same input embedding. -->

---

# Analogy 3: the spotlight

For "sat" in "The cat sat on the mat" (illustrative):

| Token | cat | on | others (The, sat, the, mat) |
|---|---|---|---|
| Brightness (weight) | **0.70** | 0.20 | 0.10 combined |

`new_sat = 0.70·v_cat + 0.20·v_on + 0.10·(others)`

<!-- say: Third analogy, a spotlight. Each token shines a spotlight over all the tokens, with different brightness on each. These brightnesses are the attention weights, and they add up to one. For sat, maybe seventy percent on cat, twenty percent on on, and ten percent spread over the rest. The new representation of sat is then zero point seven times cat's value, plus zero point two times on's value, plus zero point one times the others. These numbers are illustrative, but the formula is exactly what the code computes. -->

---

# The math in plain English

Input `X`: (seq, d_model) = (6, 768)

1. **Project**: Q = X·W_q, K = X·W_k, V = X·W_v → each (6, 64)
2. **Score**: sᵢⱼ = qᵢ · kⱼ → (6, 6)
3. **Scale**: sᵢⱼ / √64
4. **Softmax** each row → weights that sum to 1
5. **Mix**: outᵢ = Σⱼ wᵢⱼ · vⱼ → (6, 64)

## Attention(Q, K, V) = softmax(Q·Kᵀ / √d_k) · V

<!-- say: Now the maths in plain words. Start with X, six tokens by seven sixty eight. Step one, project X with three weight matrices to get Q, K and V, each six by sixty four. Step two, score every pair: the dot product of query i with key j. That gives a six by six table. Step three, divide by the square root of sixty four, which is eight. Step four, apply softmax to each row so the weights are positive and sum to one. Step five, each output is the weighted sum of value vectors. All of that compresses into the famous formula: softmax of Q K transpose over root d k, times V. -->

---

# The full flow, with shapes

![w:1700](img/qkv_flow.png)

<!-- say: Here's the same thing as a diagram. X, six by seven sixty eight, branches into three projections. Each produces a six by sixty four matrix. Q and K meet to form the six by six score table, scaled by root sixty four. That goes through masking and softmax, still six by six. Then the weights multiply V to give the output, six by sixty four. Notice V doesn't take part in the scoring at all. It only gets mixed at the end. -->

---

# Self-attention vs cross-attention

- **Self-attention**: queries, keys and values all come from the **same sequence**
- **Cross-attention**: queries from one sequence (decoder), keys/values from another (encoder) — e.g. translation
- GPT is **decoder-only** → only (causal) self-attention

<!-- say: One more term. What we're building is self-attention: queries, keys and values all come from the same sequence, so the sentence attends to itself. The original transformer for translation also used cross-attention, where the decoder's queries look at the encoder's keys and values, which come from a different sentence, the source language. GPT is a decoder only model, so we only need self-attention, with a causal mask, which we'll add shortly. -->

---

<!-- _class: divider -->
# 10.3 Building Self-Attention Step by Step
Every line, every shape

<!-- say: Section three. Building self-attention, step by step, every line, every shape. -->

---

# Step 0 · setup (notebook cells 2 & 4)

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

batch_size = 2
seq_len = 6
embed_dim = 768
embeddings = torch.randn(batch_size, seq_len, embed_dim)
print(f"Input embeddings shape: {embeddings.shape}")
```
**Real output:** `Input embeddings shape: torch.Size([2, 6, 768])`

<!-- say: Step zero, the setup. We import torch, the neural network module nn, the functional module F, which gives us softmax and gelu, and math for the square root. Then we fake the output of chapter nine: torch dot randn creates random numbers of shape two by six by seven sixty eight. Two sentences, six tokens each, seven sixty eight numbers per token. When I ran it, the print confirmed torch size two, six, seven sixty eight. In a real model these would be the embeddings, here they're random because we only care about the mechanics. -->

---

# Step 1 · Q, K, V projections (cell 6)

```python
d_model = 768  # From embeddings (Ch9)
d_k = 64       # Dimension for Q, K, V (typical: d_model / num_heads)

W_q = nn.Linear(d_model, d_k, bias=False)  # Query projection
W_k = nn.Linear(d_model, d_k, bias=False)  # Key projection
W_v = nn.Linear(d_model, d_k, bias=False)  # Value projection

Q = W_q(embeddings)  # (batch, seq, d_k) = (2, 6, 64)
K = W_k(embeddings)  # (batch, seq, d_k) = (2, 6, 64)
V = W_v(embeddings)  # (batch, seq, d_k) = (2, 6, 64)
```
**Real output:** `Q shape: torch.Size([2, 6, 64])` (same for K, V)

<!-- say: Step one, the projections. d model is seven sixty eight, d k is sixty four. We create three linear layers, each mapping seven sixty eight numbers to sixty four. Bias equals false, in GPT two style, because the layer norm before attention already handles centring. Then we apply each to the embeddings. A linear layer acts on the last dimension only, so two by six by seven sixty eight becomes two by six by sixty four. Every one of the twelve tokens across both sentences now has a sixty four number query, key and value. These three weight matrices are learned during training. Right now they're random. -->

---

# What `nn.Linear` does to shapes

- `nn.Linear(768, 64)` stores a weight matrix **W: (64, 768)**
- Computes `y = x @ W.T` on the **last** dimension; all leading dims are "batch"
- (2, 6, **768**) @ (768, 64) → (2, 6, **64**)
- Parameters per projection: 768 × 64 = **49,152** (no bias)
- Why 64? Single-head demo now; later 768 / 12 heads = 64 per head

<!-- say: A quick zoom into nn dot Linear, since it's everywhere. Linear seven sixty eight to sixty four stores a weight matrix of shape sixty four by seven sixty eight, and computes x times W transpose on the last dimension. All the leading dimensions, batch and seq, just come along for the ride. So two by six by seven sixty eight times seven sixty eight by sixty four gives two by six by sixty four. Each projection has seven sixty eight times sixty four, which is forty nine thousand one hundred fifty two parameters. Why sixty four? It's what each head will get later, when we split seven sixty eight across twelve heads. -->

---

# Step 2 · scores = Q·Kᵀ (cell 8)

```python
# Q shape: (batch, seq, d_k) = (2, 6, 64)
# K shape: (batch, seq, d_k) = (2, 6, 64)
# K.transpose(-2, -1) swaps the last two dimensions
# So K goes from (2, 6, 64) → (2, 64, 6)

# Matrix multiplication: (2, 6, 64) @ (2, 64, 6) → (2, 6, 6)
scores = Q @ K.transpose(-2, -1)
```
**Real output:** `K transposed shape: torch.Size([2, 64, 6])`
`Attention scores shape: torch.Size([2, 6, 6])`

<!-- say: Step two, the scores. We want the dot product of every query with every key. For matrix multiplication the inner dimensions must match, so we transpose K's last two dimensions with transpose minus two, minus one. K goes from two by six by sixty four to two by sixty four by six. Now Q, two by six by sixty four, times K transpose, two by sixty four by six, gives two by six by six. The leading two is a batch dimension, handled automatically. Entry i j of the six by six matrix is query i dotted with key j. -->

---

# Reading the 6×6 score matrix

- Row *i* = query token *i*; column *j* = key token *j*
- `scores[0, 2, 4]` = how strongly token 2 ("sat") matches token 4 ("the") in sentence 0
- Dot product = Σ (64 element-wise products) → large if q and k point the same way
- **Real row 0 from my run:** `[-2.60, 2.49, -4.42, -0.17, 2.60, 3.94]`
- Raw scores span roughly ±5 here — that's the problem the next step fixes

<!-- say: How do we read this matrix? Rows are queries, the token doing the looking. Columns are keys, the token being looked at. So scores zero, two, four is how strongly token two matches token four in the first sentence. A dot product is the sum of sixty four element-wise products, large and positive when the query and key point in similar directions. Here's the real first row from my notebook run: minus two point six, two point four nine, minus four point four two, minus zero point one seven, two point six, three point nine four. These are spread out over about plus or minus five, and that's a problem the next step fixes. -->

---

# Worked example by hand (notebook exercise 1)

Q = [[1,0,1],[0,1,1]], K = [[1,1,0],[0,1,1]], V = [[2,0,1],[1,2,0]], d_k = 3

| | step | row 0 | row 1 |
|---|---|---|---|
| 1 | Q·Kᵀ | [1, 1] | [1, 2] |
| 2 | ÷ √3 | [0.577, 0.577] | [0.577, 1.155] |
| 3 | softmax | [0.500, 0.500] | [0.360, 0.640] |
| 4 | · V | [1.50, 1.00, 0.50] | [1.36, 1.28, 0.36] |

<small>Verified with PyTorch on my machine.</small>

<!-- say: Let's do one completely by hand. This is exercise one from the notebook, and I checked every number in PyTorch. Two tokens, three dimensions. Query zero is one, zero, one. Key zero is one, one, zero. Their dot product is one. Query zero with key one, zero one one, is also one. Query one, zero one one, with key zero gives one, with key one gives two. Divide by root three, about one point seven three, giving zero point five seven seven and one point one five five. Softmax of two equal numbers is a half and a half. Softmax of zero point five seven seven and one point one five five is zero point three six and zero point six four. Finally mix the values: row zero is half of two, zero, one plus half of one, two, zero, which is one point five, one, zero point five. Row one is zero point three six times the first value plus zero point six four times the second, giving one point three six, one point two eight, zero point three six. -->

---

# Step 3 · scale by √d_k (cell 10)

```python
# Scale by sqrt(dimension)
# Why sqrt? Math proof shows this keeps variance stable
scores = scores / math.sqrt(d_k)

print(f"Scaled scores shape: {scores.shape}")  # Still (2, 6, 6)
```
**Real output:** `Scaled scores shape: torch.Size([2, 6, 6])` · √64 = 8.00

- Shape unchanged; every score divided by **8**

<!-- say: Step three, scaling. One line: divide the scores by the square root of d k. With d k equal to sixty four, that's dividing by eight. The shape stays two by six by six. But why the square root? Let's actually look at the maths, because the notebook just says a proof shows this keeps variance stable. -->

---

# Why √d_k? The variance argument

If q and k have independent entries with mean 0, variance 1:
**q·k = Σᵢ qᵢkᵢ** → sum of d terms, each variance 1 → **Var = d, std = √d**

![w:1000](img/dot_std.png)

Measured std: d=64 → **7.94**, d=768 → **27.95**; after ÷√d → **≈1.0**

<!-- say: Here's the argument. Suppose the entries of q and k are independent with mean zero and variance one. The dot product is a sum of d products, each with variance one, so the total variance is d and the standard deviation is root d. I measured it with twenty thousand random pairs. At d equals sixty four the standard deviation was seven point nine four, almost exactly eight. At seven sixty eight it was about twenty eight. Divide by root d, and the green line sits right at one regardless of dimension. That's the whole justification: scaling keeps the scores at a consistent size no matter how wide the heads are. -->

---

# Why big scores hurt: softmax saturates

![w:1300](img/softmax_sharp.png)

- Scores [1,2,3] → [0.090, 0.245, 0.665] — attention spread across tokens
- ×8 → [0.000, 0.000, 1.000] — one token takes everything
- Saturated softmax ⇒ **near-zero gradients** ⇒ training stalls

<!-- say: And why do large scores matter? Because softmax exaggerates differences. Scores of one, two and three give weights of about nine percent, twenty four percent and sixty six percent. Multiply those scores by eight, roughly what happens without scaling at d equals sixty four, and you get essentially zero, zero, and one. All the attention collapses onto one token. Worse, in that saturated regime the gradients of softmax are nearly zero, so the query and key weights barely learn. Scaling keeps softmax in its sensitive range. -->

---

# Step 4 · softmax → attention weights (cell 12)

```python
# Apply softmax over the last dimension (across keys)
# This makes each row (each query) sum to 1
attn_weights = F.softmax(scores, dim=-1)

print(attn_weights[0, 0])
print(f"Sum of weights for token 0: {attn_weights[0, 0].sum().item():.4f}")
```
**Real output:** `tensor([0.1084, 0.2047, 0.0864, 0.1470, 0.2078, 0.2456])`
`Sum of weights for token 0: 1.0000`

softmax(sᵢ) = e^sᵢ / Σⱼ e^sⱼ — applied along **dim = -1** (across keys)

<!-- say: Step four, softmax. F dot softmax with dim equals minus one normalises along the last dimension, the keys. So each row, one query, becomes a probability distribution over the keys. In my run, token zero's weights were zero point one one, zero point two oh, zero point oh nine, zero point one five, zero point two one, zero point two five, and they sum to exactly one. The dim argument matters enormously. Softmax over dim zero would normalise across the batch, which is meaningless. Always minus one here. -->

---

# Step 5 · weighted sum of values (cell 14)

```python
# Attention weights: (batch, seq, seq) = (2, 6, 6)
# Values:           (batch, seq, d_k)  = (2, 6, 64)
# We want:          (batch, seq, d_k)  = (2, 6, 64)
output = attn_weights @ V
```
**Real output:** `Output shape: torch.Size([2, 6, 64])`

- (6, **6**) @ (**6**, 64) → (6, 64): row *i* of output = Σⱼ wᵢⱼ · vⱼ
- e.g. token 2 weights token 1 at 0.7, token 3 at 0.2 → `out[2] ≈ 0.7·V[1] + 0.2·V[3] + …`

<!-- say: Step five, mix the values. Attention weights are two by six by six, V is two by six by sixty four. Multiply, and we get two by six by sixty four. Look at a single sentence: a six by six matrix times a six by sixty four matrix. Row i of the result is the sum over j of weight i j times value j. A weighted average of value vectors. If token two gave seventy percent to token one and twenty percent to token three, its output is mostly token one's value, with some of token three's. Each token's output now carries information from the tokens it attended to. -->

---

# The five steps on real numbers (my run)

![w:1700](img/scores_steps.png)

<small>Random weights, seed 42, tokens of "The cat sat on the mat". Raw scores span about ±6; after ÷8 they're within ±1; softmax rows sum to 1.</small>

<!-- say: Here are those steps on real numbers from a run I did with the tokens of the cat sat on the mat. Left: raw scores, spanning about plus or minus six. Middle: the same after dividing by eight, now within about plus or minus one. Right: after softmax. Every row sums to one, and with random untrained weights the attention is fairly spread out, which is what you'd expect. Training is what will make these patterns meaningful. -->

---

<!-- _class: small -->
# All together: `scaled_dot_product_attention` (cell 16)

```python
def scaled_dot_product_attention(Q, K, V, mask=None):
    d_k = Q.size(-1)  # Get dimension of queries/keys
    # Step 1: Compute scores Q @ K^T
    scores = Q @ K.transpose(-2, -1)  # (batch, seq, seq)
    # Step 2: Scale by sqrt(d_k)
    scores = scores / math.sqrt(d_k)
    # Step 3: Apply mask if provided
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
    # Step 4: Softmax to get attention weights
    attn_weights = F.softmax(scores, dim=-1)  # (batch, seq, seq)
    # Step 5: Weighted sum of values
    output = attn_weights @ V  # (batch, seq, d_k)
    return output, attn_weights
```
<small>Docstring trimmed for space.</small>

<!-- say: Now we package everything into one function, scaled dot product attention. It takes Q, K, V, and an optional mask. Line one reads d k from the last dimension of Q, so the function works for any head size. Then scores equals Q times K transpose, shape batch, seq, seq. Divide by root d k. If a mask is provided, masked fill replaces every score where the mask is zero with minus infinity. We'll see why in a moment. Softmax along the last dimension gives the weights. Multiply by V for the output, and return both the output and the weights, so we can visualise them later. About ten lines of real logic. This is the core of every transformer. -->

---

# Shape tracking summary

| Operation | Input | Output |
|---|---|---|
| Q/K/V projection | (2, 6, 768) | (2, 6, 64) each |
| K transpose | (2, 6, 64) | (2, 64, 6) |
| Q @ Kᵀ | (2, 6, 64) @ (2, 64, 6) | (2, 6, 6) |
| ÷ √d_k, mask, softmax | (2, 6, 6) | (2, 6, 6) |
| weights @ V | (2, 6, 6) @ (2, 6, 64) | (2, 6, 64) |

**Common bugs:** `Q @ K` (forgot transpose) · softmax on `dim=0` · mask that doesn't broadcast

<!-- say: Here is the shape table to memorise. Projection: two six seven sixty eight to two six sixty four. Transpose K: two sixty four six. Q times K transpose: two six six. Scale, mask, softmax keep two six six. Weights times V: back to two six sixty four. And the three classic bugs: forgetting the transpose, which crashes with a shape error, or worse, silently works when d k happens to equal seq. Softmax on the wrong dimension. And a mask with a shape that doesn't broadcast. When learning, print shapes after every line. -->

---

<!-- _class: divider -->
# 10.4 Causal Masking
No peeking at the future

<!-- say: Section four. Causal masking, no peeking at the future. -->

---

# The cheating problem

Training text "The cat sat on the mat" gives 5 lessons at once:
`The → cat` · `The cat → sat` · `The cat sat → on` · …

Without a mask, "cat" can attend to **sat, on, mat** — the answers (illustrative):

| The | cat | **sat** | **on** | **the** | **mat** |
|---|---|---|---|---|---|
| 0.10 | 0.30 | 0.40 | 0.10 | 0.05 | 0.05 |

Like an exam with the answer key on the desk → fails at generation time.

<!-- say: Why do we need a mask? In training, one sentence gives us several lessons at once. After the, predict cat. After the cat, predict sat, and so on. All positions are processed in parallel. But the attention we built lets every token see every other token. So while the model is supposed to predict what comes after cat, cat can attend to sat, which is the answer. In this illustrative row, more than half the attention goes to future tokens. That's like sitting an exam with the answer key on the desk. The model learns to copy, and then fails completely at generation time, when the future doesn't exist yet. -->

---

# The rule: token *i* sees only positions 0…i

- Position 2 ("sat") → may attend to The, cat, sat — not on, the, mat
- Allowed cells form a **lower-triangular** matrix
- Like reading a mystery novel: remember every page so far, never peek ahead

<!-- say: The rule is simple. The token at position i can attend to positions zero through i, itself and the past, never the future. So sat at position two can look at the, cat and itself. If you draw allowed cells in a grid with queries as rows and keys as columns, you get a lower triangle. The book's analogy: reading a mystery novel, you can remember every page you've read, but you can't flip ahead. -->

---

<!-- _class: small -->
# Creating the mask (cell 18)

```python
def create_causal_mask(seq_len):
    # torch.tril creates a lower triangular matrix
    # 1s below diagonal (including diagonal), 0s above
    mask = torch.tril(torch.ones(seq_len, seq_len))
    return mask

mask = create_causal_mask(6)
print(mask)
```
```text
tensor([[1., 0., 0., 0., 0., 0.],
        [1., 1., 0., 0., 0., 0.],
        [1., 1., 1., 0., 0., 0.],
        [1., 1., 1., 1., 0., 0.],
        [1., 1., 1., 1., 1., 0.],
        [1., 1., 1., 1., 1., 1.]])
```

<!-- say: Building the mask is one line. Torch dot ones makes a six by six matrix of ones, and torch dot tril keeps the lower triangle including the diagonal, zeroing everything above. This is the real output. Row zero has a single one: token zero sees only itself. Row two has three ones: tokens zero, one and two. Row five is all ones: the last token sees everything. One small note: the docstring calls this a boolean tensor, but it's actually float ones and zeros. That works fine because the attention function compares mask equals zero. -->

---

<!-- _class: small -->
# Applying it: −∞ before softmax (cell 20)

```python
Q_test = torch.randn(2, 6, 64)  # (batch, seq, d_k)
K_test = torch.randn(2, 6, 64)
V_test = torch.randn(2, 6, 64)
causal_mask = create_causal_mask(6)  # (seq, seq)
output_masked, attn_weights_masked = scaled_dot_product_attention(
    Q_test, K_test, V_test, mask=causal_mask)
```
**Real output (first rows):**
```text
[[1.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
 [0.3963, 0.6037, 0.0000, 0.0000, 0.0000, 0.0000],
 [0.4882, 0.0887, 0.4230, 0.0000, 0.0000, 0.0000], ...
```
`masked_fill(mask == 0, -inf)` → e^(−∞) = 0 → future weight exactly 0

<!-- say: Now we use it. Random Q, K and V of shape two by six by sixty four, the mask, and call our function with mask equals causal mask. Inside, masked fill sets every blocked score to minus infinity before softmax. Since e to the minus infinity is zero, those positions get exactly zero weight, and the remaining weights in each row still sum to one. Here's my real output. Token zero puts all its weight, one point zero, on itself. Token one splits zero point four and zero point six. Token two splits across three tokens. And the upper triangle is exactly zero. Notice also that the six by six mask broadcasts automatically across the batch of two. -->

---

# Mask → masked scores → weights (my run)

![w:1700](img/causal.png)

<!-- say: Here is the masking pipeline visually, from my run. On the left, the mask, ones in the lower triangle. In the middle, the scaled scores after masked fill: every future cell is minus infinity. On the right, after softmax: the first row is a single one, and every future cell is exactly zero. Why minus infinity and not just zero? Because a score of zero still gets e to the zero, which is one, a real chunk of weight. Only minus infinity gives exactly nothing. -->

---

# Training vs inference

| | Training | Inference (generation) |
|---|---|---|
| Input | whole sequence at once | one new token per step |
| Future tokens | in the batch → **must be masked** | don't exist yet |
| Mask's job | simulate generation conditions | naturally enforced |

**Key insight:** the mask makes training match generation; skip it and the model learns to cheat.

<!-- say: Let's be clear about training versus inference. In training we feed the whole sequence at once for efficiency, so the future tokens are physically present and must be hidden by the mask. During generation we produce one token at a time, so the future simply doesn't exist, and the restriction is automatic. The mask is what makes training conditions match generation conditions. That's why a decoder model like GPT can learn from every position of a sentence in one parallel pass. -->

---

<!-- _class: divider -->
# 10.5 From One Head to Many
Multi-head attention and the reshape trick

<!-- say: Section five. From one head to many. -->

---

# Why one head isn't enough

| Relationship | Example | Attend from → to |
|---|---|---|
| Subject–verb agreement | The cats **sit** | sit → cats |
| Coreference | Alice … **She** | She → Alice |
| Syntax | The cat **that** chased | that → cat |
| Semantics | Paris … **capital** | capital → Paris |
| Position | sat **on** | previous word |

One softmax row = **one** distribution → can't specialise in all of these at once.

<!-- say: A single head has one set of attention weights per token, one probability distribution. But language has many simultaneous relationships. Subject verb agreement, coreference, syntax, semantic links, and plain positional patterns like look at the previous word. One distribution can't do all of those at once. If it focuses on the subject, it can't simultaneously focus on the previous word. So we run several attention heads in parallel, each free to learn its own pattern. -->

---

# Multi-head = several perspectives, same budget

- 12 heads × 64 dims = **768** = d_model · each head has its own Q/K/V slice and pattern
- Concatenate the 12 outputs → (seq, 768) → output projection blends them
- Attention params identical for 1 or 12 heads (**verified: 2,359,296** both)

![w:1300](img/multihead.png)

<!-- say: The neat part is that multi-head attention costs no extra parameters. Instead of one head with seven sixty eight dimensions, we use twelve heads with sixty four dimensions each. Twelve times sixty four is seven sixty eight. Each head gets its own slice of Q, K and V, computes its own attention pattern, and produces a sixty four dimension output. Concatenate the twelve and you're back at seven sixty eight, and a final output projection blends them. I verified that the attention module has two million three hundred fifty nine thousand two hundred ninety six parameters whether you configure one head or twelve. -->

---

<!-- _class: small -->
# MultiHeadAttention · `__init__` (cell 22)

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads, dropout=0.1):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_head = d_model // num_heads  # 768 / 12 = 64
        # Combined QKV projection (3x more efficient than separate!)
        self.qkv_proj = nn.Linear(d_model, 3 * d_model, bias=False)
        # Output projection
        self.out_proj = nn.Linear(d_model, d_model, bias=False)
        # Dropout on attention weights
        self.dropout = nn.Dropout(dropout)
```

<!-- say: Here's the constructor. The assert checks that d model divides evenly by the number of heads, seven sixty eight by twelve is sixty four, fine. We store d head. Then the first efficiency trick: instead of three separate linear layers, one linear layer maps seven sixty eight to three times seven sixty eight, two thousand three hundred and four outputs, producing Q, K and V for all heads in a single matrix multiply. Then an output projection, seven sixty eight to seven sixty eight, which mixes the heads after concatenation. And a dropout layer that we'll apply to the attention weights during training. -->

---

<!-- _class: small -->
# `forward` part 1 · project and split (cell 22)

```python
    def forward(self, x, mask=None):
        batch, seq, d_model = x.shape
        # ===== Step 1: Project to Q, K, V (all at once!) =====
        qkv = self.qkv_proj(x)  # (batch, seq, 3 * d_model)
        # ===== Step 2: Split into Q, K, V and reshape for multi-head =====
        # Reshape to (batch, seq, 3, num_heads, d_head)
        qkv = qkv.reshape(batch, seq, 3, self.num_heads, self.d_head)
        # Permute to (3, batch, num_heads, seq, d_head)
        qkv = qkv.permute(2, 0, 3, 1, 4)
        # Split into Q, K, V: each is (batch, num_heads, seq, d_head)
        Q, K, V = qkv[0], qkv[1], qkv[2]
```
(2, 6, 768) → (2, 6, **2304**) → (2, 6, **3, 12, 64**) → (**3**, 2, **12**, 6, 64) → Q, K, V each (2, 12, 6, 64)

<!-- say: The forward pass, part one. Unpack batch, seq and d model from x. Project: two by six by seven sixty eight becomes two by six by two thousand three hundred and four. Now the reshape trick. Reshape the last dimension, two thousand three hundred four, into three by twelve by sixty four: which of Q, K, V, which head, and which of the sixty four dimensions. Then permute the axes into the order three, batch, heads, seq, d head. That's what the indices two, zero, three, one, four mean: take old axis two first, then old axis zero, and so on. Finally index zero, one, two to split out Q, K and V, each of shape two by twelve by six by sixty four. Heads now sit next to batch, like an extra batch dimension. -->

---

# The reshape trick, visualised

| Stage | Shape | Meaning |
|---|---|---|
| after qkv_proj | (2, 6, 2304) | per token: [all Q heads · all K heads · all V heads] |
| reshape | (2, 6, 3, 12, 64) | label each number: Q/K/V? which head? which dim? |
| permute(2,0,3,1,4) | (3, 2, 12, 6, 64) | Q/K/V first, heads before seq |
| Q, K, V | (2, 12, 6, 64) | **12 independent 6×64 problems per sentence** |

`Q @ K.transpose(-2,-1)` acts on the **last two** dims → broadcasts over batch AND heads → 24 attention maps in **one** matmul

<!-- say: Let's slow down on this trick, because it's the hardest part of the chapter. After the projection, each token's two thousand three hundred four numbers are laid out as all the Q's for the twelve heads, then all the K's, then all the V's. Reshape doesn't move any data, it just labels each number: this one is Q, head five, dimension thirty. Permute then rearranges the axes so the head axis sits before the sequence axis. The result: for each of the two sentences, twelve independent six by sixty four problems. And since matrix multiply in PyTorch only works on the last two dimensions and broadcasts over the rest, Q times K transpose computes all twenty four attention maps in a single call. No Python loop over heads. -->

---

<!-- _class: small -->
# `forward` part 2 · attention per head (cell 22)

```python
        d_k = self.d_head
        scores = Q @ K.transpose(-2, -1)  # (batch, num_heads, seq, seq)
        scores = scores / math.sqrt(d_k)
        if mask is not None:
            # Expand mask for heads: (seq, seq) → (1, 1, seq, seq)
            if mask.dim() == 2:
                mask = mask.unsqueeze(0).unsqueeze(0)
            scores = scores.masked_fill(mask == 0, float('-inf'))
        attn_weights = F.softmax(scores, dim=-1)  # (batch, num_heads, seq, seq)
        attn_weights = self.dropout(attn_weights)
        attn_output = attn_weights @ V  # (batch, num_heads, seq, d_head)
```
Scores (2, 12, 6, 6) · mask (1, 1, 6, 6) broadcasts over batch & heads

<!-- say: Part two is the same five steps as before, just with an extra head axis. Scores are now two by twelve by six by six: a six by six table per head per sentence. Scale by root sixty four. For the mask, if it's two dimensional, we unsqueeze twice to make it one by one by six by six, so it broadcasts across batch and heads. Masked fill with minus infinity, softmax on the last dimension, then dropout on the attention weights, which randomly zeroes some weights during training as regularisation. Then weights times V gives two by twelve by six by sixty four. -->

---

# `forward` part 3 · concatenate and project (cell 22)

```python
        # ===== Step 4: Concatenate heads =====
        # Transpose to (batch, seq, num_heads, d_head)
        attn_output = attn_output.transpose(1, 2)
        # Reshape to (batch, seq, d_model) — this concatenates heads
        attn_output = attn_output.reshape(batch, seq, d_model)
        # ===== Step 5: Final projection =====
        output = self.out_proj(attn_output)
        return output, attn_weights
```
(2, 12, 6, 64) → transpose → (2, 6, 12, 64) → reshape → (2, 6, 768) → out_proj → (2, 6, 768)

<!-- say: Part three undoes the split. Transpose axes one and two, so we have batch, seq, heads, d head: two by six by twelve by sixty four. Now for each token, the twelve head outputs sit next to each other. Reshape to two by six by seven sixty eight, which concatenates the twelve sixty four dimension outputs into one seven sixty eight vector per token. Finally the output projection mixes information across heads. We return the output and the attention weights. -->

---

# Testing it (cell 22) · real output

```python
mha = MultiHeadAttention(d_model=768, num_heads=12, dropout=0.1)
embeddings_test = torch.randn(2, 6, 768)
mask_test = create_causal_mask(6)
output_mha, attn_weights_mha = mha(embeddings_test, mask_test)
```
```text
Input shape:  torch.Size([2, 6, 768])
Output shape: torch.Size([2, 6, 768])
Attention weights shape: torch.Size([2, 12, 6, 6])
```
**In = out shape** → blocks can be stacked. Weights: one 6×6 map **per head**.

<!-- say: Testing it: twelve heads, random input of two by six by seven sixty eight, a causal mask. My real output: input two six seven sixty eight, output two six seven sixty eight, and attention weights two by twelve by six by six, one six by six map for each of the twelve heads. The fact that the output shape equals the input shape is what lets us stack these layers as deep as we like. -->

---

# Why `.reshape()` and not `.view()`?

- `.transpose()` / `.permute()` change **strides**, not data → tensor is **non-contiguous**
- `.view()` needs contiguous memory → `RuntimeError`
- Safe: `.reshape()` (copies only if needed) or `.contiguous().view()`

```python
x = torch.randn(2, 12, 6, 64).transpose(1, 2)
x.is_contiguous()          # False
x.view(2, 6, 768)          # RuntimeError
x.reshape(2, 6, 768)       # works
```
<small>Snippet: my own illustration (not from the notebook).</small>

<!-- say: A practical PyTorch detail the book highlights. Transpose and permute don't actually move numbers in memory, they just change the strides, the recipe for walking through memory. The result is called non contiguous. View requires contiguous memory, so calling view after a transpose throws a runtime error. Reshape handles both cases: it returns a view when it can and makes a copy when it must. The alternative is contiguous then view. Rule of thumb: after transpose or permute, use reshape. The small snippet here is mine, you can paste it into the notebook to see the error yourself. -->

---

<!-- _class: divider -->
# 10.6 The Complete Transformer Block
FFN · LayerNorm · residuals · pre-norm

<!-- say: Section six. The complete transformer block. -->

---

# What attention alone is missing

1. **Non-linearity** — attention output is a weighted *average* of linear projections
2. **Trainability at depth** — deep stacks are unstable → need **residuals** + **normalisation**
3. **Per-token processing** — attention moves information *between* tokens; we also need to transform it *within* each token

**Assembly line:** each station adds something; the original item always travels alongside (residuals).

<!-- say: Attention alone isn't enough. First, it's mostly linear: projections, then a weighted average. Stacking linear operations just gives another linear operation, so we need a non-linearity to learn complex functions. Second, deep stacks are hard to train, so we need residual connections and normalisation. Third, attention moves information between tokens, but we also want to process that information inside each token. The book's picture is an assembly line: each station adds something, but the original item always travels alongside, thanks to the residual connections. -->

---

<!-- _class: small -->
# Component 1 · Feed-forward network (cell 24)

```python
class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout=0.1):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        # x: (batch, seq, d_model)
        x = self.fc1(x)        # (batch, seq, d_ff) — expand
        x = F.gelu(x)          # Non-linearity
        x = self.dropout(x)
        x = self.fc2(x)        # (batch, seq, d_model) — project back
        return x
```
Real: `(2, 6, 768) → (2, 6, 768)` · hidden (2, 6, **3072**) · same weights at every position

<!-- say: The feed forward network. Two linear layers. fc1 expands seven sixty eight to three thousand seventy two, four times wider. Then GELU, the non-linearity. Then dropout. Then fc2 projects back down to seven sixty eight. It's called position wise because the same network is applied independently to every token. Position zero gets FFN of x zero, position one gets FFN of x one, same weights. No information moves between tokens here. That's attention's job. In my run the shapes went two six seven sixty eight, to two six three oh seven two inside, and back to two six seven sixty eight. -->

---

# GELU vs ReLU

![w:950](img/gelu.png)

- GELU(x) = x · Φ(x), Φ = standard normal CDF · smooth everywhere
- Small negatives leak through (−0.159 at x = −1) · used by GPT-2, BERT, most Transformers

<!-- say: GELU, the Gaussian error linear unit, is x times phi of x, where phi is the cumulative distribution of a standard normal. Compared to ReLU, which is a hard zero for negatives, GELU is smooth. At x equals minus one it outputs about minus zero point one six instead of zero, and at plus one it gives about zero point eight four. The smooth curve gives gradients everywhere, which tends to train a bit better. GPT two, BERT, and most transformers use it. -->

---

# FFN parameters & why bias here

| Layer | Weights | Bias | Total |
|---|---|---|---|
| fc1 768→3072 | 2,359,296 | 3,072 | 2,362,368 |
| fc2 3072→768 | 2,359,296 | 768 | 2,360,064 |
| **FFN total** | | | **4,722,432** |

- FFN ≈ **2/3** of a block's parameters
- FFN keeps `bias=True`; our attention uses `bias=False` (LayerNorm already centres). Original GPT-2 **does** have attention biases — Ch 11's loader handles it.

<!-- say: Parameters. fc1 has seven sixty eight times three oh seven two weights, about two point three six million, plus three thousand seventy two biases. fc2 is the same size the other way, plus seven sixty eight biases. Total about four point seven two million, roughly two thirds of a whole block. Notice the FFN keeps the default bias equals true, while our attention uses bias false. That's a simplification common in educational code. The original GPT two actually does have attention biases, and the book's chapter eleven weight loading code deals with that difference. -->

---

<!-- _class: small -->
# Component 2 · LayerNorm

For each token's vector **x** ∈ ℝ⁷⁶⁸: **LN(x) = γ ⊙ (x − μ) / √(σ² + ε) + β** (μ, σ over the 768 features)

```python
ln = nn.LayerNorm(768)           # NOT nn.LayerNorm(d_model=768)
x_ln = torch.randn(2, 6, 768)
output_ln = ln(x_ln)             # per token: mean ≈ 0, std ≈ 1
```
- Normalises across **features**, per token (BatchNorm normalises across the batch)
- Learnable γ (scale) and β (shift): 2 × 768 = **1,536** params

⚠️ The book's printed snippet `nn.LayerNorm(d_model=768)` raises **TypeError** (the argument is `normalized_shape`). The notebook's classes use `nn.LayerNorm(d_model)` correctly.

<!-- say: Layer normalisation. For each token separately, compute the mean and variance across its seven sixty eight features, subtract the mean, divide by the standard deviation, then apply a learned scale gamma and shift beta. This keeps the activations in a healthy range as data flows through many layers. Note it normalises across features for each token, unlike batch norm, which normalises across the batch. Parameters: gamma and beta, seven sixty eight each, one thousand five hundred thirty six. One catch I hit: the book's printed snippet writes LayerNorm with a keyword d model equals seven sixty eight, and that raises a type error, because the parameter is actually called normalized shape. Just pass the number positionally, as the notebook's classes do. -->

---

# Component 3 · Residual (skip) connections

```python
x = attention(x)        # without residual: a brand-new representation
x = x + attention(x)    # with residual: old representation + refinement
```
![w:1000](img/residual_grad.png)

<!-- say: Residual connections. Instead of replacing x with attention of x, we add: x plus attention of x. The layer only has to learn a refinement, a delta, rather than rebuilding the representation from scratch. The book's piano analogy: each lesson adds improvements to what you already know. And there's a training benefit. The derivative of x plus f of x with respect to x includes a plain one from the skip path, so gradients can flow straight back. Without it, as in the book's example, if every layer scales the gradient by zero point eight, after twelve layers a gradient of zero point five shrinks to about zero point oh three. With the skip, there's always an unimpeded path. That's how GPT three can stack ninety six blocks. -->

---

# Component 4 · Pre-norm vs post-norm

![w:1300](img/prepost.png)

Pre-norm normalises each sub-layer's **input**; the residual path is pure addition → stabler, often no warmup needed.

<!-- say: Where does layer norm go? The original 2017 paper used post norm: add the residual, then normalise. GPT two and most modern models use pre norm: normalise the input to the sub-layer, then add the result back to the untouched x. The difference matters. In pre norm, the residual stream from input to output is pure addition, it never passes through a normalisation. That clean highway makes deep networks train more stably and often without the learning rate warm up that post norm needs. We'll use pre norm. -->

---

# The block, top to bottom

![w:720](img/block.png)

<!-- say: Here is the whole block. Input x, batch by seq by seven sixty eight. Layer norm one, then multi-head attention, then add the result back to the original x. That sum goes through layer norm two, then the feed forward network, and the result is added back again. The dashed lines are the residual skips. Two sub-layers, each wrapped in norm, then add. That's the entire transformer block. -->

---

<!-- _class: small -->
# `TransformerBlock` (cell 26)

```python
class TransformerBlock(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.ln2 = nn.LayerNorm(d_model)
        self.attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.ffn = FeedForward(d_model, d_ff, dropout)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        attn_out, attn_weights = self.attn(self.ln1(x), mask)
        x = x + self.dropout(attn_out)  # Residual connection
        ffn_out = self.ffn(self.ln2(x))
        x = x + self.dropout(ffn_out)  # Residual connection
        return x, attn_weights
```
<small>Docstrings and section comments trimmed.</small>

<!-- say: And the code, which reads exactly like the diagram. The constructor creates two layer norms, the multi-head attention, the feed forward network, and a dropout. In forward: normalise x with ln1, run attention with the mask, apply dropout to the output and add it to x. Then normalise with ln2, run the feed forward network, dropout, add to x. Return x and the attention weights. Two residual lines, that's the whole block in about ten lines, built from pieces we've already written. -->

---

# Testing the block · real output

```python
block = TransformerBlock(d_model=768, num_heads=12, d_ff=3072, dropout=0.1)
embeddings_block = torch.randn(2, 6, 768)
mask_block = create_causal_mask(6)
output_block, attn_weights_block = block(embeddings_block, mask_block)
```
```text
Input shape:  torch.Size([2, 6, 768])
Output shape: torch.Size([2, 6, 768])
Attention weights shape: torch.Size([2, 12, 6, 6])
Input mean: 0.0108   Output mean: 0.0122   Difference: 0.2575
```
Output ≈ input + a moderate refinement (residuals at work)

<!-- say: Running the block on random input. Shapes in and out are both two six seven sixty eight, attention weights two twelve six six. The notebook also prints means: input mean zero point oh one oh eight, output zero point oh one two two, and the average absolute difference is about zero point two six. That's the residual design in action: the output is the input plus a moderate refinement, not a completely new vector. Your exact numbers will differ, since the weights are random. -->

---

# Parameter count for one block (verified)

![w:1100](img/params.png)

- Total **7,084,800** (≈ 7.1M) = `sum(p.numel() for p in block.parameters())`
- × 12 blocks ≈ **85M**; GPT-2 small ≈ 124M total (rest: embeddings, final LN)

<!-- say: How many parameters in one block? The QKV projection is seven sixty eight times two three oh four, one point seven seven million. The output projection, five hundred ninety thousand. fc1 and fc2 about two point three six million each including biases. Two layer norms, three thousand seventy two. Total seven million eighty four thousand eight hundred, and I confirmed it by summing the parameters of the actual module. Twelve blocks gives about eighty five million. GPT two small has about a hundred twenty four million in total, the rest mostly being the token and position embeddings. -->

---

# Information flow through one block

```text
Input (2, 6, 768)
  → LayerNorm
  → MHA: split (2, 12, 6, 64) → attend per head → concat (2, 6, 768)
  → + residual
  → LayerNorm
  → FFN: 768 → 3072 (GELU) → 768
  → + residual
Output (2, 6, 768)
```
Attention = **communication** between tokens · FFN = **computation** within each token

<!-- say: Let's trace it once more as a summary. Input two six seven sixty eight. Layer norm. Multi-head attention splits into two by twelve by six by sixty four, attends per head, and concatenates back. Add the residual. Layer norm. Feed forward expands to three oh seven two with GELU and comes back to seven sixty eight. Add the residual. Output, same shape. A useful mental model: attention is communication between tokens, the feed forward network is computation within each token. A block does one round of each. -->

---

<!-- _class: small -->
# From block to model (Ch 11 preview)

```python
class GPT2(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = GPT2Embeddings(...)   # From Chapter 9
        self.blocks = nn.ModuleList([TransformerBlock(...) for _ in range(12)])
        self.ln_f = nn.LayerNorm(768)          # Final layer norm
        self.lm_head = nn.Linear(768, 50257)   # Predict next token
    def forward(self, token_ids):
        x = self.embedding(token_ids)          # (batch, seq, 768)
        for block in self.blocks:
            x, _ = block(x, mask)
        x = self.ln_f(x)
        return self.lm_head(x)                 # (batch, seq, vocab_size)
```
<small>The book's preview sketch (condensed); `mask` is built from the sequence length in Ch 11.</small>

<!-- say: And here's a preview of chapter eleven. A GPT two model is the embedding layer, twelve transformer blocks in a module list, a final layer norm, and a language model head, a linear layer from seven sixty eight to fifty thousand two hundred fifty seven vocabulary logits. The forward pass embeds, loops through the blocks, normalises, and projects to logits. This is a condensed sketch from the book, and the mask is created from the sequence length in the real chapter eleven code. Everything inside the loop, you now understand completely. -->

---

<!-- _class: divider -->
# 10.7 Visualising Attention
Useful for intuition — careful with interpretation

<!-- say: Section seven. Visualising attention. -->

---

<!-- _class: small -->
# `visualize_attention` (cell 28)

```python
def visualize_attention(attn_weights, tokens, head_idx=0, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    weights = attn_weights[0, head_idx].detach().cpu().numpy()
    im = ax.imshow(weights, cmap='viridis', aspect='auto', vmin=0, vmax=1)
    ax.set_xticks(range(len(tokens)))
    ax.set_yticks(range(len(tokens)))
    ax.set_xticklabels(tokens, rotation=45, ha='right')
    ax.set_yticklabels(tokens)
    ax.set_xlabel('Key (attending TO)', fontsize=10)
    ax.set_ylabel('Query (attending FROM)', fontsize=10)
    ax.set_title(f'Attention Weights - Head {head_idx}', fontsize=12)
    plt.colorbar(im, ax=ax, label='Attention Weight')
    return ax
```

<!-- say: The visualisation helper. It takes the attention weights, a list of token strings, and a head index. It picks the first sentence and that head, giving a seq by seq matrix. Detach removes it from the autograd graph, cpu and numpy convert it for matplotlib. imshow draws it as a heatmap with values fixed between zero and one. Then it labels the axes: keys, attended to, along the bottom, queries, attending from, down the side, and adds a colour bar. -->

---

<!-- _class: small -->
# Running it on a real sentence (cell 28)

```python
tokenizer = AutoTokenizer.from_pretrained("gpt2")
text = "The quick brown fox jumps over the lazy dog"
token_ids = tokenizer.encode(text, return_tensors="pt")  # (1, seq)
tokens = [tokenizer.decode([t]) for t in token_ids[0]]
embed_layer = nn.Embedding(50257, 768)
embeddings_viz = embed_layer(token_ids)  # (1, seq, 768)
seq_len_viz = embeddings_viz.size(1)
mask_viz = create_causal_mask(seq_len_viz)
block_viz = TransformerBlock(d_model=768, num_heads=12, d_ff=3072, dropout=0.1)
output_viz, attn_weights_viz = block_viz(embeddings_viz, mask_viz)
```
**Real output:** `Tokens: ['The', ' quick', ' brown', ' fox', ' jumps', ' over', ' the', ' lazy', ' dog']`
`Attention weights shape: torch.Size([1, 12, 9, 9])`

<!-- say: Then the notebook runs a real sentence. The GPT two tokenizer turns the quick brown fox jumps over the lazy dog into nine tokens. Notice the leading spaces, GPT two's tokenizer attaches the space to the start of each word. A fresh, untrained embedding layer and a fresh transformer block process them, and we get attention weights of one by twelve by nine by nine. Then it plots the first four heads in a two by two grid. Important: this block is untrained, so the patterns will be the causal triangle with fairly random weights inside. -->

---

# Untrained block (notebook figure, my run)

![w:820](img/heads_untrained.png)

Lower-triangular ✔ (mask works) · patterns inside are **random** (untrained weights)

<!-- say: Here's the figure the notebook produced on my machine. You can see the causal structure: everything above the diagonal is dark, exactly zero. The first token always puts all its weight on itself, so the top left cell is bright. But inside the triangle, the patterns are essentially random, because nothing has been trained. That's still useful: it verifies the mask works. -->

---

# Trained GPT-2 heads (my experiment)

![w:1600](img/gpt2_heads.png)

Layer 0 h1: **itself** · Layer 4 h11: **previous token** · Layer 5 h1: almost all on **the first token**

<!-- say: To see what trained heads look like, I loaded pretrained GPT two and plotted three heads for the sentence, the cat sat on the mat because it was tired. Layer zero, head one, attends mostly to the token itself, a bright diagonal. Layer four, head eleven, is a previous token head: each token looks at the one right before it, a diagonal shifted by one. And layer five, head one, dumps nearly all its attention on the very first token. You might hope the word it would attend to cat, but in this head, it puts zero point nine eight on the first token, the. That's a well known pattern often called an attention sink, where the first token acts as a place to park attention. Which leads directly to the next slide. -->

---

# Attention ≠ explanation

**You CAN conclude:** the causal mask works (upper triangle = 0) · heads differ, some local, some long-range

**You CANNOT conclude:** "this head encodes syntax" · "that head learns semantics" · "the weights explain the decision"

**Why:** FFNs, residuals and norms carry information too; heads interact; weights show *where* a head reads, not *what* it does with it. (The sink above: high weight, little meaning.)

<!-- say: The book is careful here, and so should we be. From heatmaps you can conclude that masking works, and that heads behave differently, some local, some long range. You cannot conclude that a head encodes syntax or semantics, or that attention weights explain a decision. The feed forward layers, residual stream and norms carry a lot of the computation, heads interact with each other, and a weight tells you where a head reads from, not what it does with what it read. The attention sink we just saw is a perfect example: high weight, almost no meaning. Use visualisations for intuition, not explanation. -->

---

<!-- _class: divider -->
# 10.8 Practical Considerations
The O(n²) cost and the full pipeline

<!-- say: Section eight. Practical considerations. -->

---

# Memory is O(n²) in sequence length

Scores tensor: (batch, heads, **n, n**) per layer

![w:1150](img/memory.png)

batch 8 · 12 heads · n = 2048 → 8·12·2048²·4 B ≈ **1.6 GB** for one layer's scores

<!-- say: Attention's big cost is memory that grows with the square of the sequence length, because the score tensor is batch by heads by n by n. At n equals five twelve, that's two hundred sixty two thousand scores per head. At two thousand forty eight, about four million. With a batch of eight and twelve heads at two thousand forty eight tokens, that's eight times twelve times two thousand forty eight squared, about four hundred million floats, times four bytes, roughly one point six gigabytes, for just one layer's scores. Double the context, quadruple the memory. GPT two used ten twenty four tokens. Longer contexts need more efficient techniques, which the book returns to in chapter sixteen. -->

---

<!-- _class: small -->
# The full pipeline in code (cell 30) · real output

```python
text = "The cat sat on the mat"
tokenizer = AutoTokenizer.from_pretrained("gpt2")
token_ids = tokenizer.encode(text, return_tensors="pt")  # (1, 6)
embed_layer = nn.Embedding(50257, 768)
embeddings = embed_layer(token_ids)  # (1, 6, 768)
seq_len_final = token_ids.size(1)  # 6
mask_final = create_causal_mask(seq_len_final)
block_final = TransformerBlock(d_model=768, num_heads=12, d_ff=3072, dropout=0.1)
output_final, attn_weights_final = block_final(embeddings, mask_final)  # (1, 6, 768)
```
```text
Token IDs: tensor([[ 464, 3797, 3332,  319,  262, 2603]])
Embeddings shape: torch.Size([1, 6, 768])     Output shape: torch.Size([1, 6, 768])
```
<small>Prints omitted. Note: the book's text lists " mat" as 21547; the real GPT-2 ID (above) is **2603**.</small>

<!-- say: The notebook ends by running everything end to end. Tokenise the cat sat on the mat into six IDs, embed them to one by six by seven sixty eight, build a causal mask of size six, and push them through one transformer block. Output one by six by seven sixty eight, context aware vectors. In my run the token IDs were four sixty four, three seven nine seven, three three three two, three nineteen, two sixty two, and two six oh three. Small detail: the book's text lists mat as two one five four seven, but the real GPT two tokenizer gives two six oh three, so trust the notebook output. -->

---

<!-- _class: divider -->
# 10.9 Key Takeaways

<!-- say: Let's wrap up with the key takeaways. -->

---

# What we built

1. **Scaled dot-product attention**: softmax(QKᵀ/√d_k)·V
2. **Causal masking**: `tril` + `masked_fill(-inf)` → no future
3. **Multi-head attention**: 12 × 64 = 768, one fused QKV matmul, reshape/permute trick
4. **Transformer block**: pre-norm, MHA + FFN (GELU), two residuals — **7,084,800 params**
5. **Attention heatmaps**: verify masking, don't over-interpret

<!-- say: What did we build? Scaled dot product attention, softmax of Q K transpose over root d k, times V. Causal masking with tril and masked fill minus infinity. Multi-head attention, twelve heads of sixty four, one fused projection, and the reshape and permute trick. A complete pre norm transformer block with attention, a GELU feed forward network and two residual connections, about seven point one million parameters. And attention heatmaps, which are great for checking the mask and dangerous for over-interpretation. -->

---

# Core concepts to remember

- Static embeddings (Ch 9) → **context-aware** vectors (Ch 10), same shape
- **Q** what I seek · **K** how I'm found · **V** what I give
- Scale by √d_k because dot-product std grows as √d_k
- Multi-head = different perspectives, **no extra parameters**
- Residuals + LayerNorm make **deep stacks trainable**
- Same attention powers GPT-4, BERT, ViT, AlphaFold

<!-- say: The core concepts. Static embeddings become context aware vectors with the same shape. Query is what I seek, key is how I'm found, value is what I give. We scale by root d k because the dot product's spread grows like root d k. Multi-head attention gives different perspectives at no extra parameter cost. Residuals and layer norm make deep stacks trainable. And this exact mechanism powers GPT four, BERT, vision transformers and even AlphaFold, applied to different kinds of sequences. -->

---

<!-- _class: small -->
# Review questions 1–3

**Q1. Why aren't static embeddings enough?** "bank" gets the same vector in *river bank* and *money bank*; a lookup can't see neighbours. Attention mixes in context so the two vectors diverge.

**Q2. Roles of Q, K, V; why does Q·Kᵀ measure relevance?** Q = what a token seeks, K = what it advertises, V = what it passes on. The dot product is large when q and k point the same way.

**Q3. Why scale by √d_k?** Dot-product std ≈ √d_k (≈ 8 for 64). Unscaled, softmax saturates → near one-hot weights and vanishing gradients.

<!-- say: Review questions. Pause and answer each one before I do. Question one: why aren't static embeddings enough? Because bank gets the same vector in river bank and money bank. The lookup can't see neighbours, attention mixes in context so the vectors diverge, as we saw with real GPT two. Question two: the roles of Q, K and V, and why the dot product measures relevance. The query is what a token seeks, the key is what it advertises, the value is what it passes on. The dot product is large when query and key point the same way. Question three: why scale by root d k? Because the dot product's standard deviation grows like root d k, about eight for sixty four. Without scaling softmax saturates, the weights become nearly one hot and the gradients vanish. -->

---

<!-- _class: small -->
# Review questions 4–6

**Q4. What is causal masking; how does it stop cheating?** Lower-triangular mask; future scores → −∞ → weight 0. Training then matches generation, where the future doesn't exist.

**Q5. Perspectives without more parameters?** 12 heads × 64 = 768. The fused projection is still 768 × 2304; each head gets its own slice and its own pattern.

**Q6. The reshape trick; why faster than a loop?** (B,S,2304) → (B,S,3,12,64) → permute → (3,B,12,S,64): heads become a batch dim, so one batched matmul computes all heads in parallel on optimised kernels.

<!-- say: Question four: what is causal masking? A lower triangular mask that sets future scores to minus infinity, so their weights become zero. That makes training match generation, where the future doesn't exist yet. Question five: how do multiple heads give different perspectives without more parameters? We split seven sixty eight into twelve heads of sixty four, which is still seven sixty eight. The fused projection is still seven sixty eight by two three oh four. Each head just gets its own slice and learns its own pattern. Question six: the reshape trick. We reshape to separate Q, K, V and heads, then permute so heads act like a batch dimension, and one batched matrix multiply handles all heads at once on optimised kernels, instead of a slow Python loop. -->

---

<!-- _class: small -->
# Review questions 7–8

**Q7. Four components of a block?** **Attention**: tokens exchange information · **FFN**: non-linear per-token processing (768→3072→768) · **Residuals**: keep the original signal, gradient highway · **LayerNorm**: stable activation scale

**Q8. Pre-norm vs post-norm?** Post: `LN(x + F(x))` (2017 paper). Pre: `x + F(LN(x))` (GPT-2). Pre-norm keeps the residual path pure addition → stabler deep training, less need for warmup.

<!-- say: Question seven: the four components of a block. Attention, for exchanging information between tokens. The feed forward network, for non-linear processing within each token. Residual connections, which preserve the original signal and give gradients a highway. And layer norm, which keeps activations in a stable range. Question eight: pre norm versus post norm. Post norm is layer norm of x plus f of x, as in the original paper. Pre norm is x plus f of layer norm of x, used by GPT two, because the residual path stays pure addition and deep models train more stably. -->

---

<!-- _class: small -->
# Review questions 9–10

**Q9. O(n²) memory: batch 4, 12 heads, n = 2048?** 4 × 12 × 2048² = 201,326,592 floats × 4 B ≈ **0.8 GB** per layer's scores. Double n → 4× memory.

**Q10. Why be cautious with attention heatmaps?** They show *where* a head reads, not *what* it computes; FFNs/residuals matter; heads interact; sinks get high weight with little meaning. **Can:** confirm masking, see head diversity. **Can't:** claim a head "does syntax" or that weights explain decisions.

<!-- say: Question nine: memory for batch four, twelve heads, sequence two thousand forty eight. Four times twelve times two thousand forty eight squared is about two hundred one million floats. At four bytes each, that's about zero point eight gigabytes for one layer's scores. Double the length and memory quadruples. Question ten: why be cautious with heatmaps? They show where a head reads, not what it computes. Feed forward layers and residuals matter too, heads interact, and attention sinks get huge weight with little meaning. You can confirm masking and see diversity. You can't claim a head does syntax or that weights explain a decision. -->

---

<!-- _class: small -->
# Practice this (notebook ch10.ipynb)

- ☐ Run cells 2–30 in Colab; print shapes after **every** line
- ☐ **Cell 32 · Ex 1** manual attention → `[[1.50, 1.00, 0.50], [1.36, 1.28, 0.36]]`
- ☐ **Cell 34 · Ex 2** seq 5, with/without mask; assert upper triangle == 0
- ☐ **Cell 36 · Ex 3** d_model 512, 8 heads, seq 10 → (…, 10, 1536) then (…, 8, 10, 64)
- ☐ **Cell 38 · Ex 4** 1 vs 12 heads → both **2,359,296** attention params
- ☐ **Cell 40 · Ex 5** visualise heads 0, 3, 7, 11 for "Alice gave Bob a book"
- ☐ **Cell 42 · Ex 6** stack 3 blocks · **Cell 44 · Ex 7** post-norm block · **Cell 46 · Ex 8** count → **7,084,800**

<!-- say: Your practice list, all in the chapter ten notebook. Run cells two through thirty in Colab and print shapes after every line. Then the exercises. Cell thirty two, exercise one: manual attention, you should get one point five, one, zero point five, and one point three six, one point two eight, zero point three six. Cell thirty four: with and without the mask, assert the upper triangle is zero. Cell thirty six: trace shapes for d model five twelve with eight heads and sequence ten. The projection gives fifteen thirty six, heads give eight by ten by sixty four. Cell thirty eight: compare one head and twelve heads, both should have two million three hundred fifty nine thousand two hundred ninety six attention parameters. Cell forty: visualise heads for your own sentence. Cells forty two to forty six: stack three blocks, write a post norm block, and count the block parameters, seven million eighty four thousand eight hundred. -->

---

# Up next: Chapter 11

**Building the Transformer**
Stack 12 blocks · final LayerNorm · LM head (768 → 50,257) · load GPT-2 weights · generate text

<!-- say: In chapter eleven, we complete the picture. We stack twelve of these blocks, add the final layer norm and the language model head, load real GPT two weights into our own code, and generate text. See you there. -->

---

<!-- _class: lead -->
# Credits
Based on **"Build Your First LLM"** by **Hasan Degismez** — buy the book: **leanpub.com/FirstLLM**
Code: **FirstLLM/code (MIT License)** · github.com/FirstLLM/code/blob/main/notebooks/ch10.ipynb
Slides, narration, diagrams & experiments: my own teaching adaptation · **Waqar Shaikh Builds**

<!-- say: This video is based on the book Build Your First LLM by Hasan Degismez. The code is from the FirstLLM code repository under the MIT license, and the diagrams, narration and extra experiments are my own adaptation for study. If this helped you, please buy the book at leanpub dot com slash First LLM, it has much more detail than I could fit here. Thanks for watching. -->
