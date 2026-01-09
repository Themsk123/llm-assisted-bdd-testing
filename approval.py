def approve(scenarios):
    approved = []
    for s in scenarios:
        print("\n" + s)
        choice = input("Approve this scenario? (yes/no): ")
        if choice.lower() == "yes":
            approved.append(s)
    return approved
