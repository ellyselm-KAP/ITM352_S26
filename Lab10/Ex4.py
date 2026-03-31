import pandas as pd

taxi_df = pd.read_json("/Users/ellysemcchesney/Documents/GitHub/ITM352_S26/Lab10/Taxi_Trips.json")

print("First 10 rows:")
print(taxi_df.head(10))

print("\nSummary statistics:")
print(taxi_df.describe())

median_fare = taxi_df["fare"].median()
print("\nMedian fare:")
print(median_fare)