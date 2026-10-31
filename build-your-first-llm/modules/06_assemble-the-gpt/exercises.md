# M06 — Exercises (with solutions)

**1. MLP params.** One GPT-2 small MLP (768→3072→768, biases): how many parameters?
<details><summary>Solution</summary>768·3072+3072 + 3072·768+768 = 4,722,432.</details>

**2. LayerNorm by hand.** Normalise `[2, 4, 6]` (no learned scale/shift, ignore epsilon).
<details><summary>Solution</summary>mean 4, population std √(8/3)≈1.633 → `[−1.22, 0, 1.22]`. Sum = 0 ✔.</details>

**3. Tying.** What does weight tying save in GPT-2 small, and does `lm_head.weight` disappear from `state_dict()`?
<details><summary>Solution</summary>50257×768 = 38,597,376 parameters. No — both keys appear; they share storage, and `torch.save` stores it once.</details>

**4. Pre vs post norm.** Where does LayerNorm sit in GPT-2 vs the 2017 Transformer?
<details><summary>Solution</summary>GPT-2: before each sub-layer (pre-norm). 2017: after the residual add (post-norm).</details>

**5. Debug.** Your loaded model outputs "to to to to". List two checks.
<details><summary>Solution</summary>(a) Compare logits to HF on one input. (b) Check every HF key was copied (biases!) and Conv1D weights were transposed. Also check GELU approximation.</details>
