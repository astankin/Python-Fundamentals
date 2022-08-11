message = input()
command = input()
while not command == "Decode":
    command = command.split("|")
    instruction = command[0]
    if instruction == "Move":
        number = int(command[1])
        message = message[number:] + message[:number]
    elif instruction == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    elif instruction == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

    command = input()
print(f"The decrypted message is: {message}")
