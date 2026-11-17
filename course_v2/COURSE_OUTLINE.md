# Introduction to Python — Course Outline (v2)

**Channel:** Fun Skill Builders · **Audience:** complete beginners aged 7 to 20 · **Host:** Ziggy the Python (AI voice, Kokoro `af_heart`)
**Format:** one lesson = one video, rendered by `eduvid pycourse` (see [README.md](README.md)).

Topic order follows the attached booklet *Unit 3 – Programming with Python* (chapters 1–4: Introduction, Input and Output,
Data Structures, Control Structures), with a Module 5 added so the course ends with functions, modules and a final project.
All wording, examples and programs here are original.

## The host: Ziggy the Python

A friendly cartoon python snake in the Python-logo colours: a blue body with a yellow belly stripe and yellow spots,
a big round blue head with a yellow muzzle, large shiny eyes, pink cheeks, a smile and a little forked tongue, with a
white sticker edge so it reads on the dark editor background and on the cream cards. Ziggy is drawn entirely in code
(`eduvid/pycourse/pip.py`, Pillow; no image generation, no image files), stands beside the code panel / card, slides
in on the title card, and its mouth opens and closes while the narration is speaking. Ziggy introduces itself in every
intro ("It's Ziggy the Python here"). Look: dark editor theme, soft background music ducked under the voice.

## How every lesson is built

| Phase | Section(s) | What happens on screen |
|---|---|---|
| — | `INTRO` | Title card: lesson number, title, "In this lesson" goals, Ziggy slides in |
| **Study** | `STUDY` (1–3 cards) | The concept explained first, in detail: everyday analogy → precise idea → "Level up" point for older learners. Points, variable boxes, flow arrows, tables and code snippets pop in as Ziggy says them |
| **Study** | `CODE` (2–5 programs) | An editor window: every line is **typed character by character while Ziggy explains that line**, with syntax colours, a blinking caret, the current line highlighted and a speech-bubble note. Then **Run** is pressed and the real output (produced by actually running the program) appears in the output panel; typed answers to `input()` show in yellow, errors in red. Before most runs Ziggy asks "What do you think will happen?" (`@ predict`) and gives thinking time; deliberate mistakes are shown and fixed live |
| **Study** | `STUDY` (Common mistakes) | A table of the usual mistakes for the topic and what happens |
| **Revise** | `REVISE` | 4 ticked recap points |
| **Practice** | `PRACTICE` | Task card + hint + a 15–20 s countdown ("Pause and try it!") |
| **Practice** | `ANSWER` | The model answer typed line by line and run |
| — | `OUTRO` | "Up next" card |

The narration never mentions these phase names or any production notes, and it never splits the audience into
parents and children: everyone watching is a learner.

## Lessons

Lengths are measured with `eduvid pycourse render --timing` on the box (real voice and program runs). The full renders
match these to within a second or two.

### Module 1 — Getting Started (booklet ch. 1) · fully written
| # | Lesson | Key ideas | Programs typed line by line | Practice | Measured length |
|---|---|---|---|---|---|
| 1.1 | Meet Python | What a program is; Why we use a programming language; The editor, the Run button and the output; Text versus maths in Python | `first_steps.py`, `maths_machine.py` | Your turn | 8.31 min |
| 1.2 | Hello, World! | What a program is made of; How print shows text; Strings and comments; Python reads top to bottom | `hello.py`, `order_matters.py`, `quotes_and_commas.py`, `level_up.py` | Your turn | 9.04 min |
| 1.3 | Errors Are Clues | Why errors happen; How to read an error message; NameError, SyntaxError, IndentationError; Bugs that give no error at all | `bug_hunt.py`, `more_bugs.py`, `sneaky_bug.py` | Bug hunt | 8.71 min |
| 1.4 | Mini-Project: My Welcome Card | Plan a program before coding; Repeat a string with *; Line things up with spaces; Build a project step by step | `repeat_tricks.py`, `welcome_card.py`, `tree.py` | Your turn | 8.49 min |

### Module 2 — Variables, Input and Output (booklet ch. 2) · fully written
| # | Lesson | Key ideas | Programs typed line by line | Practice | Measured length |
|---|---|---|---|---|---|
| 2.1 | Variables: Labelled Boxes | What a variable is; = means store, not equals; Changing a variable's value; Printing variables with text | `variables.py`, `game_score.py`, `copy_boxes.py` | Pet profile | 8.85 min |
| 2.2 | Good Names and Constants | The rules for variable names; snake_case and other naming styles; Choosing meaningful names; Constants in CAPITALS | `names.py`, `mystery.py`, `constants.py` | Fix the names | 8.37 min |
| 2.3 | Strings: Playing with Text | What a string is; Joining strings with +; len(), .upper() and .lower(); Building sentences with f-strings | `strings.py`, `badge.py`, `shout.py`, `methods.py` | Name badge | 9.09 min |
| 2.4 | Asking Questions with input() | Input, process, output; How input() waits for an answer; Storing answers in variables; input() always gives text | `chat.py`, `robot.py`, `story.py`, `empty_answer.py` | Mini quiz | 8.35 min |
| 2.5 | Numbers: int and float | Whole numbers (int); Decimal numbers (float); Checking a type with type(); Converting with int(), float() and str() | `numbers.py`, `shopping.py`, `type_detective.py`, `conversions.py`, `value_error.py` | Pet calculator | 8.8 min |
| 2.6 | Maths with Python | The 7 maths operators; / versus //; Remainders with %; Order of operations and brackets | `maths.py`, `even_odd.py`, `shortcuts.py`, `pizza_party.py`, `surprises.py` | Minutes to hours | 9.48 min |
| 2.7 | True or False? | The bool type: True and False; Comparing with == != < >; = versus ==; and, or, not + truth tables | `true_false.py`, `password.py`, `compare_more.py`, `ride_check.py` | Warm day checker | 8.43 min |
| 2.8 | Comments and Clean Code | Why comments matter; Three rules for good comments; Planning with comment stubs; TODO notes | `pocket_money.py`, `turn_off.py`, `clean_up.py` | Screen time planner | 7.31 min |
| 2.9 | Mini-Project: Recipe Scaler | Plan a real program; Constants, variables and input together; Maths with floats; round() for neat answers | `scaler_v1.py`, `recipe_scaler.py`, `test_one_person.py`, `tidy_output.py` | Add an ingredient | 8.99 min |

### Module 3 — Collections (booklet ch. 3) · fully written
| # | Lesson | Key ideas | Programs typed line by line | Practice | Measured length |
|---|---|---|---|---|---|
| 3.1 | Lists: Many Things in One Box | Why we need lists; Making a list with [ ] and commas; Printing a list and counting it with len(); Lists and arrays | `snacks.py`, `games.py`, `weather.py` | My games | 8.29 min |
| 3.2 | Indexes and Slices | Index numbers start at 0; Negative indexes count from the end; Slices: from... up to but not including; Reading an IndexError | `planets.py`, `slices.py`, `word_slices.py` | First and last | 8.53 min |
| 3.3 | Changing Lists | Lists are mutable: they can change; append, insert, remove and pop; Changing an item by its index; sort, and checking with in | `shopping.py`, `top_scores.py`, `playlist.py`, `oops.py` | To-do list | 8.71 min |
| 3.4 | Going Through a List with for | What a loop is; for item in list: the loop variable; Indentation shows what belongs to the loop; Counting and totals with a loop | `snacks_loop.py`, `numbered.py`, `total.py`, `reset_bug.py`, `shout_list.py` | Score adder | 8.89 min |
| 3.5 | Grids: Lists Inside Lists | A list can hold other lists; grid[row][col]: two indexes; Changing one square; Printing a grid with a loop | `seats.py`, `board.py`, `score_table.py`, `pixel_art.py` | Change the centre | 8.42 min |
| 3.6 | Dictionaries | Keys and values; Looking up, adding and changing entries; Checking for a key with in; Looping through a dictionary | `capitals.py`, `safe_lookup.py`, `loop_dict.py`, `votes.py` | Pet sounds | 8.71 min |
| 3.7 | Records and Fields | What a record and a field are; A dictionary as a record; A list of records, like a table; Looping through records to make a report | `student.py`, `class_list.py`, `top_student.py` | Add a field | 7.26 min |
| 3.8 | Tuples and Sets | Tuples: ordered values that can't change; Unpacking a tuple; Sets: no duplicates, no order; Union, intersection and difference | `tuples.py`, `swap.py`, `unique_names.py`, `fruit_venn.py` | Unique fruits | 8.23 min |
| 3.9 | Mini-Project: Daily Task Planner | Choose the right data structure; Store tasks as a list of records; Totals and counts with a loop; Build and test a project in stages | `planner_v1.py`, `planner_v2.py`, `planner_v3.py`, `time_left.py` | Time left | 8.05 min |

### Module 4 — Making Decisions and Loops (booklet ch. 4) · fully written
| # | Lesson | Key ideas | Programs typed line by line | Practice | Measured length |
|---|---|---|---|---|---|
| 4.1 | Sequence and Flowcharts | What an algorithm is; The three building blocks: sequence, selection, iteration; Flowchart shapes; Turning a flowchart into code | `morning.py`, `sandwich.py` | An everyday algorithm | 7.42 min |
| 4.2 | if: Making a Choice | Selection: choosing what runs; if condition: then an indented block; The colon and indentation; Conditions with input and variables | `ride.py`, `bonus.py`, `password_check.py` | Ride check | 7.55 min |
| 4.3 | if / else | Two paths: exactly one runs; else has no condition; Even or odd with %; Choosing between if/else and two ifs | `even_odd.py`, `quiz.py`, `two_ifs.py` | Pass or fail | 5.81 min |
| 4.4 | elif: Many Choices | More than two choices with elif; The first True condition wins; Why the order of conditions matters; Using else as a catch-all | `grades.py`, `wrong_order.py`, `weather.py` | Traffic light | 6.53 min |
| 4.5 | Complex and Nested Conditions | and, or, not inside if statements; Brackets and named booleans for clear conditions; Nested ifs: a decision inside a decision; Choosing between nesting and and | `ride_rules.py`, `weekend_bug.py`, `login.py`, `delivery.py` | Club entry | 8.25 min |
| 4.6 | match / case | Choosing between exact values with match; case _ as the default; Several values in one case with /; When to use match and when to use elif | `day_name.py`, `calculator.py`, `commands.py` | Snack menu | 6.86 min |
| 4.7 | while Loops | Iteration with a condition; while condition: repeat the block; Counters that change each time round; Avoiding infinite loops | `countdown.py`, `savings.py`, `password_loop.py`, `halving.py` | Keep asking | 7.91 min |
| 4.8 | for Loops and range() | Repeat an exact number of times; range(stop), range(start, stop), range(start, stop, step); Looping over strings; Loops inside loops | `range_demo.py`, `times_table.py`, `letters.py`, `triangle.py` | Stars triangle | 7.98 min |
| 4.9 | Loop Control and Validation | break: leave a loop early; continue: skip to the next repeat; while True + break (do-while / repeat-until); Validating input with .isdigit() | `find_it.py`, `skip_it.py`, `menu.py`, `validate.py` | Quit on q | 7.88 min |
| 4.10 | Mini-Project: Guess the Number | Random numbers with the random module; A game loop with if / elif / else; Counting guesses and setting a limit; Validating every guess | `guess_v1.py`, `guess_v2.py`, `guess_final.py` | Your version | 8.58 min |

### Module 5 — Next Steps (beyond the booklet) · fully written
| # | Lesson | Key ideas | Programs typed line by line | Practice | Measured length |
|---|---|---|---|---|---|
| 5.1 | Functions: Your Own Commands | What a function is and why we use them; def, the colon and the indented body; Defining vs calling; Functions calling other functions | `hello_function.py`, `banner.py`, `song.py` | Banner function | 7.28 min |
| 5.2 | Parameters and return | Parameters: information going in; Parameters vs arguments; return: an answer coming out; return vs print | `greet.py`, `area.py`, `print_vs_return.py`, `converter.py` | Converter | 8.47 min |
| 5.3 | Python's Toolbox: Modules | What a module is and how import works; random: randint, choice, shuffle; math: sqrt, pi, ceil, floor; datetime: dates and days between them | `dice.py`, `random_tools.py`, `maths_tools.py`, `birthday.py` | Compliment generator | 8.18 min |
| 5.4 | Testing Your Code | Smoke tests and test plans; Normal, boundary and invalid test data; assert: tests that check themselves; Using a failing test to find and fix a bug | `test_is_even.py`, `test_can_ride.py`, `valid_rating.py` | Test area() | 7.67 min |
| 5.5 | Coding with AI, Wisely | What AI coding helpers can and can't do; Ask, read, test, understand: checking suggestions; Finding a bug in AI-written code; Honesty and privacy when using AI | `ai_biggest.py`, `ai_average.py` | Fix the suggestion | 7.87 min |
| 5.6 | Final Project: Big Five Wellbeing Check-In | Turn a design brief into a plan; Plan with stubs, then build one piece at a time; Combine functions, loops, validation, a dictionary and if/elif; Test the finished program | `checkin_plan.py`, `get_rating.py`, `feedback.py`, `wellbeing_checkin.py` | Make it your own | 11.7 min |

**Totals:** 38 lessons (4 + 9 + 9 + 10 + 6), all fully scripted in `lessons/`. Measured with `eduvid pycourse render --timing` (real Kokoro voice at speed 0.92, real program runs): 5.8 to 11.7 min per lesson, 313 min in total (about 5.2 hours). There is no target length: each lesson is as long as its content needs.

## Writing rules used in every script
* Concept first, code second. Every STUDY card: an everyday analogy a 7-year-old follows, then the precise idea, then a **Level up** point for teens.
* Narration explains each line **as it is typed**; the on-screen note (`@ line N | note`) is a short label, never a copy of the narration.
* Every program is real: the output on screen is produced by running it. `eduvid pycourse check` runs them all.
* Deliberate mistakes are shown and fixed live in most lessons so learners see real error messages; every lesson has a Common mistakes card.
* Predict-then-run: before a run, Ziggy asks what will happen and pauses so learners can think.
* No length target: a lesson is as long as its content needs. Lengths in the tables are measured, not planned.
* Exercises have a pause/countdown, a hint, and an answer typed and run on screen.
* Numbers in narration are written as words where the TTS could misread symbols; no symbols like `=` or `-` in spoken text.
