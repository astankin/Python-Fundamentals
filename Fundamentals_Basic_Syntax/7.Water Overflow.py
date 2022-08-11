n = int(input())
capacity = 255
water_in_the_tank = 0
for i in range(n):
    liters_of_water = int(input())
    if water_in_the_tank + liters_of_water <= capacity:
        water_in_the_tank += liters_of_water
    elif water_in_the_tank + liters_of_water > capacity:
        print("Insufficient capacity!")
print(water_in_the_tank)