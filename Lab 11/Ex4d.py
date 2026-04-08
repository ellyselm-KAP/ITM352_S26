import pandas as pd
import time

def load_csv(filename):
    print(f"\nLoading file: {filename}")
    start_time = time.time()

    try:
        data = pd.read_csv(
            filename,
            on_bad_lines="skip",
            dtype_backend="pyarrow"
        )

        if "order_date" in data.columns:
            data["order_date"] = pd.to_datetime(data["order_date"], errors="coerce")

        load_time = time.time() - start_time
        print("File loaded successfully.")
        print(f"Time to load: {load_time:.4f} seconds")
        print(f"Number of rows: {len(data)}")
        print("Columns:")
        print(list(data.columns))

        required_columns = ["quantity", "unit_price"]
        missing_columns = [col for col in required_columns if col not in data.columns]

        if missing_columns:
            print("Warning: Missing required fields:", missing_columns)
            print("Some analytics will not function without them.")

        return data

    except Exception as e:
        print("Error loading or parsing CSV file:", e)
        return None


def display_initial_rows(data):
    if data is None:
        print("No data loaded.")
        return

    user_input = input("\nHow many initial rows would you like to see? Enter a number, 'all', or press Enter to skip: ").strip().lower()

    if user_input == "":
        print("Skipping preview.")
    elif user_input == "all":
        print(data)
    elif user_input.isdigit():
        print(data.head(int(user_input)))
    else:
        print("Invalid input. Please enter a number, 'all', or press Enter to skip.")


def show_employees_by_region(data):
    if data is None:
        print("No data loaded.")
        return

    required_columns = ["sales_region", "employee_id"]
    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        print("Missing required columns for this report:", missing_columns)
        return

    pivot_table = pd.pivot_table(
        data,
        index="sales_region",
        values="employee_id",
        aggfunc=pd.Series.nunique
    )

    print("\nNumber of employees by region:")
    print(pivot_table)


def exit_program(data):
    print("Exiting program.")
    raise SystemExit


def display_menu(menu_options):
    print("\nMenu Options:")
    for i, (label, func) in enumerate(menu_options, start=1):
        print(f"{i}. {label}")

    choice = input("Enter your choice: ").strip()
    return choice


def main():
    filename = "sales_data_test.csv"
    data = load_csv(filename)

    menu_options = (
        ("Show the first n rows of sales data", display_initial_rows),
        ("Show the number of employees by region", show_employees_by_region),
        ("Exit the program", exit_program)
    )

    while True:
        choice = display_menu(menu_options)

        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(menu_options):
                selected_function = menu_options[choice_num - 1][1]
                selected_function(data)
            else:
                print("Invalid selection. Please try again.")
        else:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()