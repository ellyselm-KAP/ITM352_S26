# Quiz game. Version 6
# Name : Ellyse McChesney
# Date : Feb. 24, 2026
# Randomize the question order and the answer order

import random
from string import ascii_lowercase

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Dallas", "Houston", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

num_correct = 0

# Turn the dictionary into a list first so it can be shuffled
question_list = list(QUESTIONS.items())
random.shuffle(question_list)

question_number = 1

for question, options in question_list:
    print()
    print("Question", question_number)
    print(question)

    correct_answer = options[0]

    # Copy the options so the original list does not get changed
    mixed_options = options[:]
    random.shuffle(mixed_options)

    labeled_alternatives = {}
    index = 0

    # Match each answer choice with a letter
    for option in mixed_options:
        labeled_alternatives[ascii_lowercase[index]] = option
        index += 1

    for label, alternative in labeled_alternatives.items():
        print(f"{label}. {alternative}")

    answer_label = input("Your answer: ").lower()

    while answer_label not in labeled_alternatives:
        print("Please enter one of the letters shown.")
        answer_label = input("Your answer: ").lower()

    answer = labeled_alternatives[answer_label]

    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print("Incorrect.")
        print("The correct answer was:", correct_answer)

    question_number += 1

print()
print("You got", num_correct, "out of", len(QUESTIONS), "correct.")

