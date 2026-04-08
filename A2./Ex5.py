# Assignment 2 dashboard - step-by-step build
# This version builds on Ex4.py by adding:
# 1. Data summary when the file loads
# 2. Stored analytics tracking
# 3. A menu option to display saved results
# 4. Basic defensive checks to make later analytics easier to add
# This program creates an interactive dashboard using pandas pivot tables.
# It allows users to explore sales data through predefined analytics
# and custom queries.

# Requirement 2: Displays a data summary and removes invalid analytics if columns are missing
# Requirement 10: Stores analytics results and allows users to view them later

import time
import sys
import pandas as pd
import numpy as np
from pandas import pivot_table
import pyarrow

pd.set_option('display.max_columns', None)


# Store analytics results here for Requirement 10
stored_results = {}


def load_csv(filepath):
    print(f"Loading data from {filepath}...")
    start_time = time.time()

    try:
        df = pd.read_csv(
            filepath,
            engine='python',
            on_bad_lines='skip',
            dtype_backend='pyarrow'
        )

        end_time = time.time()
        load_time = end_time - start_time

        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {df.columns.tolist()}")

        # Convert dates safely because the sample data mixes formats
        if 'order_date' in df.columns:
            df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', errors='coerce', dayfirst=True)

        # Convert numeric fields safely
        for col in ['quantity', 'unit_price']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')


        # Fill missing values with 0 to match assignment requirement
        df = df.fillna(0)

        # Create sales column if possible
        if 'quantity' in df.columns and 'unit_price' in df.columns:
            df['sales'] = df['quantity'] * df['unit_price']

        required_columns = ['quantity', 'unit_price', 'order_date']
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            print(f"Warning: Missing required columns: {missing_columns}")
            print("Some analytics may not function correctly.")
        else:
            print("All required columns are present.")

        return df

    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


def display_data_summary(dataframe):
    print("\n--- Data Summary ---")

    if dataframe is None or dataframe.empty:
        print("No data available for summary.")
        return

    total_orders = len(dataframe)

    num_employees = dataframe['employee_id'].nunique() if 'employee_id' in dataframe.columns else "N/A"
    num_regions = dataframe['sales_region'].nunique() if 'sales_region' in dataframe.columns else "N/A"
    num_customers = dataframe['customer_name'].nunique() if 'customer_name' in dataframe.columns else "N/A"
    num_categories = dataframe['product_category'].nunique() if 'product_category' in dataframe.columns else "N/A"
    num_states = dataframe['customer_state'].nunique() if 'customer_state' in dataframe.columns else "N/A"

    total_sales = dataframe['sales'].sum() if 'sales' in dataframe.columns else "N/A"
    total_quantity = dataframe['quantity'].sum() if 'quantity' in dataframe.columns else "N/A"

    if 'order_date' in dataframe.columns:
        valid_dates = dataframe.loc[dataframe['order_date'] != 0, 'order_date']
        if len(valid_dates) > 0:
            min_date = valid_dates.min()
            max_date = valid_dates.max()
            date_range = f"{min_date} to {max_date}"
        else:
            date_range = "N/A"
    else:
        date_range = "N/A"

    print(f"Total orders: {total_orders}")
    print(f"Number of employees: {num_employees}")
    print(f"Sales regions: {num_regions}")
    print(f"Date range of orders: {date_range}")
    print(f"Number of unique customers: {num_customers}")
    print(f"Product categories: {num_categories}")
    print(f"Unique states: {num_states}")
    print(f"Total sales amount: {total_sales}")
    print(f"Total quantities sold: {total_quantity}")


def display_initial_rows(dataframe):
    print("Enter rows to display:")
    print(f"- Enter a number 1 to {len(dataframe)}")
    print("- Enter 'all' to display all rows")
    print("- To skip preview, press Enter")

    user_input = input("Your choice: ").strip().lower()

    if user_input == '':
        print("Skipping preview.")
        return

    elif user_input == 'all':
        print("Displaying all rows:")
        print(dataframe)
        return

    elif user_input.isdigit():
        n = int(user_input)
        if 1 <= n <= len(dataframe):
            print(f"Displaying first {n} rows:")
            print(dataframe.head(n))
        else:
            print("Invalid number of rows.")
    else:
        print("Invalid input. Please try again.")


def show_employees_by_region(dataframe):
    required = ['employee_id', 'sales_region']

    for col in required:
        if col not in dataframe.columns:
            print(f"Cannot run this analytic because '{col}' is missing.")
            return None

    pivot_table = pd.pivot_table(
        dataframe,
        values='employee_id',
        index='sales_region',
        aggfunc=pd.Series.nunique
    )

    pivot_table.columns = ['Number of Employees']

    print("\nNumber of employees by region:")
    print(pivot_table)

    # Save result for Requirement 10
    stored_results['employees_by_region'] = pivot_table
    export_to_excel(pivot_table)
    return pivot_table

def total_sales_by_region_order_type(dataframe):
    # Requirement R3:
    # This pivot table shows total sales grouped by region and order type.
    # This helps analyze where revenue is coming from and how retail vs wholesale perform.

    required = ['sales_region', 'order_type', 'sales']

    for col in required:
        if col not in dataframe.columns:
            print(f"Cannot run this analytic because '{col}' is missing.")
            return None

    pivot_table = pd.pivot_table(
        dataframe,
        values='sales',
        index='sales_region',
        columns='order_type',
        aggfunc='sum'
    )

    print("\nTotal sales by region and order type:")
    print(pivot_table)

    # Requirement 10: store result
    stored_results['sales_by_region_order_type'] = pivot_table
    export_to_excel(pivot_table)
    return pivot_table

def display_stored_results(dataframe):
    print("\n--- Stored Analytics Results ---")

    if not stored_results:
        print("No analytics have been stored yet.")
        return

    for name, result in stored_results.items():
        print(f"\nResult name: {name}")
        print(result)


def exit_program(dataframe):
    print("Exiting the program. Goodbye!")
    sys.exit(0)

def get_menu_options(dataframe):
    menu_options = [
        ("Show the first n rows of sales data", display_initial_rows),
        ("Total sales by region and order type", total_sales_by_region_order_type),
        ("Average sales by region with average sales by state and sale type", average_sales_by_region_state_sale_type),
        ("Sales by customer type and order type by state", sales_by_customer_type_order_type_by_state),
        ("Total sales quantity and price by region and product", total_sales_quantity_and_price_by_region_product),
        ("Total sales quantity and price by customer type", total_sales_quantity_and_price_by_customer_type),
        ("Max and min sales price by category", max_min_sales_by_category),
        ("Number of unique employees by region", show_employees_by_region),
        ("Display stored results", display_stored_results),
        ("Create a custom pivot table", generate_custom_pivot_table),
        ("Exit", exit_program)
    ]

    available_menu = []

    for description, function in menu_options:
        if function == total_sales_by_region_order_type:
            if all(col in dataframe.columns for col in ['sales_region', 'order_type', 'sales']):
                available_menu.append((description, function))

        elif function == average_sales_by_region_state_sale_type:
            if all(col in dataframe.columns for col in ['sales_region', 'customer_state', 'order_type', 'sales']):
                available_menu.append((description, function))

        elif function == sales_by_customer_type_order_type_by_state:
            if all(col in dataframe.columns for col in ['customer_state', 'customer_type', 'order_type', 'sales']):
                available_menu.append((description, function))

        elif function == total_sales_quantity_and_price_by_region_product:
            if all(col in dataframe.columns for col in ['sales_region', 'produce_name', 'quantity', 'sales']):
                available_menu.append((description, function))

        elif function == total_sales_quantity_and_price_by_customer_type:
            if all(col in dataframe.columns for col in ['customer_type', 'order_type', 'quantity', 'sales']):
                available_menu.append((description, function))

        elif function == max_min_sales_by_category:
            if all(col in dataframe.columns for col in ['product_category', 'sales']):
                available_menu.append((description, function))

        elif function == show_employees_by_region:
            if all(col in dataframe.columns for col in ['employee_id', 'sales_region']):
                available_menu.append((description, function))

        else:
            available_menu.append((description, function))

    return tuple(available_menu)


def total_sales_quantity_and_price_by_region_product(dataframe):
    # This analytic groups sales by region and product and sums both quantity and sales.
    # It matches one of the required predefined dashboard analytics.

    required = ['sales_region', 'produce_name', 'quantity', 'sales']

    for col in required:
        if col not in dataframe.columns:
            print(f"Cannot run this analytic because '{col}' is missing.")
            return None

    pivot_table = pd.pivot_table(
        dataframe,
        index=['sales_region', 'produce_name'],
        values=['quantity', 'sales'],
        aggfunc='sum'
    )

    print("\nTotal sales quantity and price by region and product:")
    print(pivot_table)

    stored_results['sales_quantity_price_by_region_product'] = pivot_table
    export_to_excel(pivot_table)
    return pivot_table

def max_min_sales_by_category(dataframe):
    if 'product_category' not in dataframe.columns or 'sales' not in dataframe.columns:
        print("Missing required columns")
        return

    pivot = pd.pivot_table(
        dataframe,
        index='product_category',
        values='sales',
        aggfunc=['max', 'min']
    )

    print("\nMax and min sales by category:")
    print(pivot)

    # Requirement 10 storage
    stored_results['max_min_sales_by_category'] = pivot
    export_to_excel(pivot)
    return pivot

#Ghost of deleted requirement 2 mini section 

#Exeel import section 
def export_to_excel(pivot_table):
    choice = input("Do you want to export this result to Excel? (y/n): ").strip().lower()

    if choice == 'y':
        filename = input("Enter filename (without .xlsx): ").strip()
        try:
            pivot_table.to_excel(f"{filename}.xlsx")
            print(f"File saved as {filename}.xlsx")
        except Exception as e:
            print(f"Error saving file: {e}")

#Helper function 
def get_user_selection(options, prompt):
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()

    if choice == "":
        return []

    try:
        selected = [options[int(i.strip()) - 1] for i in choice.split(',')]
        return selected
    except (ValueError, IndexError):
        print("Invalid selection.")
        return []

#Pivot Function 
def generate_custom_pivot_table(dataframe):
    row_options = list(dataframe.columns)
    value_options = list(dataframe.select_dtypes(include=['number']).columns)
    agg_options = ['sum', 'mean', 'count']

    rows = get_user_selection(row_options, "Select rows:")
    if not rows:
        print("At least one row field is required.")
        return None

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "Select columns (optional, press Enter for none):")

    values = get_user_selection(value_options, "Select values:")
    if not values:
        print("At least one value field is required.")
        return None

    agg_choice = get_user_selection(agg_options, "Select aggregation function:")
    if not agg_choice:
        print("You must choose one aggregation function.")
        return None

    agg_func = agg_choice[0]

    pivot_table = pd.pivot_table(
        dataframe,
        index=rows,
        columns=cols if cols else None,
        values=values,
        aggfunc=agg_func
    )

    print("\nCustom pivot table:")
    print(pivot_table)

    stored_results[f'custom_pivot_{len(stored_results) + 1}'] = pivot_table
    export_to_excel(pivot_table)
    return pivot_table

def display_previous_results_summary():
    print("\n--- Saved Results So Far ---")
    if not stored_results:
        print("None")
    else:
        for i, key in enumerate(stored_results.keys(), start=1):
            print(f"{i}. {key}")


def display_menu(dataframe):
    menu_options = get_menu_options(dataframe)

    display_previous_results_summary()

    print("\n--- Sales Data Dashboard ---")
    for i, (description, _) in enumerate(menu_options, start=1):
        print(f"{i}. {description}")

    try:
        choice = int(input(f"Enter your choice (1-{len(menu_options)}): "))
        if 1 <= choice <= len(menu_options):
            action = menu_options[choice - 1][1]
            action(dataframe)
        else:
            print("Invalid choice. Please enter a valid menu number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def sales_by_customer_type_order_type_by_state(dataframe):
    required = ['customer_state', 'customer_type', 'order_type', 'sales']

    for col in required:
        if col not in dataframe.columns:
            print(f"Cannot run this analytic because '{col}' is missing.")
            return None

    pivot_table = pd.pivot_table(
        dataframe,
        index='customer_state',
        columns=['customer_type', 'order_type'],
        values='sales',
        aggfunc='sum'
    )

    print("\nSales by customer type and order type by state:")
    print(pivot_table)

    stored_results['sales_by_customer_type_order_type_by_state'] = pivot_table
    export_to_excel(pivot_table)
    return pivot_table

def average_sales_by_region_state_sale_type(dataframe):
    required = ['sales_region', 'customer_state', 'order_type', 'sales']

    for col in required:
        if col not in dataframe.columns:
            print(f"Cannot run this analytic because '{col}' is missing.")
            return None

    pivot_table = pd.pivot_table(
        dataframe,
        index='sales_region',
        columns=['customer_state', 'order_type'],
        values='sales',
        aggfunc='mean'
    )

    print("\nAverage sales by region with average sales by state and sale type:")
    print(pivot_table)

    stored_results['average_sales_by_region_state_sale_type'] = pivot_table
    export_to_excel(pivot_table)
    return pivot_table


def total_sales_quantity_and_price_by_customer_type(dataframe):
    required = ['customer_type', 'order_type', 'quantity', 'sales']

    for col in required:
        if col not in dataframe.columns:
            print(f"Cannot run this analytic because '{col}' is missing.")
            return None

    pivot_table = pd.pivot_table(
        dataframe,
        index=['customer_type', 'order_type'],
        values=['quantity', 'sales'],
        aggfunc='sum'
    )

    print("\nTotal sales quantity and price by customer type:")
    print(pivot_table)

    stored_results['sales_quantity_price_by_customer_type'] = pivot_table
    export_to_excel(pivot_table)
    return pivot_table

def main():
    # Use the small test file while building
    filename = "sales_data.csv"
    sales_data = load_csv(filename)

    if sales_data is None:
        print("Program cannot continue because the data did not load.")
        return

    display_data_summary(sales_data)

    while True:
        display_menu(sales_data)


if __name__ == "__main__":
    main()


