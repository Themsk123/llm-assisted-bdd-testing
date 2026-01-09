def extract_happy_paths(gherkin_text):
    blocks = gherkin_text.split("Scenario:")
    happy = []

    for b in blocks:
        text = b.lower()
        if not text.strip():
            continue
        if any(w in text for w in ["invalid", "error", "fail"]):
            continue
        happy.append("Scenario:" + b)

    return happy
