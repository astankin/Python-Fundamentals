n = int(input())
parking_dict = {}
for i in range(n):
    data = input().split()
    command = data[0]
    username = data[1]
    if command == "register":
        license_plate_number = data[2]
        if username not in parking_dict:
            parking_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif command == "unregister":
        if username not in parking_dict:
            print(f"ERROR: user {username} not found")
        else:
            del parking_dict[username]
            print(f"{username} unregistered successfully")

[print(f"{username} => {license_plate_number}") for username, license_plate_number in parking_dict.items()]