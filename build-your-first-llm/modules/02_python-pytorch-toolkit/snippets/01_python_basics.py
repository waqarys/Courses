# M02 · snippet 01 — five Python moves we use all course
sentence = "Large language models predict the next token"
print(f"{sentence!r} has {len(sentence)} characters (spaces count!)")

words = sentence.lower().split()
lengths = [len(w) for w in words]                 # list comprehension
print(words, lengths)

vocab = {w: i for i, w in enumerate(sorted(set(words)))}   # word -> id
print(vocab)

def encode(text):
    return [vocab[w] for w in text.lower().split()]

class Tokenizer:
    def __init__(self, vocab):
        self.vocab = vocab
        self.inverse = {i: w for w, i in vocab.items()}
    def encode(self, text):
        return [self.vocab[w] for w in text.lower().split()]
    def decode(self, ids):
        return " ".join(self.inverse[i] for i in ids)

tok = Tokenizer(vocab)
ids = tok.encode("predict the next token")
print(ids, "->", tok.decode(ids))
