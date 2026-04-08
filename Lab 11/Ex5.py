def generate_custom_pivot_table(data):
    print("custom table")

menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", show_employees_by_region),
    ("Generate custom pivot table", generate_custom_pivot_table),
    ("Exit the program", exit_program)
)

