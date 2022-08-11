input_data = input().split("|")
health = 100
bitcoins = 0
for room in input_data:
    command, number = room.split()
    number = int(number)
    if command == "potion":
        if health + number > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100

        else:
            health += number
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        monster = command
        health -= number
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {input_data.index(room) + 1 }")
            exit()
print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")
