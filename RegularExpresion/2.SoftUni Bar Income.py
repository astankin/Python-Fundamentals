import re

text = input()
income = 0
while not text == "end of shift":
    matches = re.search(r"(\%[A-Z][a-z]+\%)([^\|\$\%\.]*?)(\<\w+\>)([^\|\$\%\.]*?)(\|[0-9]+\|)([^\|\$\%\.]*?)([0-9.]+[0-9])(?=\$)", text)
    if matches:
        name = matches.group(1)[1:-1]
        product = matches.group(3)[1:-1]
        count = int(matches.group(5)[1:-1])
        price = float(matches.group(7))
        amount = count * price
        income += amount
        print(f"{name}: {product} - {amount:.2f}")

    text = input()
print(f"Total income: {income:.2f}")

