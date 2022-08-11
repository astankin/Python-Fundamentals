import re

text = input()

pattern = r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z]{1}[a-z]{2})\2(?P<year>\d{4})"
matches = re.finditer(pattern, text)
for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")
    print(f"Day: {day}, Month: {month}, Year: {year}")
