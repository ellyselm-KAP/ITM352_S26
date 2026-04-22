# Get a JSON file from the City of Chicago's Data Portal and analyze driver types

import pandas as pd
import requests

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

search_results = requests.get(url)
results_json = search_results.json()

print("Driver Types and their Counts:")
print(results_json)

print("\nType of data returned:")
print(type(results_json))

# Convert the JSON results to a DataFrame
results_df = pd.DataFrame(results_json)

print("\nOriginal DataFrame:")
print(results_df)

print("\nOriginal columns:")
print(results_df.columns)

# Rename and organize columns
results_df.columns = ["driver_type", "count"]
results_df = results_df[["count", "driver_type"]]
results_df = results_df.set_index("driver_type")

print("\nDriver Types and their Counts (DataFrame):")
print(results_df)