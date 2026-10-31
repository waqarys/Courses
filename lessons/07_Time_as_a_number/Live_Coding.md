# Live Coding – Lesson 07 Time as a number

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/10_*.py`.

## live_01 – Now

**Type this slowly, saying each part out loud:**

```python
from time import time, ctime
current_time = time()
print(current_time)
print(ctime(current_time))
```

**Expected output** (Run ▶ / F5):
```
1793469197.217821
Sat Oct 31 23:23:17 2026
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Years since 1970

**Type this slowly, saying each part out loud:**

```python
seconds_in_a_year = 365.25 * 24 * 60 * 60
years = current_time / seconds_in_a_year
print(years)
```

**What to say:**
- 365.25 covers leap years.
- This year minus 1970 should be close.

**Expected output** (Run ▶ / F5):
```
1793469197.2354603
Sat Oct 31 23:23:17 2026
56.83160941375327
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 07 — Time as a number

Book 2.2.3. Length: 8 min. File: `time_stamp.py`. Keep it light.

1. A timestamp is a count of seconds since 1 January 1970, UTC. A giant stopwatch.
2. SWITCH.

```python
from time import time, ctime

current_time = time()
print(current_time)
print(ctime(current_time))
```

3. Years since 1970. There are about 31557600 seconds in a year (365.25 days).

```python
seconds_in_a_year = 365.25 * 24 * 60 * 60
years_since_1970 = current_time / seconds_in_a_year
print(years_since_1970)
```

4. Check: this year minus 1970 should be close to that number. A fraction is fine. It is not January 1st anymore.
5. Your turn: print how many seconds are in one day (`24 * 60 * 60`). Next: True and False.
