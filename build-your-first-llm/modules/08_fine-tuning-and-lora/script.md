# M08 — Fine-Tuning: Teaching a Smart Model a New Job (with LoRA)

Target length: **16 min** · Segments: 7
Big idea: *Pre-training is a general education; fine-tuning is a short job-training course. LoRA is doing that course with sticky notes on the textbook instead of rewriting the textbook.*

## S1 · CAM · Hook (≈40s)
- Training GPT-2 from scratch cost real money. You and I don't have a data centre.
- But we can take a model that already knows English and teach it a new habit — answer in a format, follow instructions, speak like our brand — in minutes.
- And with LoRA we train less than one percent of the weights.

## S2 · SLIDES · Three ways to adapt a model (≈2.5 min)
- Prompting: just ask nicely. Zero training. Module 9.
- Full fine-tuning: keep training all weights on your data. Powerful, but heavy — you need memory for every weight's gradient and optimiser state, and you can wreck what it knew — "catastrophic forgetting".
- Parameter-efficient fine-tuning: freeze the original, train a small add-on. LoRA is the famous one.
- Rule of thumb: try prompting first, then LoRA, and full fine-tuning only if you must.

## S3 · SLIDES · Instruction tuning: the format is the lesson (≈2 min)
- A base model completes text. Ask it a question and it may just write more questions.
- Instruction tuning shows it thousands of examples shaped like: Instruction, Response.
- It learns the pattern: after "### Response:" comes a helpful answer, then stop.
- Trick: compute the loss only on the response tokens, so it learns to answer, not to write prompts.

## S4 · SLIDES · LoRA: sticky notes on the textbook (≈2.5 min)
- A weight matrix W is 768 by 2304 — about 1.8 million numbers.
- LoRA says: the change we need is simple. Write it as B times A, where A is 768 by 8 and B is 8 by 2304. That's about 25 thousand numbers.
- W stays frozen. Output = W x plus a scale times B A x.
- B starts at zero, so on step one the model is exactly the original. No damage at the start.
- After training you can merge the sticky note into W, or keep several notes and swap them per task.

## S5 · IDE · LoRA from scratch on GPT-2 (≈4 min)
- Snippet 01: the LoRA wrapper class — 15 lines.
- Snippet 02: load GPT-2, freeze everything, wrap every attention c_attn with LoRA.
- Print trainable parameters: about 295 thousand of 124 million — roughly a quarter of a percent.
- Our dataset: twenty tiny instruction pairs about our channel's style — "Explain X in one line with an analogy".
- Mask the prompt part of the labels with minus 100 so the loss ignores it.
- Before training: ask a question — it rambles. Train 60 steps on CPU. Ask again — it answers in our one-line format.

## S6 · SLIDES · When fine-tuning goes wrong (≈1.5 min)
- Too few examples, too many epochs: it memorises and repeats training answers.
- Learning rate too high: forgetting — general skills degrade.
- Messy data: it learns the mess. Ten clean examples beat a hundred noisy ones.
- Always keep a small held-out set and eyeball outputs before and after.

## S7 · CAM · Recap (≈40s)
- Prompt first, LoRA next, full fine-tune last.
- Instruction format + loss on responses only.
- LoRA = frozen W + tiny B·A, B starts at zero.
- Next: prompt engineering and building real apps on top of LLMs.
