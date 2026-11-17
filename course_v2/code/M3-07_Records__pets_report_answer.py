# M3-07_Records - pets_report.py
pets = [{"name": "Biscuit", "type": "dog"},
        {"name": "Luna", "type": "cat"}]
pets[0]["age"] = 4
pets[1]["age"] = 2
for p in pets:
    print(f"{p['name']} the {p['type']} is {p['age']}")
