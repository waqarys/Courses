# M08 — Exercises (with solutions)

**1. LoRA size.** W is 4096×4096, r = 16. Trainable LoRA params for this one matrix?
<details><summary>Solution</summary>4096·16 + 16·4096 = 131,072 (vs 16.8 M full).</details>

**2. Why B = 0?** What would go wrong if both A and B started random?
<details><summary>Solution</summary>The model's outputs would change before any training — you start from a damaged model. B = 0 makes step 0 identical to the base.</details>

**3. Label masking.** What does `-100` mean in Hugging Face labels?
<details><summary>Solution</summary>`ignore_index` of cross-entropy: those positions contribute no loss, so the model isn't trained to produce the prompt.</details>

**4. Merge.** Write the line that merges LoRA into the base weight for inference (Conv1D layout, weight is in×out).
<details><summary>Solution</summary>`base.weight.data += (A @ B) * scale` — then drop A and B.</details>

**5. Choose.** You want a support bot that cites your company's latest docs. Fine-tune or retrieval?
<details><summary>Solution</summary>Retrieval (RAG, M09) for facts that change; fine-tune only for tone/format. Often both.</details>
