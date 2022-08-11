def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(current_sum, third_num):
    return current_sum - third_num


num1 = int(input())
num2 = int(input())
num3 = int(input())
result = subtract(sum_numbers(num1, num2), num3)

print(result)
