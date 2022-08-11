num_list = list(map(int, input().split(" ")))
n = int(input())

for i in range(n):
    num_list.remove(min(num_list))

print(*num_list, sep=", ")
