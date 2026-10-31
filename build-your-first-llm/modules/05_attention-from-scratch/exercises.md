# M05 — Exercises (with solutions)

**1. Shapes.** Q is (2, 12, 10, 64). What is the shape of `Q @ K.transpose(-2,-1)`?
<details><summary>Solution</summary>(2, 12, 10, 10) — per batch, per head, every token vs every token.</details>

**2. Why √d?** What happens to softmax if scores are very large?
<details><summary>Solution</summary>It saturates: nearly all weight on one token, gradients ≈ 0 for the rest. Dividing by √d keeps the score variance ≈ 1.</details>

**3. Mask check.** In a 5-token causal mask, how many positions can token 3 (0-indexed) see?
<details><summary>Solution</summary>4 (positions 0–3).</details>

**4. Bottleneck vs vanishing gradient.** Explain the difference in one sentence each.
<details><summary>Solution</summary>Bottleneck: during reading, all history must fit in one fixed-size state. Vanishing gradient: during training, the error signal shrinks as it is propagated back through many steps.</details>

**5. Heads.** d_model 512, 8 heads — size of each head? Total parameters of `c_attn` with bias?
<details><summary>Solution</summary>64 per head. 512×1536 + 1536 = 787,968.</details>
