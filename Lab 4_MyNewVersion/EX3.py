url = input("Enter a URL: ")

parts = url.split(".")
domain = parts[-2]
tld = parts[-1]

print("Domain:", domain)
print("TLD:", tld)

