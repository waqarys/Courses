# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter five of my study series on Build Your First LLM by Hasan Degismez. This is where part two begins, and where we stop drawing diagrams and start writing code. In this chapter we'll run a real language model in a few lines, learn the Python we need to understand what just happened, and build our own tokenizer from scratch, the very first stage of every LLM. I ran the book's chapter five notebook end to end for this video, and I'll show you the real outputs.

## Slide 2 — Where we are

In part one we learned how LLMs work on paper. Part two gives us the tools: Python, NumPy, PyTorch, tokenizers and small neural networks. Today we run GPT-2, learn the Python essentials, and build a tokenizer. Everything follows the book's chapter five notebook, which you can open in Colab from the link in the description.

## Slide 3 — Chapter 5 roadmap

Here's the roadmap. We start with the hook: running GPT-2 in about ten lines. Then why Python. Then the basics: variables, strings, numbers and f-strings. Lists and dictionaries give us a vocabulary. Control flow and loops handle unknown words. Functions give us tokenize and detokenize. A class packages it all into a SimpleTokenizer shaped like Hugging Face's. Then we come full circle, solve the exercises and do the review questions.

## Slide 4 — Key terms for this chapter

The vocabulary for today. A variable is a name attached to a value. A string is text, which is what language models read and write. A list is an ordered collection, perfect for a sequence of tokens. A dictionary maps keys to values, which is exactly what a vocabulary is. A function is reusable code with inputs and an output. A class is a blueprint that bundles data and functions, like a tokenizer object. A tokenizer converts text to numbers and back. And a token is one unit of text, a word, a piece of a word, or a character.

## Slide 5 — Part 1

Part one. The hook. Let's run GPT-2.

## Slide 6 — GPT-2 in a few lines (book notebook, cell 3)

Here's the cell from the book's notebook. pipeline, from Hugging Face's transformers library, downloads and loads GPT-2, a hundred and twenty four million parameters. Then we call the generator with a prompt, the secret to building AI is, ask for twenty new tokens, and turn on sampling so the output is a little random. The pad token ID just silences a warning. That's it. You're driving one of the most important models in AI history.

## Slide 7 — What I got (real run, CPU)

And here's what I got when I ran it on a plain CPU. The secret to building AI is to know that people are not afraid to learn. Then it wanders off into conducted by the National Academy of. Your output will be different, because sampling draws random tokens each time. It's fluent-ish but drifts off topic, which is typical of a small base model. One small detail: the comment says twenty more words, but max new tokens counts tokens, and a token can be part of a word.

## Slide 8 — Why Python?

Why Python? Two reasons. It's readable: for word in sentence says exactly what it does. And the ecosystem: NumPy, PyTorch and Hugging Face already exist. Isn't Python slow? Raw Python is, yes. But it doesn't do the heavy lifting. When you called pipeline, Python was gluing together highly optimised C and GPU code. Python conducts, and the orchestra plays.

## Slide 9 — Part 2

Part two. Storing and processing text.

## Slide 10 — Variables and strings (notebook cell 5)

A variable is a labelled container. Here output and prompt hold two strings. len gives the number of characters, and type confirms it's a string. split breaks the text into a list of words, and lower makes everything lowercase first, which is called method chaining. And output, square bracket, len of prompt, colon, is slicing: everything after the prompt. When I ran it, the length printed was seventy one.

## Slide 11 — ⚠️ Book check: `len(output)`

A small erratum. In the book's text, the comment says this prints sixty eight. But the real answer, and what the book's own notebook prints, is seventy one. len counts every character, including the eleven spaces between the twelve words. It's a trivial slip, but it's a good habit to form right now: never trust a comment over the actual output. Run it.

## Slide 12 — Slicing — you'll use it everywhere

Slicing deserves a slide of its own, because we'll use it constantly. Index zero is the first item, minus one is the last. Colon three means the first three. Four colon means from index four to the end. And two slices we'll see in every training loop: colon minus one, everything except the last, and one colon, everything except the first. Keep those last two in mind, because they come back in the review questions.

## Slide 13 — Numbers and f-strings (notebook cell 7)

Numbers come in two main kinds: integers like fifty thousand two hundred and fifty seven, and floats like point zero zero zero one. Underscores make big numbers readable. And f-strings let you put values straight into text: colon comma adds thousands separators, colon point two e gives scientific notation, and you can even compute inside the braces, like integer division by two. Fifty thousand two hundred and fifty seven divided by two, rounded down, is twenty five thousand one hundred and twenty eight. You'll write f-strings in every training loop.

## Slide 14 — Part 3

Part three. Building a vocabulary.

## Slide 15 — GPT-2 sees numbers, not words

Here's the crucial insight. GPT-2 never sees words. It sees numbers. The book's prompt, the secret to building AI is, becomes four six four, three two hundred, two eight four, two six one five, nine five five two, three one eight. I checked those with the real tokenizer and they're right. So we need a tokenizer. Text goes in, gets lowercased and split, each word is looked up in a vocabulary, and out come token IDs.

## Slide 16 — Lists: collect the words (notebook cell 9)

First, collect all the words from some training text. The notebook uses three short sentences. We loop over them, lowercase and split each one, and use extend to add the words to one big list. extend adds each item separately. If you used append, you'd add the whole list as a single item, a classic beginner bug. Then indexing: the first word is the, the last is examples, and the first three are the, secret, to.

## Slide 17 — Dictionaries: word → ID (notebook cell 9)

Now the key step: a dictionary mapping each word to a number. We start with two special tokens. PAD, ID zero, fills empty space so that sequences in a batch line up to the same length. UNK, ID one, is the fallback for words we've never seen. Then for each word, if it isn't in the vocabulary yet, we give it the next free ID, which is just the current size of the dictionary. Fourteen unique words plus two special tokens gives sixteen. The IDs follow the order in which words were first seen.

## Slide 18 — Part 4

Part four. Handling edge cases.

## Slide 19 — Unknown words: `if/else` and `.get()`

What happens with a word that isn't in the vocabulary? Indexing the dictionary directly raises a KeyError and crashes. We could check with if and else: if the word is in the vocabulary use its ID, otherwise use UNK. Or more neatly, use dot get with a default value. That pattern is everywhere in machine learning code. With our vocabulary, neural maps to one, the unknown token.

## Slide 20 — Loops and list comprehensions (notebook cell 11)

Now a whole sentence: the neural network learns. The loop version goes word by word, gets each ID with a fallback, and appends it to a list. The list comprehension does exactly the same thing in one line: square brackets, the expression, for each w in the words. Both give two, one, one, one. Three unknowns. Our tiny vocabulary has never seen neural, network or learns. That's the weakness of word level tokenizers, and subword tokenizers in chapter eight fix it.

## Slide 21 — Part 5

Part five. Functions and classes.

## Slide 22 — Functions: encode and decode (notebook cell 13)

Functions package reusable code. def, a name, parameters in parentheses, and return sends back the result. tokenize lowercases, splits, and looks up each word. detokenize needs the reverse mapping, from ID to word, so it builds one with a dictionary comprehension that flips every pair, then joins the words with spaces. The secret to AI encodes to two, three, four, six and decodes back. Notice we lost the capital letters, because we lowercased. GPT-2's tokenizer gives completely different numbers, from a different vocabulary, but the principle is the same: text to numbers.

## Slide 23 — Classes: a blueprint with state

Hugging Face organises its tokenizers as classes, so let's do the same. A class is a blueprint, and an object is one thing built from it. You can build many objects from one class, each with its own data. The special method init runs once when the object is created and sets up its starting state. self means this particular object. Methods are functions that live on the object. And defining the special method len lets you call len on your tokenizer.

## Slide 24 — SimpleTokenizer (notebook cell 15)

Here's the full class from the notebook. init creates both directions of the mapping, word to ID and ID to word, already containing the two special tokens. fit builds the vocabulary from training texts, assigning each new word the next ID and recording the reverse mapping at the same time. encode turns text into IDs, using one for unknown words. decode turns IDs back into text. And len returns the vocabulary size. About twenty lines, and it's a real, working tokenizer.

## Slide 25 — Using it — same interface as Hugging Face

Using it looks just like using Hugging Face. Create the object, fit it on texts, and call encode. With GPT-2's tokenizer, you load it with from pretrained and call encode, the same interface. My run printed a vocabulary of sixteen, the encoding two, three, four, six, and the decoding. The real tokenizer just has many more features: subword tokenization, more special tokens, saving and loading, and batching.

## Slide 26 — Word-level vs subword (preview of Ch 8)

Our tokenizer is word level. GPT-2 uses subword byte pair encoding, which we'll build in chapter eight. Our vocabulary grows with the data, sixteen words here, while GPT-2's is fixed at fifty thousand two hundred and fifty seven. We map unseen words to UNK, while GPT-2 never needs to, because it can always fall back to smaller pieces or raw bytes. And GPT-2 keeps case, and treats the leading space as part of the token. The book says understanding can split into under and standing. I checked: that's true without a leading space, but with a space in front, as it would appear mid-sentence, GPT-2 keeps it as one token. Spaces matter.

## Slide 27 — Part 6

Part six. Full circle.

## Slide 28 — What `pipeline()` really did (my redraw)

Now we can explain the hook. When you called pipeline at the start, five things happened. One: your text went through a tokenizer, like the one you just built. Two: the IDs became embeddings, from chapter two. Three: those vectors flowed through twelve transformer layers with attention, chapters three and four. Four: a token was sampled from the predicted probabilities. Five: it was decoded back to text. And then it looped, appending the new token and running again, twenty times. You've now built stage one.

## Slide 29 — Why `tokens[:-1]` matters (my redraw)

And here's why those two slices matter. To train a language model, we take a sequence of token IDs. The inputs are all tokens except the last, and the targets are all tokens except the first, shifted by one. At every position, the model sees the tokens so far and has to predict the next one. The cat sat on the mat gives five training examples from one sentence. This one line of slicing is at the heart of every LLM training loop.

## Slide 30 — Part 7

Part seven. The exercises, with my solutions.

## Slide 31 — Exercises 1–3 solved (my own code)

Here are my solutions to the three exercises. This is my own code, not from the book's repository. Exercise one, strip punctuation: a clean helper that lowercases, removes every punctuation character using string dot punctuation and translate, and splits. Both fit and encode use it, so learning comma becomes learning. Exercise two, count unknowns: encode each sentence and count how many ones appear. Exercise three, save and load: dump the word to ID dictionary to JSON, and a class method loads it and rebuilds the reverse mapping. I ran all three: the punctuation was stripped, my test sentences had three unknown words, and a saved and reloaded tokenizer encoded identically. The full file is in the repo next to the notes.

## Slide 32 — A gotcha in Exercise 3

One gotcha in exercise three. JSON keys are always strings, so if you save the ID to word dictionary directly, your integer keys come back as strings, and decoding silently fails. The fix is to save only word to ID, and rebuild the reverse mapping on load. Hugging Face does exactly this: GPT-2's vocab dot json maps token strings to IDs.

## Slide 33 — Part 8

Part eight. Wrapping up.

## Slide 34 — Python cheat sheet (my redraw)

Here's everything from today on one page. Variables to name values. Strings, with lower and split. Lists, with indexing like minus one and slicing like colon minus one. Dictionaries, with dot get and a default. Functions with def. And classes that bundle data and methods together. That's enough Python to read most of the code in this book.

## Slide 35 — Key takeaways

The key takeaways. One: you ran a hundred and twenty four million parameter model in about ten lines, because Python orchestrates optimised code. Two: language models see token IDs, never words. Three: a vocabulary is a dictionary from words to IDs, with special tokens for padding and unknowns. Four: encode turns text into IDs, and decode turns IDs back into text. Five: our SimpleTokenizer has the same interface as Hugging Face's. Six: the two slices, colon minus one and one colon, give the inputs and targets for next token training.

## Slide 36 — Notebook run & book check

My notebook run and book check. The chapter five notebook ran end to end on a CPU, all nine code cells, with no errors. The GPT-2 token IDs, the vocabulary size of sixteen and the encodings all match the book. One erratum: the length of the output string is seventy one, not sixty eight. One clarification: understanding splits into under and standing only without a leading space. And the notebook pins transformers version four point four six, but it ran fine with a newer version too.

## Slide 37 — Review questions

The review questions, with my answers. One: what does GPT-2 see? Token IDs, integers from a vocabulary of fifty thousand two hundred and fifty seven. Two: why use dot get with UNK? Because looking up an unknown word directly raises a KeyError, while get returns a safe default. Three: a function is one reusable operation, while a class bundles state, like the vocabulary, together with the methods that use it. Four: tokens colon minus one is everything but the last token, used as the inputs, while tokens one colon gives the targets. Five: our tokenizer follows the same pattern as Hugging Face's, create, fit or load, encode and decode, but theirs adds subword BPE, special tokens and saving.

## Slide 38 — Practice this

Your practice list. Open the chapter five notebook in Colab and run every cell, then change the prompt and the number of new tokens. Set do sample to false and check whether the output becomes the same every run. Add the three exercise methods and test them with your own sentences. Compare our tokenizer with GPT-2's on a sentence containing a rare word. And next up, the chapter six notebook.

## Slide 39 — Up next: Chapter 6

That's chapter five. We can now turn text into token IDs. But IDs are just the start: next they become vectors, and vectors become matrices, and we need to compute on millions of numbers at once. That's chapter six, with NumPy and PyTorch, the language of tensors.

## Slide 40 — Credits

This video is based on the book Build Your First LLM by Hasan Degismez. Everything here is my own adaptation for study, so please support the author and buy the book at leanpub dot com slash First LLM. The code shown comes from the companion repository at github dot com slash First LLM slash code, under the MIT license. Thanks for watching, and see you in chapter six.

