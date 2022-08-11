import re

text = input()
pattern = r"\b_{1}[a-zA-Z0-9]+\b"
matches = re.findall(pattern, text)
for i in range(len(matches)):
    matches[i] = matches[i][1:]
print(",".join(matches))
