# M09 · snippet 01 — temperature / top-k / top-p on GPT-2. pip install transformers
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

tok = GPT2TokenizerFast.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2").eval()
prompt = "My favourite thing about learning to code is"
ids = tok(prompt, return_tensors="pt").input_ids

with torch.no_grad():
    logits = model(ids).logits[0, -1]
for t in (0.2, 0.8, 1.5):
    p = (logits / t).softmax(-1)
    top = p.topk(5)
    print(f"T={t}: " + ", ".join(f"{tok.decode([i])!r} {v:.2f}" for v, i in zip(top.values, top.indices)))

for t in (0.2, 0.8, 1.5):
    torch.manual_seed(0)
    out = model.generate(ids, do_sample=True, temperature=t, top_p=0.9, top_k=50,
                         max_new_tokens=25, pad_token_id=tok.eos_token_id)
    print(f"\n--- T={t}\n" + tok.decode(out[0][ids.shape[1]:]))
