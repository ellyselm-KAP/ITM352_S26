# Ask the user for a number between 1 and 100. Square the number and print the number and its square.
# Name: Ellyse McChesney
# Date: Jan. 20, 2026 

print("Welcome to the program")
valueEntered = input("Please enter a number between 1 and 100: ")
print("You entered: " + valueEntered)

value_as_integer = int(valueEntered)
squared_value = value_as_integer ** 2
print("The square of " + str(value_as_integer) + " is " + str(squared_value))

# Ask the user to enter a floating point number. Square the number. 
# Print out the original number and the squared result. 
# Name : Ellyse McChesney 
# Date : Jan. 22. 2026
input_value = input ("Please neter a floating point number: ")
float_value = float(input_value) 
squared_value = float_value ** 2
# Round the number to two decimals 

print ("You entered:", float_value)
print (f"The squared value is : {squared_value}")
