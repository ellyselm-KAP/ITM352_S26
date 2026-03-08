# Handy library of mathematical functions
# Name : Ellyse Mcchesney 
# Date : Jan 27, 2026

def midpoint(num1, num2):
    """Calculate the midpoint between two numbers"""
    mid = (num1 + num2) / 2
    return mid

def sqrt(number):
    """Calculate the square root of a number"""
    if number < 0
        return None  # Return None for negative numbers
    return number ** 0.5

def exponent(base,exp,precision):
    """Calculate the exponentiation of a base to a given exponent"""
    result = base ** exp
    rounded_result = round(result, precision)
    
    return result

def apply_function(x, y, func):
    """Apply a function to x and y and return a formatted string"""
    return f"The function {func.__name__}({x}, {y}) = {func(x, y)}"

from HandyMath import min, max, exponent, apply_function

print(apply_function(3, 5, min)
print(apply_function(3, 5, max))
print(apply_function(3, 5, exponent))


