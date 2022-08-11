def printing(legendary_items, junk):
    for elem, value in legendary_items.items():
        print(f"{elem}: {value}")
    for elem, count in junk.items():
        print(f"{elem}: {count}")


legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
condition = False
while not condition:
    data = input().split()
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        item = data[i + 1].lower()
        if item in legendary_items:
            legendary_items[item] += quantity
            if legendary_items[item] >= 250:
                legendary_items[item] = legendary_items[item] - 250
                special_item = ''
                if item == "shards":
                    special_item = "Shadowmourne"
                elif item == "fragments":
                    special_item = "Valanyr"
                elif item == "motes":
                    special_item = "Dragonwrath"
                print(f"{special_item} obtained!")
                condition = True
                break
        else:
            if item not in junk:
                junk[item] = quantity
            else:
                junk[item] += quantity

printing(legendary_items, junk)
