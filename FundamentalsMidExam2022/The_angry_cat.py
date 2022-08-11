price_rating = [int(num) for num in input().split(", ")]
entry_point = int(input())
items_type = input()
left_sum = []
right_sum = []
if items_type == "cheap":
    left_sum = [num for num in price_rating[:entry_point] if num < price_rating[entry_point]]
    right_sum = [num for num in price_rating[entry_point + 1:] if num < price_rating[entry_point]]
elif items_type == "expensive":
    left_sum = [num for num in price_rating[:entry_point] if num >= price_rating[entry_point]]
    right_sum = [num for num in price_rating[entry_point + 1:] if num >= price_rating[entry_point]]
if sum(left_sum) > sum(right_sum):
    print(f"Left - {sum(left_sum)}")
elif sum(left_sum) < sum(right_sum):
    print(f"Right - {sum(right_sum)}")
else:
    print(f"Left - {sum(left_sum)}")
