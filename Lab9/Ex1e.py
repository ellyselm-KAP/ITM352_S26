# Open the file names.txt and read its contents using readlines()
# Then print the number of names

with open("names.txt", "r") as file_object:
    contents_list = file_object.readlines()

for line in contents_list:
    print(line.strip())

print(f"Number of names: {len(contents_list)}")
