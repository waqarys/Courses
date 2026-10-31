# M04 — Exercises (with solutions)

**1. Table size.** A model has vocab 32 000 and d_model 4096. How many embedding parameters?
<details><summary>Solution</summary>131,072,000 (~131 M).</details>

**2. Why not one-hot?** Give two reasons.
<details><summary>Solution</summary>(a) Every pair of words is equally distant → no similarity. (b) 50k-wide sparse vectors are wasteful; dense 768-d vectors are compact and learned.</details>

**3. Space trap.** In snippet 02, `vec("dog")` and `vec(" dog")` give different neighbours. Why?
<details><summary>Solution</summary>They are different tokens (9703 vs 3290). The no-space piece mostly appears inside other words, so it learned a different meaning.</details>

**4. Order.** Without position information, would "dog bites man" and "man bites dog" look different to attention?
<details><summary>Solution</summary>No — attention treats inputs as a set; the outputs would be the same vectors in permuted order. Position embeddings break the tie.</details>

**5. Which models?** Match: learned positions / sinusoidal / RoPE → GPT-2, BERT, 2017 Transformer, Llama.
<details><summary>Solution</summary>GPT-2 and BERT: learned. 2017 Transformer: sinusoidal. Llama: RoPE.</details>
