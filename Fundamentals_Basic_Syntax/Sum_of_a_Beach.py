string = input().lower()
new_string = ""
word_list = ["sand", "water", "fish", "sun"]
counter = 0
for i in range(len(string)):
    new_string += string[i]
    if any(x in new_string for x in word_list):
        counter += 1
        new_string = ""
print(counter)
