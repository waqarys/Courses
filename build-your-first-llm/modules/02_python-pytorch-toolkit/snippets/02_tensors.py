# M02 · snippet 02 — tensors, shapes, matmul, broadcasting
import torch

x = torch.tensor([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])        # 2 x 3
W = torch.ones(3, 4)                       # 3 x 4
print("x", x.shape, x.dtype)
y = x @ W                                  # (2x3) @ (3x4) -> 2x4
print("x @ W ->", y.shape)
b = torch.tensor([0.1, 0.2, 0.3, 0.4])     # 4 numbers
print("broadcast add:\n", y + b)           # b is added to every row

batch = torch.randn(8, 16, 768)            # batch x tokens x features
print("LLM-shaped activations:", tuple(batch.shape))
