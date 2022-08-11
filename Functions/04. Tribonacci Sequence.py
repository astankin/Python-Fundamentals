def tribonacci(number):
    for i in range(number - 3):
        result = num_list[i] + num_list[i + 1] + num_list[i + 2]
        num_list.append(result)
    for index in num_list:
        print(index, end=" ")


num = int(input())
num_list = [1, 1, 2]
if num == 1:
    print(f"{1}")
elif num == 2:
    print(f"{1} {1}")
elif num == 3:
    print(f"{1} {1} {2}")
else:
    tribonacci(num)
