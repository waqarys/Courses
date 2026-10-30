# Chapter 6 — Taxonomy: The Seven Words and the One Test That Sorts Them

**Video Title:** The Seven Words and the One Test  
**Duration:** ~5.4 min (learning version)  
**Goal:** Gather the vocabulary in one place and show how the single authorship test sorts every word and every artifact.

## Learning Video
Full narrated MP4 available locally: `Chapter6_Learning_Video.mp4` (~5.4 minutes).

## Voiceover Script (used in the video)

Welcome to Chapter 6 of Harness Engineering: Taxonomy — The Seven Words and the One Test That Sorts Them.

A reviewer once sent back a design doc of mine with a single margin note: You’re using harness to mean four different things on this page. He was right. In one paragraph it meant Claude Code, in the next the retry policy I had written, in the third the CI job that ran my tests, and in the fourth the whole apparatus around the model. Four referents, one word.

That page is why this chapter exists. It gathers the whole vocabulary in one place, sorted by a single question you can ask of any artifact.

Everything in this book is constraint engineering: adding just enough deterministic structure around a non-deterministic model to narrow its output into a band you can read, debug, and ship. It runs at three altitudes: the charter, the harness, and orchestration. Same craft, three scales. The skill is the minimum structure that buys reliability, not the maximum.

The one test. Point at any piece of your setup and ask: did you author it to specify how the agent should behave, or is it the engine that applies what’s specified?

You author the charter; the harness you run consumes and applies it. The sort is authorship, not executability. A hook you wrote is charter even though it runs. The runner that fires it is harness.

Of the reviewer’s four meanings, the retry policy is charter; Claude Code, the CI runner, and the whole apparatus are harness. The test tells them apart every time.

The seven words.

Model. The weights. The one part you never build; you call it. Agent equals Model plus Harness.

Charter. Everything you author to specify how the agent should behave: CLAUDE.md, rule files, skills, the hooks and gates you write, declared policy packs, tool definitions. Mostly markdown, sometimes code. Parts II through IV.

Harness. The engine that interprets and applies the charter against the model: the coding agent, a framework, the orchestrator, the loop, the runner that fires your hooks. It wraps a single agent, one bounded run. Part V.

Orchestration. The engine one altitude up: the queue, the daemon, the governed process that runs many agents unattended. Harness is to one agent what orchestration is to a fleet. Part VI.

Three more words name jobs that sit inside the two boxes.

Prompt engineering. Shaping the single request. A charter job at the leaf; the harness assembles the prompt the charter specifies.

Context engineering. Deciding what the model sees before it acts. The policy for what to include is charter; the machinery that retrieves and packs it is harness.

Loop engineering. Designing the act-check-route cycle, its bounds, its recovery. Purely the engine.

The symmetry. Most jobs genuinely exist on both levels. There is a charter version and a harness version: same job, two levels.

Evals: did a rule change the agent’s behavior? (charter). Does the machinery route and execute correctly? (harness).

Tools: declaring and bounding a tool (charter). Building the tool (harness).

Verification: the gate you author (charter). The verification node that runs it (harness).

Guardrails: the policy (charter). The runtime guard that enforces it (harness).

Workflow: the process you author (charter). The executor that registers and drives it (harness).

With the one test and these seven words, the vocabulary stops drifting. You can point at any artifact, any job, any altitude, and know exactly which box it belongs in.

## Quick Reference

**The One Test**  
Did you author it to specify how the agent should behave?  
- Yes → Charter  
- No → Harness (the engine that applies it)

**Seven Words**  
1. Model  
2. Charter  
3. Harness  
4. Orchestration  
5. Prompt engineering  
6. Context engineering  
7. Loop engineering  

## Quiz
1. What is the single test that sorts every artifact?
2. Name the three altitudes of constraint engineering.
3. Give one example of a job that has both a charter version and a harness version.
