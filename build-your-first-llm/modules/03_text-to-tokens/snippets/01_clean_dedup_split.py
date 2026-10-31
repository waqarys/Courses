# M03 · snippet 01 — clean, deduplicate, split (and CHECK the sizes)
import hashlib, random, re

docs = [
    "The  river   flows to the sea.",
    "Stars are   far away suns.",
    "The river flows to the sea.",          # duplicate after cleaning
    "Bread rises because yeast makes gas.",
    "Cats sleep for most of the day.",
]

def clean(t):
    return re.sub(r"\s+", " ", t).strip()

def dedup(items):
    seen, out = set(), []
    for t in items:
        h = hashlib.sha1(t.lower().encode()).hexdigest()   # fingerprint, not security
        if h not in seen:
            seen.add(h); out.append(t)
    return out

docs = dedup([clean(d) for d in docs])
random.seed(42); random.shuffle(docs)
n = len(docs); n_train = int(0.8 * n); n_val = int(0.1 * n)
train, val, test = docs[:n_train], docs[n_train:n_train + n_val], docs[n_train + n_val:]
print(f"{n} docs -> train {len(train)} / val {len(val)} / test {len(test)}")
