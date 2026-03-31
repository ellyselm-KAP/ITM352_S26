import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option("display.max_columns", None)

try:
    df = pd.read_csv(
        url,
        on_bad_lines="skip",
        dtype_backend="pyarrow"
    )
except Exception as e:
    print("Error reading CSV file:", e)
    exit()

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Convert to numeric before calculating sales
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

# Create sales column
df["sales"] = df["quantity"] * df["unit_price"]

pivot_table_1 = pd.pivot_table(
    df,
    values="sales",
    index="region",
    columns="order_type",
    aggfunc=np.sum,
    margins=True
)

print("Pivot table: total sales by region and order type")
print(pivot_table_1)

