import re

count = 0
mirror_word = []
output = []
string = input()
pattern = r"(?<=(@|#))([a-zA-Z]{3,})(\1)(\1)([a-zA-z]{3,})(\1)"
matches = re.finditer(pattern, string)
for match in matches:
    count += 1
    first_word = match.group(2)
    second_word = match.group(5)
    if first_word == second_word[::-1]:
        mirror_word.append([first_word, second_word])
if count == 0:
    print("No word pairs found!")
else:
    print(f"{count} word pairs found!")
if not mirror_word:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    for pair in mirror_word:
        current_pair = " <=> ".join(pair)
        output.append(current_pair)
    print(", ".join(output))

