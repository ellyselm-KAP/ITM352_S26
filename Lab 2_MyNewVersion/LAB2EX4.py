# Ask the user to enter a decimal number between 1 and 100
while True:
    number = float(input("Enter a decimal number between 1 and 100: "))
    if 1 <= number <= 100:
        break
    else:
        print("Error: Please enter a number between 1 and 100.")

# Square the number
square = number ** 2

# Round the values to two decimal places
number_rounded = round(number, 2)
square_rounded = round(square, 2)

# Get the length (number of characters) of the number as a string
number_length = len(str(number_rounded))

# Display the rounded results
print("You entered:", number_rounded)
print("The square of the number is:", square_rounded)
print("Length of the number:", number_length)
