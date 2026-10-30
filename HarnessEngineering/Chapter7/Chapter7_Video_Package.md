# Chapter 7 — The Repo as a Behavioral System

**Video Title:** The Repo as a Behavioral System  
**Duration:** ~6.9 min (learning version)  
**Goal:** Show that a repo emits three signal classes (instruction, imitation, feedback). Imitation usually wins. The agent’s behavior is the joint of all three. Includes the full Repo Audit template.

## Learning Video
Full narrated MP4 available locally: `Chapter7_Learning_Video.mp4` (~6.9 minutes).

## Voiceover Script (used in the video)

Welcome to Chapter 7 of Harness Engineering: The Repo as a Behavioral System.

The CLAUDE.md said use the repository pattern. The codebase had no repositories. What it had was a God file named helpers.py. The team had polished the CLAUDE.md for two afternoons. It was also a lie, and the agent figured that out on its first turn.

Sofia asked for a new endpoint. The agent read the CLAUDE.md, then opened three files in the existing codebase. It found no repository, no seam. It produced the endpoint the existing codebase taught it to produce and ignored the careful CLAUDE.md.

The agent did the right thing. Given written guidance and demonstrated guidance, it weighted demonstration higher. The actual fix was to write one repository and let the next agent find it.

Your charter is the part you author, but it is not the only thing teaching the agent. The code teaches too, and louder.

A repo emits three kinds of signal.

Direct instruction. The charter the agent reads: CLAUDE.md, rules, skills. Weakest at shaping what gets written.

Imitation surface. The existing code. Names, structure, tests, layout. The largest signal. What the agent copies.

Feedback channel. Tests, linters, type checkers, pre-commit hooks, CI. The only signal that speaks back.

The agent’s behavior is the joint of all three. A polished CLAUDE.md cannot save a chaotic codebase or a silent feedback channel.

Most teams over-invest in instruction. The repo is teaching with examples, and the examples are what the agent takes home.

Why instruction loses to imitation. The codebase is the most recent and most local evidence. Direct instruction is general; imitation is specific. When they conflict, the specific example wins.

Direct instruction is a claim. Imitation surface is evidence. Feedback channel is consequence. Claims without evidence read as marketing.

The repo is the environment. The agent is the animal. Changing the environment changes the behavior. You do not retrain the model. You write a repository, add a test, wire a hook.

Two engineers on the same model can get wildly different results because one is in a clean repo and one is in a 2,000-line controller. The variance is repo variance.

In the worked example, two repos with identical CLAUDE.md and the same prompt produce completely different outputs. Repo A (mess) yields an unsafe function with no test. Repo B (clean) yields a proper service, test, and thin view. Direct instruction was constant. The other two channels moved the band.

Each channel does a specific job. Instruction expresses intent the codebase does not yet demonstrate. Imitation teaches the specific shape. Feedback keeps the other two consistent.

If output is unpredictable, the answer is almost never “write more rules.” Ask three questions of a representative diff:
1. Does it match existing code structure? If no → imitation bottleneck.
2. Did the charter catch anything before a human? If no → feedback bottleneck.
3. Did the agent ignore something the CLAUDE.md explicitly said? Only then touch direct instruction (usually by cutting aspirational rules).

Every agent PR is a measurement of the repo. It is the repo’s report card.

## Repo Audit Template

```
REPO AUDIT — THREE SIGNAL CLASSES
=================================
Mark each prompt: strong / weak / missing.

DIRECT INSTRUCTION — WHAT DOES THE AGENT READ?
[ ] 1. Open CLAUDE.md. Pick the three most prescriptive statements. For each, find one file that demonstrates it. If you cannot, the statement is aspirational.
[ ] 2. List every rule file under .claude/. For each, name the last time it fired on a real PR. Any rule that has never fired is a candidate for prune.
[ ] 3. Pick one skill. Walk it on a fresh task. Does the output look like the skill or like the existing code?
[ ] 4. Read CLAUDE.md aloud to a teammate. Then show them the most-touched file. The gap is the aspirational gap.
[ ] 5. Count the words in CLAUDE.md. If above 3,000, identify the 30% not re-read in the last month. Cut or scope it.

IMITATION SURFACE — WHAT DOES THE AGENT COPY?
[ ] 1. Run: git log --since="3 months ago" --name-only --pretty=format: | sort | uniq -c | sort -rn | head -5
The top five files are what the agent reads first. Would you hand each to a new hire?
[ ] 2. Compare the newest module to the oldest module that does similar work. Same shape = convention.
[ ] 3. Pick a domain term. Search for every name that refers to it. More than two synonyms and the agent will produce a fourth.
[ ] 4. Read a test the agent wrote and one it did not. If you can tell which is which and the agent's feels off, your test style is the problem.
[ ] 5. Identify one god file. Every edit near it inherits its shape. Splitting it is probably the highest-leverage refactor.

FEEDBACK CHANNEL — WHAT SPEAKS BACK?
[ ] 1. Time the pre-commit hook. Over 30s and it gets skipped; under 5s and it checks too little.
[ ] 2. List every check that runs on CI but not pre-commit. Anything that could run locally and doesn’t is feedback delayed.
[ ] 3. Pick the last three agent PRs that needed a human-caught fix. Could a sensor have caught it?
[ ] 4. Look at type coverage. Default strictness = the checker is barely speaking. Tighten one knob.
[ ] 5. Find the last test that failed and stayed red over a day. A muted channel is worse than none.

STRONGEST signal in each class -> <what you are accidentally amplifying>
WEAKEST signal in each class -> <the gap you thought was covered>
```

## Quiz
1. What are the three signal classes a repo emits to an agent?
2. Why does imitation usually beat direct instruction?
3. What is the practical first step when an agent’s output is unpredictable?
