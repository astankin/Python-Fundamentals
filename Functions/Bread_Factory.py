input_string = input().split("|")
current_energy = 100
current_coins = 100
condition = False
for elem in input_string:
    event, number = elem.split("-")

    if event == "rest":
        gained_energy = int(number)
        if current_energy >= 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            current_energy += gained_energy
            print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif event == "order":
        earned_coins = int(number)
        if current_energy - 30 >= 0:
            current_energy -= 30
            current_coins += earned_coins
            print(f"You earned {earned_coins} coins.")
            condition = True
        else:
            current_energy += 50
            print("You had to rest!")

    else:
        ingredient = event
        spent_coins = int(number)
        if current_coins - spent_coins >= 0:
            current_coins -= spent_coins
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            exit()

if condition:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")
