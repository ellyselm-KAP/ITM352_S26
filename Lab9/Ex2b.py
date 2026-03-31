import os

filename = "my_custom_spreadsheet.csv"

if os.path.exists(filename) and os.access(filename, os.R_OK):
    print("File exists and is readable.")
    print(f"File size: {os.path.getsize(filename)} bytes")

    with open(filename, "r") as file_object:
        print("First line of file:")
        print(file_object.readline().strip())
else:
    print("File does not exist or is not readable.")
    