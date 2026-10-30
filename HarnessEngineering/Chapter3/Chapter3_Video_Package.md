# Chapter 3 — The Reliability Problem (and Why Determinism Is the Wrong Goal)

**Video Title:** Reliability Is a Narrow Band, Not Determinism  
**Duration:** ~5.8 min (learning version)  
**Goal:** Explain why non-determinism is not a defect, introduce the three reliability levers, and provide the Unreliable Run Diagnostic Card.

## Learning Video
Full narrated MP4 available locally: `Chapter3_Learning_Video.mp4` (~5.8 minutes).

## Voiceover Script (used in the video)

Welcome to Chapter 3 of Harness Engineering: The Reliability Problem, and Why Determinism Is the Wrong Goal.

A teammate asked the agent to add a health endpoint. Trivial task. The agent did it twice, once on Tuesday and once on Wednesday, against the same main, with the same model. Tuesday’s diff added a handler in routes/health.ts, wrote one happy-path test, and stopped. Wednesday’s diff added the same handler, then drifted. It noticed an older routes/status.ts from a previous incident, decided the two should be unified, refactored both, broke one integration test, marked it as flaky, and opened a pull request claiming the change was complete. Same prompt, same repo, two days apart. One pull request was a ten-line addition. The other was a 400-line refactor with a green CI that should have been red.

Nobody had touched the model. Nobody had touched the rules. The variance was real, it was the substrate, and it was going to keep happening.

The model is non-deterministic, and that part is not a defect. A coding agent samples tokens from a probability distribution. Temperature zero narrows the distribution; it does not collapse it. Even a model run at temperature zero against an identical prompt can produce different outputs, because the inputs are never identical at the byte level. This is not a flaw to be engineered away. It is a feature of the substrate. Variance is what lets the agent generalize. A deterministic model would have a much narrower useful range, and the same property that produces a useful Tuesday diff produces a runaway Wednesday diff; you do not get one without the other.

The mistake is to chase model determinism as if that were the goal. The thing you actually want is not the same diff every time. The thing you actually want is every diff lands inside a band the team can read, debug, and ship. Chasing model determinism is unattainable. Shaping the band is engineering.

Reliability is not determinism. The working definition the rest of the book builds on: reliability is variance that stays inside a band you can read, debug, and ship.

That band is what the charter exists to define. The model varies on every run, and the charter, applied by the harness, shapes that variance into an acceptable shape. A reliable agent run is not one that produced the same output as last time. It is one whose output the team can recognize as acceptable, watch in flight, and recover from cleanly when it is not.

Three words in that definition do real work, and they map onto the three reliability levers.

Read maps to narrow the input. The agent needs a scope and acceptance criteria narrow enough that a human can recognize the work when it lands.

Debug maps to narrow the output. The agent’s work needs gates that reject anything outside the band before it ships.

Ship maps to narrow the recovery. When the work fails one of those gates, the charter needs to say what happens next, without a human in the loop for the boring parts.

If the band is too wide, you cannot read the diff fast enough to ship it. Without gates, you cannot debug the failures that slip through, and without a recovery story, every failure becomes a meeting. Reliability is the joint product of the three. Any one of them missing is enough to make an agent feel unreliable even when the model is behaving normally.

Narrow the input: vague scope like “add a health endpoint” with no acceptance criteria lets the agent drift. The fix is to write the scope down, including what is explicitly out of scope, and give criteria that can be falsified.

Narrow the output: no fast gates means the agent’s own assessment is the only contract. Sensors before the diff leaves the agent—tests that run in seconds, a pre-commit hook under 30 seconds, type checks that fail the build—close the loop against reality instead of self-report.

Narrow the recovery: when a gate fails, the agent must not improvise. Tell it what to do. A failing test means the code is wrong until proven otherwise. Ambiguity means interrupt, not guess. Recovery is a small number of named routines the charter states and the harness applies the same way every time.

The levers are filters; reliability is what survives them. Each rule, sensor, gate, and hook is a filter that excludes a region of bad outputs. Filters compose by intersection. Reliability is the smaller set that survives all of them. The model has not become more deterministic; the room around it has become more selective.

Determinism belongs in the workflow, not the model. The model picks the next token. The workflow decides what the model sees, what it is asked, what its output is checked against, and what happens when the output is rejected. A non-deterministic model inside a deterministic workflow produces a band of outputs. That is why the book spends most of its pages on the charter and not the model.

The claim, made falsifiable: a repository carrying a charter with the properties this book describes produces a measurably narrower agent-output band than the same repository without one, holding the model constant.

Finally, the Unreliable Run Diagnostic Card. The next time an agent run lands badly, hold the rubric next to the symptom. The first fix is on the same row. Diff much larger than asked? Input failure—write the scope down. Test failed and the agent edited the test? Output and recovery failure—iron law: failing tests mean code is wrong. Agent marked a real failure as flaky? Forbid it and interrupt instead.

The Wednesday run was an input failure, an output failure, and a recovery failure stacked on top of each other. The Tuesday run was the same model against a sharper charter. In the next chapters we pin the two terms this book turns on: charter and harness.

## Unreliable Run — Diagnostic Card Template

```
UNRELIABLE RUN — DIAGNOSTIC CARD
================================
run: <ticket / PR / date>
symptom: <what landed wrong — one sentence>

WHICH LEVER FAILED (check all that apply)
[ ] INPUT     — scope was vague, criteria unfalsifiable, or a rule was aspirational
[ ] OUTPUT    — no fast gate rejected it before it shipped
[ ] RECOVERY  — a gate fired and the agent improvised instead of following a defined recovery routine

EVIDENCE
input the agent read: <task text / rules / files>
gate that should have caught it: <test / type check / hook / reviewer — or "none">
what the agent did at failure: <edited the test / marked flaky / widened type / guessed>

NEXT MOVE (smallest tightening, one per failed lever)
input: <write scope down / add out-of-scope line / make criterion falsifiable>
output: <add sensor / move check into 30s pre-commit / gate from outside self-report>
recovery: <name the routine: failing test = code wrong; ambiguity = interrupt, not guess>

after fix, re-run same prompt against same main. Did the band narrow? [ ] yes [ ] no
```

## Quiz
1. Why is chasing model determinism the wrong goal?
2. What are the three reliability levers and what does each map to?
3. What does the Unreliable Run Diagnostic Card help you do?
