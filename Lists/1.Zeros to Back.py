num_list = list(map(int, input().split(", ")))
zero_list = []
new_num_list = []
for num in num_list:
    if num == 0:
        zero_list.append(num)
    else:
        new_num_list.append(num)
print(new_num_list + zero_list)
