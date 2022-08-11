gifts_list = input().split()
command = input().split()

while command != ['No', 'Money']:
    index = 0
    gift = ""

    if command[0] == "OutOfStock" and command[1] in gifts_list:
        gift = command[1]
        gifts_list = list(map(lambda x: x.replace(gift, 'None'), gifts_list))
    elif command[0] == "Required":
        index = int(command[2])
        gift = command[1]
        if 0 < index < len(gifts_list):
            gifts_list[index] = gift
    elif command[0] == "JustInCase":
        gift = command[1]
        gifts_list[-1] = gift
    command = input().split()

print(" ".join(elem for elem in gifts_list if elem != "None"))
