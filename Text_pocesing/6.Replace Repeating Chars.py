string = input()
current_char = ""
new_word = ""
for el in string:
    if current_char != el:
        current_char = el
        new_word += el
    else:
        continue


print(new_word)