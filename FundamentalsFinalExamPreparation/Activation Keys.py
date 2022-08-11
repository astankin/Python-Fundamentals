string = input()
data = input()
while not data == "Generate":
    data = data.split(">>>")
    command = data[0]
    if command == "Contains":
        substring = data[1]
        if substring in string:
            print(f"{string} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        start_index = int(data[2])
        end_index = int(data[3])
        if data[1] == "Upper":
            sub_string = string[start_index:end_index].upper()
            string = string[:start_index] + sub_string + string[end_index:]
        elif data[1] == "Lower":
            sub_string = string[start_index:end_index].lower()
            string = string[:start_index] + sub_string + string[end_index:]
        print(string)
    elif command == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])
        string = string[:start_index] + string[end_index:]
        print(string)

    data = input()

print(f"Your activation key is: {string}")