# Ask the user to enter a decimal number between 1 and 100
while True:
    number = float(input("Enter a decimal number between 1 and 100: "))
    if 1 <= number <= 100:
        break
    else:
        print("Error: Please enter a number between 1 and 100.")

# Square the number
square = number ** 2

# Display the original number and its square
print("You entered:", number)
print("The square of the number is:", square)
