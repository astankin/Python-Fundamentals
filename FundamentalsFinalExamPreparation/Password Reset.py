string = input()
data = input()
while not data == "Done":
    command = data.split()[0]
    if command == "TakeOdd":
        new_raw_pass = ""
        for i in range(len(string)):
            if i % 2 != 0:
                new_raw_pass += string[i]
        string = new_raw_pass
        print(string)

    elif command == "Cut":
        index = int(data.split()[1])
        length = int(data.split()[2])
        sub_string = string[index:index+length]
        string = string.replace(sub_string, "", 1)
        print(string)
    elif command == "Substitute":
        sub_string = data.split()[1]
        substitute = data.split()[2]
        if sub_string in string:
            string = string.replace(sub_string, substitute)
            print(string)
        else:
            print("Nothing to replace!")

    data = input()
print(f"Your password is: {string}")
