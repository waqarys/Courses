# M07 · snippet 01 — data: download, char-tokenize, split, batch
import os, urllib.request, torch

URL = "https://www.gutenberg.org/cache/epub/1661/pg1661.txt"   # Sherlock Holmes (public domain)
if not os.path.exists("book.txt"):
    urllib.request.urlretrieve(URL, "book.txt")
text = open("book.txt", encoding="utf-8").read()
start, end = text.find("*** START"), text.find("*** END")      # strip Gutenberg licence boilerplate
text = text[text.find("\n", start) + 1:end] if start != -1 else text

chars = sorted(set(text))
stoi = {c: i for i, c in enumerate(chars)}
itos = {i: c for c, i in stoi.items()}
encode = lambda s: [stoi[c] for c in s]
decode = lambda ids: "".join(itos[i] for i in ids)

data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data))
train_data, val_data = data[:n], data[n:]

def get_batch(split, block=128, batch=32):
    d = train_data if split == "train" else val_data
    ix = torch.randint(len(d) - block - 1, (batch,))
    x = torch.stack([d[i:i + block] for i in ix])
    y = torch.stack([d[i + 1:i + 1 + block] for i in ix])       # shifted by one
    return x, y

if __name__ == "__main__":
    print(f"{len(text):,} chars, vocab {len(chars)}, train {len(train_data):,} / val {len(val_data):,}")
    x, y = get_batch("train", block=12, batch=1)
    print(repr(decode(x[0].tolist())), "->", repr(decode(y[0].tolist())))
