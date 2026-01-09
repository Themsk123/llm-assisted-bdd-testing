from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def clean_gherkin(text):
    allowed = (
        "Scenario:",
        "Given user is on login page",
        "When user login",
        "And user submit",
        "Then application",
        "Then error message"
    )

    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("```") or not line:
            continue
        for a in allowed:
            if a.lower() in line.lower():
                lines.append(line)
                break

    return "\n".join(lines)



def generate_scenarios(requirement):
    prompt = f"""
Generate ONLY valid Gherkin.

STRICT FORMAT:
- Must include the keyword "Scenario:" for each scenario.
- Generate exactly two scenarios:
    Scenario: Successful login and submission
    Scenario: Invalid login
- Allowed steps ONLY:
    Given user is on login page
    When user login with valid credentials
    When user login with invalid credentials
    And user submit application
    Then application should be submitted successfully
    Then error message should be displayed
- Do not add explanations or markdown.

Business Requirement:
{requirement}
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content


