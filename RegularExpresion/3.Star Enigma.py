import re
n = int(input())
attacked_planets = []
destroyed_planets = []
for row in range(n):
    message = input()
    count = len(re.findall(r"[STARstar]", message))
    new_message = ""
    for el in message:
        new_message += chr(ord(el) - count)
    pattern = r"@([A-Za-z]+)[^@\-\!\:\>]*:(\d+)[^@\-\!\:\>]*?!([AD])![^@\-\!\:\>]*\->(\d+)"
    matches = re.search(pattern, new_message)
    if matches:
        planet_name = matches.group(1)
        population = int(matches.group(2))
        type_of_attack = matches.group(3)
        soldier_count = int(matches.group(4))
        if type_of_attack == "A":
            attacked_planets.append(planet_name)
        elif type_of_attack == "D":
            destroyed_planets.append(planet_name)
attacked_planets.sort()
destroyed_planets.sort()
print(f"Attacked planets: {len(attacked_planets)}")
for planet in attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")
