# Chapter 5 — Harness and Charter: The Boundary

**Video Title:** The Boundary: Authored vs Applied  
**Duration:** ~6.5 min (learning version)  
**Goal:** Draw the precise line between charter and harness. Show why the authorship test (not executability) is the one that holds, and why the seam matters for reliability.

## Learning Video
Full narrated MP4 available locally: `Chapter5_Learning_Video.mp4` (~6.5 minutes).

## Voiceover Script (used in the video)

Welcome to Chapter 5 of Harness Engineering: Harness and Charter — The Boundary.

A vendor published a launch post last March. Three paragraphs in, it promised a new harness for agentic coding. A sentence later, the harness was their CLI. A sentence after that, it was the orchestration layer. By the closing paragraph, the harness was the marketplace. One word, three referents. The comment thread split. Nobody argued about the same thing.

The CLI is a harness. The orchestration layer is a harness. The marketplace is a distribution channel. The mistake was calling any single piece the harness. Under that sat a quieter mistake: nowhere was the part the reader actually writes — the rules, the standards, the file the agent reads before it touches a line of code. That part has its own name, and it is not the harness.

A discipline without a shared vocabulary cannot be taught, measured, or improved. Two words fix it, with one line between them.

Charter is the standards you author for the agent to obey. Harness is the engine that applies them against the model. The line that holds is authored versus applied.

The machine runs: charter, then harness, then model, then result. Only one stage is active.

A model predicts text and does nothing else. Wrap that prediction loop in everything needed to turn it into work: the prompt, the tools, the control flow, the retry, the loop. That wrapping is the harness.

The model emits a tool call: read auth.py. Opening the file, handing the contents back, and asking the model what to do next is the harness. Every concrete action is the harness acting on text the model only proposed. The model decides; the machinery does.

The charter does not run. It gets read. Prefer composition over inheritance is a sentence the agent weighs, not a branch a runtime takes.

The tempting test is to sort by whether a thing executes, and it fails on the first hook you write. A pre-commit hook is a script, and a script runs, but you wrote it to state a standard, which is charter. The engine that fires it is the harness. The test that holds is: did you author it to specify behavior?

A hook lives in your .claude folder and encodes a standard. That makes it charter. The hook runner is the engine.

Tools and plugins split the same way. The definition and config you check into the repo are charter. The installed body is external. The harness loads and invokes.

Why the seam is worth the trouble. The vendor ships you the harness. What every team writes is the charter.

A team swaps Claude Code for Cursor and back. The PR quality does not move. Then they turn an empty CLAUDE.md into a real one. The band tightens. They had been swapping the harness and waiting for a result only the charter could give.

On Tom’s repo the agent kept reintroducing a deleted helper. They wrote four lines into the charter: the helper is gone, do not recreate it. The function stayed dead. Nothing about the model changed. They changed the part with their names on it.

When a vendor claims its harness makes agents more reliable, the seam turns the claim into a question: did you change the machinery, or did you ship a charter and call it a harness?

A discipline that calls both things the harness cannot answer: we are not getting reliable output; what do we change? Name the line and the question answers itself. You change the charter. You change the harness rarely.

Get the boundary right and you stop arguing about the word. You finally know which half of the work is yours, and which half you can change.

## The Card (template)

```
HARNESS / CHARTER — THE CARD
============================

HARNESS. The engine that interprets and applies the charter against the model: the coding agent, the frameworks, the orchestrator, the loop, the runner that fires your hooks. Agent = Model + Harness.
NOT the standards it applies, and not any single one of its pieces; calling one piece "the harness" is the most common mistake.

CHARTER. Everything you author to specify how the agent should behave: your repo's .claude folder, all of it (rules, hooks, agents, skills, commands), plus your declared dependencies. Mostly prose, sometimes code. Versioned, reviewed, gated.
NOT machinery; the charter is inert until the harness runs it.

THE TEST.
[ ] Authored or applied? You author the charter. The harness is the engine that applies it against the model.
[ ] The trap: do not sort by whether a thing executes. A pre-commit hook executes and is still charter, because you authored it to state a standard; the runner that fires it is the harness.
```

## Quiz
1. What is the one test that sorts charter from harness?
2. Why does sorting by “does it execute?” fail?
3. Why does swapping the harness rarely tighten the output band, while improving the charter does?
