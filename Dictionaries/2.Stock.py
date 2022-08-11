items = input().split()
products = input().split()
my_dict = {}
keys = 0
value = 0
for index in range(len(items)):
    if index % 2 == 0:
        keys = items[index]
    else:
        value = int(items[index])
    my_dict[keys] = value
for elem in products:
    if elem in my_dict:
        print(f"We have {my_dict[elem]} of {elem} left")
    else:
        print(f"Sorry, we don't have {elem}")