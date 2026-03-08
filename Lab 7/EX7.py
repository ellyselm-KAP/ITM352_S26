for num in range(1, 11):

    if num == 5:
        continue   # skip 5

    if num == 8:
        print("Reached 8. Stopping the loop.")
        break      # stop completely

    print(num)