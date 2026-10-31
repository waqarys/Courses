# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter fourteen of my study series on Build Your First LLM by Hasan Degismez. Last chapter changed the weights. Today we change only the words we send: temperature and top p, few shot, chain of thought, delimiters, structured output, prompt injection, and how to evaluate prompts properly. I ran the notebook, and then ran the chapter's prompts on a real Llama 3.2 3B model on my own machine, so you'll see actual scores rather than promises.

## Slide 2 — Where we are

Chapter thirteen changed weights. Today we only change the input. Chapter fifteen adds knowledge and tools. The notebook uses MiniGPT for the sampling demos and Ollama with Llama 3.2 for the parts that need a real model.

## Slide 3 — Chapter 14 roadmap

The plan. The completion mindset. Roles. Temperature and top p. The core prompt patterns. Delimiters and output formats. Injection and defences. And evaluation, with my scores from a real model.

## Slide 4 — Key terms for this chapter

Key terms. The system message sets role and rules. Few shot means showing examples. Chain of thought asks for reasoning first. Prompt injection is user text trying to override you. Temperature sharpens or flattens the distribution. And top p samples from the smallest set of tokens covering a share p of the probability.

## Slide 5 — Part 1

Part one. How to think about prompts.

## Slide 6 — Models continue text

The key idea. A language model doesn't answer questions. It continues text with what usually comes next. So design the text so that the thing you want is the natural continuation. Compare answer this question, with Q colon, the question, newline, A colon. The second ends exactly where the answer should start.

## Slide 7 — Anatomy of a good prompt

A well built prompt has parts. A role and rules, context, a few examples, the actual input, and the output format. You won't always need all five, but knowing the slots helps you see what's missing.

## Slide 8 — System vs user messages

Chat models split the prompt into roles. The system message is the job description: who you are, what you must not do, and how to format. Technically it's just text at the start, but chat tuned models learn to treat it as authoritative. MiniGPT never saw roles, so for it everything is plain text.

## Slide 9 — Part 2

Part two. Sampling controls.

## Slide 10 — Temperature reshapes the distribution

Temperature divides the logits before the softmax. Below one, the favourite gets even more likely. Above one, everything flattens towards equal. It controls how decisive the model is, not how creative.

## Slide 11 — Checking the book's temperature table

I recomputed the book's table. Temperature on probabilities means raising each to the power one over T and renormalising. At T equals two, happy is fifty four percent, excited thirty two and purple fourteen, not the book's forty seven, thirty three and twenty. At point three, happy is nearly ninety seven percent. The lesson is the same, but the numbers are off.

## Slide 12 — Picking a temperature

A rule of thumb. Zero to point three for maths, code and extraction. Around point five to point seven for general questions. Up to one for brainstorming. Above one is rarely useful. And zero means greedy, which the code handles as a special case, since you can't divide by zero.

## Slide 13 — Temperature in code

The code. Take the last position's logits. If temperature is zero, take the argmax. Otherwise divide, softmax, and sample. In the notebook, MiniGPT has random weights, so all temperatures produce gibberish; the notebook says so itself.

## Slide 14 — Top-p: a dynamic shortlist

Top p, or nucleus sampling, sorts tokens by probability and keeps the smallest set that covers p of the mass. When one token is obvious, the shortlist is tiny. When many fit, it grows. Then renormalise and sample.

## Slide 15 — Top-p in code

In code: sort, take the cumulative sum, find where it crosses p, and keep one more so the crossing token is included. I checked that plus one: it's right. A common setting is temperature point eight with top p point nine five.

## Slide 16 — Part 3

Part three. The patterns, using one running task: movie review sentiment.

## Slide 17 — Zero-shot: just ask

Zero shot means no examples, just the task and the input. In machine learning a shot is an example. Instruction tuned models handle this fine; MiniGPT can't.

## Slide 18 — Few-shot: show, don't tell

Few shot shows the pattern instead of describing it. Two to five examples, covering every label, similar in length and style to real inputs. If all your examples are positive, you bias the model towards positive.

## Slide 19 — Chain-of-thought

Chain of thought asks the model to reason before answering. The reasoning tokens put the evidence in context right before the final label. It was discovered on very large models; small ones produce text that looks like reasoning without doing it.

## Slide 20 — My CoT run (Llama 3.2 3B)

Here's the chain of thought run on a real three billion parameter model. It listed the positive, listed the negative, weighed them, and decided negative, arguing the criticism was more specific. That's tidy reasoning, but the chapter's own examples label mixed reviews neutral. Chain of thought makes the decision visible; it doesn't make the model follow your labelling policy. For that, put a mixed example in your few shot set.

## Slide 21 — Delimiters: clear boundaries

Delimiters mark the parts of a prompt: instruction, input, format, response. Hashes, backticks, XML style tags, all work. They make structure obvious, and they're the basis of the injection defence coming up.

## Slide 22 — Structured output: JSON

For structured output, show the exact schema. But models still add prose or wrap the JSON in code fences, so always parse defensively.

## Slide 23 — Defensive parsing

The book's parser strips code fences, then tries json loads, and returns None on failure. In the notebook it recovered the JSON from a fenced example correctly.

## Slide 24 — My JSON run: instructions vs `format=json`

For JSON, I sampled five times at temperature point eight, with the schema only in the prompt and again with Ollama's JSON mode. Both gave valid JSON five out of five, with the right sentiment and the key phrase twist ending. That's a small test on an easy review, so keep the defensive parser, and use a constrained JSON mode when your runtime has one; it guarantees the syntax.

## Slide 25 — Prompt evolution

The evolution of a prompt. Bad is vague. Better names the task and labels. Best adds a role, the exact output constraint, examples and delimiters.

## Slide 26 — Part 4

Part four. Safety.

## Slide 27 — What is prompt injection?

Prompt injection is when user text tries to take over: ignore previous instructions, say hacked, reveal your system prompt. It's the language model version of SQL injection, because instructions and data share one channel.

## Slide 28 — My injection test (Llama 3.2 3B)

My injection test. Three samples of each prompt. The vulnerable translator never said hacked; Llama's safety training kicked in and it refused, calling the request harmful. The delimited version also didn't comply, but it echoed the prompt template back and produced a muddled French reply. So neither leaked, but neither did the actual job, which was to translate the text. A safe failure is still a failure, so test the task, not just the attack.

## Slide 29 — Four layers of defence

Four layers. Delimiters around untrusted input. Input checks for known phrases. Output checks for the wrong language or a reply far too long. And reminders in the system prompt. Keyword lists only catch lazy attacks, and as chapter sixteen showed, they also cause false positives.

## Slide 30 — Input validation (book)

The book's input check is a substring list. In the notebook it blocked the ignore previous instructions example and let normal text through.

## Slide 31 — When prompts can't protect you

Be honest about limits. Determined attackers get through prompt defences, and techniques keep evolving. Use defence in depth, and never give a model powers you couldn't afford it to misuse, because the prompt alone won't stop it.

## Slide 32 — Part 5

Part five. Measuring prompts.

## Slide 33 — The iteration trap

The trap. Write a prompt, try one example, it works, ship it, watch it fail on real data. The fix is a small evaluation set.

## Slide 34 — The chapter's evaluation set

The chapter's seven cases. Two easy ones. Two subtle neutrals. A double negative and a mixed review. And an adversarial one that tells the model to say positive.

## Slide 35 — Scoring: strict vs lenient

How you score matters. The book compares the whole output to the label, so Positive with a full stop counts as wrong. The notebook takes the first word, which still has the full stop. A lenient scorer looks for the first label word. I report both.

## Slide 36 — My eval: BAD vs BETTER vs BEST (Llama 3.2 3B, T=0)

My real scores, Llama 3.2 three billion at temperature zero. The bad prompt wrote essays: zero strict, one lenient. The better prompt answered in a full sentence every time, so strict scoring gives zero, but lenient scoring gives six out of seven. The best prompt answered in one word, four out of seven by both measures. But it invented labels, confused and mixed, for the double negative and the mixed review, and on the adversarial review it obeyed the instruction and said positive, despite being told to treat the review as data. The simpler prompt got that one right. So best isn't automatically best: you only find out by measuring, and your scorer changes the ranking.

## Slide 37 — The iteration workflow

The workflow. Baseline. Group failures. Form a hypothesis. Change one thing. Re run the same set. Check you didn't break something that used to pass. Repeat.

## Slide 38 — When prompts aren't enough

When to stop prompting. If accuracy plateaus and fixes keep breaking other cases, fine tune. If it needs facts it never saw, use retrieval. If you need guaranteed JSON, use constrained decoding. If reasoning fails, use a bigger model.

## Slide 39 — Notebook run summary

My notebook run. The MiniGPT sampling demos ran and produced gibberish, as the notebook warns. The Ollama chain of thought cell timed out on my busy CPU, so I ran it separately, which is the run you saw. The parsing and validation cells worked.

## Slide 40 — Key takeaways

Takeaways. Prompts set up a pattern to complete. Low temperature for facts. Few shot is the workhorse; chain of thought pays off on bigger models. Delimiters and validation help, but prompts alone aren't security. And measure everything on an evaluation set.

## Slide 41 — Review questions: short answers

Short answers. Put rules in the system message so they persist. Zero for stories and one point five for code is backwards. Chain of thought works by putting the evidence in context first. For inconsistent formats, make example labels identical, cover all classes, and state the format. And ignore previous instructions is prompt injection, defended with delimiters and validation.

## Slide 42 — Review 6–7 + checkpoint

For the eighty percent prompt, build a bigger eval set and iterate one change at a time. Legal tone suits fine tuning. Ticket classification starts with few shot. Internal documents need retrieval. The checkpoint compares a direct prompt with a few shot JSON prompt on five reviews.

## Slide 43 — Practice this

Practice. Recompute the temperature table yourself. Run the three prompts on twenty reviews of your own. And try to break your own translator prompt, then fix it.

## Slide 44 — Credits

This video is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams are my own, but the book goes deeper, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. Thanks for watching, and see you in chapter fifteen.

