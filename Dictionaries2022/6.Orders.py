data = input()
orders = {}
while not data == "buy":
    product, price, quantity = data.split()
    quantity = int(quantity)
    price = float(price)
    if product not in orders:
        orders[product] = {}
        if price not in orders[product]:
            orders[product]['price'] = price
        if quantity not in orders[product]:
            orders[product]['quantity'] = quantity
    else:
        orders[product]['price'] = price
        orders[product]['quantity'] += quantity

    data = input()
for item, value in orders.items():
    total_amount = value['price'] * value['quantity']
    print(f"{item} -> {total_amount:.2f}")
