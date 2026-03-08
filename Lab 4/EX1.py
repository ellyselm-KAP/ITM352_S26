# Name : Ellyse mcchesney 
# Date : Feb 1, 2026

first = input("First name: ")
middle = input("Middle initial: ")
last = input("Last name: ")

full_name = first + " " + middle + " " + last
print(full_name)

first = input("First name: ")
middle = input("Middle initial: ")
last = input("Last name: ")

full_name = f"{first} {middle} {last}"
print(full_name)


first = input("First name: ")
middle = input("Middle initial: ")
last = input("Last name: ")

full_name = "%s %s %s" % (first, middle, last)
print(full_name)


first = input("First name: ")
middle = input("Middle initial: ")
last = input("Last name: ")

full_name = "{} {} {}".format(first, middle, last)
print(full_name)


first = input("First name: ")
middle = input("Middle initial: ")
last = input("Last name: ")

parts = [first, middle, last]
full_name = " ".join(parts)
print(full_name)


first = input("First name: ")
middle = input("Middle initial: ")
last = input("Last name: ")

parts = [first, middle, last]
full_name = "{} {} {}".format(*parts)
print(full_name)
