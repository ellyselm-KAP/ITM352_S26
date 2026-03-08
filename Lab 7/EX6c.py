data = ("hello", 10, "goodbye", 3, "goodnight", 5)

new_value = input("Enter a value to add: ")

try:
    data.append(new_value)
except Exception as e:
    print("Attempted to append to a tuple.")
    print("Error:", e)

print(data)