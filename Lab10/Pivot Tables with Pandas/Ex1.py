import pandas as pd
import numpy as np

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

try:
    df = pd.read_csv(
        url,
        on_bad_lines="skip",
        dtype_backend="pyarrow"
    )
except Exception as e:
    print("Error reading CSV file:", e)
    print("If needed, download the file and use a local copy instead.")
    exit()

print("First 5 rows:")
print(df.head())

print("\nColumn data types:")
print(df.dtypes)

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

print("\nData types after converting order_date:")
print(df.dtypes)

