from collections import Counter

word = input()
word = word.replace(" ", "")
result = Counter(word)

for key, value in result.items():
    print(f"{key} -> {value}")
