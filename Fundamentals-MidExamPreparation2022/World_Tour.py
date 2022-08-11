array = list(map(lambda x: int(x), input().split()))
data = input()
while not data == "end":
    data = data.split()
    command = data[0]
    if command == "swap":
        index1 = int(data[1])
        index2 = int(data[2])
        array[index1], array[index2] = array[index2], array[index1]
    elif command == "multiply":
        index1 = int(data[1])
        index2 = int(data[2])
        array[index1] *= array[index2]
    elif command == "decrease":
        array = [num - 1 for num in array]

    data = input()
print(*array, sep=", ")