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