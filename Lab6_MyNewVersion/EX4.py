year = 2006 

is_leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

print("Birth year:", year)
print("Leap year?", is_leap)

# Test closest leap year
closest_leap = 2008
print("Closest leap year:", closest_leap)
print("Leap year?", ((closest_leap % 4 == 0) and (closest_leap % 100 != 0)) or (closest_leap % 400 == 0))



def isLeapYear(year):
    if year % 400 == 0:
        return "Leap year"
    if year % 100 == 0:
        return "Not a leap year"
    if year % 4 == 0:
        return "Leap year"
    return "Not a leap year"


# Test the function
print(isLeapYear(2006))
print(isLeapYear(2008))
