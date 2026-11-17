# M3-09_Task_Planner - planner_v1.py
# Daily task planner - step 1: the data
tasks = [
    {"name": "Homework", "minutes": 40, "done": True},
    {"name": "Practise piano", "minutes": 20, "done": False},
    {"name": "Walk the dog", "minutes": 30, "done": True},
    {"name": "Read", "minutes": 25, "done": False},
]
for task in tasks:
    mark = "x" if task["done"] else " "
    print(f"[{mark}] {task['name']} ({task['minutes']} min)")
