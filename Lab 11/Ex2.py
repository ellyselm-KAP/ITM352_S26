# Read in DCSV file and create a dataframe
# Pivot the dataframe, aggregating sales by region, with columns defies by order_type and totals

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

        # Convert date columns if present
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


# Test with local and cloud files
local_file = "sales_data_test.csv"
cloud_file = "https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

test_data_local = load_csv(local_file)
test_data_cloud = load_csv(cloud_file)
