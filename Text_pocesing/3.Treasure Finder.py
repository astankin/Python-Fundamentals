keys = list(map(lambda x: int(x), input().split()))

while True:
    data = input()
    if data == "find":
        break
    message = ""
    start_index = 0
    treasure_type = ""
    coordinates = ""
    for el in data:
        message += chr(ord(el) - keys[start_index])
        start_index += 1
        if start_index == len(keys):
            start_index = 0
    first_index = message.find("&")
    k = first_index + 1
    while message[k] != "&":
        treasure_type += message[k]
        k += 1
    index1 = message.index("<")
    index2 = message.index(">")
    coordinates = message[index1 + 1: index2]

    print(f"Found {treasure_type} at {coordinates}")