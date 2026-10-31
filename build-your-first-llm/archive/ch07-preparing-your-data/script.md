# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter seven of my study series on Build Your First LLM by Hasan Degismez. Part three begins, and it begins not with the model but with the data. Garbage in, garbage out is truer for language models than for almost anything else. Today we build a complete data pipeline: clean, deduplicate, split, chunk and store. I ran the book's chapter seven notebook, and I also pushed three real public domain novels through the same pipeline to see what happens on real text. And I found a couple of mistakes in the book's worked example.

## Slide 2 — Where we are

In part two we learned Python, tensors and the training loop. Today we produce a clean dataset in JSON lines format. In chapter eight we tokenize it, and from there we embed it, model it and train on it. Everything follows the chapter seven notebook, which is linked in the description.

## Slide 3 — Chapter 7 roadmap

Here's the roadmap. Why quality matters. Where to get text you're allowed to use. Five new Python tools: files, sets, JSON, regular expressions and hashing. Then the pipeline itself: cleaning, deduplication, splitting without leakage, chunking, storage and quality checks. Then my experiment with three real novels, and the review.

## Slide 4 — Key terms for this chapter

The vocabulary. A corpus is the collection of text you train on. Splits divide it into training, validation and test sets. Data leakage is when evaluation data sneaks into training, making scores look better than they are. Deduplication removes repeated text. A chunk is a piece of long text sized to fit the model. The context window is the maximum number of tokens the model can see at once. And JSON lines stores one JSON object per line.

## Slide 5 — Part 1

Part one. Why data quality rules everything.

## Slide 6 — Junk in, junk out

Language models happily memorise whatever you give them: typos, navigation menus, licence boilerplate, spam. Cleaning your data is the cheapest accuracy boost there is. The book's analogy is cooking: fresh ingredients and a good recipe beat a fancy stove with rotten produce. The pipeline goes raw text, clean, deduplicate, split, chunk, and store as JSON lines. And because each stage inherits the problems of the one before, check the data after every stage.

## Slide 7 — Sourcing text: ethics & licensing

Where do you get text? You don't need billions of tokens to learn the pipeline. A few megabytes is plenty. Use public domain books like Project Gutenberg, permissively licensed text, documentation, or your own writing. Avoid personal data, sensitive records, and giant scraped dumps, where you inherit every mess and every legal risk. And keep a small README recording where each text came from and its licence. For my experiment I used three H. G. Wells novels from Project Gutenberg, which are public domain in the United States.

## Slide 8 — Part 2

Part two. Five new Python tools.

## Slide 9 — Files, sets, JSON

Three of the tools. Files: open with a with block, which closes the file automatically even if something crashes, and always pass encoding utf eight. Sets: they store only unique items, and checking whether something is in a set is instant, while a list checks item by item. That matters when you ask have I seen this before thousands of times. JSON: dumps converts a dictionary to a string, and ensure ascii equals false keeps characters like Chinese or emoji readable instead of escaping them. JSON lines puts one record per line, so you can stream a huge file without loading it all.

## Slide 10 — Regex and hashing

Regular expressions describe patterns. Less than, then one or more characters that aren't greater than, then greater than, matches any HTML tag. Backslash s plus matches any run of whitespace. And hashing gives a short fingerprint of any text. The same input always gives the same hash, and a tiny change gives a completely different one. I checked the book's SHA-1 values for hello and world, and they're correct. For deduplication we compare forty character fingerprints instead of eight hundred character chunks.

## Slide 11 — ⚠️ Book check: SHA-1 collision odds

One correction. The book says SHA-1's collision risk is roughly one in two to the power one sixty. That's the size of the output space, but the birthday paradox means collisions become likely after about two to the power eighty hashes, not one sixty. And SHA-1 is cryptographically broken: researchers produced a deliberate collision in 2017. For removing accidental duplicates from a small corpus, the book's conclusion still holds: SHA-1 is fine. But if anyone could craft inputs against you, use SHA-256.

## Slide 12 — Part 3

Part three. Cleaning and normalising.

## Slide 13 — `clean_text` (notebook)

Here's the cleaning function. First, NFKC Unicode normalisation, which converts compatibility characters to standard forms: the fi ligature becomes two letters, full width digits become normal digits, and the ellipsis character becomes three dots, which you can see in the notebook's output. Accented letters like é stay as they are. Then strip HTML tags, turn tabs and carriage returns into spaces, and collapse runs of whitespace. Notice the smart quotes survive. NFKC doesn't straighten them.

## Slide 14 — Decisions to make

A few policy decisions. Lowercasing shrinks the vocabulary but loses information, for example US the country versus us the pronoun. Either choice is fine if you're consistent. Keep punctuation, because models learn sentence structure from it. Keep emoji and non-Latin scripts only if you'll support them. And always look at the text before and after cleaning to make sure nothing important vanished.

## Slide 15 — Part 4

Part four. Deduplication and filtering.

## Slide 16 — Dedup by hash (notebook)

Models memorise duplicates instead of learning patterns, so remove them early. Hash every chunk, keep a set of hashes you've seen, and keep only first occurrences. continue skips to the next loop iteration. The notebook goes from four documents to three. Then filter: drop chunks that are very short, under forty characters, or very long, over two thousand, and optionally run a language or content check.

## Slide 17 — Exact vs near duplicates

One limitation to keep in mind. Hashing only catches exact duplicates. The cat sat full stop and the cat sat exclamation mark get completely different hashes. Large scale pipelines use near duplicate detection, like MinHash with locality sensitive hashing, or n-gram overlap. A cheap trick is to clean and normalise before hashing, which turns many near duplicates into exact ones. That's why cleaning comes first.

## Slide 18 — Part 5

Part five. Splits without leakage.

## Slide 19 — Split by document, with a seed

Splits measure how well the model generalises to text it hasn't seen. The rules: split by whole document, not by paragraph; eighty, ten, ten is typical; and set a seed so the split is reproducible. The function copies the list, shuffles it with a fixed seed, and slices it. Leakage example: if chapter one of a book is in training and chapter two is in validation, the model already knows the author's style and characters, and the validation score looks better than it really is. Keep whole documents together.

## Slide 20 — ⚠️ Book check: the worked example's split

And here's a real bug in the book's worked example. It splits three documents with train at point three four and validation at point three three, and claims one document in each split. But int of three times point three three is int of point nine nine, which is zero. So validation is empty, and test gets two documents. The book's own notebook prints exactly that: train one, validation zero, test two. The same example also says the bird flew over the house has length thirty three, but it's twenty nine characters. The lesson: int truncates, so for tiny data sets compute split sizes with round, or guarantee at least one item per split.

## Slide 21 — Part 6

Part six. Chunking for the context window.

## Slide 22 — Overlapping chunks

Transformers have a fixed context window, so long text must be cut into chunks. The function takes windows of eight hundred characters, and advances by eight hundred minus the overlap of two hundred, a stride of six hundred, so neighbouring chunks share two hundred characters. The rule of thumb is about four characters per token for English, so eight hundred characters is roughly two hundred tokens, leaving room inside a five hundred and twelve token window.

## Slide 23 — Overlap, visualised (my redraw)

Here's the overlap visualised. Chunk one is zero to eight hundred, chunk two six hundred to fourteen hundred, chunk three twelve hundred to two thousand. A sentence near position seven hundred appears whole in chunk two. One side effect the book doesn't mention: with two thousand characters, the loop makes a fourth chunk from eighteen hundred to two thousand, which is entirely contained in chunk three. That's a small duplicate. You can stop the loop once a chunk reaches the end of the text.

## Slide 24 — Store as JSONL + quality checks

Store the result as JSON lines, with fields for the text, its source, its split, and optionally its length. Then run quality checks on every split: counts, average and maximum lengths, the most common words, and a few random samples read by a human. Red flags include HTML words like div or href among the top words, a duplicate rate above five percent, a maximum length many times the average, and the replacement character that signals an encoding problem. And always deduplicate before splitting, otherwise the same chunk can land in both train and test.

## Slide 25 — The notebook's end-to-end walkthrough

Here's the notebook's complete walkthrough, as it actually printed on my run. Four raw documents, two of them identical once the HTML is removed. Cleaning normalises the tab and the extra spaces. Deduplication leaves three. The split gives one, zero and two, as we just saw. The single training document becomes one chunk, and the JSON record has a length of twenty four. The book's printed version shows a different, impossible split, so always trust the run over the page.

## Slide 26 — Sanity checks after every stage (notebook)

The notebook includes a sanity check function that prints the count, average, maximum and minimum length of the chunks, plus a sample. On the toy corpus it found four chunks, average sixty three characters, no HTML leakage, and it warned that one chunk is shorter than ten characters. That's exactly the kind of thing you want to catch before training, not after. Run it after every stage.

## Slide 27 — Duplicate rate and top words (notebook)

Two more quick checks. The duplicate rate is one minus unique hashes over total hashes. And top words just counts the most frequent lowercase words. If markup words like div or href show up, cleaning isn't done. On the Time Machine, the top words were the, and, then I, at fifteen hundred and thirty eight, and of. The capital I ranks third because the story is told by a first person narrator. Top words tell you about your corpus, not just about bugs.

## Slide 28 — Dedup **before** split — why order matters

Let's stress the ordering rule, because it's the most common pipeline mistake. If you split first and deduplicate afterwards within each split, a paragraph that appears twice can land once in train and once in test. Then the model has literally seen the test answer, and the test score lies. On web scale data, boilerplate repeats thousands of times, so this matters enormously. The order is clean, deduplicate, split, then chunk.

## Slide 29 — A provenance README (example)

And here's what a provenance README might look like: each file, its author, its source with the Gutenberg number, its licence status, and a one line summary of how it was processed. It takes two minutes to write, and future you, or anyone reviewing your model, will be grateful.

## Slide 30 — Part 7

Part seven. A real book experiment.

## Slide 31 — Three Wells novels through the pipeline (my experiment)

I ran three public domain novels through the same steps. First I stripped Project Gutenberg's licence header and footer, which is about ten percent of each file. Pure boilerplate you don't want the model to memorise. Then I split into paragraphs, cleaned them, deduplicated, filtered and chunked. The duplicate rate was only zero point three eight percent: things like the one word line Well, in quotes, which appears seven times, and by H. G. Wells three times. But three hundred and thirty eight paragraphs were shorter than forty characters, mostly short lines of dialogue. The book's length filter drops all of them, which for fiction may be throwing away good data. Filters are policy decisions, not universal truths.

## Slide 32 — Is "4 chars ≈ 1 token" right? (my experiment)

Is the four characters per token rule right? I ran GPT-2's real tokenizer over The Time Machine. The answer is four point three characters per token, so the rule holds well for English prose. The eight hundred character chunks came out between a hundred and eight and two hundred and forty six tokens, averaging a hundred and eighty seven, all comfortably inside a five hundred and twelve token window. Victorian prose with long words and dialogue gives a fair amount of spread.

## Slide 33 — Part 8

Part eight. Wrapping up.

## Slide 34 — Exercises (my answers)

My answers to the exercises. Hash detective: a duplicated paragraph gives an identical SHA-1, and with a set each check is instant. Splitter check with seed one twenty three and twelve documents: int of nine point six is nine for training, int of one point two is one for validation, and the remaining two go to test. A rerun gives exactly the same split. Chunk reality, three thousand characters with eight hundred and two hundred: chunks start at zero, six hundred, twelve hundred, eighteen hundred and twenty four hundred, so five chunks, with the last one six hundred characters long. And the end of chapter exercises, the full pipeline, the statistics and the casing comparison, are what I did with the Wells novels.

## Slide 35 — Key takeaways

The key takeaways. Data quality is the cheapest accuracy boost you can buy. Use text you're allowed to use, and record where it came from. Clean it, deduplicate before splitting, and split by whole documents. Chunk with overlap, remembering about four characters per token, four point three in my measurement. And store it as JSON lines, with sanity checks after every stage.

## Slide 36 — Notebook run & book check

My notebook run and book check. The chapter seven notebook ran end to end on a CPU, all eleven code cells, no errors. Three errata: the worked example's split is one, zero, two rather than one, one, one, which the notebook itself confirms. The bird sentence is twenty nine characters, not thirty three. And the SHA-1 collision odds are overstated. Plus one note: the chunking loop can produce a redundant final chunk.

## Slide 37 — Review questions

The review questions, with my answers. One: lowercasing shrinks the vocabulary and merges variants, but loses names and acronyms. Keep case when they matter, or when you want natural looking generated text. Two: deduplication prevents memorisation and wasted compute, and stops inflated evaluation when duplicates cross splits. Three: a hash is a fixed length fingerprint, and SHA-1 is fine for accidental duplicates at small scale, though not against an adversary. Four: split by document because text from the same document is correlated, which would leak into validation. Five: overlap ensures text near a boundary appears whole in at least one chunk. Six: JSON lines is streamable, greppable and appendable, with one record per line.

## Slide 38 — Practice this

Your practice list. Run the chapter seven notebook, and fix the worked example's split so every set gets at least one document. Download a Gutenberg book, strip its header and footer, and run the full pipeline. Measure characters per token on your own text. Compare the top fifty words with and without lowercasing. And keep your train dot jsonl, because chapter eight tokenizes it.

## Slide 39 — Up next: Chapter 8

That's chapter seven. We now have clean, deduplicated, well split text chunks. In chapter eight, we turn those strings into token IDs, building byte pair encoding from scratch and comparing it to production tokenizers.

## Slide 40 — Credits

This video is based on the book Build Your First LLM by Hasan Degismez. Everything here is my own adaptation for study, so please support the author and buy the book at leanpub dot com slash First LLM. The code shown comes from the companion repository at github dot com slash First LLM slash code, under the MIT license, and the novels came from Project Gutenberg. Thanks for watching, and see you in chapter eight.

