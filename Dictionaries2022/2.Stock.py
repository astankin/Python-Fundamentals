data_input = input().split()
stock = {}
for i in range(0, len(data_input), 2):
    key = data_input[i]
    value = data_input[i + 1]
    stock[key] = int(value)
searched_items = input().split()
for item in searched_items:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

