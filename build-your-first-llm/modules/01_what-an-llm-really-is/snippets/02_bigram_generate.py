# M01 · snippet 02 — run the loop: predict, pick, append, repeat
import random
from collections import Counter, defaultdict

text = "the cat sat on the mat . the cat ate the fish . the dog sat on the cat ."
words = text.split()
follows = defaultdict(Counter)
for a, b in zip(words, words[1:]):
    follows[a][b] += 1

def next_word(word, greedy=False):
    options = follows[word]
    if greedy:
        return options.most_common(1)[0][0]          # always the top choice
    choices, weights = zip(*options.items())
    return random.choices(choices, weights=weights)[0]  # sample by frequency

random.seed(0)
for mode in (True, False):
    out = ["the"]
    for _ in range(12):
        out.append(next_word(out[-1], greedy=mode))
    print("greedy " if mode else "sampled", " ".join(out))
