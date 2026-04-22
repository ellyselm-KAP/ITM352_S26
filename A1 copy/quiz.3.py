# Quiz game. First version.
# Name : Ellyse McChesney
# Date : Feb. 24, 2026
# Make QUESTIONS a dictionary, to include answer options and the correct choice.

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Dallas", "Houston", "San Antonio"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

for question, options in QUESTIONS.items():
    print()
    print(question)

    correct_answer = options[0]  # The first option is the correct answer
    sorted_options = sorted(options)

    for label, alternative in enumerate(sorted_options, start=1):
        print(f"{label}. {alternative}")

    answer = input("Your answer: ")

    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}' not '{answer}'")