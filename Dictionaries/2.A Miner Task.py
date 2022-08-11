resource = ""
value = ""
my_dict = {}
while True:
    resource = input()
    if resource == "stop":
        break
    value = int(input())
    if resource not in my_dict:
        my_dict[resource] = value
    else:
        my_dict[resource] += value
for key, value in my_dict.items():
    print(f"{key} -> {value}")


