# M03 · snippet 02 — character vs word tokenizers
text = "tokens are the bricks models build with"

chars = sorted(set(text))
stoi = {c: i for i, c in enumerate(chars)}
itos = {i: c for c, i in stoi.items()}
ids = [stoi[c] for c in text]
print("char vocab", len(chars), "| sequence length", len(ids))
assert "".join(itos[i] for i in ids) == text        # lossless round trip

words = sorted(set(text.split()))
wtoi = {"<unk>": 0, **{w: i + 1 for i, w in enumerate(words)}}
new = "models build tokenizers"
print("word vocab", len(wtoi), "| encode:", [wtoi.get(w, 0) for w in new.split()])  # unknown -> 0
