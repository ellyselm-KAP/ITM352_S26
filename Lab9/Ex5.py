# Write a program that takes a dictionary of quiz questions
# and saves it as a JSON file

import json

quiz_questions = [
    {
        "question": "What is the capital of Texas?",
        "options": ["Austin", "Dallas", "Houston", "San Antonio"],
        "answer": "Austin"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "Who painted The Last Supper?",
        "options": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"],
        "answer": "Da Vinci"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
        "answer": "Pacific"
    }
]

with open("quiz_questions.json", "w") as file_object:
    json.dump(quiz_questions, file_object, indent=4)

print("Quiz questions saved to quiz_questions.json")

