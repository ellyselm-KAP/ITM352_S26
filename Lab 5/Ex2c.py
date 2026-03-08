trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)

trips = dict(zip(trip_durations, trip_fares))
print(trips) 

trip_num = input("What trip do you want? [1-4]:")
trip_index = int(trip_num) - 1
print(f"Duration: {list(trips.keys())[trip_index]) miles")
print(f"Fare: $(lists)")


trips_list = [{"miles": miles, "fare": fare} for miles, fare in duration_to_fare.items()]

print(trips_list)

# Print 3rd trip duration and cost (index 2)
print(f"The third trip was {trips_list[2]['miles']} miles long.")
print(f"The fare for the third trip was {trips_list[2]['fare']}.")


trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)  # numbers now

duration_to_fare = dict(zip(trip_durations, trip_fares))

# List of dictionaries (each trip)
trips_list = [{"miles": miles, "fare": fare} for miles, fare in zip(trip_durations, trip_fares)]

# Print 3rd trip duration and cost with currency formatting
print(f"The third trip was {trips_list[2]['miles']} miles long.")
print(f"The fare for the third trip was ${trips_list[2]['fare']:.2f}.")
