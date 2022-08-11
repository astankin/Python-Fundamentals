import re

pattern_health = r'[^0-9\+\-\*\/\.]'
pattern_damage = r'(-?\d+(\.\d+)?)'
line = [el.strip() for el in input().split(',')]
demon_health = 0
damage = 0

for name in sorted(line):

    matches_health = re.findall(pattern_health, name)
    matches_damage = re.findall(pattern_damage, name)
    for match in matches_health:
        if match:
            demon_health += ord(match)
    for el in matches_damage:
        if el:
            damage += float(el[0])
    for char in name:
        if char == '*':
            damage *= 2
        elif char == '/':
            damage /= 2
    print(f'{name} - {demon_health} health, {damage:.2f} damage')
    demon_health = 0
    damage = 0