def check_budget(purchase, limit):
    if purchase > limit:
        return "This purchase is over budget!"
    else:
        return "This purchase is within budget."
    
tests = [
    (36.13, 50),    # within
    (23.87, 50),    # within
    (183.35, 50),   # over
    (50, 50),       # edge case: equal (within)
    (50.01, 50)     # just over
]

for purchase, limit in tests:
    result = check_budget(purchase, limit)
    print(purchase, "->", result)


    recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50

for price in recent_purchases:
    print(check_budget(price, budget))