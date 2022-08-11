budget = int(input())
while True:
    command = input()
    if command == "End":
        break
    price = int(command)
    if budget < price:
        print("You went in overdraft!")
        break
    budget -= price
if command == "End":
    print("You bought everything needed.")

