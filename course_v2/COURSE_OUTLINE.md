# Introduction to Python — Course Outline (v2)

**Channel:** Fun Skill Builders · **Audience:** complete beginners aged 7 to 20 · **Host:** Pip the Python (AI voice, Kokoro `af_heart`)
**Format:** one lesson = one video, rendered by `eduvid pycourse` (see [README.md](README.md)).

Topic order follows the attached booklet *Unit 3 – Programming with Python* (chapters 1–4: Introduction, Input and Output,
Data Structures, Control Structures), with a Module 5 added so the course ends with functions, modules and a final project.
All wording, examples and programs here are original.

## The host: Pip the Python (name to be confirmed)

A friendly cartoon python snake in the Python-logo colours: a blue body with a yellow belly stripe and yellow spots,
a big round blue head with a yellow muzzle, large shiny eyes, pink cheeks, a smile and a little forked tongue, with a
white sticker edge so it reads on both the dark background and the cream cards. Pip is drawn entirely in code
(`eduvid/pycourse/pip.py`, Pillow; no image generation, no image files), stands beside the code panel / card, slides
in on the title card, and its mouth opens and closes while the narration is speaking. Pip introduces itself in every
intro. Name alternatives if Waqar prefers: Sunny, Scout, Ziggy.

## How every lesson is built

| Phase | Section(s) | What happens on screen |
|---|---|---|
| — | `INTRO` | Title card: lesson number, title, "In this lesson" goals, Pip slides in |
| **Study** | `STUDY` (1–3 cards) | The concept explained first, in detail: everyday analogy → precise idea → "Level up" point for older learners. Points, variable boxes, flow arrows, tables and code snippets pop in as Pip says them |
| **Study** | `CODE` | An editor window: every line is **typed character by character while Pip explains that line**, with syntax colours, a blinking caret, the current line highlighted and a speech-bubble note. Then **Run** is pressed and the real output (produced by actually running the program) appears in the output panel; typed answers to `input()` show in yellow, errors in red |
| **Revise** | `REVISE` | 4 ticked recap points |
| **Practice** | `PRACTICE` | Task card + hint + a 10–15 s countdown ("Pause and try it!") |
| **Practice** | `ANSWER` | The model answer typed line by line and run |
| — | `OUTRO` | "Up next" card |

The narration never mentions these phase names or any production notes, and it never splits the audience into
parents and children: everyone watching is a learner.

## Lessons

Length = rendered length (Modules 1–2 measured from real renders at voice speed 0.92) or an estimate.

### Module 1 — Getting Started (booklet ch. 1) · fully written
| # | Lesson | Key ideas | Main program | Exercise | Length |
|---|---|---|---|---|---|
| 1.1 | Meet Python | instructions in order, code, programs, what a language is, interpreter, editor/Run/output, text vs maths | `first_steps.py`: `print("Hi")`, `print(2 + 3)`, `print("2 + 3")` | print your name, then 7 × 6 | 5.2 min |
| 1.2 | Hello, World! | print, brackets, strings, comments, sequence, smoke test | `hello.py` | three-line "about me" | 5.7 min |
| 1.3 | Errors Are Clues | reading a traceback, NameError, SyntaxError, IndentationError, fix → run again | `bug_hunt.py` with three live mistakes and fixes | 2-bug hunt, fixed one error at a time | 5.3 min |
| 1.4 | Mini-Project: My Welcome Card | plan first, `"*" * 30`, spaces in strings, layout | `welcome_card.py` | birthday card with a `#` border | 4.5 min |

### Module 2 — Variables, Input and Output (booklet ch. 2) · fully written
| # | Lesson | Key ideas | Main program | Exercise | Length |
|---|---|---|---|---|---|
| 2.1 | Variables: Labelled Boxes | name + value, `=` means store, changing values, print with commas | `variables.py` | pet profile | 5.5 min |
| 2.2 | Good Names and Constants | naming rules, snake_case, meaningful names, CONSTANTS, camelCase/PEP 8 | `names.py` (live SyntaxError on `player-score`) | fix 3 bad names | 4.8 min |
| 2.3 | Strings: Playing with Text | quotes, `+`, `len()`, `.upper()/.lower()`, f-strings, immutability | `strings.py` | name badge | 5.6 min |
| 2.4 | Asking Questions with input() | input → process → output, input waits, always returns text | `chat.py` (ends in a TypeError on purpose) | colour + animal sentence | 4.9 min |
| 2.5 | Numbers: int and float | types, int/float/str/bool, `type()`, `int()`, `float()`, ValueError | `numbers.py` (fixes 2.4's error) | double the pets | 5.1 min |
| 2.6 | Maths with Python | `+ - * / // % **`, float division, order of operations | `maths.py` (sharing 17 sweets) | 135 minutes → hours and minutes | 5.0 min |
| 2.7 | True or False? | bool, `== != < > <= >=`, `=` vs `==`, `and/or/not`, truth tables, chained comparisons | `true_false.py` | warm-day checker (tested at 30 and 40) | 5.4 min |
| 2.8 | Comments and Clean Code | why comments, 3 rules, stubs (plan as comments), TODO | `pocket_money.py` | screen-time planner | 4.3 min |
| 2.9 | Mini-Project: Recipe Scaler | constants + input + float maths + `round()` (banker's rounding) | `recipe_scaler.py` | add sugar | 4.2 min |

### Module 3 — Collections (booklet ch. 3) · detailed outline, scripts next
| # | Lesson | Study (concept + analogy) | Code, line by line | Practice |
|---|---|---|---|---|
| 3.1 | Lists: Many Things in One Box | a list = a train of carriages; `[ ]`, commas, mixed items; arrays vs lists (level up: arrays store one type in a row of memory, Python lists are flexible) | `snacks = ["apple", "banana", "mango"]`, print the list, `len()` | list of 4 favourite games, print it and its length |
| 3.2 | Indexes and Slices | seats numbered from 0; `[0]`, `[-1]`; slices `[1:3]` as "from…up to but not including"; IndexError live | index/slice a list of planets; deliberate `planets[8]` error | print the first 3 and the last planet |
| 3.3 | Changing Lists | lists are mutable: `append`, `insert`, `remove`, `pop`, `sort`, `in` | build a shopping list step by step, output after each change | to-do list: add 2, remove 1, sort |
| 3.4 | Going Through a List with for | "for each item in the bag…"; loop variable; indentation as "belongs to"; a first look at loops (full detail in 4.8) | print every snack with a number using a counter | total of a list of scores with a loop |
| 3.5 | Grids: Lists Inside Lists | 2D list = a seating chart / tic-tac-toe board; `grid[row][col]` | draw a 3×3 board, place an X, print rows | change the centre square and print the board |
| 3.6 | Dictionaries | a real dictionary: word → meaning; key → value; `{}`; look up, add, change, `in`, KeyError | `capitals = {...}` lookups and updates | pet → sound dictionary, print one sound |
| 3.7 | Records and Fields | a record = one row in a table (a student card); fields = its parts; a dict as a record; a list of records | list of 3 student dicts, print each name and score | add a field `age` and print a report line |
| 3.8 | Tuples and Sets | tuple = sealed envelope (cannot change): coordinates, RGB colours; set = bag of unique stickers: no duplicates, `union`, `&` | tuple point `(3, 4)`; remove duplicate names with a set | classmates' favourite fruits → unique set |
| 3.9 | Mini-Project: Daily Task Planner | choose the right structure: list of dicts | tasks with name/minutes/done, totals and a done count | add a task and print time left |

### Module 4 — Making Decisions and Loops (booklet ch. 4) · detailed outline
| # | Lesson | Study | Code | Practice |
|---|---|---|---|---|
| 4.1 | Sequence and Flowcharts | algorithm = recipe; flowchart shapes (start/stop, process, input/output, decision) | a 4-step morning-routine program next to its flowchart | draw + code a "make a sandwich" sequence |
| 4.2 | if: Making a Choice | a fork in the road; condition → True runs the block; colon + indentation | ticket price check | "Ride allowed" if height >= 120 |
| 4.3 | if / else | two paths, exactly one runs | even or odd with `%` | pass/fail checker |
| 4.4 | elif: Many Choices | a ladder of questions, first True wins; order matters | grade calculator A/B/C/D | weather → clothing advice |
| 4.5 | Complex and Nested Conditions | and/or in ifs, writing conditions clearly with brackets and named booleans; if inside if | theme-park ride rules (age and height) | login: username then password |
| 4.6 | match / case | a menu with numbered buttons; `case _` default (Python 3.10+) | day number → day name | calculator menu with match |
| 4.7 | while Loops | "keep going while…"; counter; infinite loop danger and Ctrl+C | countdown 10 → liftoff | keep asking until the right password |
| 4.8 | for Loops and range() | repeat a set number of times; `range(start, stop, step)`; loops over strings | times table with range | stars triangle pattern |
| 4.9 | Loop Control and Validation | `break`, `continue`; do-while and repeat-until patterns in Python (`while True` + `break`); validating input with `.isdigit()` | ask for a number from 1 to 10 until valid | menu loop that quits on "q" |
| 4.10 | Mini-Project: Guess the Number | random number, loop, if/elif/else, counting guesses, validation, extension ideas | full game (seeded for the video) | add "too high/too low" hints and a guess limit |

### Module 5 — Next Steps (beyond the booklet) · detailed outline
| # | Lesson | Study | Code | Practice |
|---|---|---|---|---|
| 5.1 | Functions: Your Own Commands | a function = a recipe card you can reuse; `def`, call, indentation | `def say_hello():` called 3 times | a function that prints a banner |
| 5.2 | Parameters and return | ingredients in, dish out; parameters vs arguments; `return` vs print | `area(width, height)` | `celsius_to_fahrenheit()` |
| 5.3 | Python's Toolbox: Modules | `import`; `random`, `math`, `datetime` (booklet 2.2.3 date and time) | dice roller + today's date + days until a birthday | random compliment generator |
| 5.4 | Testing Your Code | smoke test (booklet 1.8), test cases, normal/boundary/invalid data, `assert` | tests for `is_even()` | write 3 asserts for `area()` |
| 5.5 | Coding with AI, Wisely | what AI helpers do (booklet 1.6), checking and understanding suggestions, honesty, privacy | ask-and-verify walkthrough; spotting a bug in "AI-written" code | fix and explain a suggested snippet |
| 5.6 | Final Project: Big Five Wellbeing Check-In | design brief → plan with stubs → build: input 1–5 ratings for 5 areas, validation loop, total and average, dictionary of areas, friendly feedback with if/elif | complete program | add a sixth area and a weekly-average feature |

**Totals:** 38 lessons (4 + 9 + 9 + 10 + 6). Modules 1–2 (13 lessons) are fully scripted in `lessons/`. Their real rendered
lengths are 4.2–5.7 min (65.5 min in total, about 5 min each). Modules 3–5 should run a little longer (6–8 min) because the
programs grow, so the full course is about 3.5–4 hours of video.

## Writing rules used in every script
* Concept first, code second. Every STUDY card: an everyday analogy a 7-year-old follows, then the precise idea, then a **Level up** point for teens.
* Narration explains each line **as it is typed**; the on-screen note (`@ line N | note`) is a short label, never a copy of the narration.
* Every program is real: the output on screen is produced by running it. `eduvid pycourse check` runs them all.
* Deliberate mistakes are shown and fixed live (1.3, 2.2, 2.4) so learners see real error messages.
* Exercises have a pause/countdown, a hint, and an answer typed and run on screen.
* Numbers in narration are written as words where the TTS could misread symbols; no symbols like `=` or `-` in spoken text.
