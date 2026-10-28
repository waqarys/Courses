# My own solutions to Ch 5 exercises (not from the book repo)
import json, string
class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {"<PAD>": 0, "<UNK>": 1}; self.id_to_word = {0: "<PAD>", 1: "<UNK>"}
    @staticmethod
    def _clean(text):                      # Exercise 1
        return text.lower().translate(str.maketrans("", "", string.punctuation)).split()
    def fit(self, texts):
        for t in texts:
            for w in self._clean(t):
                if w not in self.word_to_id:
                    i = len(self.word_to_id); self.word_to_id[w] = i; self.id_to_word[i] = w
    def encode(self, text): return [self.word_to_id.get(w, 1) for w in self._clean(text)]
    def decode(self, ids): return " ".join(self.id_to_word.get(i, "<UNK>") for i in ids)
    def count_unknowns(self, sentences):   # Exercise 2
        return sum(self.encode(s).count(1) for s in sentences)
    def save(self, path):                  # Exercise 3
        json.dump(self.word_to_id, open(path, "w"))
    @classmethod
    def load(cls, path):
        t = cls(); t.word_to_id = json.load(open(path))
        t.id_to_word = {i: w for w, i in t.word_to_id.items()}; return t
