import HandyMath

# Ask user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculations using the HandyMath module
mid = HandyMath.midpoint(num1, num2)
sqrt_square = HandyMath.sqrt(num1 ** 2)
exp_result = HandyMath.exponent(num1, num2)
max_val = HandyMath.max_value(num1, num2)
min_val = HandyMath.min_value(num1, num2)

# Output results using f-strings
print(f"The midpoint of {num1} and {num2} is {mid}")
print(f"The square root of the square of {num1} is {sqrt_square}")
print(f"{num1} raised to the power of {num2} is {exp_result}")
print(f"The maximum of {num1} and {num2} is {max_val}")
print(f"The minimum of {num1} and {num2} is {min_val}")

from HandyMath import max, min, midpoint, sqrt, exponent

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"The midpoint of {num1} and {num2} is {midpoint(num1, num2)}")
print(f"The square root of the square of {num1} is {sqrt(num1 ** 2)}")
print(f"{num1} raised to the power of {num2} is {exponent(num1, num2)}")
print(f"The maximum of {num1} and {num2} is {max(num1, num2)}")
print(f"The minimum of {num1} and {num2} is {min(num1, num2)}")