# M3-09_Task_Planner - still_to_do.py
tasks = [
    {"name": "Homework", "minutes": 40, "done": True},
    {"name": "Practise piano", "minutes": 20, "done": False},
    {"name": "Walk the dog", "minutes": 30, "done": True},
    {"name": "Read", "minutes": 25, "done": False},
]
tasks.append({"name": "Tidy room", "minutes": 15, "done": False})
not_done = 0
minutes_left = 0
for task in tasks:
    if not task["done"]:
        not_done += 1
        minutes_left += task["minutes"]
print(f"{not_done} tasks to go, {minutes_left} minutes")
