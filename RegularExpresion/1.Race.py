import re
from collections import Counter

participants = input().split(", ")
data = input()
results = {}
while not data == "end of race":
    name = "".join(re.findall(r"[a-zA-Z]+", data))
    distance = sum([int(num) for num in re.findall(r"\d", data)])
    if name in participants:
        if name not in results:
            results[name] = distance
        else:
            results[name] += distance
    data = input()
c = Counter(results)
top_3 = c.most_common(3)
for i in range(len(top_3)):
    if i == 0:
        print(f"1st place: {top_3[i][0]}")
    elif i == 1:
        print(f"2nd place: {top_3[i][0]}")
    elif i == 2:
        print(f"3rd place: {top_3[i][0]}")
