# Narration script — Build Your First LLM

One block per slide, in order. Generated from the `say:` notes in slides.md.

## Slide 1 — Build Your First LLM

Welcome to chapter thirteen of my study series on Build Your First LLM by Hasan Degismez. Today we turn a generalist model into a specialist: instruction data, loss masking, and LoRA adapters built from scratch. I ran the notebook, found why it can't show any improvement, and then ran the same recipe on a properly pretrained GPT-2 with a real held-out test set, so you can see what fine-tuning actually does.

## Slide 2 — Where we are

Chapter twelve was pretraining: predict the next token of raw text. Today is fine-tuning: teach the model to answer in a specific way using question and answer pairs. Chapter fourteen gets better behaviour without touching the weights at all.

## Slide 3 — Chapter 13 roadmap

The plan. When to fine tune at all. How to shape the data. Loss masking. LoRA, from the maths to the code. How to evaluate. How to ship adapters. And then my two runs: the notebook as written, and a fixed version on GPT-2.

## Slide 4 — Key terms for this chapter

Key terms. Supervised fine tuning trains on input and output pairs. Loss masking grades only the answer. LoRA learns a small low rank change next to frozen weights. An adapter is a small trainable add on. The rank is the width of LoRA's bottleneck. And freezing means a weight never updates.

## Slide 5 — Part 1

Part one. Do you even need to fine tune?

## Slide 6 — Generalist vs specialist

A pretrained model is a generalist. It knows language but hasn't mastered any job. Ask a Shakespeare model about your refund policy and you get thee and thou. You have two levers. Give it better instructions, which is prompting, or show it many examples of the right behaviour, which is fine tuning.

## Slide 7 — When each one wins

Prompting wins for simple, varied tasks, when you have no examples and need results today. Fine tuning wins when you need the same format and vocabulary every time, on one high volume task, and you have at least a hundred good examples.

## Slide 8 — My decision rule (from the book's idea)

The rule of thumb. Try five to ten prompt variations first. Then ask three questions. Do I have a hundred or more correct examples? Must the model use specific terms every time? Is the task far from what the base model saw? Two or more yeses, fine tune. Otherwise keep working on the prompt.

## Slide 9 — The cost trade-off

Cost. Prompting is fast and free to set up, but long instructions cost tokens on every single request. Fine tuning costs compute once, then prompts stay short. At high volume that can win. The hidden cost is that every fine tune is a new artifact to store, version and deploy.

## Slide 10 — Part 2

Part two. The data.

## Slide 11 — From raw text to instruction pairs

In chapter seven a record was just text. Now each record is an instruction and the ideal response. Pretraining is like reading the whole textbook; fine tuning is drilling flashcards.

## Slide 12 — The TechStartup FAQ dataset

The dataset is an FAQ for a fictional company called TechStartup. The book says eighty training examples and twenty test examples. The notebook actually has sixty nine, and it takes the first eighty for training, which is all of them. So the test set is empty, and that breaks evaluation later. Keep that in mind.

## Slide 13 — JSONL: one example per line

JSON lines stores one JSON object per line. You can stream it, append to it and diff it. Saving is a loop of json dumps; loading reads each line back.

## Slide 14 — Quality over quantity

In fine tuning, each example is seen many times, so errors get amplified. One wrong answer becomes a habit. Check that answers are accurate, use consistent terms, never contradict each other, cover varied phrasings, and contain nothing unsafe. If one record says Amsterdam and another says Berlin, the model learns confusion.

## Slide 15 — Part 3

Part three. Loss masking.

## Slide 16 — Why not train on every token?

In chapter twelve every position was graded. For question answer data, that means grading the model on predicting the words of the question itself, which teaches nothing useful and even encourages it to parrot the question. We only care about producing the answer.

## Slide 17 — Loss masking: grade only the answer

Here's the idea. The prompt tokens, from the instruction marker to the closing marker, get the label minus one hundred. Only the answer tokens are graded. Like a teacher who doesn't mark you for copying the question correctly.

## Slide 18 — Building the labels

In code: format the prompt with the markers, tokenize prompt plus response, tokenize the prompt alone to find where the answer starts, then set everything before that to minus one hundred. In the notebook, one example had a hundred and fifteen masked positions and only thirteen trained ones, because the padding is masked too.

## Slide 19 — The masked loss

The loss is chapter twelve's shifted cross entropy with ignore index minus one hundred. The training loop is the same five steps. One tip the chapter skips: put an end of text token after each answer, so the model learns when to stop. My GPT-2 run does that.

## Slide 20 — Part 4

Part four. LoRA.

## Slide 21 — The efficiency problem

Full fine tuning needs gradients and optimizer state for every weight, and you ship a full copy of the model for every task. At billions of weights that's impractical. And updating everything risks catastrophic forgetting, where the new task overwrites the old skills.

## Slide 22 — The LoRA idea

LoRA's insight is that the change a fine tune needs is low rank. So freeze the big matrix W and learn a thin correction made of two small matrices, scaled by alpha over r. On a two fifty six square layer with rank eight, that's four thousand ninety six trainable numbers instead of sixty five thousand. Sixteen times fewer.

## Slide 23 — Counting parameters honestly

The book's headline is forty eight times. That's true for a seven sixty eight square layer. MiniGPT's real attention projection goes from two fifty six to seven sixty eight, which gives twenty four times. The notebook's demo layer gives sixteen. The ratio depends on the shape, so don't quote forty eight as a property of LoRA.

## Slide 24 — Scale = α / r

The scale is alpha divided by rank. Alpha is a volume knob for the adapter. Dividing by rank means that if you try a different rank, the update size stays roughly the same, so you don't need to retune the learning rate. Rank eight with alpha sixteen gives a scale of two.

## Slide 25 — The LoRALinear layer (book)

Here's the book's layer. A frozen base linear layer, two small matrices, and a scale. One matrix gets a small random start; the other starts at zero, so the adapter adds exactly nothing at step zero and training grows the correction from there.

## Slide 26 — Naming gotcha: A and B are swapped

A naming gotcha. The book calls the down projection B and the up projection A. The original paper and Hugging Face's PEFT library do the opposite: A is down and starts random, B is up and starts at zero. The maths is the same, but if you ever load or compare PEFT weights, the names are reversed. The notebook shows lora B as two fifty six by eight.

## Slide 27 — Freeze, then inject

Injecting LoRA: freeze every parameter, then in every block replace the combined query key value projection with a LoRA version that copies the old weights into its frozen base. Only the new small matrices can learn.

## Slide 28 — Does it "primarily affect Q and V"?

The book says adapting the fused projection primarily affects queries and values. It doesn't. One adapter on the fused output can change queries, keys and values equally. If you want only Q and V, split the projection or mask the key slice. The paper's finding was about which matrices you choose to adapt.

## Slide 29 — Notebook: trainable parameters

In the notebook, thirty two thousand seven hundred and sixty eight parameters are trainable out of sixteen million, which is zero point two percent. The book prints a different pair of numbers from an older configuration. Either way only a fifth of a percent of the model learns.

## Slide 30 — QLoRA in one line

QLoRA keeps the frozen base in four bit precision and trains LoRA on top, which is how people fine tune seven billion parameter models on one consumer GPU. It's the same idea plus quantisation, using bitsandbytes and PEFT.

## Slide 31 — Part 5

Part five. Did it work?

## Slide 32 — Simple metrics

Three checks. Exact match, which is strict. Word overlap, the share of expected words that show up. And actually reading the outputs, because numbers can hide nonsense. All on held out questions the model never trained on.

## Slide 33 — A gotcha in the eval code

The book's evaluation calls model dot generate with Hugging Face style arguments. MiniGPT doesn't have that method. You need a small greedy loop: take the argmax, append it, stop at end of text. And set seeds before both training and evaluation.

## Slide 34 — Notebook run: what actually happens

Here's my notebook run. The base model is randomly initialised, so it knows nothing. Loss moved from ten point eight six to ten point seven four, about one percent. Outputs were gibberish before and after. And because the test set is empty, the evaluation cell divides by zero. LoRA can't teach language to a random model; it can only nudge one that already knows it.

## Slide 35 — Notebook: adapter file size

The part that does work in the notebook: file size. The adapter is a hundred and thirty two kilobytes, the full model sixty one megabytes, four hundred and seventy eight times bigger. The book's numbers come from an older configuration, but the point stands.

## Slide 36 — My fix: the same recipe on a real base

So I ran the same recipe properly. A pretrained GPT-2 small, LoRA rank eight alpha sixteen on every attention projection, the book's sixty nine FAQ examples shuffled into fifty five for training and fourteen held out, with loss masking and an end of text token.

## Slide 37 — My GPT-2 + LoRA results

Here are my numbers. Training loss fell from three point one five to point seven three over twelve epochs. On the fourteen held out questions, exact match stayed at zero, and word overlap rose from five percent to eighteen and a half. On questions it trained on, overlap was fifty three percent, with three of fourteen word perfect. Only a quarter of a percent of GPT-2's weights trained, and the adapter is about one megabyte. So the book's fifty percent exact match isn't realistic for unseen questions: with sixty nine examples, the model learns the style, not facts it never saw.

## Slide 38 — What the held-out answers look like

Reading the answers tells the real story. Where are you based: Amsterdam, correct, because other training answers mention it, though it repeats itself. Customer service: it invents an email address and a phone number. Uptime: a vague non answer instead of ninety nine point nine percent. The fine tune learned the company's voice and answer format perfectly, but facts it never saw get made up. Fine tuning teaches behaviour; for facts, use retrieval, which is chapter fifteen.

## Slide 39 — Part 6

Part six. Shipping.

## Slide 40 — Save and load only the adapter

Save only the parameters whose names contain lora. To use it, build the same model, add the same LoRA structure, and load with strict equals false, because the base weights aren't in the adapter file. Remember the base must be the same pretrained weights you trained against.

## Slide 41 — Merge or keep separate?

Keep adapters separate if you want to swap tasks like apps. Merge if you want one simple file and slightly faster inference, accepting that it's permanent. Merging is just adding the scaled product into W, transposed for the linear layer's layout.

## Slide 42 — Key takeaways

Takeaways. Prompt first, fine tune when you have the data and a clear need. Loss masking grades only the answer. LoRA trains a tiny low rank update on frozen weights. And the lesson from my runs: fine tuning only works on a pretrained base, and you only know it worked with a real held out test set.

## Slide 43 — Review questions: short answers

Short answers. Two hundred examples and a fixed format: fine tune, after trying prompts. Masking stops wasted signal. LoRA works because task changes are low rank, though bigger shifts may need more rank. Freezing prevents forgetting. And ten thousand noisy examples can be worse than a hundred clean ones.

## Slide 44 — Checkpoint exercise (fixed)

The checkpoint, fixed. Load trained weights first. Shuffle and split the data so the test set isn't empty. Rank eight, end of text on answers, a greedy evaluation loop. Report exact match, overlap, three before and after pairs and the adapter size.

## Slide 45 — Practice this

Practice. Sweep the rank and plot overlap against parameters. Train once without masking and see if it parrots the questions. And train a second adapter for another domain and swap between them.

## Slide 46 — Credits

This video is based on Build Your First LLM by Hasan Degismez. The explanations and diagrams are my own, but the book goes deeper, so please support the author and buy it at leanpub dot com slash First LLM. The code is on GitHub at First LLM slash code, under the MIT licence. Thanks for watching, and see you in chapter fourteen.

