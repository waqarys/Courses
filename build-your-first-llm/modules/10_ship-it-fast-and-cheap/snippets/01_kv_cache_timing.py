# M10 · snippet 01 — KV cache on vs off
import time, torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

tok = GPT2TokenizerFast.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2").eval()
ids = tok("Serving a language model is like running a kitchen because", return_tensors="pt").input_ids

for cache in (True, False):
    t = time.perf_counter()
    out = model.generate(ids, max_new_tokens=100, do_sample=False, use_cache=cache, pad_token_id=tok.eos_token_id)
    print(f"use_cache={cache}: {time.perf_counter() - t:.2f}s")
print(tok.decode(out[0][ids.shape[1]:])[:120])
