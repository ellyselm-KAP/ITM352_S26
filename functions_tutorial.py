# Python Functions Tutorial
# Name: Ellyse McChesney
# Date: Jan. 22, 2026

# ===== 1. FUNCTION WITH NO PARAMETERS =====
def say_hello():
    print("Hello, World!")

# Call it
say_hello()


# ===== 2. FUNCTION WITH ONE PARAMETER =====
def greet(name):
    print("Hello, " + name + "!")

# Call it
greet("Ellyse")
greet("Alice")


# ===== 3. FUNCTION WITH MULTIPLE PARAMETERS =====
def add_numbers(a, b):
    result = a + b
    print(str(a) + " + " + str(b) + " = " + str(result))
    return result

# Call it
add_numbers(5, 3)
add_numbers(10, 20)


# ===== 4. FUNCTION WITH DEFAULT PARAMETERS =====
def introduce(name, age=18, city="Unknown"):
    print("My name is " + name)
    print("I am " + str(age) + " years old")
    print("I live in " + city)

# Call with all parameters
introduce("Ellyse", 20, "Hawaii")
print()

# Call with some parameters (uses defaults for others)
introduce("Bob", 25)
print()

# Call with only required parameter (uses all defaults)
introduce("Charlie")
print()


# ===== 5. FUNCTION THAT RETURNS A VALUE =====
def calculate_square(num):
    square = num ** 2
    return square

# Store returned value in a variable
result = calculate_square(5)
print("The square of 5 is: " + str(result))


# ===== 6. FUNCTION WITH MULTIPLE RETURN VALUES =====
def get_user_info():
    name = "Ellyse"
    age = 20
    return name, age

# Unpack returned values
person_name, person_age = get_user_info()
print("Name: " + person_name + ", Age: " + str(person_age))
