n = int(input())
for _ in range(n):
    data = input()
    name = ""
    age = ""
    index1 = 0
    index2 = 0
    condition = False
    condition1 = False
    for ch in data:
        if ch == "@":
            condition = True
            index1 = data.index("@")
        elif ch == "|" and condition:
            index2 = data.index("|")
            name = data[index1 + 1: index2]
            condition = False
        elif ch == "#":
            condition1 = True
            index1 = data.index("#")
        elif ch == "*" and condition1:
            index2 = data.index("*")
            age = data[index1 + 1:index2]
            condition1 = False

    print(f"{name} is {age} years old.")
