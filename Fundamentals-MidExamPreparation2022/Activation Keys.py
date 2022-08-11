string = input()
string_list = list(string)
data = input()
while not data == "Generate":
    command = data.split(">>>")[0]
    if command == "Contains":
        sub_string = data.split(">>>")[1]
        if sub_string in string:
            print(f"{string} contains {sub_string}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        start_index = int(data.split(">>>")[2])
        end_index = int(data.split(">>>")[3])
        if data.split(">>>")[1] == "Upper":
            sub_string = string[start_index:end_index].upper()
            string = string[:start_index] + sub_string + string[end_index:]
        elif data.split(">>>")[1] == "Lower":
            sub_string = string[start_index:end_index].lower()
            string = string[:start_index] + sub_string + string[end_index:]
        print(string)

    elif command == "Slice":
        start_index = int(data.split(">>>")[1])
        end_index = int(data.split(">>>")[2])
        string = string[:start_index] + string[end_index:]
        print(string)

    data = input()
print(f"Your activation key is: {string}")