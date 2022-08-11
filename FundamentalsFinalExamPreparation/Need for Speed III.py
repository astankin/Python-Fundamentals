n = int(input())
cars_info = {}
for i in range(n):
    car, mileage, fuel = input().split("|")
    if car not in cars_info:
        cars_info[car] = [int(mileage), int(fuel)]
data = input()
while not data == "Stop":
    command = data.split(" : ")[0]
    car = data.split(" : ")[1]
    if command == "Drive":
        distance = int(data.split(" : ")[2])
        fuel = int(data.split(" : ")[3])
        if cars_info[car][1] >= fuel:
            cars_info[car][0] += distance
            cars_info[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_info[car][0] >= 100000:
                del cars_info[car]
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")

    elif command == "Refuel":
        fuel = int(data.split(" : ")[2])
        liters = 0
        if cars_info[car][1] + fuel >= 75:
            liters = 75 - cars_info[car][1]
            cars_info[car][1] = 75
        else:
            liters = fuel
            cars_info[car][1] += liters
        print(f"{car} refueled with {liters} liters")
    elif command == "Revert":
        kilometers = int(data.split(" : ")[2])
        cars_info[car][0] -= kilometers
        if cars_info[car][0] < 10000:
            cars_info[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    data = input()

for car, value in cars_info.items():
    print(f"{car} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
