import json
import os
import unittest

from app import app


class QuizAppTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

        # Make sure scores.json exists for tests
        self.scores_path = os.path.join(os.path.dirname(__file__), "scores.json")
        if not os.path.exists(self.scores_path):
            with open(self.scores_path, "w") as file:
                json.dump([], file)

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Quiz Game", response.data)

    def test_start_quiz_redirects(self):
        response = self.client.post("/start", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/quiz", response.headers["Location"])

    def test_quiz_page_loads_after_start(self):
        with self.client as client:
            client.post("/start")
            response = client.get("/quiz")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Question", response.data)

    def test_feedback_page_loads_after_answer(self):
        with self.client as client:
            client.post("/start")
            client.get("/quiz")

            with client.session_transaction() as session:
                questions = session["questions"]
                current_question = questions[0]
                correct_answer = current_question["answer"]

            response = client.post("/quiz", data={"answer": correct_answer}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b"Correct" in response.data or b"Incorrect" in response.data)

    def test_results_page_loads(self):
        with self.client as client:
            client.post("/start")

            with client.session_transaction() as session:
                session["current_index"] = len(session["questions"])
                session["score"] = 0
                session["answer_history"] = []
                session["start_time"] = 0

            response = client.get("/results")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Quiz Complete", response.data)

    def test_leaderboard_page_loads(self):
        response = self.client.get("/leaderboard")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Leaderboard", response.data)

    def test_api_questions_returns_json(self):
        response = self.client.get("/api/questions")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)

        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_api_scores_returns_json(self):
        response = self.client.get("/api/scores")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)

        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_api_scores_post_adds_score(self):
        new_score = {
            "name": "TestUser",
            "score": 3,
            "total": 5
        }

        response = self.client.post("/api/scores", json=new_score)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.is_json)

        data = response.get_json()
        self.assertIn("message", data)

    def test_results_rejects_blank_username(self):
        with self.client as client:
            client.post("/start")

            with client.session_transaction() as session:
                session["score"] = 2
                session["questions"] = [{"question": "Test"}]
                session["answer_history"] = []
                session["start_time"] = 0

            response = client.post("/results", data={"username": ""})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Please enter your name", response.data)


if __name__ == "__main__":
    unittest.main()