input_data = input()
string = ""
output = ""
i = 0
while i < len(input_data):
    if not input_data[i].isdigit():
        string += input_data[i].upper()
        i += 1
    elif input_data[i].isdigit():
        n = ""
        while input_data[i].isdigit():
            n += input_data[i]
            i += 1
            if i == len(input_data):
                break
        output += string * int(n)
        string = ""
counter = len(set(output))

print(f"Unique symbols used: {counter}")
print(output)
