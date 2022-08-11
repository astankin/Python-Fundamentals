n = int(input())
record = {}
for i in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    if plant not in record:
        record[plant] = [rarity, []]
    else:
        record[plant][0] = rarity

data = input()
while data != "Exhibition":
    command = data.split(": ")[0]
    plant = data.split(": ")[1].split(" - ")[0]
    if command == "Rate":
        rating = float(data.split(":")[1].split(" - ")[1])
        if plant in record:
            record[plant][1].append(rating)
        else:
            print("error")
    elif command == "Update":
        new_rarity = int(data.split(": ")[1].split(" - ")[1])
        if plant in record:
            record[plant][0] = new_rarity
        else:
            print("error")

    elif command == "Reset":
        if plant in record:
            record[plant][1] = []
        else:
            print("error")
    data = input()

for k, v in record.items():
    if not record[k][1]:
        record[k][1] = 0
    else:
        record[k][1] = sum(record[k][1]) / len(record[k][1])


print("Plants for the exhibition:")
for name, value in record.items():
    print(f"- {name}; Rarity: {value[0]}; Rating: {value[1]:.2f}")
