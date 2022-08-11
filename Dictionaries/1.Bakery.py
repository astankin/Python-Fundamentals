data = input().split()
bakery = dict()
word = 0
value = 0
for index in range(len(data)):
    if index % 2 == 0:
        word = data[index]
    else:
        value = int(data[index])
    bakery[word] = value
print(bakery)