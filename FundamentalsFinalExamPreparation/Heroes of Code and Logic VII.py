n = int(input())
party = {}
for i in range(n):
    info = input()
    hero_name, hit_points, mana_points = info.split()
    if hero_name not in party:
        party[hero_name] = [int(hit_points), int(mana_points)]
data = input()
while not data == "End":
    data = data.split(" - ")
    command = data[0]
    name = data[1]
    if command == "CastSpell":
        mp_needed = int(data[2])
        spell_name = data[3]
        if party[name][1] >= mp_needed:
            party[name][1] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {party[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        party[name][0] -= damage
        if party[name][0] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {party[name][0]} HP left!")
        else:
            del party[name]
            print(f"{name} has been killed by {attacker}!")
    elif command == "Recharge":
        amount = int(data[2])
        value = 0
        if party[name][1] + amount > 200:
            value = 200 - party[name][1]
            party[name][1] = 200
        else:
            party[name][1] += amount
            value = amount
        print(f"{name} recharged for {value} MP!")

    elif command == "Heal":
        amount = int(data[2])
        value = 0
        if party[name][0] + amount > 100:
            value = 100 - party[name][0]
            party[name][0] = 100
        else:
            party[name][0] += amount
            value = amount
        print(f"{name} healed for {value} HP!")


    data = input()

for name, value in party.items():
    print(name)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
