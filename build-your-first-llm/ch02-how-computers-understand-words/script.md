# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome back to my study series on Build Your First LLM by Hasan Degismez. In chapter one we learned that a language model predicts the next word. But a computer only understands numbers. So in this chapter we answer a deceptively simple question: how do you turn a word into numbers in a way that actually captures what the word means? The answer is embeddings, and it is one of the most elegant ideas in all of AI. I've also run real experiments with real word vectors for this video, so you'll see the ideas working, and occasionally failing, on actual data.

## Slide 2 — Where we are

A quick orientation. Chapter one gave us the big picture: a model is a big pile of numbers trained to predict the next token. Today we zoom in on the very first step of that machine, turning words into numbers. Chapter three adds attention, and chapter four puts the whole transformer together. These four chapters are conceptual, so the book has no notebook for them. The small code snippets you'll see today are my own illustrations, clearly labelled, run with the open source GloVe word vectors.

## Slide 3 — Chapter 2 roadmap

Here's the plan. We start with two naive ways of turning words into numbers, and see exactly why they fail. Then we introduce the key idea: give each word a position in a space, so distance means difference in meaning. We'll see why that space needs hundreds of dimensions, and then look at the famous king minus man plus woman equals queen result, with real numbers. After that, we'll see where embeddings come from: context, learned without any human labels. We'll separate static from contextual embeddings, see why simply averaging word vectors loses meaning, and finish with exercises, the checkpoint, takeaways and review questions.

## Slide 4 — Key terms for this chapter

Let's set up the vocabulary. A vector is just a list of numbers, which you can think of as a position in space. A dimension is one axis of that space. An embedding is a word's vector, arranged so that its position reflects its meaning. The space where all those vectors live is the word space. The distributional hypothesis says that words used in similar contexts have similar meanings. Cosine similarity measures how similar two vectors are by their angle, from minus one to one. Word2Vec is the 2013 system that made learned embeddings famous. And self-supervised learning means the training signal comes from the data itself, not from human labels.

## Slide 5 — Part 1

Part one. The computer's dilemma.

## Slide 6 — Teaching someone who only speaks numbers

Imagine explaining the idea of a cat to a friend who only understands numbers. That is exactly the position we're in with a computer. It can't read the word cat. It can only store and manipulate numbers. So we need some mapping from words to numbers. Making a mapping is easy. The hard part is making one where the numbers themselves carry meaning, so that the model can compute with meaning. Let's try the obvious approaches first.

## Slide 7 — Attempt 1: ASCII codes

The first instinct is to use the codes computers already use for text. In ASCII, c is ninety nine, a is ninety seven and t is one hundred and sixteen, so cat is ninety nine, ninety seven, one sixteen. Car is ninety nine, ninety seven, one fourteen. Those are almost identical, but a cat and a car have nothing in common. Meanwhile kitten and feline, which mean essentially the same creature, get completely different numbers, even different lengths. In the chart you can see cat and car almost on top of each other, while kitten and feline wander off.

## Slide 8 — Why ASCII fails

The core problem is that ASCII captures spelling, and spelling is mostly an accident of history. There's nothing cat-like about the letters c, a, t. Words that look alike, like cat, car, cart and cut, have unrelated meanings, and words that mean the same thing can look nothing alike. So whatever numbers we pick, they have to reflect meaning, not spelling.

## Slide 9 — Attempt 2: one ID per word

Second attempt. Forget letters, and give every word its own ID number. Cat is one, dog is two, fish is three, feline four, kitten five, automobile six. Now cat and car are definitely different. Problem solved?

## Slide 10 — Why word IDs fail

Not really. IDs are just labels. The gap between two IDs means nothing. Cat is one and kitten is five, while automobile is six, so by these numbers a kitten is almost as unrelated to a cat as a car is. And arithmetic is nonsense: cat plus dog equals three, which is fish. So we can write down our wish list. Similar words should get similar numbers. Unrelated words should get different numbers. And relationships between words should be preserved. It turns out we can have all three, but only if we stop using a single number per word.

## Slide 11 — Part 2

Part two. Words as locations.

## Slide 12 — The key insight: a position, not a number

Here's the key insight. Instead of giving each word one number, give it a position. Think of a city map. Every place has coordinates. Two cafés next to each other have similar coordinates, and a café and a park on opposite sides of town have very different ones. What if words had coordinates too, arranged so that nearby words have similar meanings?

## Slide 13 — A toy word space (my redraw)

Here's a toy two dimensional word space that I've drawn. The horizontal axis is a made up gender axis, masculine on the left and feminine on the right. The vertical axis is age, young at the bottom and old at the top. Boy sits at one comma two, man at one comma seven, woman at nine comma seven. Boy and girl share a height because they're the same age, and differ left to right. Man and woman show the same pattern. Notice the distances: boy to man is exactly five, boy to woman is the square root of eight squared plus five squared, about nine point four three. So boy is closer to man than to woman, which matches our intuition.

## Slide 14 — Vectors and distance

In this picture each word is a vector, a list of two numbers. The straight line distance between two vectors is the square root of the sum of squared differences in each coordinate. Boy to man differs only in age, by five, so the distance is five. Boy to woman differs by eight in gender and five in age, giving the square root of eighty nine, about nine point four three. One important warning that the book also makes: these neat named axes are just for teaching. In real embeddings the dimensions are learned automatically, and they almost never line up with tidy human concepts like gender or age.

## Slide 15 — Cosine similarity: compare directions

In high dimensional embeddings the standard measure is not distance but cosine similarity, which looks at the angle between two vectors. You take the dot product, multiply matching coordinates and add them up, and divide by both lengths. In my example, a is four comma three and b is three comma four. Their dot product is twelve plus twelve, twenty four, and each has length five, so the cosine is twenty four over twenty five, zero point nine six. Very similar directions. Vector c points elsewhere, and its cosine with a is about minus zero point five seven. Cosine runs from one, same direction, through zero, unrelated, to minus one, opposite. Because it ignores length, it compares what a vector points at, not how long it is.

## Slide 16 — Two dimensions aren't enough

Two dimensions quickly run out of room. A king is similar to a queen because both are royalty. A king is similar to a man because both are male. And a king is similar to a president because both are leaders. Each of those is a different kind of similarity, and to represent all of them at once we need more axes.

## Slide 17 — Add a third axis: royalty (my redraw)

Here's the same idea in three dimensions, again with illustrative axes: gender, age, and now royalty. The commoners, boy, girl, man and woman, sit on the floor of the cube in blue. The royals, prince, princess, king and queen, float above them in gold. Prince is now closer to king than to boy, and princess is closer to queen than to girl. And that's with just three dimensions. We can't draw seven hundred and sixty eight, but the maths works exactly the same way.

## Slide 18 — Part 3

Part three. The magic of embeddings.

## Slide 19 — What an embedding is

This list of numbers that places a word in a high dimensional space is called an embedding. The book shows a stylised example: king and queen have similar numbers in each position, and banana has very different ones. Those numbers are illustrative. On the next slides I'll show you the real thing, using GloVe, a set of one hundred dimensional word vectors trained on Wikipedia and newswire text that anyone can download.

## Slide 20 — Real vectors: GloVe-100 (my experiment)

Here's the tiny program I used. It loads the GloVe vectors through the gensim library, about four hundred thousand words, each with one hundred numbers. Then it prints part of a vector, computes a cosine similarity, and asks for the nearest words to king minus man plus woman. This is my own snippet, not from the book's repository.

## Slide 21 — Cosine similarity on real vectors

And here are the real cosine similarities. Cat and dog: zero point eight eight. King and queen: zero point seven five. Cat and kitten: zero point five six, and cat and feline: zero point four nine, lower than you might expect, because feline appears in more formal, scientific contexts than cat. Cat and car, despite the near identical spelling: only zero point three one. And king and banana: zero point one six. The ordering is broadly what we wanted. Notice that these vectors capture how words are used, which is not always the same as dictionary meaning.

## Slide 22 — Why more dimensions help

Why so many dimensions? Think about describing a person. With just height you can tell tall from short. Add weight and you can tell tall and thin from tall and heavy. Add age, hair and eye colour, and descriptions get much more specific. Words are the same. Two dimensions give crude groupings, around a hundred can separate mammals from reptiles and pets from wild animals, and seven hundred and sixty eight can capture the difference between a leisurely stroll and a deliberate march. Seven sixty eight is common because GPT-2 small and BERT base used it, and very large models go to twelve thousand two hundred and eighty eight or more. Importantly, no single dimension means something nameable. Meaning is spread across all of them.

## Slide 23 — Why is it called an "embedding"?

Why the name embedding? In mathematics, an embedding maps objects from one space into another while keeping important structure. Here we take discrete symbols, where cat and car have no inherent relationship, and place them into a continuous space where position encodes meaning. Once they're in that space, we can do all the things computers are good at: measure distances, find neighbours, and do arithmetic. That's what makes language processing mathematical.

## Slide 24 — Did you know? Across languages

Here's a nice fact from the book. In models trained on many languages, the English word dog and the German word Hund end up as neighbours, because they appear in similar contexts. Nobody tells the model they're translations. I tested this with GloVe, which is trained on English only, and the cosine between dog and hund is basically zero, minus zero point zero zero six. That's not a contradiction of the book. It's a useful lesson: the cross language alignment comes from multilingual training data. An embedding only knows what its training text showed it.

## Slide 25 — Part 4

Part four. The famous equation.

## Slide 26 — king − man + woman = ?

In 2013, researchers at Google found that you could do arithmetic with word vectors. Take the vector for king, subtract the vector for man, and add the vector for woman. The result is a point in space that doesn't exactly match any word. But when you look for the nearest word in the vocabulary, leaving out the three input words, you get queen.

## Slide 27 — Real GloVe result (my experiment)

Here's what that looks like with real GloVe vectors, projected down to two dimensions so we can see it. The arrow from man to woman, and the arrow from king to the computed point, are the same vector. The computed point, the gold cross, lands right next to queen. Its cosine similarity with queen is about zero point seven eight. The top three results from gensim are queen at zero point seven seven, then monarch and throne. Remember that a two dimensional projection is a squashed view of a hundred dimensions, so distances in this picture are only approximate.

## Slide 28 — Parallel relationships (my redraw)

This chart shows why the trick works. I took ten real GloVe vectors and projected them to two dimensions. The gold arrows go from man to woman, king to queen, boy to girl, uncle to aunt, and prince to princess. They're roughly parallel and of similar length. The embedding has learned something like a consistent gender direction, without anybody defining gender.

## Slide 29 — What this reveals

So embeddings do more than put similar words near each other. They organise words so relationships are consistent: the same offset means the same relation. There's a gender direction, man to woman, king to queen, uncle to aunt. There's a capital of direction, from France to Paris and Italy to Rome. Nobody programmed any of this. It emerged purely from patterns in text.

## Slide 30 — The book's examples, tested on GloVe-100

The book lists several analogy examples, and it's honest that these only work around forty to seventy percent of the time. So I ran them. Paris minus France plus Italy gives Rome. Walking minus walk plus swim gives swimming. Uncle minus man plus woman gives aunt. But three missed at the top spot. Tokyo minus Japan plus Germany gives Frankfurt first, with Berlin a close second. Bigger minus big plus small gives larger, just ahead of smaller. And brother minus man plus woman gives daughter, then wife and mother. Sister isn't in the top three. Four out of seven, which fits the book's forty to seventy percent nicely.

## Slide 31 — Why analogies miss

Why do they miss? Often the right offset lands near the starting word's own neighbourhood, so bigger plus a little nudge lands on larger. Words that are frequent in similar contexts compete: in newswire text, Frankfurt shows up constantly as Germany's financial centre. Different training data produces different answers. And training data carries biases, which show up as directions in the space too, which is a real concern. The arithmetic is approximate. But the fact that it works at all shows embeddings capture genuine structure. They are a map of meaning, a fuzzy one.

## Slide 32 — Connection: lossy compression (Ch 1)

This connects to chapter one's lossy compression idea. Embeddings are the first stage of compressing the endless variety of language into fixed size vectors, and the rest of the model keeps compressing. That's why a model can reason about combinations it's never seen exactly, and it's also why it sometimes fills gaps with plausible but wrong details.

## Slide 33 — Part 5

Part five. How are embeddings learned?

## Slide 34 — "You shall know a word by the company it keeps"

Where do these numbers come from? The answer is beautifully simple: context. The linguist J. R. Firth said you shall know a word by the company it keeps. Fill in the blank: the blank sat on the mat, the blank chased the mouse. Cat, dog, kitten or puppy all fit. These words share contexts, so they must be related. Now: I deposited money at the blank, the blank approved my loan. That's bank, the financial kind. Different contexts, different cluster. This is the distributional hypothesis.

## Slide 35 — Learning from prediction (Word2Vec idea)

Here's how Word2Vec style systems learn. Take a huge amount of text. Slide a small window across it. For each position, either predict the middle word from the words around it, which is called continuous bag of words, or predict the surrounding words from the middle one, which is called skip gram. Every time the prediction is wrong, nudge the vectors a little so the prediction improves. After billions of these tiny updates, words that keep showing up in similar contexts end up with similar vectors.

## Slide 36 — What the system ends up learning

What comes out? Cat and dog share so many contexts that GloVe puts them at a cosine of zero point eight eight. King appears near royalty, rulers and male words, so its vector encodes all of that at once. And bank appears both near river and near money, so it gets a single compromise vector. In GloVe, which is trained largely on news text, bank's nearest neighbours are banks, banking, credit, investment and financial. The money sense completely dominates, and the river sense is buried.

## Slide 37 — The beauty of self-supervision

What's remarkable is that none of this needed human labels. Nobody marked cat and kitten as related. The thing to predict is simply a word that's already in the text. That's self-supervised learning, and it's why we can train on billions of words. Labelling that much by hand would be impossible. And it's exactly the same principle that trains large language models: predict the next token.

## Slide 38 — Static vs contextual embeddings

Now an important distinction. Word2Vec and GloVe give static embeddings: one fixed vector per word, whatever the context. So bank gets the same vector in river bank and in bank account. Modern language models produce contextual embeddings. They start from a lookup table too, but then the attention layers modify each vector based on the surrounding words, so bank in river bank ends up somewhere very different from bank in bank account. Static embeddings are the stepping stone. Contextual ones are what LLMs actually use, and attention, our next chapter, is how they get there.

## Slide 39 — Static embeddings and "apple"

Here's a striking example from my GloVe run. The nearest neighbours of apple are Microsoft, IBM, Intel, software, Dell, PC, Macintosh and iPhone. Not a single fruit in the top eight. In news text, the company is mentioned far more than the fruit, and a single static vector can only lean one way. A contextual model would treat apple pie and Apple shares completely differently.

## Slide 40 — Part 6

Part six. From words to sentences.

## Slide 41 — The naive approach: average the vectors

We can now represent single words. But language comes in sentences and documents. The simplest idea is to average the vectors of all the words in a sentence. That gives one fixed size vector for any sentence, and for some tasks, like finding similar documents, it works surprisingly well. But there's a fatal flaw.

## Slide 42 — Order matters!

Dog bites man, and man bites dog. Same three words, so exactly the same average. I checked with the real vectors, and the two averages are identical, cosine one. But one is a boring Tuesday, and the other is front page news. Or take the movie was not good, versus the movie was good, not bad. Very similar bags of words, opposite meanings. Averaging just can't see the difference.

## Slide 43 — What averaging throws away

Let's list what averaging throws away. Word order. Long range relationships, like linking was back to cat across a whole clause. Modifiers, like not flipping the meaning of good. And disambiguation, like which bank we mean. All of that depends on how words relate to each other, and averaging erases it.

## Slide 44 — What we need → attention (Ch 3)

So here's what we need. Process words in sequence and keep track of order. Let words influence each other's meaning. Handle relationships across long distances. And give the same word different representations in different contexts. That is exactly what the attention mechanism does, and it's chapter three. Static embeddings are necessary, they give us a mathematical starting point, but they aren't sufficient.

## Slide 45 — Part 7

Part seven. Let's get hands on.

## Slide 46 — Online tools to explore

You can explore embeddings yourself. The TensorFlow Embedding Projector at projector dot tensorflow dot org shows word vectors in three dimensions. Search for a word, see its neighbours, and rotate the cloud. There are also many word arithmetic demos online. Or run my five line gensim snippet from the notes, on your own machine or in Colab.

## Slide 47 — Exercise 1: find clusters (my GloVe answers)

Exercise one asks you to look at the neighbours of happy, doctor and red. Here's what GloVe gave me. Red is perfect: the other colours. Doctor: physician, nurse, doctors, surgeon, hospital, the medical world. But happy is interesting. Its neighbours are fragments like I'm, feel, you're and really. That's because happy appears in phrases like I'm really happy, so this model learned the grammatical company it keeps more than other emotions. That's the distributional hypothesis in action, warts and all.

## Slide 48 — Exercise 2: word arithmetic (my GloVe answers)

Exercise two has three analogies. France minus Paris plus London gives Britain, with England second. Good minus better plus worse gives bad. And dog minus puppy plus kitten gives cat, though at a cosine of only zero point six nine, with dogs and monkey not far behind. Try them yourself, and when they miss, ask why: is the answer a rare word, an ambiguous word, or a word used in different contexts in the training text?

## Slide 49 — Exercise 3: the "apple" puzzle

Exercise three is the apple puzzle. You might expect two clusters around apple, fruits and technology. In GloVe, technology completely dominates. Try it in the embedding projector, which uses a different dataset, and see whether the fruit sense appears. Either way, the lesson is that a static vector ends up wherever the training text pulls it.

## Slide 50 — Part 8

Part eight. The checkpoint exercise.

## Slide 51 — Build a 3-D animal embedding (20–30 min)

The checkpoint asks you to build your own three dimensional embedding for ten animals, on paper or in a spreadsheet. Choose three properties, for example size, how domestic, and how dangerous. Rate each animal from minus one to plus one. Then compare them. Which animals are closest? Do cat and lion cluster because they're both felines, or do cat and hamster cluster because they're small pets? And what does that tell you about your choice of dimensions?

## Slide 52 — The book's example table, computed (my analysis)

I took the example ratings from the book and computed every pairwise cosine similarity. The answer is dramatic. Cat and lion have a cosine of minus zero point nine nine: they're almost opposite. Cat and hamster are at zero point nine seven, and cat and rabbit at zero point nine seven. Lion and shark are nearly identical at zero point nine nine eight. With these three dimensions, the space sorts animals into small, safe pets versus large, dangerous wild animals. Biology doesn't come into it at all.

## Slide 53 — What the checkpoint teaches

That's the lesson. The dimensions you choose decide which similarities exist. With size, domestic and dangerous, a goldfish is almost the same as a hamster, even though one is a fish and one is a mammal. Add a feline dimension, or water dwelling, or number of legs, and new groupings appear. Real models don't hand pick dimensions. They learn hundreds of them from data, so many kinds of grouping can coexist in one space.

## Slide 54 — Part 9

Part nine. Wrapping up.

## Slide 55 — The embedding pipeline

Here's the whole pipeline in one picture. A word, like king, is looked up in a big table, so its embedding is just one row of that table. The result is a vector, maybe seven hundred and sixty eight numbers. And its position in the semantic space puts it near queen and far from banana. In chapter five you'll build exactly this lookup table in PyTorch, with nn dot Embedding.

## Slide 56 — Key takeaways

The key takeaways. One: ASCII captures spelling, not meaning. Two: embeddings represent words as positions in a high dimensional space. Three: similar words cluster together, and unrelated words are far apart. Four: word arithmetic works, approximately, like king minus man plus woman landing near queen. Five: context teaches meaning, without any human labels. And six: static embeddings, especially when averaged, lose word order, so we need something more. That something is attention.

## Slide 57 — Notes on the book (checked)

A quick note on accuracy, since I'm checking the book as I go. I tested the chapter's examples against real vectors, and everything behaves as the book says, including its warning that analogies only work some of the time. A few of its listed examples don't come out first in GloVe, but the book presents them as typical relationships, not guaranteed outputs. The embedding numbers for king, queen and banana are illustrative, which the book itself signals by calling them simplified. I found no factual errors in this chapter.

## Slide 58 — Review questions 1

Review questions, with my answers. Question one: why not ASCII codes? Because they encode spelling, which is arbitrary, so cat and car look almost identical while cat and kitten look unrelated. Question two: what is an embedding, and why that name? It's a word's vector in a learned space where position reflects meaning. The name comes from maths: mapping discrete symbols into a continuous space while preserving structure. Question three: why hundreds of dimensions? Because words are similar in many different ways at the same time, royalty, gender, leadership and so on, and each kind of relationship needs room.

## Slide 59 — Review questions 2

Question four: explain king minus man plus woman. Subtracting man and adding woman moves the king vector along a consistent gender direction, and the nearest word to where you land is queen. It shows that embeddings encode relationships as consistent offsets. Question five: what does you shall know a word by the company it keeps mean? That meaning comes from context. Embedding systems learn by predicting words from their neighbours, so words used in similar contexts end up with similar vectors. Question six: why isn't averaging enough? Because it throws away order and interactions. Dog bites man and man bites dog average to exactly the same vector.

## Slide 60 — Practice this

Here's your practice list. Compute the boy, man and woman distances by hand, and the cosine of four three and three four. Run the gensim snippet from the notes, try ten analogies of your own, and record your hit rate. Explore the embedding projector and find a word with two senses. Do the animal checkpoint, then add a fourth dimension and watch the groupings change. And peek ahead at the book's companion repository on GitHub, where chapter five builds the embedding table in PyTorch. The code in this video is my own illustration, since Part One has no book notebook.

## Slide 61 — Up next: Chapter 3

That's chapter two. We can turn words into vectors that capture meaning. But meaning lives in relationships. In the sentence the cat sat on the mat because it was tired, how does a computer know that it means the cat? It has to look at the whole sentence and work out what relates to what. That's the problem attention solves, and it's chapter three.

## Slide 62 — Credits

This video is based on the book Build Your First LLM by Hasan Degismez. Everything here is my own adaptation for study, so please support the author and buy the book at leanpub dot com slash First LLM. The companion code is at github dot com slash First LLM slash code, under the MIT license. The word vectors I used are GloVe, from the Stanford NLP group. Thanks for watching, and see you in chapter three.

