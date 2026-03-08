email = input("Enter an email address: ")

parts = email.split("@")
username = parts[0]
domain = parts[1]

print("Username:", username)
print("Domain:", domain)


email = input("Enter an email address: ")

at_index = email.index("@")
username = email[:at_index]
domain = email[at_index + 1:]

print("Username:", username)
print("Domain:", domain)





