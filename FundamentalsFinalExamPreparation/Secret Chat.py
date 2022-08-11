message = input()
data = input()
while not data == "Reveal":
    command = data.split(":|:")[0]
    if command == "InsertSpace":
        index = int(data.split(":|:")[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif command == "Reverse":
        substring = (data.split(":|:")[1])
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message = message + substring
            print(message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring = (data.split(":|:")[1])
        replacement = (data.split(":|:")[2])
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)
    data = input()
print(f"You have a new text message: {message}")
