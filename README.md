# LLM-Assisted BDD Functional Testing Framework

This project demonstrates how **Large Language Models (LLMs)** can be used to automatically convert **plain-English business requirements** into **executable BDD (Behavior Driven Development) test cases**, with validation, manual approval, and real browser execution.

The goal is to reduce manual effort in writing test scenarios while keeping **control, reliability, and human oversight** in AI-generated tests.

---

## 🚀 What This Project Does

1. Takes a **business requirement in natural language**
2. Uses an **LLM (Groq API)** to generate Gherkin BDD scenarios  
   - One positive (happy path)
   - One negative flow
3. Cleans and validates the generated scenarios
4. Selects only **happy-path scenarios**
5. Requires **manual approval** before execution
6. Executes approved scenarios using **Behave + Playwright**
7. Produces a real execution result in the browser

---

## 🧠 Why This Project?

In real enterprise systems:
- Writing BDD scenarios is repetitive
- AI-generated output cannot be blindly trusted
- Human-in-the-loop validation is essential

This framework shows how **LLMs can assist testing without removing control**.

---

## 🏗️ Architecture Overview

Business Requirement
↓
LLM Scenario Generator
↓
Scenario Cleaning & Validation
↓
Happy Path Selector
↓
Manual Approval
↓
BDD Automation (Behave + Playwright)
↓
Execution Report

---

## 📁 Project Structure

llm_bdd_testing/
├── main.py
├── scenario_generator.py
├── scenario_validator.py
├── happy_path_selector.py
├── manual_approval.py
├── features/
│ ├── generated.feature
│ ├── environment.py
│ └── steps/
│ └── login_steps.py
├── README.md
└── .gitignore

---

## 🛠️ Tech Stack

- **Python**
- **Groq LLM API**
- **Behave** (BDD framework)
- **Playwright** (browser automation)

---

## 📌 Sample Business Requirement

User should be able to login to the application using valid credentials and submit an application successfully.
If the user logs in with invalid credentials, an error message should be displayed.

---

## 🧾 Example Generated Gherkin

Scenario: Successful login and submission
Given user is on login page
When user login with valid credentials
And user submit application
Then application should be submitted successfully

Scenario: Invalid login
Given user is on login page
When user login with invalid credentials
Then error message should be displayed

Only the **happy-path scenario** is approved and executed.

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install groq behave playwright
playwright install
2️⃣ Set Groq API Key (Windows)
setx GROQ_API_KEY "your_api_key_here"
Restart the terminal after this.
3️⃣ Run Scenario Generation & Approval
python main.py

Enter the business requirement
Approve the happy-path scenario when prompted
4️⃣ Execute Automated Tests
behave features/generated.feature
A browser will open and the scenario will execute automatically.
✅ Output
1 feature passed
1 scenario passed
4 steps passed
0 failed

👤 Author

Mohd Sahil
Final-Year B.Tech CSE (2026)
IIIT Kota
