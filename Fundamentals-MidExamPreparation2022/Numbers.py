numbers = list(map(int, input().split()))
average = round(sum(numbers) / len(numbers), 2)
greater_then_average = [num for num in numbers if num > average]
if len(greater_then_average) == 0:
    print("No")
else:
    greater_then_average.sort(reverse=True)
    # print(*greater_then_average[:5])
    print(' '.join(map(str, greater_then_average[:5])))

