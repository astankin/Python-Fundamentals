def price_calc(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "water":
        return quantity * 1
    elif product == "snacks":
        return quantity * 2


product_input = input()
numbers_of_products = int(input())
price = price_calc(product_input, numbers_of_products)
print(f"{price:.2f}")
