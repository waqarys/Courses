# Live Coding – Lesson 11 Pancake calculator

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/14_*.py`.

## live_01 – The program

**Type this slowly, saying each part out loud:**

```python
STANDARD_SERVINGS = 4
flour_cups = 2.5
sugar_tablespoons = 3
eggs_count = 2
milk_liters = 0.5
is_vegetarian = True
desired_servings = 6
scaling_factor = desired_servings / STANDARD_SERVINGS
print("Flour", flour_cups * scaling_factor)
print("Sugar", sugar_tablespoons * scaling_factor)
print("Eggs", eggs_count * scaling_factor)
print("Milk", milk_liters * scaling_factor)
```

**Expected output** (Run ▶ / F5):
```
Flour 3.75
Sugar 4.5
Eggs 3.0
Milk 0.75
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Ask, do not hard-code

**Type this slowly, saying each part out loud:**

```python
desired_servings = int(input("How many servings? "))
```

**What to say:**
- Replace the old 6.
- Run it with 8.

**Expected output** (Run ▶ / F5):
```
How many servings? ValueError: invalid literal for int() with base 10: 'Sam'
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 11 — Project: pancake calculator

Book 2.7. Length: 12 min. File: `pancake_recipe.py`. This is the first project they can finish.

1. A recipe for 4 people. We scale it to 6. Constants shout. Variables whisper in snake_case.
2. SWITCH. Type the whole program. Run it.

```python
# Scales a 4-serve pancake recipe

STANDARD_SERVINGS = 4

flour_cups = 2.5
sugar_tablespoons = 3
eggs_count = 2
milk_liters = 0.5
is_vegetarian = True

desired_servings = 6
scaling_factor = desired_servings / STANDARD_SERVINGS

new_flour = flour_cups * scaling_factor
new_sugar = sugar_tablespoons * scaling_factor
new_eggs = eggs_count * scaling_factor
new_milk = milk_liters * scaling_factor

print("New recipe amounts")
print("Flour:", new_flour, "cups")
print("Sugar:", new_sugar, "tablespoons")
print("Eggs:", new_eggs)
print("Milk:", new_milk, "liters")
print("Vegetarian:", is_vegetarian)
```

3. Point at types: flour is float, eggs is int, `is_vegetarian` is bool, the word `"cups"` is a string. `new_flour` becomes float because of `/`.
4. Ask for servings instead of hard-coding 6.

```python
desired_servings = int(input("How many servings? "))
```

Replace the old line. Run with 8.
5. Survey add-on, short:

```python
pancakes_per_month = 12
price = 3.50
monthly_revenue = pancakes_per_month * price
print("Monthly revenue: $", monthly_revenue)
print("*" * 20)
```

6. Your turn: change the price, or add a topping string and print it. Next: a 5-question check-in.
