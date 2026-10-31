# M03 · snippet 04 — the real GPT-2 tokenizer (pip install tiktoken)
import tiktoken

enc = tiktoken.get_encoding("gpt2")
for s in ["cat", " cat", "The cat sat on the mat", "tokenization", "😀", "Hello 😀 world"]:
    ids = enc.encode(s)
    print(f"{s!r:26} -> {len(ids):2} tokens {ids} {[enc.decode([i]) for i in ids]}")
