data = input()
new_string = ""
strength = 0

for i in range(len(data)):
    if data[i] == ">":
        strength += int(data[i + 1])
        new_string += data[i]
    elif data[i] != ">" and strength > 0:
        strength -= 1
    else:
        new_string += data[i]

print(new_string)