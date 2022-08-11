def calculation(string1, string2):
    total_sum = 0
    for i in range(len(string1)):
        if i in range(len(string2)):
            total_sum += ord(string1[i]) * ord(string2[i])
        else:
            total_sum += ord(string1[i])
    return total_sum


number = 0
data = input().split()
first_string = data[0]
second_string = data[1]
if len(first_string) > len(second_string):
    number = calculation(first_string, second_string)
else:
    number = calculation(second_string, first_string)

print(number)
