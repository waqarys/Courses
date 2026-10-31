# M01 — What an LLM Really Is (and what it isn't)

Target length: **12 min** · Segments: 6 · Scenes used: CAM, SLIDES, IDE
Big idea: *An LLM is a very well-read autocomplete that predicts one token at a time — everything else is engineering around that loop.*

Reading rules for the teleprompter: one beat = one breath. Pause one second between beats. If you fumble, pause 2 s and re-read the beat — CapCut "remove silences" + the jump is invisible under the webcam circle.

## S1 · CAM · Hook (≈45s)
- Open your phone keyboard and type "I'll be there in five…"
- It suggests "minutes". That is a language model. A tiny one.
- Now imagine that keyboard read a big slice of the public internet, every manual, every forum.
- And instead of three suggestions, it keeps going — word after word — until it has written an essay.
- That's ChatGPT, Grok, Claude, Llama. Same trick, gigantic scale.
- In this series we build one ourselves, in plain Python, on a laptop.
- I'm Waqar, this is Waqar Shaikh Builds. Let's start with what an LLM really is.

## S2 · SLIDES · The ladder: AI → ML → deep learning → LLM (≈2 min)
- Slide: the ladder. Think of nested boxes.
- AI is the biggest box: any machine behaviour we'd call smart. Even a chess program from the 90s.
- Machine learning is the box inside: instead of writing rules, we show examples and let the machine find the rules.
- Spam filter example: you don't list every spam word. You show ten thousand emails labelled spam / not spam.
- Deep learning is ML with many stacked layers of simple maths units — "neurons" — that learn features by themselves.
- And an LLM is deep learning pointed at one task: guess the next piece of text.
- Next slide: why "large"? Billions of adjustable numbers — parameters — and trillions of training tokens.
- GPT-2 small, the model we'll rebuild, has about 124 million. Modern frontier models are reported in the hundreds of billions.

## S3 · SLIDES · The one loop that runs everything (≈3 min)
- Slide: the loop. Text in → tokens → model → probabilities → pick one → append → repeat.
- Step one: chop text into tokens. A token is a chunk — often a word, sometimes part of a word, sometimes a space plus a word.
- Step two: each token becomes a list of numbers. Coordinates in a "meaning map". Module 4 is all about that.
- Step three: the model mixes information between tokens — that's attention, Module 5.
- Step four: out comes a score for every token in its vocabulary. Fifty thousand scores for GPT-2.
- Step five: turn scores into probabilities and pick one. Pick the top one every time and it gets boring and repetitive. Sample a bit and it gets creative.
- Step six: glue it on the end and go again.
- That's it. A "conversation" is this loop with your message pasted in front.
- Slide: what that means — no memory between chats unless the app re-sends history, and no fact database, just patterns.

## S4 · IDE · See next-token prediction with your own eyes (≈3 min)
- Switch to IntelliJ. File: m01_next_token.py. Paste snippet 01.
- We're not training anything yet — we're building the dumbest possible language model: counting.
- Read the snippet: we count which word follows which word in a tiny text.
- Run it. Look — after "the", it predicts "cat" or "mat" by how often each followed.
- Now snippet 02: we let it generate. Start with "the" and loop.
- Run. It babbles: "the cat sat on the mat the cat…". Grammar-ish, meaning-free.
- That is a bigram model. An LLM does the same job, but it looks at the whole context, not just the last word, and it learns smarter statistics than raw counts.
- Keep this file. In Module 7 our trained transformer will beat it, and we'll compare.

## S5 · SLIDES · What LLMs are bad at — and why (≈2 min)
- Slide: four honest limits.
- One: hallucination. The loop always produces a fluent next token — even when it doesn't "know". Fluent ≠ true.
- Two: counting letters and arithmetic. It sees tokens, not letters. "strawberry" may be two or three chunks.
- Three: knowledge cutoff. It only knows its training data, unless an app feeds it fresh text — Module 9, retrieval.
- Four: context limit. It can only look at a fixed window of tokens at once.
- Each limit falls out of the loop we just drew. Once you understand the loop, the weirdness stops being mysterious.

## S6 · CAM · Recap + what's next (≈45s)
- Recap: LLM = next-token predictor + scale.
- Tokens in, probabilities out, sample, repeat.
- Our bigram toy already does the loop — badly.
- Next module: the Python and PyTorch toolkit you need — only the 20 percent we'll actually use.
- Exercises and code are linked in the description. Try exercise 2 before the next video.
- See you in Module 2.
