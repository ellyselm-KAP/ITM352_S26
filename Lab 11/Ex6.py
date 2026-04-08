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


def get_user_selection(options, prompt):
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()

    if choice == "":
        return []

    try:
        selected = [options[int(i.strip()) - 1] for i in choice.split(",")]
        return selected
    except (ValueError, IndexError):
        print("Invalid selection.")
        return []


def generate_custom_pivot_table(data):
    if data is None:
        print("No data loaded.")
        return

    row_options = list(data.columns)
    rows = get_user_selection(row_options, "Select rows:")

    if not rows:
        print("At least one row selection is required.")
        return

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "Select columns (optional):")

    value_options = list(data.select_dtypes(include=["number"]).columns)
    values = get_user_selection(value_options, "Select values:")

    if not values:
        print("At least one value selection is required.")
        return

    agg_options = ["sum", "mean", "count"]
    agg_choice = get_user_selection(agg_options, "Select one aggregation function:")

    if not agg_choice:
        print("An aggregation function is required.")
        return

    agg_func = agg_choice[0]

    pivot_table = pd.pivot_table(
        data,
        index=rows,
        columns=cols if cols else None,
        values=values,
        aggfunc=agg_func
    )

    print("\nCustom Pivot Table:")
    print(pivot_table)


def exit_program(data):
    print("Exiting program.")
    raise SystemExit


def display_menu(menu_options):
    print("\nMenu Options:")
    for i, (label, func) in enumerate(menu_options, start=1):
        print(f"{i}. {label}")

    return input("Enter your choice: ").strip()


def main():
    filename = "sales_data_test.csv"
    data = load_csv(filename)

    menu_options = (
        ("Show the first n rows of sales data", display_initial_rows),
        ("Show the number of employees by region", show_employees_by_region),
        ("Generate custom pivot table", generate_custom_pivot_table),
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