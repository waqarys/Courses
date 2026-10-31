# M08 · snippet 02 — instruction-tune GPT-2 with LoRA on CPU (~3-5 min). pip install transformers
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from lora import LoRA                                   # snippet 01 saved as lora.py

torch.manual_seed(0)
tok = GPT2TokenizerFast.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
for p in model.parameters():
    p.requires_grad = False
for block in model.transformer.h:                       # GPT-2 c_attn is Conv1D: weight (768, 2304)
    block.attn.c_attn = LoRA(block.attn.c_attn, 768, 2304)
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
total = sum(p.numel() for p in model.parameters())
print(f"trainable {trainable:,} of {total:,} ({100 * trainable / total:.2f}%)")

pairs = [
    ("a tokenizer", "A tokenizer is a LEGO sorter: it snaps text into reusable bricks."),
    ("an embedding", "An embedding is a GPS pin for a word on a map of meaning."),
    ("attention", "Attention is a group chat where each word reads the messages it needs."),
    ("a residual connection", "A residual is a note in the margin so the original page is never erased."),
    ("LayerNorm", "LayerNorm is a deep breath that calms every token's numbers before thinking."),
    ("the learning rate", "The learning rate is your stride length when hiking downhill in fog."),
    ("overfitting", "Overfitting is memorising last year's exam instead of learning the subject."),
    ("LoRA", "LoRA is a sticky note on the textbook instead of rewriting the whole book."),
    ("a GPU", "A GPU is a stadium of tiny calculators all working at the same moment."),
    ("a context window", "A context window is the size of the desk the model can spread papers on."),
    ("temperature", "Temperature is the spice knob: low is plain and safe, high is bold and risky."),
    ("a vector database", "A vector database is a library shelved by meaning instead of by title."),
]
fmt = lambda q: f"### Instruction: Explain {q} in one line with an analogy.\n### Response:"

def example(q, a):
    p, full = tok.encode(fmt(q)), tok.encode(fmt(q) + " " + a + tok.eos_token)
    labels = [-100] * len(p) + full[len(p):]               # loss on the response only
    return torch.tensor([full]), torch.tensor([labels])

def ask(q):
    ids = tok(fmt(q), return_tensors="pt").input_ids
    out = model.generate(ids, max_new_tokens=30, do_sample=False, pad_token_id=tok.eos_token_id)
    return tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True).strip()

print("BEFORE:", ask("a checkpoint"))
opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=2e-3)
model.train()
for step in range(60):
    x, y = example(*pairs[step % len(pairs)])
    loss = model(input_ids=x, labels=y).loss
    opt.zero_grad(); loss.backward(); opt.step()
    if step % 12 == 0:
        print(f"step {step} loss {loss.item():.3f}")
model.eval()
print("AFTER :", ask("a checkpoint"))
