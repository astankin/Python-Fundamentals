import re

urls = []
pattern = r"www\.[a-zA-Z0-9-]+(\.[a-z]+)+"
while True:
    data = input()
    if not data:
        break
    else:
        matches = re.finditer(pattern, data)
        for match in matches:
            urls.append(match.group())

print("\n".join(urls))
