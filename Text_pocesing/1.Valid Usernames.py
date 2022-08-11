text = input().split(", ")

for word in text:
    condition = True
    if len(word) in range(3, 17):
        for ch in word:
            if ch.isalpha() or ch.isdigit() or ch == "_" or ch == "-":
                condition = True
            else:
                condition = False
                break
        if condition:
            print(word)