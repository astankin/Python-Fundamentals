words = input().split()
my_dict = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in my_dict:
        my_dict[word_lower] = 0
    my_dict[word_lower] += 1
for elem in my_dict:
    if my_dict[elem] % 2 != 0:
        print(elem, end=" ")