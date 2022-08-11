targets = [int(num) for num in input().split()]
data = input()
while not data == "End":
    command, index, value = data.split()
    index = int(index)
    value = int(value)
    if command == "Shoot":
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        start_index = index - value
        end_index = index + value
        if index in range(len(targets)) and start_index in range(len(targets)) and end_index in range(len(targets)):
            targets = targets[:start_index] + targets[end_index + 1:]
        else:
            print("Strike missed!")

    data = input()
print(*targets, sep="|")