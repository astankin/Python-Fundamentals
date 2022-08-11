import re

string = input()
pattern = r"(?<=(\=|\/))([A-Z][a-zA-Z]{2,})\1"
destinations = []
count = 0
matches = re.finditer(pattern, string)
for elem in matches:
    destinations.append(elem.group(2))
    count += len(elem.group(2))


print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {count}")
