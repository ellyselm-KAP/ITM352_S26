# Read the JSON file created in question 5 and print it

import json

with open("quiz_questions.json", "r") as file_object:
    quiz_data = json.load(file_object)

for item in quiz_data:
    print("Question:", item["question"])
    print("Options:", item["options"])
    print("Answer:", item["answer"])
    print()

    