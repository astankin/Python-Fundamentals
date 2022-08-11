events_list = input().split("|")
energy = 100
coins = 100
are_all_events_completed = True

for elem in events_list:
    event, amount = elem.split("-")
    amount = int(amount)
    if event == "rest":
        gained_energy = 0
        if energy + amount > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            energy += amount
            gained_energy = amount
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= 30:
            print(f"You earned {amount} coins.")
            coins += amount
            energy -= 30
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if coins >= amount:
            coins -= amount
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            are_all_event_completed = False
            exit()

if are_all_events_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
