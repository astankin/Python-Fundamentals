string = input()
counter = int(input())

new_string = lambda a, n: a * n
result = new_string(string, counter)
print(result)
