stops = input()
while True:
    data = input()
    if data == "Travel":
        break
    command = data.split(":")[0]
    if command == "Add Stop":
        index = int(data.split(":")[1])
        string = data.split(":")[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
    elif command == "Remove Stop":
        start_index = int(data.split(":")[1])
        end_index = int(data.split(":")[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]
    elif command == "Switch":
        old_string = data.split(":")[1]
        new_string = data.split(":")[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
