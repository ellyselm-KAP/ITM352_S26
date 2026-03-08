# Quiz game. Version 8
# Name : Ellyse McChesney
# Date : Feb. 24, 2026
# Separate program to create quiz questions and save them to a JSON file

import json


def main():
    questions = []

    print("Question Builder")
    print()

    keep_going = "yes"

    while keep_going == "yes":
        question_text = input("Enter the question: ")

        options = []

        for number in range(1, 5):
            if number == 1:
                choice = input("Enter choice 1 (correct answer): ")
            else:
                choice = input(f"Enter choice {number}: ")

            options.append(choice)

        question_data = {
            "question": question_text,
            "options": options,
            "answer": options[0]
        }

        questions.append(question_data)

        print()
        keep_going = input("Add another question? (yes/no): ").lower()
        print()

    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)

    print("Questions saved to questions.json")


main()