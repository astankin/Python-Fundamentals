while True:
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue
    for char in string:
        print(f"{char*2}", end="")
    print()

