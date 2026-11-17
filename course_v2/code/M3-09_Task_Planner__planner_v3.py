# M3-09_Task_Planner - planner_v3.py
tasks = [
    {"name": "Homework", "minutes": 40, "done": True},
    {"name": "Read", "minutes": 25, "done": False},
]
name = input("New task: ")
minutes = int(input("How many minutes? "))
tasks.append({"name": name, "minutes": minutes, "done": False})
tasks[1]["done"] = True
for task in tasks:
    mark = "x" if task["done"] else " "
    print(f"[{mark}] {task['name']} ({task['minutes']} min)")
