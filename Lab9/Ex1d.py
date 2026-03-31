# Open the file names.txt and read its contents one line at a time
# Then print the number of names

with open("names.txt", "r") as file_object:
    count = 0
    line = file_object.readline()

    while line:
        print(line.strip())
        count += 1
        line = file_object.readline()

print(f"Number of names: {count}")
