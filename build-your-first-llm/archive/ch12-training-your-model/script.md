# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter twelve of my study series on Build Your First LLM by Hasan Degismez. This is the chapter where our hand built MiniGPT finally learns something. We cover the next token objective, cross entropy, data loaders, the five step training loop, validation, perplexity, checkpoints and sampling. I ran the notebook on a CPU for the full three epochs, and the numbers I got are very different from the book's. I'll show you why: a padding bug hiding in one argument, and a data pipeline that wastes a lot of compute. Then I'll show a fixed version and how much better it trains.

## Slide 2 — Where we are

So far we have a tokenizer, embeddings, attention and a complete MiniGPT, but every weight is random. Today we train it on Shakespeare. Next chapter we fine tune. Everything follows the chapter twelve notebook.

## Slide 3 — Chapter 12 roadmap

Here's the plan. Training as a feedback loop. The objective. Cross entropy and the ignore index. The data pipeline. The five step recipe with warmup and clipping. Validation, overfitting and perplexity. Checkpoints and generation. Then my run against the book, the bug, and a better pipeline. Then exercises and review.

## Slide 4 — Key terms for this chapter

Some terms. Cross entropy is minus the log of the probability given to the right token. The learning rate is the step size. Warmup ramps it up gently. An epoch is one pass over the data. Perplexity is e to the loss. Overfitting is when training loss falls but validation loss rises. And a checkpoint saves everything you need to resume.

## Slide 5 — Part 1

Part one. What training actually is.

## Slide 6 — Learning = closing a loop

The book uses a nice engineering framing, which I've redrawn here. The target is the true next token. The error signal is the loss. The controller is the optimizer, AdamW. Its action is a weight update, and the plant output is the model's new predictions, which we compare with the targets again. Measure, adjust, repeat, thousands of times.

## Slide 7 — Part 2

Part two. What exactly are we asking the model to do?

## Slide 8 — One sequence, many examples

Take one sequence of six tokens. Drop the last token to get the inputs, and drop the first to get the targets. Now every position has a job: predict the next token. Six tokens give five training examples in one forward pass. And because of the causal mask from chapter ten, position two can only see positions zero to two, so asking it for token three is a fair question.

## Slide 9 — The label-shifting helper

Here's the book's helper. Slice the inputs, slice and clone the targets, then replace padding with minus one hundred, which cross entropy ignores by default. Notice that the default padding id is zero. Hold on to that, because it comes back to bite us in part eight.

## Slide 10 — Part 3

Part three. How we score a prediction.

## Slide 11 — Cross-entropy = −ln p(correct)

Cross entropy looks only at the probability the model gave the correct token, and takes minus its log. Ninety percent gives a loss of about point one. Ten percent gives two point three. One percent gives four point six. A brand new model that spreads probability evenly over fifty thousand tokens scores about ten point eight, which is why a loss stuck near ten or eleven means nothing has been learned.

## Slide 12 — Flattening for `F.cross_entropy`

PyTorch's cross entropy wants a two D table of scores and a one D list of correct classes, so we flatten batch and time together. The targets use reshape rather than view, because slicing off the first column leaves a tensor that isn't contiguous in memory.

## Slide 13 — Before training: noise

Before any training, here's what my random model wrote after "The fair maiden". Pure noise. Every token is about equally likely, so whichever one happens to score highest wins. That's our starting point.

## Slide 14 — Part 4

Part four. Getting data into the model.

## Slide 15 — TinyShakespeare

The data is TinyShakespeare, about one point one million characters. With the GPT-2 tokenizer that's about three hundred and thirty eight thousand tokens. The dataset class cuts the raw text into fixed size chunks. Note that the chunks are measured in characters, not tokens. That matters later.

## Slide 16 — The collate function

The collate function turns a list of strings into a padded tensor. It tokenises them, truncates at one hundred and twenty eight tokens and pads each batch to its longest member. GPT-2 has no padding token, so the notebook borrows the end of text token. Its id is fifty thousand two hundred and fifty six, not zero.

## Slide 17 — Batch vs epoch

A batch is the group processed together for one update. An epoch is one pass over everything. The book's arithmetic example says ten thousand examples give about three hundred and twelve batches. But the actual notebook, with two hundred and fifty six character chunks, has three thousand nine hundred and twenty one training chunks, so one epoch is only one hundred and twenty three batches. And the book's printed training output also shows three hundred and twelve, which doesn't match its own code.

## Slide 18 — The DataLoader

A seeded ninety ten split, a partial to bind the tokenizer into the collate function, and data loaders that shuffle the training set but not the validation set. Standard and sensible.

## Slide 19 — Part 5

Part five. The heart of the chapter.

## Slide 20 — The 5-step recipe

Every neural network trains with the same five steps. Zero the gradients, because PyTorch accumulates them. Run the forward pass. Compute the loss. Backpropagate. Optionally clip the gradients. Then let the optimizer step, and advance the learning rate scheduler. Repeat for every batch.

## Slide 21 — Learning rate and warmup

The learning rate is the step size. Too big and you overshoot, too small and it takes forever. Warmup starts tiny because early gradients from random weights aren't trustworthy. The notebook uses AdamW at three e minus four, with a hundred warmup steps and a linear decay. One thing I noticed: with only a hundred and twenty three steps per epoch, warmup takes up most of the first epoch.

## Slide 22 — Gradient clipping

Gradient clipping is a safety limiter. If the overall gradient norm is bigger than one, the whole gradient is scaled down, so one bad batch can't wreck the weights. It has to happen after backward, when the gradients exist, and before the optimizer step.

## Slide 23 — `train_epoch`, in the notebook

Here's the training function, condensed. It's the five step recipe exactly, after calling model dot train. But look at the loss: ignore index zero, with a comment saying padding is token id zero. We just saw that the padding id is fifty thousand two hundred and fifty six. I'll come back to this.

## Slide 24 — Part 6

Part six. Is it learning, or memorising?

## Slide 25 — Reading loss curves

Always watch training and validation loss together. If both fall, you're healthy. If training keeps falling but validation turns upward, the model is memorising, which is overfitting. If both stay high, the model is underfitting: too small, too little training or a bug.

## Slide 26 — Perplexity = e^loss

Perplexity is e to the validation loss, and you can read it as how many equally likely tokens the model is torn between. Ten point eight means guessing across the whole vocabulary. Six means it has learned word frequencies, around four hundred. Four and a half is ninety. And it's only fair to compare perplexities that use the same tokenizer and the same data.

## Slide 27 — Evaluation and early stopping

Evaluation runs without gradients and with dropout off. It sums the loss and divides by the number of counted tokens to get average loss and perplexity. Early stopping halts training when validation loss has risen several epochs in a row. With only three epochs, the book's patience of three can never actually trigger.

## Slide 28 — Part 7

Part seven. Saving and sampling.

## Slide 29 — What goes in a checkpoint

A checkpoint needs more than the weights. AdamW keeps two running averages for every parameter, and the scheduler knows where it is in the warmup and decay. Save all of it, and keep the checkpoint with the best validation loss.

## Slide 30 — Sampling with temperature

Generation now samples instead of always picking the top token. Divide the last position's logits by a temperature, softmax, and draw one token. Below one sharpens the distribution. Above one flattens it. As temperature goes to zero you get greedy decoding back. Chapter fourteen goes deeper with top k and top p.

## Slide 31 — Part 8

Part eight. What actually happened when I ran it.

## Slide 32 — The book's printed result vs my run

Here's the book's printed run next to mine, same notebook, same seed, on a CPU. The parameter count is sixteen million, not ten point eight. One epoch is a hundred and twenty three batches, not three hundred and twelve. My validation loss went six point two two, five point six six, five point five one, ending at a perplexity of two hundred and forty six. The book prints three point seven five and forty two. That's a big gap, and the perplexity table from part six tells us what it means: my model has learned word frequencies and some line structure, nothing like a perplexity of forty two.

## Slide 33 — What it wrote after 3 epochs

And here's what it actually wrote after three epochs, for "to be or not to be". It has learned the shape of a play: short lines, speaker tags in capitals, thee, thy and hath. But these aren't sentences. The book shows the king is a man of great virtue and honour, which my run is nowhere near. The notebook's own closing message says training makes all the difference. It does, but three epochs on this setup isn't enough to get there.

## Slide 34 — Bug 1: `ignore_index=0` ignores the wrong token

Here's the first bug. Ignore index zero doesn't ignore padding, because in GPT-2 token zero is the exclamation mark, a real character, about point six percent of the text. Meanwhile the real padding token, fifty thousand two hundred and fifty six, is counted in the loss. Batches are padded to about a hundred tokens when the average chunk is about seventy eight. I counted: twenty two percent of all target positions are padding that the model is scored on. The fix is to mask using the attention mask, or the real pad id, and set those targets to minus one hundred.

## Slide 35 — Bug 2 (design): short, padded, character chunks

The second issue is design rather than a bug. Chunks are measured in characters, so they're only about seventy eight tokens long, less than the model's hundred and twenty eight. Every batch needs padding. And three epochs is only three hundred and sixty nine weight updates, a hundred of which are warmup. A better pipeline tokenises the whole text once and samples random hundred and twenty eight token windows, which needs no padding at all.

## Slide 36 — My fix: stream training, same model, same lr

Here's my fix: the same sixteen million parameter model, same learning rate and warmup, but trained on random hundred and twenty eight token windows from the token stream, with no padding at all. The two curves overlap early, which is reassuring. At step three fifty, mine was at five point three seven, against the notebook's five point five one after three sixty nine steps, and my metric counts every token, with no padding to make it easier. Running on to twelve hundred steps reached a validation loss of four point eight seven, a perplexity of about a hundred and thirty, roughly half the notebook's. Still nowhere near the book's forty two. It took about an hour and a half on a shared CPU.

## Slide 37 — Stream model samples

And here's what that model writes when prompted with King Henry. It answers with Queen Margaret, a real character from the history plays, uses line breaks, thou and my lord, and sounds roughly like Shakespeare. But it makes no sense. That's honestly what a perplexity of a hundred and thirty looks like on a small model trained for an hour on a CPU.

## Slide 38 — Why the book's 42 is suspicious

Why do I doubt the book's perplexity of forty two? Three hundred and thirty eight thousand tokens, sixteen million parameters, and only three hundred and sixty nine small updates. Neither the notebook nor my better pipeline gets anywhere near that, and the printed sample about a man of great virtue and honour reads like an illustration rather than a logged run. The lesson: trust your own logs, and always check what your ignore index actually points at.

## Slide 39 — Part 9

Part nine. Practice.

## Slide 40 — Exercises, worked

Quick notes on the exercises. A custom dataset smaller than about a megabyte overfits quickly, so watch the validation curve. In the learning rate sweep, one e minus five barely moves, three e minus four is healthy, and one e minus two tends to spike. Low temperature loops, high temperature is soup. For resuming, reload the optimizer and scheduler too. Early stopping needs more epochs than its patience. And the perplexity improvement is one minus final over first.

## Slide 41 — Review questions: short answers

Short answers. The five steps, as we've seen. Without shifting, the model can see the answer and learns to copy. Ignore index skips positions, but only if it points at the right id. Ten thousand over thirty two is three hundred and twelve point five, so three hundred and thirteen batches including the last partial one, or one thousand five hundred and sixty five updates over five epochs. And saving only weights resets the optimizer and the schedule.

## Slide 42 — Practice this

Your practice: run the notebook, change the ignore index to the real pad id, and compare. Log loss every few steps, not just every epoch. And try the stream sampler from my notes for a thousand steps.

## Slide 43 — Credits

This video is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams are my own, but the book goes deeper, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. Thanks for watching, and see you in chapter thirteen.

