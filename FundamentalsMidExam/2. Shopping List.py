items = input().split("!")
command_type = input()
while not command_type == "Go Shopping!":
    command = command_type.split()[0]
    item = command_type.split()[1]
    if command == "Urgent" and item not in items:
        items.insert(0, item)
    elif command == "Unnecessary" and item in items:
        items.remove(item)
    elif command == "Correct" and item in items:
        new_item = command_type.split()[2]
        for index in range(len(items)):
            if items[index] == item:
                items[index] = new_item
    elif command == "Rearrange" and item in items:
        items.remove(item)
        items.append(item)

    command_type = input()
print(", ".join(items))