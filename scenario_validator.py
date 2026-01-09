ALLOWED_ACTIONS = ["login", "submit", "approve"]

NORMALIZE = {
    "logs in": "login",
    "log in": "login",
    "logged in": "login",
    "submits": "submit",
    "submitting": "submit",
    "submitted": "submit"
}

def normalize(line):
    line = line.lower()
    for k, v in NORMALIZE.items():
        if k in line:
            return v
    for a in ALLOWED_ACTIONS:
        if a in line:
            return a
    return None

def validate_scenarios(gherkin_text):
    invalid = []
    lines = gherkin_text.splitlines()

    for line in lines:
        l = line.strip().lower()
        if l.startswith(("when", "and")):
            if not normalize(l):
                invalid.append(line)

    return invalid
