# Chapter 1 — What is AI, Really? (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025). Written in my own words as a learning companion — not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>. Companion code: <https://github.com/FirstLLM/code> (MIT). Chapter 1 has no notebook; the notebooks start at Chapter 5.

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters

Before writing any code we need an accurate mental model of the thing we're going to build. Chapter 1 replaces the science-fiction picture of AI with a mechanical one: a model is a big pile of numbers, learning is adjusting those numbers to reduce error, and a large language model (LLM) is such a pile of numbers trained to predict the next token of text. Everything later in the course — tokenizers, embeddings, attention, Transformer blocks, training loops — is detail inside this picture.

### Learning goals
1. Separate movie AI (conscious, scheming) from real AI (pattern recognition).
2. Explain what "learning" means: adjusting parameters based on feedback.
3. Place LLMs in the hierarchy AI ⊃ ML ⊃ Deep Learning ⊃ LLM.
4. List what LLMs can and can't do on their own.
5. Explain hallucination with the "lossy compression" idea.
6. Articulate why building one yourself is worth it.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Artificial Intelligence | Computer systems doing tasks we'd call intelligent if a person did them |
| Machine Learning | AI where behaviour is learned from data instead of hand-written rules |
| Deep Learning | ML with neural networks that have many stacked layers |
| Large Language Model | A deep network trained on huge amounts of text to predict the next token |
| Parameters / weights | The adjustable numbers inside a model |
| Training | Repeatedly adjusting parameters so predictions get less wrong |
| Emergence | Complex abilities appearing from a simple objective once the system is large enough |
| Hallucination | Fluent, confident output that is false |

---

## 1.1 Forget the movies

Films show AI as conscious, emotional, plotting. Today's systems show **no evidence** of feelings, desires, or inner experience; they don't "want" anything; and nothing about them is magic — it's maths, data, and computation running on GPUs (mostly matrix multiplication).

| Movie AI | Real AI |
|---|---|
| Conscious, has feelings | No evidence of inner experience |
| Wants to take over | Wants nothing; it's a tool |
| Thinks like a human, faster | Processes patterns in data |
| Can do anything once activated | Does what it was trained for |
| Mysterious future tech | GPUs doing matrix multiplication |
| Saviour or destroyer | A very sophisticated autocomplete |

**"Sophisticated autocomplete" is the literal training objective.** Given "The cat sat on the", an LLM outputs a probability for every token in its vocabulary (illustratively: *mat* 0.46, *floor* 0.21, *sofa* 0.17, *roof* 0.12, *moon* 0.04), picks one, appends it, and repeats. The surprise of the last decade is how much capability falls out of doing this one task extremely well.

![next token](img/next_token.png)

The book quotes Dijkstra's line that asking whether a computer can think is like asking whether a submarine can swim. Submarines move through water very well without swimming like fish; models process information usefully without thinking like us. As engineers we care about behaviour and mechanism, not the label.

(Alignment — making AI do what we intend — is a real research area, but that's a different topic from Hollywood's conscious villains.)

---

## 1.2 AI is pattern recognition

**Working definition:** AI finds patterns in data that are too complex or too numerous for humans to write down by hand, and uses them to make predictions — *at scale*.

### Rules vs learning

![rules vs ml](img/rules_vs_ml.png)

- **Traditional programming:** rules + data → program → answers.
- **Machine learning:** data + answers → training → rules (stored as numbers).

### The spam filter
1. **Training data:** millions of emails, each labelled spam / not spam by people.
2. **Pattern discovery:** the system notices signals on its own — lots of capitals, talk of money, prizes and urgency, suspicious senders, odd formatting.
3. **Prediction:** a new email is scored against those patterns.

Nobody typed the rules. The book compares it to training a new employee by sorting a stack of mail together rather than handing them a 500-page rulebook.

**Toy model (my own illustration):** give each word a weight, add up the weights of words present, call it spam if the total is positive.

![spam weights](img/spam_weights.png)

"free lunch meeting" → 2.1 − 1.5 − 1.3 = −0.7 → not spam. The numbers here are invented; the principle — *a learned pattern is a number* — is real.

### The formula

![formula](img/formula.png)

**AI = statistics + lots of data + computing power.** The statistics is decades old; what changed is internet-scale data and GPU compute. That's why AI "suddenly" works.

### What "learning" actually means

A model is a big collection of numbers (parameters) that start random. Training is a loop:

![loop](img/train_loop.png)

1. Predict. 2. Measure the error (the **loss**). 3. Nudge every number slightly in the direction that reduces the error (a **gradient step**). 4. Repeat — billions of times for an LLM.

#### Worked example: fitting a line (I ran this)

Model: ŷ = w·x + b (two parameters). Data: 40 points from y = 3x + 2 plus Gaussian noise (σ = 1.2). Start w = 4.5, b = 0.4, learning rate 0.02, mean-squared-error loss, 400 steps of gradient descent.

![line fit](img/line_fit.png)
![w and b over steps](img/wb_steps.png)
![loss](img/loss.png)

Results from my run: after 10 steps w ≈ 3.53, b ≈ 0.27; after 400 steps **w ≈ 3.085, b ≈ 1.706**; loss **10.27 → 0.88**. The loss can't hit zero because of the noise — a model can only be as good as the signal in its data.

The update rule:

```
w ← w − lr · ∂L/∂w        where L = mean((w·x + b − y)²)
b ← b − lr · ∂L/∂b        ∂L/∂w = mean(2·err·x),  ∂L/∂b = mean(2·err)
```

Illustrative code (**my own snippet, not from the book's repo**) — paste into any Python with NumPy:

```python
import numpy as np
rng = np.random.default_rng(0)
x = np.linspace(0, 5, 40)
y = 3 * x + 2 + rng.normal(0, 1.2, 40)       # hidden pattern + noise

w, b, lr = 4.5, 0.4, 0.02                     # random-ish start
for step in range(400):
    err = (w * x + b) - y                      # 1. predict, 2. measure
    w -= lr * 2 * (err * x).mean()             # 3. nudge w
    b -= lr * 2 * err.mean()                   #    nudge b
print(f"w={w:.3f}  b={b:.3f}  loss={(((w*x+b)-y)**2).mean():.2f}")
# -> w=3.085  b=1.706  loss=0.88
```

#### Same idea at scale

| | Our line | GPT-3 |
|---|---|---|
| Parameters | 2 | 175,000,000,000 |
| Training data | 40 points | hundreds of billions of tokens |
| Task | predict y from x | predict next token from context |
| Update rule | gradient descent | gradient descent (Adam, Ch 12) |

---

## 1.3 The AI family tree

![hierarchy](img/hierarchy.png)

- **AI** — anything we'd call intelligent: rule systems, search, chess engines, spam filters, ChatGPT.
- **Machine learning** — learns from data instead of fixed rules.
- **Deep learning** — ML using many-layer neural networks. Layers build abstraction: in vision, edges → parts → objects. In language, roughly word pieces → phrases/syntax → meaning.
- **LLMs** — deep learning for language, trained to predict the next token; "large" because of billions of parameters and huge training sets.

Every LLM is DL is ML is AI; not the reverse.

### Timeline

![timeline](img/timeline.png)

| Year | Event |
|---|---|
| 1950 | Turing proposes his test |
| 1956 | "Artificial Intelligence" coined at Dartmouth |
| 1960s–70s | Early optimism, then the first AI winter |
| 1997 | Deep Blue beats Kasparov |
| 2012 | AlexNet wins ImageNet → deep learning boom |
| **2017** | **"Attention Is All You Need" → the Transformer** |
| 2018 | GPT-1 (117M parameters) |
| 2020 | GPT-3 (175B parameters) |
| 2022 | ChatGPT goes mainstream |
| 2023+ | New models every few months |

The 2017 paper is the reason for this course: the book builds a GPT-2-style Transformer from scratch (ideas in Ch 3–4, attention code in Ch 10, full model in Ch 11, training in Ch 12).

---

## 1.4 What makes LLMs special?

Language is ambiguous and context-dependent. "I saw her duck" = I saw her pet bird / I saw her lower her head. Humans resolve this from context instantly; older systems had no good way to represent context. Transformers let each word consider the whole passage (attention — Chapters 3, 4 and 10).

### Can do
Write and edit; generate code; translate (quality varies); summarise; answer questions; multi-step reasoning (not always reliable); adopt personas and follow instructions. **None of this was explicitly programmed** — it emerged from next-token prediction at scale.

### Emergence
Simple objective + enough scale → complex behaviour. Whether it's "genuine reasoning" or very sophisticated pattern matching is an open, actively debated question. Builder's stance: don't assume — measure on your task.

### Can't do on its own (the base model)
| Limitation | Why |
|---|---|
| No real-time info | Knowledge frozen at training cutoff |
| No memory between sessions | Each chat starts with an empty context |
| Can't act | Only outputs text |
| Unreliable maths | Predicts digit tokens by pattern rather than calculating |
| Doesn't know when it's wrong | No built-in fact checker |

### Model vs product

![model vs product](img/llm_vs_product.png)

Products wrap the model in tools: web search (fresh facts), code interpreter (exact maths), memory, document retrieval (RAG), API actions. When a chatbot tells you the weather, the model called a tool and reported the result. The book's phrase: the LLM is the brain, tools give it hands, eyes and a phone. Part IV of the book builds these.

### Why hallucination happens

![lossy compression](img/lossy.png)

There's no fact database inside — only patterns in weights. Karpathy calls an LLM a **lossy compression of the internet**: trillions of tokens squeezed into gigabytes of numbers keeps the gist (grammar, common facts, reasoning styles) and loses detail. Answering is reconstruction; for rare details (a specific citation, an exact date) the gaps are filled with what *sounds* plausible. The model was optimised for likely text, not true text; those usually overlap, and when they don't, you get a hallucination. George Box: "All models are wrong, but some are useful." → **Verify anything important.**

---

## 1.5 Hands-on

| Prompt | Watch for |
|---|---|
| Explain photosynthesis like I'm 5 | Vocabulary and analogies adapt |
| Write a haiku about debugging code | 5-7-5 structure |
| You are a pirate captain. Explain compound interest | Persona held while explaining |
| 5 machines make 5 widgets in 5 minutes; 100 machines, 100 widgets? | Correct answer: **5 minutes** (each machine makes one widget per 5 min) |
| What major news happened yesterday? | Uses search, or admits it can't know |
| What are you unable to do? | How it describes its limits |

Exercises: **(1) Find a mistake** on a topic you know well — builds trust calibration. **(2) Variation** — same question in three fresh chats; differences show generation is probabilistic (sampling, Ch 11). **(3) Push the limits** — multi-step maths, obscure topics, exact facts, trick logic; compare with and without tools.

---

## 1.6 Why build one?

1. **Demystification** — magic invites fear and hype; understanding invites judgment (you become the person in the meeting who knows what's feasible).
2. **Career advantage** — useful across engineering, product, design, research, entrepreneurship; early understanding compounds.
3. **Customisation** — fine-tune on your documents, run small models on devices, serve a niche domain or low-resource language.
4. **Understanding through building** — Feynman: "What I cannot create, I do not understand." Karpathy's *Neural Networks: Zero to Hero* follows this philosophy; the book is designed as a companion to it.

---

## 1.7 Checkpoint exercise (15–20 min)

List five AI systems you used this week: what it does, where it sits on the tree, what patterns it recognises.

| System | Does | Category | Patterns |
|---|---|---|---|
| Gmail spam filter | Sorts email | ML | Spam vs legit signals |
| Netflix recommendations | Suggests shows | ML | Your history + similar users |
| Siri / Alexa | Voice assistant | DL (classic) / LLM (modern) | Speech, intent |
| Phone autocomplete | Next word | ML/DL | Word sequences in context |

---

## 1.8 Key takeaways
1. AI is pattern recognition at scale: statistics + data + compute.
2. ML learns by adjusting parameters from feedback (predict → measure → nudge → repeat).
3. AI ⊃ ML ⊃ Deep Learning ⊃ LLM.
4. LLMs write, code, translate, reason — but not real-time facts or reliable maths on their own.
5. Hallucination = reconstruction error of a lossy compression.
6. Products wrap the base model in tools.

## 1.9 Review questions (my answers)
1. **Simplest definition of AI?** Pattern recognition at scale — finding patterns in data and using them to predict.
2. **ML vs traditional programming?** Traditional: people write rules. ML: we supply data + answers and the system learns the rules as numbers.
3. **Where do LLMs fit?** Innermost circle: deep learning models specialised for language, trained on next-token prediction.
4. **Three strengths, three weaknesses?** Strong: writing, code, summarising. Weak alone: real-time info, reliable arithmetic, knowing when it's wrong.
5. **Why hallucination?** No fact store; weights are a lossy compression; missing details are filled with plausible text.
6. **Why understand LLMs without being a researcher?** Better feasibility judgment, career leverage, ability to customise, debugging intuition.

(The book's own answers are in its Appendix D.)

## Practice this
- [ ] Run the 6 prompts on two different chatbots; compare.
- [ ] Do the 3 exercises; keep a trust/verify log.
- [ ] Fill in your own 5-system table.
- [ ] Run the line-fit snippet above; change `lr` to 0.05 and 0.001 and watch what happens.
- [ ] Browse <https://github.com/FirstLLM/code> — notebooks start at Chapter 5.

## Up next
Chapter 2 — How Computers "Understand" Words: tokens, vectors, embeddings and similarity.

---

### Credits
Based on **"Build Your First LLM"** by **Hasan Degismez** — please buy the book: <https://leanpub.com/FirstLLM/>. Code: <https://github.com/FirstLLM/code> (MIT License). Notes, diagrams and examples: my own teaching adaptation · Waqar Shaikh Builds.
