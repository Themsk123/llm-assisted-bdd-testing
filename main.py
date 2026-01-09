from scenario_generator import generate_scenarios
from scenario_validator import validate_scenarios
from happy_path_selector import extract_happy_paths
from approval import approve

req = input("Enter Business Requirement:\n")

gherkin = generate_scenarios(req)
print("\nGenerated Scenarios:\n", gherkin)

invalid = validate_scenarios(gherkin)

if invalid:
    print("\nValidation Failed:")
    for i in invalid:
        print(i)
    exit()

happy = extract_happy_paths(gherkin)
approved = approve(happy)

if approved:
    with open("features/generated.feature", "w") as f:
        f.write("Feature: Auto Generated\n")
        for s in approved:
            f.write(s)
    print("\nApproved scenarios written. Ready to run Behave.")
else:
    print("\nNo scenario approved.")
