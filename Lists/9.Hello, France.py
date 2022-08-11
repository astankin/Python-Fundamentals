command = input().split("|")
start_money = int(input())
earned_money = 0
spent_money = 0
profit = 0
for elem in command:
    item = elem.split("->")
    item_type = item[0]
    price = float(item[1])
    condition = False
    if item_type == "Clothes" and price <= 50:
        condition = True
    elif item_type == "Shoes" and price <= 35:
        condition = True
    elif item_type == "Accessories" and price <= 20.50:
        condition = True
    if condition is True and start_money >= price:
        start_money -= price
        spent_money += price
        profit += price * 0.4
        price = price + price * 0.4
        earned_money += price
        print(f"{price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if start_money + earned_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
