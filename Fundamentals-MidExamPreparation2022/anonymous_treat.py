string = input().split()
while True:
    data = input()
    if data == "3:1":
        break
    command, num1, num2 = data.split()
    num1 = int(num1)
    num2 = int(num2)
    if command == "merge":
        if num1 < 0:
            num1 = 0
        if num2 >= len(string):
            num2 = len(string) - 1
        string[num1:num2 + 1] = ["".join(string[num1:num2 + 1])]

    elif command == "divide":
        divider = len(string[num1]) // num2
        element = string[num1]
        equal = []
        for i in range(0, len(string[num1]), divider):
            part = element[i:i + divider]
            if divider * num2 == len(element):
                equal.append(part)
            else:
                if i / divider < num2:
                    equal.append(part)
                else:
                    equal[-1] += part
        string[num1:num1 + 1] = equal

print(" ".join(string))
