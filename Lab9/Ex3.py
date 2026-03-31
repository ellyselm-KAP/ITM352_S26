# Read the 1,000 lines of taxi data from the taxi_1000.csv file
# Calculate the total of all fares, average fare, and maximum trip distance

import csv

filename = "taxi_1000.csv"

total_fare = 0.0
max_distance = 0.0
num_rows = 0

with open(filename, "r", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)

    for line in csv_reader:
        if num_rows == 0:  # Header row
            fare_index = line.index("Fare")
            distance_index = line.index("Trip Miles")
        else:
            trip_fare = float(line[fare_index])
            trip_distance = float(line[distance_index])

            total_fare += trip_fare

            if trip_distance > max_distance:
                max_distance = trip_distance

        num_rows += 1

if num_rows > 1:  # subtract header row
    average_fare = total_fare / (num_rows - 1)
else:
    average_fare = 0

print(f"We read {num_rows - 1} rows of data.")
print(f"Total fare: ${total_fare:.2f}")
print(f"Average fare: ${average_fare:.2f}")
print(f"Maximum trip distance: {max_distance:.2f} miles")
