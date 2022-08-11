string = input()
digits = ""
letters = ""
chars = ""
for el in string:
    if el.isdigit():
        digits += el
    elif el.isalpha():
        letters += el
    else:
        chars += el

print(digits)
print(letters)
print(chars)