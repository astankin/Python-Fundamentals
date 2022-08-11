message = list(input())
data = input()
while not data == "Decode":
    command = data.split("|")[0]
    if command == "Move":
        num = int(data.split("|")[1])
        message = message[num:] + message[:num]
    elif command == "Insert":
        index = int(data.split("|")[1])
        value = list(data.split("|")[2])
        message = message[:index] + value + message[index:]
    elif command == "ChangeAll":
        substring = data.split("|")[1]
        replacement = data.split("|")[2]
        for i in range(len(message)):
            if message[i] == substring:
                message[i] = replacement
    data = input()

print(f"The decrypted message is: {''.join(message)}")