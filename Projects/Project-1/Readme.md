🧠 Smart Utility Console

A modular, menu-driven Python application delivering multiple real-world utilities in a single command-line interface.

---

📘 Overview

The Smart Utility Console is a consolidated CLI tool that bundles together everyday utility programs—such as a discount evaluator, loan eligibility checker, and electricity bill calculator.
It’s built with clear conditional logic and structured input handling, serving as a foundation for more advanced refactoring (functions, loops, modules) in subsequent versions.

---

🧩 Project Description

This project demonstrates how multiple independent utilities can be integrated under a unified console menu.
Each module solves a real scenario using direct conditional branching.
Future iterations may evolve into a fully modular, function-driven or object-oriented architecture.


---

⚙️ Core Features
1️⃣ Main Menu

Displays all available utilities.

Accepts user selection.

Gracefully handles invalid input.

---

2️⃣ Utility: Discount Calculator

Inputs: total purchase amount

Logic:

10,000 → 20% discount

5,000 → 10% discount

Otherwise → no discount

Outputs the final payable amount.

---

3️⃣ Utility: Loan Eligibility Checker

Inputs: age, monthly income, credit score

Eligibility Criteria:

Age ≥ 21

Income ≥ 25,000

Credit Score ≥ 650

Returns a clear eligibility decision.


---

4️⃣ Utility: Electricity Bill Calculator

Inputs: total units consumed

Tariff Structure:

0–100 units → ₹5/unit

101–200 units → ₹7/unit

Above 200 → ₹10/unit

Adds fixed service charge of ₹50

Computes and prints the final bill.

---
---

💡 Sample Output
Welcome to Smart Utility Console

1. Discount Calculator
2. Loan Eligibility Checker
3. Electricity Bill Calculator

Enter your choice: 3

Enter your age: 25
Enter monthly income: 30000
Enter credit score: 700

You are eligible for the loan.


---
---

🧱 Skills Reinforced

Structured decision-making (if, elif, else)

Validating and processing user input

Combining conditions using logical operators

Designing readable, maintainable console applications

Preparing code for future modularization (functions, loops, OOP)
