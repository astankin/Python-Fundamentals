num1 = int(input())
num2 = int(input())
nums = list(num * num1 for num in range(1, num2 + 1))
print(nums)