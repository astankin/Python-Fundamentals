targets = list(map(int, input().split()))
data = input()
while data != "End":
    command, index, number = data.split()
    index = int(index)
    number = int(number)
    if command == "Shoot":
        if index in range(len(targets)):
            targets[index] -= number
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif command == "Add":
        if index in range(len(targets)):
            targets.insert(index, number)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        if index in range(len(targets)) and 0 <= (index - number) <= len(targets) - number and 0 <= (
                index + number) <= len(targets) + number:
            new_list = targets[:index - number] + targets[(index + 1) + number:]
            targets = new_list
        else:
            print("Strike missed!")

    data = input()
print('|'.join(map(str, targets)))