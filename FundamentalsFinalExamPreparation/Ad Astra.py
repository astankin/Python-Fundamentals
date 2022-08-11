import re

text = input()
pattern = r"([?<=#|\|])([a-zA-Z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.findall(pattern, text)
total_calories = 0
for elem in matches:
    calories = int(elem[3])
    total_calories += calories
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for el in matches:
    print(f"Item: {el[1]}, Best before: {el[2]}, Nutrition: {el[3]}")
