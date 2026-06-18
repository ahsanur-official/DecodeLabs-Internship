# ==================================
# EXPENSE TRACKER
# DecodeLabs Project 2
# Developed by: Md. Ahsanur Rahaman
# ==================================

from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "decodelabs_secure_key"
FILE_NAME = "ledger.json"


def load_state():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                pass
    return {"total": 0.0, "transactions": []}


def save_state(state):
    with open(FILE_NAME, "w") as file:
        json.dump(state, file, indent=4)


@app.route("/")
def index():
    state = load_state()
    return render_template(
        "index.html", total=state["total"], transactions=state["transactions"]
    )


@app.route("/process", methods=["POST"])
def process_expense():
    state = load_state()
    raw_amount = request.form.get("amount").strip()
    description = request.form.get("description", "General Expense").strip()

    try:
        expense = float(raw_amount)

        if expense <= 0:
            flash("Amount must be greater than zero.", "error")
            return redirect(url_for("index"))

        state["total"] += expense

        state["transactions"].insert(
            0,
            {
                "desc": description if description else "General Expense",
                "amount": expense,
                "date": datetime.now().strftime("%b %d, %I:%M %p"),
            },
        )

        save_state(state)
        flash("Transaction processed successfully.", "success")

    except ValueError:
        flash("Invalid Data: Please enter a valid number.", "error")

    return redirect(url_for("index"))


@app.route("/finalize")
def finalize_ledger():
    save_state({"total": 0.0, "transactions": []})
    flash("Ledger finalized. System ready for new cycle.", "info")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
