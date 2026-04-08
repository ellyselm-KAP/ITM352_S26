import pandas as pd

url = "https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

df = pd.read_csv(url, on_bad_lines="skip", dtype_backend="pyarrow")
df.head(10).to_csv("sales_data_test.csv", index=False)

print("Created sales_data_test.csv from first 10 rows.")