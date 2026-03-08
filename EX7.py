# ASk the user to enter a temperature in Farenheit
# Convert the temperature to Celcius using the formula: C - (F - 32) * 5/9
# Name : Ellyse Mcchesney 
# Date : Jan. 22, 2026
farenheit_input = input("Please enter a temperature in farenheit: ")
farenheit_value = float(farenheit_input)
celcius_value = (farenheit_value - 32) * 5/9
celcius_value_rounded = round(celcius_value, 1) 

print("You entered", farenheit_value)
print(f"The temperature in Celcius is: {celcius_value_rounded}")

