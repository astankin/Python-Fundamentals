from math import floor


def distance_calc(sum1, sum2):
    if sum1 <= sum2:
        print(f"({int(x1)}, {int(y1)})")
    elif sum1 > sum2:
        print(f"({int(x2)}, {int(y2)})")


x1, y1 = floor(float(input())), floor(float(input()))
x2, y2 = floor(float(input())), floor(float(input()))
first_sum = abs(x1) + abs(y1)
second_sum = abs(x2) + abs(y2)
distance_calc(first_sum, second_sum)
