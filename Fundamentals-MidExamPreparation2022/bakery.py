working_days = input().split("|")
initial_energy = 100
coins = 100
for day in working_days:
    event, number = day.split("-")
    number = int(number)
    if event == "rest":
        gained_energy = 0
        if initial_energy + number > 100:
            gained_energy = 100 - initial_energy
            initial_energy = 100
        else:
            initial_energy += number
            gained_energy = number
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event == "order":
        if initial_energy - 30 >= 0:
            print(f"You earned {number} coins.")
            coins += number
            initial_energy -= 30
        else:
            initial_energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            exit()

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {initial_energy}")
