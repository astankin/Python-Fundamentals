def rounding(nums):
    rounded = []
    for num in nums:
        rounded.append(round(num))
    return rounded


num_list = list(map(float, input().split()))

print(rounding(num_list))
