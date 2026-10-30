# Chapter 2 — Old Principles, New Substrate

**Video Title:** The Agent Amplifies Your Standards (It Doesn’t Invent Them)  
**Duration:** ~6 min (learning version)  
**Goal:** Show that the agent copies and amplifies existing patterns at machine speed. Introduce the amplification thesis and the canon-to-charter map.

## Learning Video
Full narrated MP4 available locally: `Chapter2_Learning_Video.mp4` (~6 minutes).

## Voiceover Script (used in the video)

Welcome to Chapter 2 of Harness Engineering: Old Principles, New Substrate.

A Django repository Ana worked on last year had a helper called clean_payload. It lived in utils.py. The function trimmed whitespace and lowercased an email. Nothing else. The name promised more than it delivered. Every reader who came near it had to open the body to find out what clean meant in this codebase. A real engineer had written it, three years before, in a hurry.

Ana asked an agent to add a sign-up flow. The agent read the codebase, found clean_payload, and made its peace with the name. Over the next forty-five minutes it produced six new helpers: clean_user_input, clean_form, clean_address, clean_metadata, clean_phone, and clean_request. Each did one narrow thing. None of them was named for the thing it did. The agent had not invented the bad naming convention. It had copied the one the codebase already shipped. By Friday, the helpers had spread to two more modules. A pattern a tired human laid down in seconds had been multiplied across a wing of the codebase the original author would not have recognized.

This is the whole shape of the problem. The agent is a reader before it is a writer, and it copies what it reads, fast. The only new part is the rate.

The agent did not invent any of this. Every reliability lever in this book comes from prior work. Tests, types, naming as a behavioral signal, bounded contexts, separation of concerns, information hiding, fail-fast at boundaries, command-query separation, ports and adapters, simplicity as a primary value. What the canon was always about is legibility and changeability.

The agent is a reader and a writer at speeds humans cannot match. The contracts the canon set for human readers and writers still hold for the agent. They hold harder. Whatever the codebase tells the agent about how this team writes code, the agent will believe. Whatever the codebase does not say, the agent will guess.

This brings us to the amplification thesis. The agent does not change your standards. It enforces them. The lower the standards, the more enforcement you get. A human writes a hundred lines a day on a good day. An agent writes thousands. If the codebase teaches the agent that helpers go in utils.py and get named for the verb they happen to start with, the agent will produce hundreds of those helpers per week. If the codebase teaches the agent that a function named chargeCardOrThrow does one thing and signals its failure mode in its name, the agent will produce hundreds of those per week instead. Both runs use the same model; the two codebases pull the output into very different bands.

This is the amplification thesis, and it is the entire reason the canon still applies. The agent is a multiplier on whatever discipline the codebase already enforces. A clean codebase becomes more legible. A tangled codebase becomes more tangled. Volume is the variable that did not exist before, and volume picks whichever side the existing code points at.

There are two pressures the canon now has to absorb. The first is output volume. A team that ships a hundred PRs a week with agents cannot review carefully. The charter has to do the work the review used to do, before the agent commits.

The second pressure is output legibility. A 2 a.m. incident does not care that the change was produced quickly. The on-call engineer has to read the code, find the bug, and ship the fix.

Why is “stronger standards” the wrong slogan? Because the team’s social enforcement of standards runs on human-scale signals. The agent is not slow. The fix is to encode the standard somewhere the agent reads on every turn. That somewhere is the charter.

Code review used to be how you taught a teammate. With the agent, code review is how you teach the charter.

Finally, the canon-to-charter map. Copy the template and fill a row per principle you rely on. If a row has no charter home, the standard is living in someone’s head, and the agent will guess at it. A standard in someone’s head is a standard the agent cannot read. The substrate changed; the discipline of writing things down did not.

## Canon-to-Charter Map Template

```
CANON -> CHARTER MAP
====================
principle: <e.g. naming as a behavioral signal>
lives in charter as: <rule file / skill / sensor / gate>
location: <path, e.g. .claude/rules/naming.md>
enforced by: <test / lint rule / pre-commit hook / reviewer agent>
fires when: <the agent touches which files or does which action>
status: [ ] encoded   [ ] in someone's head   [ ] aspirational (prune)
```

## Quiz
1. What does the amplification thesis claim the agent does with existing standards?
2. Why is “just use stronger standards” insufficient when agents write code?
3. What is the purpose of the canon-to-charter map?
