n = int(input())
collection = {}
for i in range(n):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]
    collection[piece] = [composer, key]
info = input()
while not info == "Stop":
    command = info.split("|")[0]
    piece = info.split("|")[1]
    if command == "Add":
        composer = info.split("|")[2]
        key = info.split("|")[3]
        if piece not in collection:
            collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command == "Remove":
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        new_key = info.split("|")[2]
        if piece in collection:
            collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    info = input()
for piece, value in collection.items():
    print(f"{piece} -> Composer: {value[0]}, Key: {value[1]}")
