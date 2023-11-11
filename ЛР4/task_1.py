# TODO решите задачу
import json

def task() -> float:
    file = "input.json"
    with open(file) as file:
        data = json.load(file)

    sum_values = sum([entry["score"] * entry["weight"] for entry in data])
    return round(sum_values, 3)

print(task())
