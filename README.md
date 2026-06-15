# DecodeLabs Project 1: Advanced To-Do List Application 🚀

Welcome to my first official project for the **DecodeLabs Industrial Training Kit (Batch 2026)**. 

This project represents the foundational logic phase of backend engineering. [cite_start]It is an Advanced To-Do List built to master Data Management, focusing on how information is captured, processed, stored, and displayed using pure programmatic logic[cite: 5, 6, 7].

## 🧠 Core Engineering Concepts Demonstrated
Instead of just building a simple list, this project was engineered following professional backend principles:
* [cite_start]**The IPO Architecture:** Built strictly following the Input (Data Entry), Process (Logic/Modification), and Output (Display/View) model[cite: 47].
* **Data Persistence:** Escaped the "Volatile Trap" of RAM by implementing JSON Serialization. [cite_start]Data is safely moved from dynamic memory to permanent disk storage (`tasks.json`)[cite: 138, 139, 149, 152, 153].
* [cite_start]**Decoupled Architecture:** Successfully separated the Data Logic (Python Model) from the User Interface (HTML/CSS View) using the Flask web framework[cite: 118, 119, 121, 122, 123].

## ✨ Key Features
* **Full CRUD Functionality:** Add, View, Update (Complete/Pending), and Delete tasks.
* **Priority Management:** Categorize tasks by High, Medium, or Low priority, with automatic sorting (High priority tasks jump to the top).
* **Timestamps:** Automatically tracks and displays the exact date and time a task was created.
* **Dynamic Summary Dashboard:** Real-time tracking of Total, Completed, and Pending tasks.
* **Bulk Operations:** A dedicated "Clear Completed" function for quick cleanup.
* **Custom UI:** A fully responsive, modern "Dark Pro" theme with interactive hover states and color-coded priority badges.

## 🛠️ Technology Stack
* **Backend Logic:** Python 3
* **Web Framework:** Flask (Server-Side Rendering)
* [cite_start]**Database / Storage:** JSON (`tasks.json`) [cite: 149]
* **Frontend UI:** HTML5 & CSS3 (Flexbox, Custom Properties)

## 📁 Project Structure
```text
Week 1/
│
├── app.py               # The Flask web server and core logic engine
├── tasks.json           # The local JSON database (auto-generated)
│
├── static/
│   └── style.css        # Dark theme styling and responsive layout
│
└── templates/
    └── index.html       # Jinja2 HTML template for the UI