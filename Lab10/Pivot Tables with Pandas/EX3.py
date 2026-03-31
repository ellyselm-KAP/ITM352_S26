import pandas as pd
import numpy as np

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "${:,.2f}".format)

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
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
df["sales"] = df["quantity"] * df["unit_price"]

pivot_table_2 = pd.pivot_table(
    df,
    values="sales",
    index=["region", "state"],
    columns="order_type",
import pandas as pd
import numpy as np

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "${:,.2f}".format)

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
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
df["sales"] = df["quantity"] * df["unit_price"]

pivot_table_2 = pd.pivot_table(
    df,
    values="sales",
    index=["region", "state"],
    columns="order_type",
    aggfunc=[np.sum, np.mean],
    margins=True
)

print("Pivot table: total and average sales by region, state, and order type")
print(pivot_table_2)    margins=True
)

print("Pivot table: total and average sales by region, state, and order type")
print(pivot_table_2)