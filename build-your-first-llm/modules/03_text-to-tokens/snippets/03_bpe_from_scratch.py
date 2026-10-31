# M03 · snippet 03 — byte-pair encoding from scratch: merge the most common pair, repeat
from collections import Counter

corpus = "the cat sat on the mat the cat ate then the cat sat there"
words = [list(w) + ["_"] for w in corpus.split()]   # "_" marks end of word

def pair_counts(words):
    c = Counter()
    for w in words:
        for a, b in zip(w, w[1:]):
            c[(a, b)] += 1
    return c

def merge(words, pair):
    out = []
    for w in words:
        i, new = 0, []
        while i < len(w):
            if i < len(w) - 1 and (w[i], w[i + 1]) == pair:
                new.append(w[i] + w[i + 1]); i += 2
            else:
                new.append(w[i]); i += 1
        out.append(new)
    return out

for step in range(8):
    pair, freq = pair_counts(words).most_common(1)[0]
    words = merge(words, pair)
    print(f"merge {step + 1}: {pair[0]!r}+{pair[1]!r} (x{freq})")

print([" ".join(w) for w in words[:6]])
