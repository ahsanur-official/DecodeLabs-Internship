# ==========================================
# FLASK WEB SERVER
# DecodeLabs Project 1 (Python Server-Side)
# ==========================================

from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
FILE_NAME = "tasks.json"

# --- Helper Functions ---
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# --- Web Routes ---
@app.route("/")
def index():
    tasks = load_tasks()
    
    total = len(tasks)
    completed = sum(1 for task in tasks if task["status"] == "Completed")
    pending = total - completed

    return render_template("index.html", tasks=tasks, total=total, completed=completed, pending=pending)

@app.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    task_name = request.form.get("task_name").strip()
    task_priority = request.form.get("task_priority")

    if task_name:
        new_id = max((task["id"] for task in tasks), default=0) + 1
        new_task = {
            "id": new_id,
            "name": task_name,
            "priority": task_priority,
            "status": "Pending",
            "dateAdded": datetime.now().strftime("%b %d, %I:%M %p")
        }
        
        if task_priority == "High":
            tasks.insert(0, new_task)
        else:
            tasks.append(new_task)
            
        save_tasks(tasks)

    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed" if task["status"] == "Pending" else "Pending"
            break
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/clear")
def clear_completed():
    tasks = load_tasks()
    tasks = [task for task in tasks if task["status"] != "Completed"]
    save_tasks(tasks)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)