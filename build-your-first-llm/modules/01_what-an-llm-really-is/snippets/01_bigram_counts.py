# M01 · snippet 01 — the dumbest language model: count which word follows which
from collections import Counter, defaultdict

text = "the cat sat on the mat . the cat ate the fish . the dog sat on the cat ."
words = text.split()

follows = defaultdict(Counter)          # follows["the"] -> Counter({"cat": 3, ...})
for current, nxt in zip(words, words[1:]):
    follows[current][nxt] += 1

for w in ["the", "sat", "cat"]:
    total = sum(follows[w].values())
    probs = {n: round(c / total, 2) for n, c in follows[w].most_common()}
    print(f"after {w!r:6} ->", probs)
