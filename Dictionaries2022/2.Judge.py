data = input()
contests_dict = {}
all_data = {}
while not data == "no more time":
    username, contest, points = data.split(" -> ")
    points = int(points)
    if username not in all_data:
        all_data[username] = {contest: points}
    else:
        if contest in all_data[username]:
            if points > all_data[username][contest]:
                all_data[username][contest] = points
        else:
            all_data[username][contest] = points
    if contest not in contests_dict:
        contests_dict[contest] = {username: points}
    else:
        if username in contests_dict[contest]:
            if points > contests_dict[contest][username]:
                contests_dict[contest][username] = points
        else:
            contests_dict[contest][username] = points

    data = input()

for content, participant in contests_dict.items():
    print(f"{content}: {len(participant)} participants")
    #  Sorting the dictionary by values in descending order
    sorted_items = dict(sorted(participant.items(), key=lambda x: (-x[1], x[0])))
    counter = 1
    for name, score in sorted_items.items():
        print(f"{counter}. {name} <::> {score}")
        counter += 1
print("Individual standings:")
#  Sorting the dictionary by sum of values in descending order
sorted_names = dict(sorted(all_data.items(), key=lambda x: (-sum(x[1].values()), x[0])))

counter = 1
for name, score in sorted_names.items():
    print(f"{counter}. {name} -> {sum(score.values())}")
    counter += 1

