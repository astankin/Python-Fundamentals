num_list = input().split()
text = input()
new_text = ""
for num in num_list:
    index = 0
    for i in range(len(num)):
        index += int(num[i])
    if index > len(text):
        index = index - len(text)
    print(f"{text[index]}", end="")
    new_text = text.replace(text[index], "", 1)
    text = new_text


