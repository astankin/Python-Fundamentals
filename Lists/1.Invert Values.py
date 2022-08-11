num_list = input().split(" ")
new_list = []
for num in num_list:
    number = int(num)
    new_list.append(number * (-1))
print(new_list)