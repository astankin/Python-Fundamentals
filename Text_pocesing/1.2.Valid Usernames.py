import string

text = input().split(", ")
for word in text:
    condition = True
    if len(word) in range(3, 16):
        aloud_elem = string.digits + string.ascii_letters + "-" + "_"
        for elem in word:
            if elem not in aloud_elem:
                condition = False
                break
        if condition:
            print(word)



