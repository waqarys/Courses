# M07 — Exercises (with solutions)

**1. Initial loss.** A model with vocab 50,257 starts at loss 10.8. Is that healthy?
<details><summary>Solution</summary>Yes — ln(50257) ≈ 10.82.</details>

**2. Perplexity.** Val loss 1.5 → perplexity?
<details><summary>Solution</summary>e^1.5 ≈ 4.48.</details>

**3. Overfitting.** Train 0.9, val 1.8 and rising. Three fixes?
<details><summary>Solution</summary>More/different data, dropout or weight decay, a smaller model, or stop early at the best val checkpoint.</details>

**4. Remove warmup.** Set `warmup=0` and `lr_max=1e-2`. What happens and why?
<details><summary>Solution</summary>Early updates from random weights are huge; loss often spikes or goes NaN. Warmup lets AdamW's statistics settle.</details>

**5. Resume.** Write the code to load `tiny_gpt.pt` and generate 200 characters.
<details><summary>Solution</summary>

```python
ck = torch.load("tiny_gpt.pt")
m = GPT(GPTConfig(**ck["cfg"])); m.load_state_dict(ck["model"]); m.eval()
itos = dict(enumerate(ck["chars"]))
print("".join(itos[i] for i in m.generate(torch.zeros((1,1),dtype=torch.long), 200, 0.8)[0].tolist()))
```
</details>
