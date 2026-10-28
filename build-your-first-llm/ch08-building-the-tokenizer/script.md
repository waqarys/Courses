# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter eight of my study series on Build Your First LLM by Hasan Degismez. Today we build the tokenizer, the piece that turns text into numbers and back. We'll write a character tokenizer and a word tokenizer from scratch, understand byte pair encoding, train our own BPE tokenizer on Shakespeare, and then use the production tokenizers, tiktoken and Hugging Face. I ran the whole notebook, and this chapter has more printed outputs that don't match a real run than any chapter so far, so I'll flag each one as we go.

## Slide 2 — Where we are

Last chapter we produced a clean dataset in JSON lines. Today we turn that text into token IDs. Next chapter, those IDs become embedding vectors. Everything follows the chapter eight notebook, linked in the description.

## Slide 3 — Chapter 8 roadmap

Here's the plan. Why we tokenize at all. Then three strategies in rising sophistication: characters, words, and subwords with byte pair encoding. We'll train BPE ourselves, then use the real tools, then look at the quirks that affect prompts and costs. Finally we connect to chapter nine.

## Slide 4 — Key terms for this chapter

A few terms. A token is a unit of text with an ID. The vocabulary is every token the tokenizer knows. Encoding goes from text to IDs, decoding goes back. Special tokens mark structure: padding, unknown, beginning and end. BPE, byte pair encoding, learns subword pieces by merging the most frequent pair again and again. And the round trip test, decode of encode equals the original text, is the first thing to check on any tokenizer.

## Slide 5 — Part 1

Part one. Why tokenize?

## Slide 6 — Text in, numbers out (my redraw)

Models only process numbers. Back in chapter five, when we typed the secret to building AI is, GPT-2 actually received six integers. The tokenizer encodes text into those IDs, the embedding layer turns them into vectors, the transformer processes them, and the output is a probability for every token in the vocabulary. Then the tokenizer decodes the chosen ID back into text. It's the front door and the back door of every model.

## Slide 7 — Special tokens

Special tokens aren't words, they're structure. Unknown is the fallback. Beginning of sequence and end of sequence mark boundaries, and end of sequence is how a model signals that it's done generating. Padding fills short sequences so a batch has a rectangular shape. GPT-2 is a good real example: it uses a single token, end of text, ID fifty thousand two hundred and fifty six, for both beginning and end, and it has no padding token at all by default.

## Slide 8 — Part 2

Part two. The simplest possible tokenizer: one character, one token.

## Slide 9 — `CharTokenizer` (notebook cell 3)

Here's the character tokenizer from the notebook, trimmed of comments. Two dictionaries, one for each direction, so both lookups are instant. Fit takes the set of characters, which removes duplicates, and sorts it so the IDs are deterministic. Encode is a list comprehension that looks each character up. Decode joins the characters back with an empty string, because characters have no spaces between them.

## Slide 10 — Try it (notebook cell 5 — my run)

Fitting on hello world gives ten characters. Because we sorted them, space and punctuation come first: their Unicode code points are smaller than letters. Hello encodes to three, five, six, six, seven, and decodes back perfectly. One thing to notice: this encode has no fallback, so a character it never saw raises a key error. Production character tokenizers either include every byte or add an unknown token.

## Slide 11 — ⚠️ Book check: the tradeoff example

Here's the first book check. The notebook's sentence, tokenization is the first step in any language model, is fifty three characters with twenty two unique characters. The book prints fifty four and twenty four. The quick brown fox sentence later on is forty three characters with twenty eight unique ones, where the book says forty four and twenty. These are small slips, and the lesson is unchanged: at character level, every character is one token, so sequences get long fast.

## Slide 12 — Characters: pros and cons

Pros: a tiny vocabulary, no unknowns as long as every character was seen, and it's trivial to write. Cons: very long sequences, the model has to learn how letters form words, and more tokens means more compute, since attention grows with the square of the length. A three thousand character essay would be three thousand tokens, and GPT-2 can only see one thousand and twenty four.

## Slide 13 — Part 3

Part three. The other extreme: whole words as tokens.

## Slide 14 — `WordTokenizer.fit` (notebook cell 9, condensed)

The word tokenizer lowercases, splits on whitespace, and counts words. IDs zero to three are reserved for the special tokens. Then it keeps only the most frequent words, enough to fill the maximum vocabulary size, starting at ID four. Everything rarer will become unknown.

## Slide 15 — encode / decode with `<UNK>` (notebook cell 9)

Encoding uses dot get with a default of one, so an unknown word becomes the unknown token instead of crashing. Optionally we wrap the sequence in beginning and end tokens. Decoding looks up each ID, optionally skips the structural tokens, and joins with spaces. Notice the round trip is already lossy: we lowercased, and any unknown word is gone for good.

## Slide 16 — ⚠️ Book check: which words make the cut (cell 11)

Here's the real output on the cat, mat example with ten slots. The book shows mat before on, and dog as the last word in. In my run, on comes before mat, and was takes the last slot, not dog. Why? Was and dog each appear once, and Counter's most common breaks ties by first appearance, and was appears first. Also notice the token mat with a full stop attached: plain split doesn't separate punctuation, which is why the book suggests a regex like backslash b, backslash w plus, backslash b.

## Slide 17 — ⚠️ Book check: vocab size vs coverage (my run)

The next example in the book isn't in the notebook, so I ran it myself. With a vocabulary of ten, the book says three of the five test words are unknown. I get one. With only six word slots, learning and of come first because they appear twice, and the remaining slots go, by first appearance, to neural, networks, learn and from, which happen to be exactly our test words. Only data is unknown. The lesson: on a tiny corpus, the most frequent list is mostly tie breaking, so be careful drawing conclusions from it.

## Slide 18 — Characters vs words, side by side (cell 13 — my run)

Side by side on the quick brown fox. Characters: vocabulary twenty eight, sequence forty three. Words: vocabulary twelve, eight distinct words plus four special tokens, and a sequence of nine. Notice the repeats ID four for both thes, because we lowercased. Words are about five times shorter here. But a word vocabulary keeps growing with every new name, typo, number and language, and each entry costs a row in the embedding table we'll build in chapter nine. Neither extreme is right.

## Slide 19 — Part 4

Part four. Subwords and byte pair encoding, the middle ground every modern LLM uses.

## Slide 20 — Three ways to split "tokenization" (my redraw)

Here are the three strategies on one word. Character level gives twelve tokens. Word level gives one token, but only if tokenization is in a huge vocabulary, and otherwise it's unknown. Subword gives two meaningful pieces, token and ization, which I confirmed with GPT-4's tokenizer. A small side note: the book says tokenization is thirteen characters in one place and twelve in another. It's twelve.

## Slide 21 — The BPE idea

Byte pair encoding is beautifully simple. Start with single characters. Count every adjacent pair. Merge the most frequent pair into a single new token and add it to the vocabulary. Repeat until you reach your target vocabulary size. It was invented by Philip Gage in nineteen ninety four as a compression trick, and Sennrich and colleagues adapted it for machine translation in twenty fifteen. GPT-2 then made a byte level version of it standard.

## Slide 22 — BPE merges, step by step (my redraw)

Here's BPE on the book's toy corpus: low three times, lower once, newest twice. I computed this in code rather than by hand. Step one: l and o appear together four times, so they merge. Step two: lo plus w, also four times, gives low. Now every remaining pair appears twice, so there's a tie. My code picks the first pair it finds, n plus e. The book picks e plus s. Both are valid; real implementations need a deterministic tie break rule, and different libraries use different ones. After a few more merges, newest becomes one token while lower stays as low plus pieces.

## Slide 23 — Why BPE won

BPE won because it balances everything. Tens of thousands of pieces cover practically any text. A byte level version, like GPT-2's, can always fall back to raw bytes, so there are no true unknowns. Frequent words are a single token. And useful prefixes and suffixes emerge just from counting. There are close cousins: WordPiece in BERT, and the Unigram model in SentencePiece, used by T5. LLaMA one and two use SentencePiece's BPE mode.

## Slide 24 — Part 5

Part five. Let's train a real BPE tokenizer on Shakespeare.

## Slide 25 — Setup (notebook cells 17 & 21)

We use Hugging Face's tokenizers library, written in Rust. A BPE model, a whitespace pre tokenizer so merges never cross word boundaries, and a trainer with a vocabulary of one thousand, a minimum pair frequency of two, and our four special tokens. TinyShakespeare is just over one point one million characters, and training took four tenths of a second on my CPU.

## Slide 26 — ⚠️ Book check: the Hamlet line (cell 23 — my run)

Now the most important correction in this chapter. The book shows twelve tokens, with question as a single token, and says the round trip is perfect. In the actual run, question splits into que, st and ion, giving fourteen tokens. And the round trip is false: the decoded text has spaces before the comma and inside question. That's because the whitespace pre tokenizer throws away spacing information and no decoder was set. Which is exactly why GPT-2 uses byte level BPE that keeps the space inside the token. Always run the round trip test yourself.

## Slide 27 — Fixing the round trip (my code)

Here's my fix, my own code. Swap the whitespace pre tokenizer for a byte level one and set a matching byte level decoder. Now the space is stored inside the token, shown as a G with a dot in front of be, and decoding reproduces the text exactly. That's the GPT-2 approach, and because every byte is in the starting alphabet, no unknown token is ever needed.

## Slide 28 — Domain mismatch (cell 25 — my run)

Now modern text that Shakespeare never wrote. Twenty five tokens. Ing is a single token, because Shakespeare is full of ing words, and hat is a token, so Chat becomes C plus hat. But ChatGPT, neural and network shatter into fragments. The book's shorter version of this example prints fourteen tokens; my run gives eighteen. The lesson is right though: a tokenizer is only as good as the text it learned from.

## Slide 29 — ⚠️ Book check: what the vocabulary looks like (my run)

The book says the lowest IDs hold the most frequent characters, e, t, o, a. In a real run, the starting alphabet is simply sorted: punctuation, then capitals, then lowercase. Only the merged tokens after the alphabet are in the order they were learned. And the longest tokens aren't common English words; they're character names like Bolingbroke and Buckingham, because every speech in the play starts with the speaker's name in capitals. That's a nice data lesson from chapter seven: your formatting gets learned too.

## Slide 30 — Vocab size is a dial (my experiment)

I trained four BPE tokenizers on the same Shakespeare file with vocabularies of five hundred, one thousand, two thousand and five thousand, then tokenized the whole file. Characters per token rose from about two and a half to almost three point nine, and the token count fell from four hundred and forty eight thousand to two hundred and eighty nine thousand. Character level would be one character per token. Bigger vocabularies mean shorter sequences, at the cost of a bigger embedding table.

## Slide 31 — Save and load

A trained tokenizer is an artifact. Save it to JSON, load it back, and check the outputs match. My file was about sixty thousand bytes; the book's was thirty eight thousand, and the size depends on the library version and the exact merges. The key point: a model's embedding table is tied to one exact tokenizer. Lose or change it, and the model's IDs mean nothing.

## Slide 32 — Part 6

Part six. The production tokenizers you'll actually use.

## Slide 33 — tiktoken — GPT-4's `cl100k_base` (cells 27 & 29)

Tiktoken is OpenAI's tokenizer library. The cl100k base encoding is the one used by GPT-4 and GPT three point five turbo. Hello, world, how are you becomes eight tokens, and notice the spaces live at the start of tokens: space world, space how. The round trip is perfect, because it's byte level. Its vocabulary has one hundred thousand two hundred and seventy seven entries. Newer OpenAI models use a larger encoding called o two hundred k base.

## Slide 34 — ⚠️ Book check: token counts for prompts (cell 31)

The notebook counts tokens for three prompts. The real counts are seven, fifteen and ten. The book prints six, fourteen and nine, each one short. Haiku, for example, is two tokens. The same kind of slip appears in the comparison section: the Hamlet line is twelve tokens in GPT-4's tokenizer, not eleven, and the backpropagation sentence is nine, with backpropagation split into back, prop and agation. Ironically, the book's own advice is the right one: don't assume, measure.

## Slide 35 — Hugging Face `AutoTokenizer` — GPT-2 (cells 33 & 35)

Hugging Face's auto tokenizer loads the tokenizer that matches any model on the hub. For GPT-2, the same sentence splits into the same eight pieces, but the IDs are completely different, because each model has its own vocabulary. You also get an attention mask: one for real tokens, zero for padding. Here there's no padding, so it's all ones.

## Slide 36 — Vocabulary sizes in the wild

Here are some real vocabulary sizes. GPT-2 and GPT-3: fifty thousand two hundred and fifty seven. GPT-4's encoding: about one hundred thousand. GPT-4o: about two hundred thousand. BERT: thirty thousand five hundred and twenty two, with WordPiece. LLaMA one and two: thirty two thousand, and LLaMA three jumped to one hundred and twenty eight thousand. The trend is clear: bigger vocabularies, shorter sequences. I added the GPT-4o and LLaMA 3 rows myself.

## Slide 37 — Part 7

Part seven. Tokenizer quirks that affect prompts and costs.

## Slide 38 — Quirk 1: the leading space (cell 37, my redraw)

Quirk one: the leading space. Hello and space Hello are different tokens with different IDs, and the same for world. Because most words in running text follow a space, BPE learns the spaced version as the common token. So Translate colon Hello and Translate colon space Hello give the same number of tokens, but the model sees a different final token. Spacing in prompts is not cosmetic.

## Slide 39 — Quirk 2: numbers split (cell 39 — my run)

Quirk two: numbers. In cl100k, digits are grouped into chunks of at most three, so ten thousand becomes one hundred, then zero zero, and twenty twenty four becomes two zero two, then four. In my run, the answer is ten thousand in digits takes seven tokens, while spelling it out takes six. Splits like this are one reason models struggle with arithmetic: the same digit sits in different positions inside different tokens.

## Slide 40 — ⚠️ Book check: emoji (cell 41 — my run)

Quirk three, and another correction. The book says common emoji are single tokens and three fire emoji are three tokens. In my run, the smiley is two tokens, the rocket and thumbs up are three each, and three fire emoji are nine. An emoji is four bytes in UTF-8, and byte level BPE only merges the byte sequences it saw often enough. Interestingly, space smiley inside a sentence is one token, so context matters. The book also says hello smiley world is four tokens while listing three; three is right.

## Slide 41 — Quirk 4: other languages (my run)

Quirk four: other languages. Café is two tokens, naive with a diaeresis is three, the Japanese word for Japanese language is four, with the last character split into two byte pieces, and hello world in Russian is five tokens for two words. English gets roughly one token per word, while many other languages pay two or three times more. That means higher cost and less text in the context window, which is why multilingual models train multilingual tokenizers.

## Slide 42 — Part 8

Part eight. Connecting to chapter nine, then exercises and review.

## Slide 43 — Tokenize the Chapter 7 dataset (cell 43 — my run)

The notebook closes the loop with chapter seven. Each JSON lines record gets two new fields, its token IDs and its token count. Three examples average five point seven tokens. That's exactly the input chapter nine needs.

## Slide 44 — ⚠️ Book check: `nn.Embedding` arguments

One last book check, in the preview of chapter nine. The book creates an embedding layer with a keyword called vocab size. PyTorch doesn't have that keyword; I ran it and got a type error. The parameter is called num embeddings, or you can pass the numbers positionally. The result is a table of fifty thousand two hundred and fifty seven rows by seven hundred and sixty eight columns, about thirty eight point six million parameters, one row per token. That's the cost of vocabulary size made concrete.

## Slide 45 — Exercises (my answers)

Some answers to the exercises, from my own runs. Exercise one: the sentence has twenty three distinct characters and eighty two characters total; the word tokenizer has thirteen entries including the four special tokens and a sequence of nine words, with no unknowns since it was fit on the same text, and note tokenization keeps its full stop. Exercise three: estimate cost as input tokens plus maximum output tokens, times the current price. Exercise four: the leading space changes the ID for every word, and for rarer words it can change the count too. Exercise five: English is usually cheapest.

## Slide 46 — Key takeaways

Key takeaways. Tokenization is a reversible mapping, so always test the round trip. The core tradeoff is vocabulary size against sequence length. BPE merges the most frequent pair over and over. Byte level BPE keeps spaces inside tokens, so it's lossless and never needs an unknown token. Tokenizers depend on their training data. And quirks with spaces, numbers, emoji and languages change token counts, so measure rather than assume.

## Slide 47 — Notebook run & book check

The notebook ran completely on my CPU once tiktoken was installed. The corrections are summarised here, and they're all in the errata file in the repo. None of them change the ideas in the chapter, but they do change the numbers you'll see on your screen, and now you know why.

## Slide 48 — Review questions

Pause and try these. The tradeoff, with numbers. When unknown and padding are used. BPE in your own words. Why the leading space changes the ID. Why digits can cost more than words. Which tokenizer to use for a Chinese chatbot. And, from our own run, why the Shakespeare tokenizer's round trip failed.

## Slide 49 — Practice this

To practise: run the notebook in Colab and compare every output with the book. Fix the round trip with a byte level pre tokenizer and decoder. Train at different vocabulary sizes. And tokenize your chapter seven dataset with two different tokenizers and compare the counts.

## Slide 50 — Up next: Chapter 9

Next time, chapter nine: embeddings, where those token IDs become vectors that carry meaning.

## Slide 51 — Credits

This video is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams here are my own, but the book goes deeper, with exercises, appendices and the full text, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. Thanks for watching, and see you in chapter nine.

