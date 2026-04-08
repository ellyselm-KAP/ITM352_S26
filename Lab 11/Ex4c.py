def display_menu(menu_options):
    print("\nMenu Options:")
    for i, (label, func) in enumerate(menu_options, start=1):
        print(f"{i}. {label}")

    choice = input("Enter your choice: ").strip()
    return choice