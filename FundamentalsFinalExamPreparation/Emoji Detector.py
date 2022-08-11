import re
text = input()
cool_threshold_sum = 1
the_coolest = []
output = []
pattern = r"(\:\:|\*\*)([A-Z][a-z]{2,})(\1)"
matches = re.finditer(pattern, text)
digits_found = re.findall(r"\d", text)
for num in digits_found:
    cool_threshold_sum *= int(num)
for match in matches:
    output.append(match.group())
for elem in output:
    coolness = 0
    for char in elem:
        if char.isalpha():
            coolness += int(ord(char))
    if coolness > cool_threshold_sum:
        the_coolest.append(elem)

print(f"Cool threshold: {cool_threshold_sum}")
print(f"{len(output)} emojis found in the text. The cool ones are:")
for el in the_coolest:
    print(el)
