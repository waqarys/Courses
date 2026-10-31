# M02 · snippet 04 — a tiny nn.Module and its parameter count
import torch
from torch import nn

class TinyNet(nn.Module):
    def __init__(self, d_in=4, d_hidden=8, d_out=2):
        super().__init__()
        self.layer1 = nn.Linear(d_in, d_hidden)   # 4*8 + 8 = 40 params
        self.layer2 = nn.Linear(d_hidden, d_out)  # 8*2 + 2 = 18 params
    def forward(self, x):
        return self.layer2(torch.relu(self.layer1(x)))

net = TinyNet()
print(net(torch.randn(3, 4)).shape)                     # torch.Size([3, 2])
print("params:", sum(p.numel() for p in net.parameters()))  # 58

# Correct keyword names (common source of TypeError):
emb = nn.Embedding(num_embeddings=1000, embedding_dim=64)
ln = nn.LayerNorm(64)                                   # normalized_shape=64
print(emb.weight.shape, ln.weight.shape)
