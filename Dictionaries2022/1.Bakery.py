input_info = input().split()
bakery_dict = {}
for i in range(0, len(input_info), 2):
    key = input_info[i]
    value = input_info[i + 1]
    bakery_dict[key] = int(value)


print(bakery_dict)
