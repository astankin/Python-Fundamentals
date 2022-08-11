import re

text = input()
pattern = r"(^| )[a-zA-Z0-9]+[._-]?[a-zA-Z0-9]*@[a-z]+-?.?[a-z]+(\.[a-z]+)+"
pattern1 = r"(^| )[a-zA-Z0-9]+[.\-_]*[a-zA-Z0-9]+@[a-z\-]+\.[a-z]+(\.[a-z]+)*"
matches = re.finditer(pattern1, text)
for match in matches:
    print(match[0])
