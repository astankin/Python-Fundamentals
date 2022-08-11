import re

n = int(input())
pattern = r"(^[$%])([A-Z][a-z]{2,})\1: (\[\d+\]\|){3}($|=\s)"
for _ in range(n):
    text = input()
    valid = []
    matches = re.finditer(pattern, text)
    for match in matches:
        valid.append(match.group())
        valid_message = match.group()
        digits = re.findall(r"\d+", valid_message)
        word = ""
        for num in digits:
            word += chr(int(num))
        print(f"{match.group(2)}: {word}")
    if not valid:
        print("Valid message not found!")
