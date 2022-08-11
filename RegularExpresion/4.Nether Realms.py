import re

text = list(map(lambda x: x.strip(), input().split(",")))
health_pattern = r"[^0-9\+\-\*\/\.]"
for name in sorted(text):
    health = 0
    health_matches = re.findall(health_pattern, name)
    damage = sum(float(num) for num in re.findall(r"-?\d+\.?\d*", name))
    for char in health_matches:
        health += ord(char)
    for symbol in name:
        if symbol == "*":
            damage *= 2
        elif symbol == "/":
            damage /= 2
    print(f"{name} - {health} health, {damage:.2f} damage")

