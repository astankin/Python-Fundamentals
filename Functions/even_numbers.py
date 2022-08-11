# def even_nums(num):
#     if num % 2 == 0:
#         return True
#     return False
#
#
# numbers = list(map(int, input().split()))
# even_list = list(filter(even_nums, numbers))
# print(even_list)


result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split()))))
print(result)