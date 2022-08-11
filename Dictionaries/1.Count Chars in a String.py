text = input()
text = text.replace(" ", "")
my_dict = {}
for elem in text:
    if elem not in my_dict:
        my_dict[elem] = 1
    else:
        my_dict[elem] += 1
for key, value in my_dict.items():
    print(f"{key} -> {value}")