data = input()
products = {}
while not data == "statistics":
    item, quantity = data.split(": ")
    if item not in products:
        products[item] = int(quantity)
    else:
        products[item] += int(quantity)

    data = input()

print("Products in stock:")
#
[print(f"- {item}: {quantity} ") for item, quantity in products]
print(f"Total Products: {len(products)}\n"
      f"Total Quantity: {sum(products.values())}")