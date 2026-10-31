# Live Coding – Lesson 14 List methods and for

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/17_*.py`.

## live_01 – Inventory

**Type this slowly, saying each part out loud:**

```python
inventory = ["sword", "shield", "armor", "bow"]
inventory.append("health potion")
inventory.insert(1, "golden sword")
inventory.remove("shield")
dropped = inventory.pop()
print(inventory)
print("Dropped", dropped)
print("Count", len(inventory))
```

**Expected output** (Run ▶ / F5):
```
['sword', 'golden sword', 'armor', 'bow']
Dropped health potion
Count 4
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Visit every item

**Type this slowly, saying each part out loud:**

```python
for item in inventory:
    print("You have a", item)
```

**What to say:**
- For is "for each".
- We go deeper in lesson 25.

**Expected output** (Run ▶ / F5):
```
You have a sword
You have a golden sword
You have a armor
You have a bow
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 14 — Add, remove, loop a list

Book 3.1.8–3.1.9. Length: 12 min. File: `inventory.py`.

1. `append` adds at the end. `insert(place, item)` squeezes in. `remove(value)` drops the first match. `pop()` drops the last and hands it back. `len`, `max`, `min`.
2. SWITCH. Inventory, not the age example. Easier to say out loud.

```python
inventory = ["sword", "shield", "armor", "bow"]
inventory.append("health potion")
inventory.insert(1, "golden sword")
inventory.remove("shield")
dropped_item = inventory.pop()
print(inventory)
print("Dropped:", dropped_item)
print("Count:", len(inventory))
```

Walk the list after each line if you can. Append, then insert, then remove, then pop.
3. A `for` loop visits every item. We go deeper in video 22. Today, just visit.

```python
for item in inventory:
    print("You have a", item)
```

`range(4)` is 0, 1, 2, 3. Prefer `for item in inventory` when you do not need the index.
4. Your turn: start with three school items, append one, pop one, print what is left. Next: slices.
