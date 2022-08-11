info = input()
cities_info = {}
while not info == "Sail":
    city, population, gold = info.split("||")
    population = int(population)
    gold = int(gold)
    if city not in cities_info:
        cities_info[city] = [population, gold]
    else:
        cities_info[city][0] += population
        cities_info[city][1] += gold
    info = input()
data = input()
while not data == "End":
    data = data.split("=>")
    event = data[0]
    town = data[1]
    if event == "Plunder":
        people = int(data[2])
        gold = int(data[3])
        cities_info[town][0] -= people
        cities_info[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_info[town][0] <= 0 or cities_info[town][1] <= 0:
            del cities_info[town]
            print(f"{town} has been wiped off the map!")

    elif event == "Prosper":
        gold = int(data[2])
        if gold >= 0:
            cities_info[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_info[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    data = input()


if cities_info:
    print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
    for city, value in cities_info.items():
        print(f"{city} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
