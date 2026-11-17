# M3-09_Task_Planner - planner_v2.py
tasks = [
    {"name": "Homework", "minutes": 40, "done": True},
    {"name": "Practise piano", "minutes": 20, "done": False},
    {"name": "Walk the dog", "minutes": 30, "done": True},
    {"name": "Read", "minutes": 25, "done": False},
]
total = 0
done_count = 0
left = 0
for task in tasks:
    total += task["minutes"]
    if task["done"]:
        done_count += 1
    else:
        left += task["minutes"]
print(f"{len(tasks)} tasks, {total} minutes in total")
print(f"Done: {done_count} of {len(tasks)}")
print(f"Still to do: {left} minutes")
