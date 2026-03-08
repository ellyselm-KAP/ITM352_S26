data = ("hello", 10, "goodbye", 3, "goodnight", 5)

new_value = input("Enter a value to add: ")

data = list(data)
data.append(new_value)

print(data)