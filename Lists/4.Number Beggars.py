nums = list(map(int, input().split(", ")))
beggars = int(input())
sum_list = [0] * beggars
counter = 0
for num in nums:
    sum_list[counter] += num
    counter += 1
    if counter == beggars:
        counter = 0
print(sum_list)
