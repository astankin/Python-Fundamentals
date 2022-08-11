import re
output = []
text = input()
#pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
pattern = r"\+359([ -])2\1\d{3}\1\d{4}\b"
matches = re.finditer(pattern, text)
for match in matches:
    output.append(match.group())
print(", ".join(output))