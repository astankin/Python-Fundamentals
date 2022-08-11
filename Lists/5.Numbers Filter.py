n = int(input())
string = []
new_string = []
for i in range(n):
    number = int(input())
    string.append(number)
command = input()
for elem in string:
    if command == "even" and elem % 2 == 0:
        new_string.append(elem)
    elif command == "odd" and elem % 2 != 0:
        new_string.append(elem)
    elif command == "negative" and elem < 0:
        new_string.append(elem)
    elif command == "positive" and elem >= 0:
        new_string.append(elem)
print(new_string)