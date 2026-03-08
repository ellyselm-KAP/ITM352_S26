import json
import random
import os
from string import ascii_lowercase


def load_questions():
    folder = os.path.dirname(__file__)
    file_path = os.path.join(folder, "questions.json")

    with open(file_path, "r") as file:
        questions = json.load(file)

    return questions


def get_score_history():
    history = []
    folder = os.path.dirname(__file__)
    file_path = os.path.join(folder, "score_history.txt")

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if line != "":
                    parts = line.split(",")

                    if len(parts) == 3:
                        username = parts[0]
                        score = int(parts[1])
                        total = int(parts[2])
                        history.append((username, score, total))
    except FileNotFoundError:
        pass

    return history


def save_score(username, score, total):
    folder = os.path.dirname(__file__)
    file_path = os.path.join(folder, "score_history.txt")

    with open(file_path, "a") as file:
        file.write(f"{username},{score},{total}\n")


def check_high_score(username, score, history):
    personal_best = 0
    grand_best = 0
    grand_champion = ""

    for old_username, old_score, old_total in history:
        if old_username == username and old_score > personal_best:
            personal_best = old_score

        if old_score > grand_best:
            grand_best = old_score
            grand_champion = old_username

    if score > personal_best:
        print("New personal high score!")

    if score > grand_best:
        print("You are now the grand champion!")
    elif grand_champion != "":
        print("Current grand champion:", grand_champion, "with", grand_best, "points.")


def ask_question(question_data, superpower_used):
    print()
    print(question_data["question"])

    correct_answer = question_data["answer"]

    options = question_data["options"][:]
    random.shuffle(options)

    labeled_alternatives = {}
    index = 0

    for option in options:
        labeled_alternatives[ascii_lowercase[index]] = option
        index += 1

    for label, alternative in labeled_alternatives.items():
        print(f"{label}. {alternative}")

    if not superpower_used:
        print("Type 'superpower' if you want to use your one-time 50/50 help.")

    answer_label = input("Your answer: ").lower()

    while True:
        if answer_label == "superpower" and not superpower_used:
            print("Superpower activated!")

            wrong_answers = []

            for option in options:
                if option != correct_answer:
                    wrong_answers.append(option)

            random.shuffle(wrong_answers)

            reduced_options = [correct_answer, wrong_answers[0]]
            random.shuffle(reduced_options)

            labeled_alternatives = {}
            index = 0

            for option in reduced_options:
                labeled_alternatives[ascii_lowercase[index]] = option
                index += 1

            for label, alternative in labeled_alternatives.items():
                print(f"{label}. {alternative}")

            superpower_used = True
            answer_label = input("Your answer: ").lower()

        elif answer_label in labeled_alternatives:
            break

        else:
            print("Please enter one of the letters shown.")
            if not superpower_used:
                print("Or type 'superpower' if you want to use it.")
            answer_label = input("Your answer: ").lower()

    answer = labeled_alternatives[answer_label]

    if answer == correct_answer:
        print("Correct!")
        return True, superpower_used
    else:
        print("Incorrect.")
        print("The correct answer was:", correct_answer)
        return False, superpower_used


def run_quiz(questions):
    num_correct = 0
    superpower_used = False

    random.shuffle(questions)

    question_number = 1

    for question_data in questions:
        print()
        print("Question", question_number)

        got_it_right, superpower_used = ask_question(question_data, superpower_used)

        if got_it_right:
            num_correct += 1

        question_number += 1

    return num_correct


def main():
    print("Welcome to the quiz game!")
    username = input("Enter your username: ")

    questions = load_questions()
    history = get_score_history()

    score = run_quiz(questions)
    total = len(questions)

    print()
    print("Quiz complete.")
    print("Final score:", score, "out of", total)

    check_high_score(username, score, history)
    save_score(username, score, total)


main()