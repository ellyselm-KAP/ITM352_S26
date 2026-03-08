def f_to_c(fahrenheit):
    return (fahrenheit - 32) * (5/9)

# Ask user for temperature in Fahrenheit
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# Convert and display result
celsius = f_to_c(fahrenheit)

print("You entered:", fahrenheit, "°F")
print("That is:", celsius, "°C")
