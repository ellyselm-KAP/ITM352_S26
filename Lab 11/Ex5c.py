def get_user_selection(options, prompt):
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()

    if choice == "":
        return []

    selected = [options[int(i.strip()) - 1] for i in choice.split(",")]
    return selected