n = int(input())
for num in range(1, n + 1):
    digit_sum = 0
    num = str(num)
    for i in range(len(num)):
        digit_sum += int(num[i])
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")



