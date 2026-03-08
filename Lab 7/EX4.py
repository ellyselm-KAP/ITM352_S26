recent_purchase = [36.13, 23.87, 183.35, 22.93, 11.62]
buget = 150
total_spent = 0

for price in recent_purchase:
    total_spent += price
    if total_spent > buget:
        print("This purchase is over budget: ", recent_purchase)
    else:
        print("This purchase is within budget: ", recent_purchase)

def : check_budget(purchase, limit):

