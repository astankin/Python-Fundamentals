command = input()
products = {}


def add_elem(key, values):
    if key in products:
        products[keys] += values
    else:
        products[key] = values
    return products


while command != "statistics":
    keys = command.split(":")[0]
    value = int(command.split(":")[1])
    add_elem(keys, value)
    command = input()
print("Products in stock:")
for elem in products:
    print(f"- {elem}: {products[elem]}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
