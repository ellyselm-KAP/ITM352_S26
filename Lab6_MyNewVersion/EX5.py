age = 70
weekday = "Tuesday"
matinee = True

price = 14  # normal price

# Senior discount
if age >= 65:
    price = min(price, 8)

# Tuesday discount
if weekday == "Tuesday":
    price = min(price, 10)

# Matinee discount
if matinee:
    if age >= 65:
        price = min(price, 5)
    else:
        price = min(price, 8)

print("Age:", age)
print("Weekday:", weekday)
print("Matinee:", matinee)
print("Final price: $", price)
