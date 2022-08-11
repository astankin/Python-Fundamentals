string = input().lower()
word_list = ["sand", "water", "fish", "sun"]
counter = 0
for word in word_list:
    if word in string:
        counter += string.count(word)
print(counter)