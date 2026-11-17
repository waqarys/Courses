# M3-09_Task_Planner - time_left.py
DAY_START = 16 * 60
BEDTIME = 21 * 60
free = BEDTIME - DAY_START
planned = 40 + 20 + 30 + 25
spare = free - planned
print(f"Free time: {free} minutes")
print(f"Planned: {planned} minutes")
print(f"Spare: {spare // 60} h {spare % 60} min")
