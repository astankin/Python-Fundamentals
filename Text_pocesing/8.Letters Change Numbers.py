import string
input_data = input().split()
total_sum = 0
for elem in input_data:
    first_letter = elem[0]
    second_letter = elem[-1]
    number = int(''.join([num for num in elem if num.isdigit()]))
    position1 = int(string.ascii_lowercase.index(first_letter.lower())) + 1
    position2 = int(string.ascii_lowercase.index(second_letter.lower())) + 1
    if first_letter.isupper():
        number /= position1
    elif first_letter.islower():
        number *= position1
    if second_letter.isupper():
        number -= position2
    elif second_letter.islower():
        number += position2
    total_sum += number
print(f"{total_sum:.2f}")
