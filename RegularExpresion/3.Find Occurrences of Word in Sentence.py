import re
matches = []
text = input()
searched_word = input()
pattern = rf"\b{searched_word}\b"
result = re.finditer(pattern, text, re.IGNORECASE)
for word in result:
    matches.append(word.group())
print(len(matches))
