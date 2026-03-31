# Open a file using with and print its type

with open("names.txt", "r") as file_object:
    print(type(file_object))