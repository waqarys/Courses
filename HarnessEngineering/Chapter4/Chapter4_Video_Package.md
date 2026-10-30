# Chapter 4 — Charter and Harness: What Each One Is

**Video Title:** Charter vs Harness — Two Boxes You Must Keep Separate  
**Duration:** ~5.3 min (learning version)  
**Goal:** Define the charter (what you author) and the harness (the engine that applies it). Introduce the four kinds of charter material and the sort sheet.

## Learning Video
Full narrated MP4 available locally: `Chapter4_Learning_Video.mp4` (~5.3 minutes).

## Voiceover Script (used in the video)

Welcome to Chapter 4 of Harness Engineering: Charter and Harness — What Each One Is.

Clone a repository that someone has tuned for agentic coding and open the .claude folder at its root. What you find is mostly prose. A CLAUDE.md that explains the project. Rule files with names like testing.md and migrations.md. A few skills, each a short markdown file describing a workflow. Maybe a settings.json wiring up a hook. Almost none of it is code that runs on its own. It is a stack of instructions, written for a reader who happens to be a model.

Now start the agent: Claude Code, or whatever the team standardized on. It reads that folder, holds it in mind, and goes to work on your repo. The folder did nothing. The agent did. There, in a single clone, sit the two things this book is about: the material you author, and the engine that acts on it.

The charter is everything you author to specify how the agent should behave in your project. That .claude folder is most of it. The word carries two plain senses, and the charter is both. First, a founding document that says how a thing is to be governed. Second, a structured agreement — the terms you author and the harness abides by, applying what you specified rather than negotiating it. Your repo’s charter governs the agent that enters it. You write it, you review it in pull requests, you amend it when it turns out wrong, and it governs every agent that works the repo until you change it.

A charter comes in four kinds of material. Guides instruct before the agent acts: the CLAUDE.md, the rule files, the slash commands, the prose half of a skill. Tool definitions declare what the agent can reach for and how it is wired. Sensors tell the agent whether the work it just did is acceptable: the test files, the lint config, the type-checker settings. Gates refuse: the pre-commit hook, the branch-protection rule, the blocking reviewer. A gate is a sensor wired to a stop.

Most of a charter is prose, and that is the point. A rule written as a sentence covers cases no control-flow graph would, because the agent weighs it instead of branching on it. Some of a charter is code you author, a hook or a gate, and that code is still charter: you wrote it to state a standard.

The charter is your repo’s .claude folder, all of it, plus the dependencies you declare: plugins, policy packs, shared skills, tools such as MCP servers. Declaration in, source out. Either way the test does not change: you authored or adopted it to specify behavior.

If you have been in this field a while, you may have called this folder the harness. It is the charter. Hold the line that the folder you author is the charter, and the engine that reads it is the harness.

The harness is the engine that applies the charter against the model. The field has a shorthand worth borrowing: an agent is a model plus a harness. The model predicts text and nothing more. The harness is everything wrapped around it to turn prediction into work, and the charter is what the harness consults while it does. So the relationship runs in a line. You author a charter; the harness applies it to drive the model; the model produces a result. Charter, harness, model, result.

You get most of a harness rather than build it. Claude Code is one, Cursor is another, and a LangGraph orchestration your platform team stood up is a third. The vendor ships the engine, you point it at your repo, and it reads your charter on the way in. For most teams that is the entire relationship with the harness: choose one, configure it, move on. The teams that build their own are doing harness engineering proper, and Part V of this book is written for them. Parts II through IV are for everyone, because everyone writes a charter.

Two words, two boxes: the charter you author, the harness that applies it. They are not the same kind of thing, and the most expensive mistake in this field is treating them as one. Where exactly the line falls is the next chapter. For now, hold the two boxes apart and know which one takes most of your time; for most of this book, it is the charter.

What is in each box? Your charter is everything you authored or adopted to specify behavior. By role: guides, tool and agent definitions, sensors, gates. By origin: written by hand in the folder, or a declared dependency whose declaration is charter and whose installed body is external.

Your harness is the engine you run, mostly not yours to write: the coding agent, any framework or orchestrator above it, the loop that runs work on repeat, the runtime that fires your hooks, invokes your tools, and enforces your permissions.

A thing on the first list, you maintain, and it is where your reliability comes from. A thing on the second, you mostly choose.

Finally, the Charter versus Harness Sort Sheet. Copy it. List every artifact your agent touches, walking the .claude folder, the config files, and the dependencies, and drop each into one column. The test for the left column is authorship: did you write it or adopt it to specify behavior? Everything else is the engine, and goes on the right.

Charter is what you mean. Harness is what runs. Keep the two straight and every choice after this one gets easier.

In the next chapter we will draw the precise boundary between them.

## Charter vs Harness — Sort Sheet Template

```
CHARTER vs HARNESS — SORT SHEET
===============================
repo: <name>

CHARTER (you authored or adopted it)          | HARNESS (you run it, mostly not yours to write)
------------------------------------------+----------------------------------
<e.g. CLAUDE.md>                              | <e.g. Claude Code>
<e.g. .claude/rules/testing.md>               | <e.g. the loop that reruns work>
<...>                                         | <...>

STUCK? apply the test to each stuck artifact:
did you write or adopt it to state a standard?
yes -> charter, no -> harness
(a hook you wrote is charter even though it runs; a vendor's built-in
slash command is harness even though it looks like a rule)
```

## Quiz
1. What are the four kinds of material in a charter?
2. What is the relationship: Charter → Harness → Model → Result?
3. What is the authorship test for sorting an artifact into charter or harness?
