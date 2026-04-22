from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import json
import random
import os
import time

app = Flask(__name__)
app.secret_key = "quiz_secret_key"


def load_questions():
    folder = os.path.dirname(__file__)
    file_path = os.path.join(folder, "questions.json")

    try:
        with open(file_path, "r") as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def load_scores():
    folder = os.path.dirname(__file__)
    file_path = os.path.join(folder, "scores.json")

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_scores(scores):
    folder = os.path.dirname(__file__)
    file_path = os.path.join(folder, "scores.json")

    with open(file_path, "w") as file:
        json.dump(scores, file, indent=4)


def get_weakest_category(answer_history):
    missed_categories = {}

    for item in answer_history:
        if not item["was_correct"]:
            category = item.get("category", "Unknown")
            missed_categories[category] = missed_categories.get(category, 0) + 1

    if not missed_categories:
        return "None - great job!"

    weakest = max(missed_categories, key=missed_categories.get)
    return weakest


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/start", methods=["POST"])
def start():
    questions = load_questions()

    if not questions:
        return "Error: Could not load questions.", 500

    random.shuffle(questions)

    for question in questions:
        random.shuffle(question["options"])

    session["questions"] = questions
    session["current_index"] = 0
    session["score"] = 0
    session["start_time"] = time.time()
    session["answer_history"] = []

    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    questions = session.get("questions", [])
    current_index = session.get("current_index", 0)

    if not questions:
        return redirect(url_for("home"))

    if current_index >= len(questions):
        return redirect(url_for("results"))

    if request.method == "POST":
        selected_answer = request.form.get("answer")
        current_question = questions[current_index]
        correct_answer = current_question["answer"]
        was_correct = (selected_answer == correct_answer)

        session["selected_answer"] = selected_answer
        session["correct_answer"] = correct_answer
        session["was_correct"] = was_correct
        session["explanation"] = current_question.get("explanation", "No explanation provided.")

        if was_correct:
            session["score"] = session.get("score", 0) + 1

        answer_history = session.get("answer_history", [])
        answer_history.append({
            "question": current_question["question"],
            "selected_answer": selected_answer,
            "correct_answer": correct_answer,
            "was_correct": was_correct,
            "category": current_question.get("category", "Unknown"),
            "explanation": current_question.get("explanation", "")
        })
        session["answer_history"] = answer_history

        return redirect(url_for("feedback"))

    current_question = questions[current_index]
    return render_template(
        "quiz.html",
        question=current_question,
        question_number=current_index + 1,
        total_questions=len(questions)
    )


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    questions = session.get("questions", [])
    current_index = session.get("current_index", 0)

    if request.method == "POST":
        current_index += 1
        session["current_index"] = current_index

        if current_index >= len(questions):
            return redirect(url_for("results"))
        return redirect(url_for("quiz"))

    return render_template(
        "feedback.html",
        was_correct=session.get("was_correct"),
        selected_answer=session.get("selected_answer"),
        correct_answer=session.get("correct_answer"),
        explanation=session.get("explanation")
    )


@app.route("/results", methods=["GET", "POST"])
def results():
    score = session.get("score", 0)
    questions = session.get("questions", [])
    total = len(questions)
    answer_history = session.get("answer_history", [])

    correct_count = score
    incorrect_count = total - score

    start_time = session.get("start_time")
    if start_time:
        time_taken = round(time.time() - start_time, 2)
    else:
        time_taken = 0

    weakest_category = get_weakest_category(answer_history)

    if request.method == "POST":
        username = request.form.get("username", "").strip()

        if username == "":
            return render_template(
                "results.html",
                score=score,
                total=total,
                correct_count=correct_count,
                incorrect_count=incorrect_count,
                time_taken=time_taken,
                weakest_category=weakest_category,
                error="Please enter your name."
            )

        scores = load_scores()
        scores.append({
            "name": username,
            "score": score,
            "total": total,
            "time_taken": time_taken
        })
        save_scores(scores)

        return redirect(url_for("leaderboard"))

    return render_template(
        "results.html",
        score=score,
        total=total,
        correct_count=correct_count,
        incorrect_count=incorrect_count,
        time_taken=time_taken,
        weakest_category=weakest_category
    )


@app.route("/leaderboard")
def leaderboard():
    scores = load_scores()
    sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)
    top_scores = sorted_scores[:10]

    return render_template("leaderboard.html", scores=top_scores)

@app.route("/review")
def review():
    answer_history = session.get("answer_history", [])
    missed_questions = [item for item in answer_history if not item["was_correct"]]

    return render_template("review.html", missed_questions=missed_questions)

# API routes
@app.route("/api/questions", methods=["GET"])
def api_questions():
    questions = load_questions()
    return jsonify(questions)


@app.route("/api/scores", methods=["GET"])
def api_scores():
    scores = load_scores()
    return jsonify(scores)


@app.route("/api/scores", methods=["POST"])
def api_add_score():
    data = request.get_json()

    if not data or "name" not in data or "score" not in data or "total" not in data:
        return jsonify({"error": "Invalid score data"}), 400

    scores = load_scores()
    scores.append(data)
    save_scores(scores)

    return jsonify({"message": "Score saved successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)