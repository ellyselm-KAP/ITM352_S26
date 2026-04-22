import json
import os

folder = os.path.dirname(__file__)
file_path = os.path.join(folder, "questions.json")

with open(file_path) as f:
    data = json.load(f)

print(data[0]["question"])
