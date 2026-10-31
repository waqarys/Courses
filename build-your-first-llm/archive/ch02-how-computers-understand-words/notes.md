# Chapter 2 — How Computers "Understand" Words (Study Notes)

> Study notes for **Build Your First LLM** by Hasan Degismez (2025), written in my own words as a learning companion, not a substitute for the book. Buy it at <https://leanpub.com/FirstLLM/>. Companion code: <https://github.com/FirstLLM/code> (MIT). Chapter 2 has no notebook (they start at Chapter 5). **All code below is my own illustration**, run against the public GloVe vectors (`glove-wiki-gigaword-100`, Stanford NLP).

**Slides:** [slides.md](slides.md) · **Narration:** [script.md](script.md) · **Captions:** [captions.srt](captions.srt)

---

## 0. Why this chapter matters
A language model can only compute with numbers. This chapter covers the first step of the machine: mapping each word (later, each *token*) to a vector whose **position encodes meaning**. Every later chapter starts from this lookup table. In Chapter 5 you build it yourself as `nn.Embedding`.

### Learning goals
1. Explain why ASCII codes and arbitrary word IDs fail as representations.
2. Treat words as points in a space. Compute Euclidean distance and cosine similarity.
3. Explain why embeddings need hundreds of dimensions.
4. Explain *king − man + woman ≈ queen* and its limits.
5. Describe how embeddings are learned from context (distributional hypothesis, self-supervision).
6. Distinguish static from contextual embeddings, and say why averaging fails for sentences.

### Vocabulary
| Term | Meaning (my words) |
|---|---|
| Vector | An ordered list of numbers, i.e. a point in space |
| Dimension | One axis or coordinate of that space |
| Embedding | A word's learned vector; nearby vectors ↔ related meanings |
| Word space | The space where embeddings live |
| Distributional hypothesis | Words used in similar contexts have similar meanings |
| Cosine similarity | a·b / (‖a‖‖b‖); 1 = same direction, 0 = unrelated, −1 = opposite |
| Word2Vec | 2013 Google method that learns embeddings by predicting words from neighbours |
| Self-supervised learning | The training target (a missing or next word) comes from the raw data |

---

## 1. The computer's dilemma
### 1.1 ASCII
`cat = [99, 97, 116]` and `car = [99, 97, 114]` differ by 2 in one position, yet the words are unrelated. `kitten = [107,105,116,116,101,110]` and `feline` look nothing like `cat`, yet they mean nearly the same thing. ASCII encodes **spelling**, and spelling is mostly arbitrary.

### 1.2 One ID per word
Say cat = 1, dog = 2, fish = 3, feline = 4, kitten = 5, automobile = 6. The IDs are now distinct, but the gaps between them mean nothing. Kitten (5) is about as far from cat as automobile (6) is. Arithmetic is nonsense: cat + dog = 3 = fish.

### 1.3 The wish list
1. Similar words → similar numbers. 2. Unrelated words → different numbers. 3. Relationships preserved.

---

## 2. Words as locations
Give each word **coordinates**, like places on a map. In a toy 2-D space with an illustrative *gender* x-axis and *age* y-axis:

| word | vector |
|---|---|
| boy | [1, 2] |
| man | [1, 7] |
| woman | [9, 7] |

- d(boy, man) = √(0² + 5²) = **5**
- d(boy, woman) = √(8² + 5²) = √89 ≈ **9.43**

**Caveat (the book makes it too):** real embedding dimensions are learned and rarely match nameable concepts.

### Cosine similarity
cos(a, b) = (a·b)/(‖a‖‖b‖). Example: a = [4, 3], b = [3, 4] → 24/(5·5) = **0.96**. With c = [−3, 1]: (−12+3)/(5·√10) ≈ **−0.57**. Cosine ignores vector length and compares direction only. That is why it is the standard measure in high dimensions.

### Why 2-D is not enough
King is like queen (royalty), like man (gender) and like president (leadership). Each kind of similarity needs its own room. Adding a third *royalty* axis separates prince, princess, king and queen from the commoners (see `img/wordspace3d.png`, my redraw).

---

## 3. Embeddings
An **embedding** is a word's vector in a space of hundreds or thousands of dimensions. The book's numbers for king, queen and banana are illustrative. Here are real ones:

```python
# my own snippet, not from the book's repo
import gensim.downloader as api
m = api.load("glove-wiki-gigaword-100")     # 400k words x 100 dims (~128 MB)
print(m["king"][:6])
for a, b in [("cat","dog"),("king","queen"),("cat","kitten"),("cat","feline"),("cat","car"),("king","banana")]:
    print(a, b, round(float(m.similarity(a, b)), 3))
print(m.most_similar(positive=["king","woman"], negative=["man"], topn=3))
```

My results (GloVe-100):

| pair | cosine |
|---|---|
| cat / dog | 0.880 |
| king / queen | 0.751 |
| cat / kitten | 0.558 |
| cat / feline | 0.486 |
| cat / car | 0.311 |
| king / banana | 0.161 |

Observation: *feline* scores lower than *dog*, because the vectors capture **usage** (feline is a formal or scientific word), not dictionary synonymy.

**Dimensions.** GPT-2 small and BERT-base use 768; the largest models use 12,288 or more. No single dimension has a clean meaning, because meaning is *distributed* across all of them.

**The name.** In maths, an embedding maps objects into another space while preserving structure. Here, discrete symbols are mapped into a continuous space.

**Multilingual note.** In multilingual models, "dog" and "Hund" become neighbours because they share contexts. In *English-only* GloVe, cos(dog, hund) = −0.006, so the alignment comes from multilingual training data.

---

## 4. The famous equation
nearest_word(E(king) − E(man) + E(woman)) = **queen**. The three input words are excluded from the search, and the result point does not exactly equal any word's vector.

- GloVe top-3: queen 0.77, monarch 0.68, throne 0.68. The raw result vector has cosine 0.783 with *queen*.
- The man→woman, king→queen, boy→girl, uncle→aunt and prince→princess offsets are roughly parallel (`img/glove_pca.png`, 2-D PCA of the real vectors).

### Testing the book's examples
| query | expected | GloVe top-3 | top-1 hit? |
|---|---|---|---|
| king − man + woman | queen | queen, monarch, throne | ✓ |
| Paris − France + Italy | Rome | rome, milan, naples | ✓ |
| Tokyo − Japan + Germany | Berlin | **frankfurt**, berlin, munich | ✗ |
| walking − walk + swim | swimming | swimming, surfing, swam | ✓ |
| bigger − big + small | smaller | **larger**, smaller, large | ✗ |
| brother − man + woman | sister | **daughter**, wife, mother | ✗ |
| uncle − man + woman | aunt | aunt, daughter, niece | ✓ |

That is 4 of 7 at top-1, which matches the book's caveat that analogy accuracy is typically 40–70%. Misses come from answers sitting close to the input word, from frequent competitors (Frankfurt is very common in news text), from the choice of corpus, and from **bias** in the training text.

**Connection to Ch 1.** Embeddings are the first stage of "lossy compression". That compression lets the model generalise, and it is also why it can produce plausible but wrong output.

---

## 5. How embeddings are learned
- **Firth:** "You shall know a word by the company it keeps." This is the *distributional hypothesis*.
- **Word2Vec (2013):** slide a window over billions of words. Either predict the centre word from its neighbours (CBOW) or predict the neighbours from the centre word (skip-gram). When a prediction is wrong, nudge the vectors. Words that share contexts drift together.
- **Self-supervised:** the label is a word that is already in the text, so no human annotation is needed. Next-token LLM training uses the same principle.
- **Compromise vectors:** a static model has one vector per word. In GloVe, *bank*'s neighbours are banks, banking, credit, investment, financial (the money sense dominates). *Apple*'s neighbours are microsoft, ibm, intel, software, dell, pc, macintosh, iphone, with no fruit in the top 8.

### Static vs contextual
| | Static (Word2Vec / GloVe) | Contextual (Transformer) |
|---|---|---|
| vectors per word | 1 fixed | 1 per occurrence |
| "river bank" vs "bank account" | same | different |
| mechanism | lookup table | lookup + attention layers |

---

## 6. From words to sentences
**Averaging** word vectors gives one fixed-size vector per sentence. That is decent for document similarity, but:
- "Dog bites man" and "Man bites dog" have the **same** average. I checked: the vectors are exactly equal.
- "not good" vs "good, not bad": similar bags of words, opposite sentiment.

Averaging loses word order, long-range links, modifiers and disambiguation. What we need is to process words in sequence, let words influence one another, handle long distances, and give the same word different vectors in different contexts. That is **attention** (Ch 3). Static embeddings are *necessary but not sufficient*.

---

## 7. Exercises (my GloVe answers)
**Tools:** projector.tensorflow.org; word2vec demo sites; or the snippet above.

**Ex 1 – clusters**
- happy → 'm, feel, 're, i, 'll, really, glad, good. These are *grammatical* companions, not other emotions.
- doctor → physician, nurse, dr., doctors, patient, medical, surgeon, hospital.
- red → yellow, blue, green, black, white, purple, pink, orange.

**Ex 2 – arithmetic**
- France − Paris + London → britain (0.89), england, australia.
- good − better + worse → bad (0.85), terrible, thing.
- dog − puppy + kitten → cat (0.69), dogs, monkey.

**Ex 3 – apple.** In GloVe the tech sense dominates completely (see §5).

---

## 8. Checkpoint: 3-D animal embedding
I used the book's example ratings (size, domestic, dangerous) and computed pairwise cosine similarity (`img/animals.png`):
- cat–lion **−0.99** (almost opposite)
- cat–hamster **0.97**, cat–rabbit **0.97**
- lion–shark **0.998**

With these dimensions the space groups animals as **small safe pets vs large dangerous animals**, and biology plays no part (goldfish ≈ hamster). So *the dimensions you choose decide which similarities exist*. Real models learn hundreds of dimensions, which lets many groupings coexist.

```python
# my own snippet
import numpy as np
names = "Cat Lion Dog Goldfish Shark Hamster Bear Horse Wolf Rabbit".split()
A = np.array([[-.5,.9,-.7],[.8,-1,.9],[0,.9,-.3],[-.9,.8,-1],[.7,-1,.9],
              [-.9,.9,-.9],[.9,-.9,.8],[.7,.7,-.2],[.3,-.8,.6],[-.7,.7,-.9]])
U = A / np.linalg.norm(A, axis=1, keepdims=True); S = U @ U.T
print(dict(zip(names, S[0].round(2))))   # similarities to Cat
```

---

## 9. Key takeaways
1. ASCII captures spelling, not meaning.
2. Embeddings are positions in a high-dimensional semantic space.
3. Similar words cluster together, and unrelated words sit far apart.
4. king − man + woman ≈ queen works, but only approximately (4/7 in my test).
5. Context teaches meaning through self-supervision.
6. Static embeddings, especially averaged ones, lose order and context, which is why we need attention.

**Pipeline:** word → embedding lookup (a row of a table) → vector (e.g. 768 numbers) → position near related words.

## 10. Review questions (my answers)
1. **ASCII?** It encodes arbitrary spelling: cat ≈ car numerically, while cat and kitten look unrelated.
2. **Embedding?** A learned vector whose position reflects meaning. The name comes from maths: mapping discrete symbols into a continuous space while preserving structure.
3. **Hundreds of dimensions?** Words relate in many ways at once (royalty, gender, leadership…), and each kind of relationship needs room.
4. **king − man + woman?** It moves along a consistent "gender" offset, and the nearest word to the result is queen. Relationships are encoded as consistent directions.
5. **Company it keeps?** Meaning comes from context. Embedding systems predict words from their neighbours, so words used in similar contexts get similar vectors.
6. **Averaging?** It discards order and interactions: "dog bites man" = "man bites dog".

## 11. Notes on the book (verification)
- I checked the analogy examples on real GloVe-100 vectors. Several are not top-1 (Tokyo − Japan + Germany → Frankfurt; bigger − big + small → larger; brother − man + woman → daughter). This is consistent with the book's own 40–70% caveat.
- The book's king, queen and banana vectors are illustrative (the book labels them "simplified").
- **No errata found in this chapter.**

## 12. Practice
- [ ] Hand-compute the distances and the cosine examples above.
- [ ] Run the gensim snippet; try 10 analogies of your own and record the hit rate.
- [ ] Find a two-sense word in projector.tensorflow.org.
- [ ] Do the animal checkpoint, then add a 4th dimension (e.g. *feline*) and compare.

---
**Credits.** Based on *Build Your First LLM* by Hasan Degismez. Please buy the book: <https://leanpub.com/FirstLLM/>. Code: <https://github.com/FirstLLM/code> (MIT). GloVe: Pennington, Socher & Manning (2014). Notes, diagrams and snippets are my own adaptation (Waqar Shaikh Builds).
