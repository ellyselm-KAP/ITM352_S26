searchMe = [2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

target = int(input("Enter a number to search for: "))

low = 0
high = len(searchMe) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    
    if searchMe[mid] == target:
        found = True
        break
    elif searchMe[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Found!")
else:
    print("Not found.")

    