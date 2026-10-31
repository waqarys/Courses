# M11 — Exercises (with solutions)

**1. MoE cost.** 8 experts of 1 B params each, router picks 2. Roughly how many expert params run per token?
<details><summary>Solution</summary>~2 B (plus shared attention/embeddings), though ~8 B must sit in memory.</details>

**2. Agent loop.** Write the 4-step loop for a tool-using agent.
<details><summary>Solution</summary>(1) model reads prompt + tool list, (2) emits a tool call, (3) code executes it, (4) result appended to the prompt → repeat until a final answer.</details>

**3. Capstone eval.** Why write expected answers *before* building?
<details><summary>Solution</summary>So you measure honestly instead of grading the model on whatever it happens to say.</details>
