# Append a new name to the end of the file and then print the full contents

with open("names.txt", "a") as file_object:
    print("Appending new name to file")
    file_object.write("Adams, Amy\n")

with open("names.txt", "r") as file_object:
    contents = file_object.read()
    print(contents)
    