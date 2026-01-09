# LLM-Assisted BDD Functional Testing Framework

This project demonstrates how Large Language Models can be used to convert business requirements into executable BDD functional tests.

## Features
- Plain English → Gherkin scenario generation using Groq LLM
- Scenario validation and happy-path selection
- Manual approval before execution
- Browser automation using Behave + Playwright

## How to Run

```bash
pip install groq behave playwright
playwright install
setx GROQ_API_KEY "your_api_key_here"
python main.py
behave features/generated.feature
