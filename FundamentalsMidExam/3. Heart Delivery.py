data = list(map(int, input().split("@")))
command = input()
position = 0
while command != "Love!":
    length = int(command.split()[1])
    position += length
    if position >= len(data):
        position = 0
    if data[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        data[position] -= 2
        if data[0] == 0:
            print(f"Place {position} has Valentine's day.")


    command = input()

print(f"Cupid's last position was {position}.")

if all(houses == 0 for houses in data):
    print("Mission was successful.")
else:
    missed_houses = len([elem for elem in data if elem != 0])
    print(f"Cupid has failed {missed_houses} places.")