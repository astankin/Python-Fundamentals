product = input()
quantity = int(input())


def calculation(item, number):
    price = 0
    if item == "coffee":
        price = 1.50
    elif item == "water":
        price = 1.00
    elif item == "coke":
        price = 1.40
    elif item == "snacks":
        price = 2.00
    amount = number * price
    return amount



print(calculation())
