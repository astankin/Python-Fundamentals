messages_list = []
while True:
    data = input()
    if data == "end":
        break
    data = data.split()
    command = data[0]
    message = data[1]
    if command == "Chat":
        messages_list.append(message)
    elif command == "Delete":
        if message in messages_list:
            messages_list.remove(message)
    elif command == "Edit":
        edited_version = data[2]
        if message in messages_list:
            index = messages_list.index(message)
            messages_list[index] = edited_version
    elif command == "Pin":
        if message in messages_list:
            messages_list.append(messages_list.pop(messages_list.index(message)))
    elif command == "Spam":
        for i in range(1, len(data)):
            messages_list.append(data[i])

print('\n'.join(messages_list))
