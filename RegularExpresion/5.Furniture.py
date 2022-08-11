import re
furniture = []
total_cost = 0
while True:
    text = input()
    if text == "Purchase":
        break
    pattern = r">>(?P<item>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)"
    matches = re.finditer(pattern, text)
    for match in matches:
        item = match.group("item")
        price = match.group("price")
        quantity = match.group("quantity")
        amount = float(price) * int(quantity)
        total_cost += amount
        furniture.append(item)
print("Bought furniture:")


pattern = r">>(?P<item>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)"

if total_cost > 0:
    print("\n".join(furniture))
print(f"Total money spend: {total_cost:.2f}")



