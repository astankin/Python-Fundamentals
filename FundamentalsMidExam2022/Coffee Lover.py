starting_list = input().split()
n = int(input())
for i in range(n):
    data = input()
    data = data.split()
    command = data[0]
    if command == "Include":
        coffee = data[1]
        starting_list.append(coffee)
    elif command == "Remove":
        number = int(data[2])
        if number <= len(starting_list):
            if data[1] == "first":
                starting_list = starting_list[number:]
            elif data[1] == "last":
                starting_list = starting_list[:-number]
    elif command == "Prefer":
        index1 = int(data[1])
        index2 = int(data[2])
        if index1 in range(len(starting_list)) and index2 in range(len(starting_list)):
            starting_list[index1], starting_list[index2] = starting_list[index2], starting_list[index1]
    elif command == "Reverse":
        starting_list = starting_list[::-1]

print("Coffees:")
print(' '.join(starting_list))

