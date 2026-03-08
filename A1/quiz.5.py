# Quiz game. Version 5
# Name : Ellyse McChesney
# Date : Feb. 24, 2026
# Improve usability and keep track of score

from string import ascii_lowercase


QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Dallas", "Houston", "San Antonio"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}


num_correct = 0

for num, (question, options) in enumerate(QUESTIONS.items(), start=1):

    print()
    print(f"Question {num}:")
    print(question)

    correct_answer = options[0]  # first option is the correct one

    # Create dictionary that maps letters to answers
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(options)))

    for label, alternative in labeled_alternatives.items():
        print(f"{label}. {alternative}")

    answer_label = input("Choice? ").lower()

    # Make sure the user enters a valid label
    while answer_label not in labeled_alternatives:
        print("Please enter one of the letters shown.")
        answer_label = input("Choice? ").lower()

    answer = labeled_alternatives.get(answer_label)

    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is '{correct_answer}' not '{answer}'")

print()
print(f"You got {num_correct} out of {len(QUESTIONS)} correct.")
