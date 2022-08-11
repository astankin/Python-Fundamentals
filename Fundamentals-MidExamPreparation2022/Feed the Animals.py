animals = []
while True:
    input_data = input()
    if input_data == "Last Info":
        break
    input_data = input_data.split(":")
    command = input_data[0]
    if command == "Add":
        animal_name = input_data[1]
        daily_food_limit = input_data[2]
        area = input_data[3]

    elif command == "Feed":
        pass
