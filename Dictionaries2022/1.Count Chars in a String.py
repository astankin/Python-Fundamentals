string = input()
string = string.replace(" ", "")
chars_dict = {}
for char in string:
    if char not in chars_dict:
        chars_dict[char] = 1
    else:
        chars_dict[char] += 1
for char, quantity in chars_dict.items():
    print(f"{char} -> {quantity}")
    