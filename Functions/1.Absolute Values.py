def absolute_value(number_list):
    abs_nums = list()
    for n in number_list:
        abs_nums.append(abs(n))
    return abs_nums


num_list = list(map(float, input().split()))

print(absolute_value(num_list))
