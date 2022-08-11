inventory = input().split(", ")
while True:
    data = input()
    if data == "Craft!":
        break
    command, item = data.split(" - ")
    if command == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif command == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)
    elif command == "Renew":
        if item in inventory:
            inventory.append(inventory.pop(inventory.index(item)))

print(", ".join(inventory))
