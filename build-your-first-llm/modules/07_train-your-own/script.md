# M07 — Train Your Own Tiny GPT on a Laptop

Target length: **17 min** · Segments: 7
Big idea: *Training is hiking downhill in fog: you can only feel the slope under your feet (the gradient), so you take small steps (learning rate), warm up slowly, and check a map you didn't train on (validation) to know you're not lost.*

## S1 · CAM · Hook (≈40s)
- Last time we borrowed GPT-2's brain. Today we grow our own — from random noise to something that writes.
- On a normal laptop CPU, in about ten minutes.
- It won't be ChatGPT. But you'll watch the loss fall and the gibberish turn into words, and you'll understand every line.

## S2 · SLIDES · What "learning" means here (≈2.5 min)
- Slide: the training sample. Take a chunk of text, shift it by one. Input "hello worl", target "ello world".
- Every position is a mini-exam: predict the next character.
- Loss = cross-entropy = how surprised the model was by the right answer. Low surprise, low loss.
- Sanity number: at the start, a random model with vocab V should have loss about the natural log of V. Our Sherlock Holmes text has 88 distinct characters, so about 4.48. If your first loss is way off, something's wrong — I once saw 84 here, because I'd forgotten the small-weight initialisation from Module 6.
- Perplexity = e to the loss. "How many choices was it effectively torn between?"

## S3 · SLIDES · The training recipe (≈2.5 min)
- AdamW optimiser — gradient descent with momentum and per-parameter step sizes, plus weight decay.
- Learning-rate schedule: warm up for a few hundred steps, then decay with a cosine curve. Fog-hiking: small first steps, then stride, then slow down near the valley.
- Gradient clipping at 1.0 — stops one bad batch from launching you off a cliff.
- Validation every N steps: if train loss falls but validation rises, you're memorising — overfitting.
- Save checkpoints. Training that crashes at 90 percent with no checkpoint is the saddest thing in ML.

## S4 · IDE · The data loader (≈2.5 min)
- Snippet 01. Download a public-domain book — we use a Project Gutenberg text.
- Character tokenizer — fine for a tiny model.
- 90/10 train/val split by position.
- get_batch: random start positions, slice x and y shifted by one. Print a sample pair to prove the shift.

## S5 · IDE · The training loop, live (≈4 min)
- Snippet 02. Our GPT class from Module 6 with a tiny config: 4 layers, width 128, 4 heads, context 128.
- Check initial loss ≈ 4.5 — ln 88. ✔.
- The loop: get batch, forward, loss, zero grad, backward, clip, step, schedule.
- Every 100 steps, estimate train and val loss, and print a sample.
- Let it run — I'll speed this part up in the edit. Watch the samples: step 0 noise, step 300 spaces and short words, step 1500 word-like lines with punctuation.
- Saved checkpoint: tiny_gpt.pt.

## S6 · SLIDES · Reading the curves (≈1.5 min)
- Three shapes. Both falling: keep going. Val rising: overfitting — more data, dropout, or stop early. Spiky or NaN: learning rate too high.
- Compare with Module 1's bigram toy — this model uses 128 characters of context, not one word.

## S7 · CAM · Recap (≈40s)
- Shift-by-one targets, cross-entropy, AdamW, warmup + cosine, clip, validate, checkpoint.
- Next: fine-tuning — teaching a pre-trained model a new job with very little data.
