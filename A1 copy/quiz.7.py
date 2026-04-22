# Quiz game. Version 7
# Name : Ellyse McChesney
# Date : Feb. 24, 2026
# Refactor the quiz using functions

import random
from string import ascii_lowercase


QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Dallas", "Houston", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}


def ask_question(question, options):

    correct_answer = options[0]

    mixed_options = options[:]
    random.shuffle(mixed_options)

    labeled_alternatives = {}
    index = 0

    for option in mixed_options:
        labeled_alternatives[ascii_lowercase[index]] = option
        index += 1

    print(question)

    for label, alternative in labeled_alternatives.items():
        print(f"{label}. {alternative}")

    answer_label = input("Your answer: ").lower()

    while answer_label not in labeled_alternatives:
        print("Please enter one of the letters shown.")
        answer_label = input("Your answer: ").lower()

    answer = labeled_alternatives[answer_label]

    if answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print("Incorrect.")
        print("The correct answer was:", correct_answer, "\n")
        return False


def run_quiz():

    num_correct = 0

    question_list = list(QUESTIONS.items())
    random.shuffle(question_list)

    question_number = 1

    for question, options in question_list:

        print("Question", question_number)

        if ask_question(question, options):
            num_correct += 1

        question_number += 1

    print("You got", num_correct, "out of", len(QUESTIONS), "correct.")


def main():
    print("Welcome to the quiz!\n")
    run_quiz()


main()
