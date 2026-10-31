# M04 · snippet 01 — an embedding layer is just a learned table you index into
import torch
from torch import nn

torch.manual_seed(0)
emb = nn.Embedding(num_embeddings=10, embedding_dim=4)
ids = torch.tensor([3, 1, 3])
vecs = emb(ids)
print(vecs.shape)                                   # (3 tokens, 4 dims)
print(torch.equal(vecs, emb.weight[ids]))           # True: lookup == indexing
print("GPT-2 token table params:", 50257 * 768)     # 38,597,376

pos = nn.Embedding(num_embeddings=8, embedding_dim=4)   # learned positions (GPT-2 style)
x = emb(ids) + pos(torch.arange(len(ids)))
print("token+position:", x.shape)
