number_of_lines = int(input())
total_sum = 0
for i in range(number_of_lines):
    letter = ord(input())
    total_sum += letter
print(f"The sum equals: {total_sum}")