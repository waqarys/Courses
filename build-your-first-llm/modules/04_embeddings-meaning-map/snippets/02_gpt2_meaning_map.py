# M04 · snippet 02 — explore GPT-2's real embedding table
# pip install transformers  (downloads ~500 MB once)
import torch, torch.nn.functional as F
from transformers import GPT2Model, GPT2TokenizerFast

tok = GPT2TokenizerFast.from_pretrained("gpt2")
W = GPT2Model.from_pretrained("gpt2").wte.weight.detach()   # (50257, 768)

def vec(word):
    ids = tok.encode(word)
    assert len(ids) == 1, f"{word!r} is {len(ids)} tokens"
    return W[ids[0]]

def neighbours(v, k=6):
    sims = F.cosine_similarity(W, v.unsqueeze(0), dim=1)
    return [tok.decode([i]) for i in sims.topk(k + 1).indices.tolist()]

print("no space :", neighbours(vec("king")))      # word-piece -> odd neighbours
print("space    :", neighbours(vec(" king")))     # the token seen mid-sentence
analogy = vec(" king") - vec(" man") + vec(" woman")
print("king-man+woman:", neighbours(analogy, 8))
