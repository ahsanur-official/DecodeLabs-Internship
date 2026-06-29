from datetime import datetime
import re

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


QUESTIONS = [
    {
        "id": "q1",
        "text": "What is the capital city of France?",
        "valid_answers": ["paris"],
        "category": "Geography",
        "difficulty": "Easy",
        "points": 10,
        "explanation": "Paris is the capital and largest city of France.",
    },
    {
        "id": "q2",
        "text": "Which planet is known as the Red Planet?",
        "valid_answers": ["mars"],
        "category": "Science",
        "difficulty": "Easy",
        "points": 10,
        "explanation": "Mars looks red because iron minerals in its soil oxidize.",
    },
    {
        "id": "q3",
        "text": "What is the largest ocean on Earth?",
        "valid_answers": ["pacific", "pacific ocean"],
        "category": "Geography",
        "difficulty": "Medium",
        "points": 10,
        "explanation": "The Pacific Ocean is the largest and deepest ocean basin.",
    },
    {
        "id": "q4",
        "text": "What is the chemical symbol for Gold?",
        "valid_answers": ["au"],
        "category": "Chemistry",
        "difficulty": "Medium",
        "points": 10,
        "explanation": "Gold's symbol is Au, from the Latin word aurum.",
    },
    {
        "id": "q5",
        "text": "Who wrote 'Romeo and Juliet'?",
        "valid_answers": ["shakespeare", "william shakespeare"],
        "category": "Literature",
        "difficulty": "Medium",
        "points": 10,
        "explanation": "William Shakespeare wrote the tragedy Romeo and Juliet.",
    },
    {
        "id": "q6",
        "text": "What is the hardest natural substance on Earth?",
        "valid_answers": ["diamond"],
        "category": "Science",
        "difficulty": "Easy",
        "points": 10,
        "explanation": "Diamond is the hardest naturally occurring material.",
    },
    {
        "id": "q7",
        "text": "How many continents are there on Earth?",
        "valid_answers": ["7", "seven"],
        "category": "Geography",
        "difficulty": "Easy",
        "points": 10,
        "explanation": "The common model counts seven continents.",
    },
    {
        "id": "q8",
        "text": "What is the freezing point of water in Celsius?",
        "valid_answers": ["0", "zero"],
        "category": "Science",
        "difficulty": "Easy",
        "points": 10,
        "explanation": "Pure water freezes at 0 degrees Celsius at standard pressure.",
    },
    {
        "id": "q9",
        "text": "Which element do humans need to breathe?",
        "valid_answers": ["oxygen", "o2"],
        "category": "Biology",
        "difficulty": "Easy",
        "points": 10,
        "explanation": "Humans need oxygen for cellular respiration.",
    },
    {
        "id": "q10",
        "text": "What is the largest mammal in the world?",
        "valid_answers": ["blue whale", "whale"],
        "category": "Biology",
        "difficulty": "Medium",
        "points": 10,
        "explanation": "The blue whale is the largest known mammal.",
    },
]


def normalize_answer(value):
    cleaned = (value or "").strip().lower()
    return re.sub(r"\s+", " ", cleaned)


def safe_question(question):
    return {
        "id": question["id"],
        "text": question["text"],
        "category": question["category"],
        "difficulty": question["difficulty"],
        "points": question["points"],
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/questions", methods=["GET"])
def get_questions():
    categories = sorted({question["category"] for question in QUESTIONS})
    total_points = sum(question["points"] for question in QUESTIONS)

    return jsonify(
        {
            "questions": [safe_question(question) for question in QUESTIONS],
            "meta": {
                "title": "Knowledge Diagnostic",
                "total_questions": len(QUESTIONS),
                "total_points": total_points,
                "categories": categories,
            },
        }
    )


@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    user_data = request.get_json(silent=True) or {}
    score = 0
    earned_points = 0
    total = len(QUESTIONS)
    total_points = sum(question["points"] for question in QUESTIONS)
    feedback = []
    categories = {}

    for index, question in enumerate(QUESTIONS, start=1):
        raw_input = user_data.get(question["id"], "")
        clean_input = normalize_answer(raw_input)
        valid_answers = [normalize_answer(answer) for answer in question["valid_answers"]]
        is_correct = clean_input in valid_answers
        category = question["category"]

        categories.setdefault(
            category, {"correct": 0, "total": 0, "earned_points": 0, "total_points": 0}
        )
        categories[category]["total"] += 1
        categories[category]["total_points"] += question["points"]

        if is_correct:
            score += 1
            earned_points += question["points"]
            categories[category]["correct"] += 1
            categories[category]["earned_points"] += question["points"]

        feedback.append(
            {
                "q": index,
                "id": question["id"],
                "text": question["text"],
                "category": category,
                "difficulty": question["difficulty"],
                "points": question["points"],
                "status": "correct" if is_correct else "incorrect",
                "user_answer": raw_input.strip() or "No answer",
                "correct_answer": question["valid_answers"][0].title(),
                "explanation": question["explanation"],
            }
        )

    percentage = round((score / total) * 100)
    point_percentage = round((earned_points / total_points) * 100)

    if percentage == 100:
        grade = "S-Rank Master"
        badge = "badge-s"
        message = "Perfect score. Excellent command of the material."
    elif percentage >= 80:
        grade = "A-Rank Expert"
        badge = "badge-a"
        message = "Strong performance with only a few review points."
    elif percentage >= 50:
        grade = "B-Rank Builder"
        badge = "badge-b"
        message = "Good start. Review the missed topics and retake."
    else:
        grade = "Needs Practice"
        badge = "badge-f"
        message = "Focus on the feedback cards, then try again."

    return jsonify(
        {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "score": score,
            "total": total,
            "percentage": percentage,
            "earned_points": earned_points,
            "total_points": total_points,
            "point_percentage": point_percentage,
            "grade": grade,
            "badge_class": badge,
            "message": message,
            "categories": categories,
            "feedback": feedback,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
