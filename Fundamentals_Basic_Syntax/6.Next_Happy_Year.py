int_number = int(input())
while True:
    int_number += 1
    str_number = str(int_number)
    num_list = list(str_number)
    num_set = set(str_number)
    if len(num_set) == len(str_number):
        print(str_number)
        break


