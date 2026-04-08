row_options = list(data.columns)
col_options = list(data.columns)
value_options = list(data.select_dtypes(include=["number"]).columns)
agg_options = ["sum", "mean", "count"]