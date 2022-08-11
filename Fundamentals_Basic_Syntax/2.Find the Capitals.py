word_list = list(input())
new_list = []
for i in range(len(word_list)):
    if word_list[i].isupper():
        new_list.append(i)
print(new_list)