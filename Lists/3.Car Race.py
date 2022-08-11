num_list = input().split()
left_time = 0
right_time = 0
for i in range(len(num_list) // 2):
    num = int(num_list[i])
    left_time += num
    if num == 0:
        left_time *= 0.8
for i in range(len(num_list) - 1, len(num_list) // 2, -1):
    num = int(num_list[i])
    right_time += num
    if num == 0:
        right_time *= 0.8

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")
