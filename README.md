# ⚙️ DecodeLabs Industrial Training: Backend Architecture Portfolio

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

Welcome to my official engineering portfolio for the **DecodeLabs Industrial Training Kit (Batch 2026)**. 

This repository documents my progression through the foundational phases of backend engineering. Rather than writing isolated scripts, these projects were engineered to master real-world system architectures—specifically focusing on data capture, validation, state preservation, and the decoupling of business logic from the user interface.

---

## 🏛️ Core Architectural Philosophy
Throughout these projects, I adhered to a strict 4-tier decoupling strategy to emulate enterprise-grade backend systems:

1. **The View (Client/UI):** "Dumb" interfaces built with HTML/CSS that strictly handle presentation and user input collection.
2. **The API Boundary:** The HTTP routing layer (Flask) that securely transports payloads between the Client and the Engine.
3. **The Computation Engine:** The Python logic layer acting as the "Validation Station," executing business rules, defensive coding, and mathematical accumulators.
4. **The Storage Layer:** The permanent data destination, bypassing the "Volatile Trap" of RAM via JSON serialization (acting as an in-memory micro-database).

---

## 🏗️ The Engineering Milestones

### 📂 [Week 1: Advanced To-Do List Engine](./Week%201)
**Theme: Data Management, CRUD & Persistence**

The goal of the first milestone was to master the fundamental **IPO (Input, Process, Output) Architecture** and establish secure data persistence.
* **Overcoming Volatility:** Implemented JSON Serialization to ensure data survives server restarts and memory dumps.
* **Decoupled Rendering:** Separated the Python Data Logic (Model) from the HTML/CSS User Interface (View) using Server-Side Rendering (SSR) via Jinja2.
* **System Features:** Full CRUD operations, priority-based sorting algorithms, automated timestamps, and bulk deletion routing.

### 📂 [Week 2: State-Preserving Financial Tracker](./Week%202)
**Theme: Data Accumulation & The Continuous Audit**

The second milestone shifted focus from static storage to **dynamic, real-time data processing**. I built a fault-tolerant financial engine capable of handling continuous, unpredictable data entry.
* **The Ledger Heartbeat (Accumulator Pattern):** Engineered a state-preserving loop that safely accumulates financial data in memory without resetting during continuous audit cycles.
* **The Digital Poka-Yoke (Defensive Coding):** Built robust input validation using `try...except ValueError` blocks to catch garbage data (e.g., text inputs) and prevent fatal server crashes.
* **Sentinel Values (The Kill Switch):** Implemented graceful shutdowns to safely break continuous loops, finalize the ledger, and render the final reality.
* **System Features:** Real-time running totals, custom auto-dismissing flash alerts, transaction history logging, and a premium "Midnight Emerald" Glassmorphism UI.

---

## 🚀 Setup & Installation Instructions

To run these isolated environments locally on your machine:

**1. Clone the repository:**
```bash
git clone [https://github.com/ahsanur-official/DecodeLabs-Internship.git](https://github.com/ahsanur-official/DecodeLabs-Internship.git)
cd DecodeLabs-Internship