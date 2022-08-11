contests_dict = {}
results = {}
while True:
    user_input = input()
    if user_input == "end of contests":
        break
    contest, password = user_input.split(":")
    contests_dict[contest] = password

while True:
    data = input()
    if data == "end of submissions":
        break
    current_contest, current_pass, username, points = data.split("=>")
    points = int(points)
    if current_contest in contests_dict and contests_dict[current_contest] == current_pass:
        if username not in results:
            results[username] = {current_contest: points}
        else:
            if current_contest in results[username]:
                if points > results[username][current_contest]:
                    results[username][current_contest] = points
            else:
                results[username][current_contest] = points

the_best_candidate = ""
the_best_score = 0
for user, score in results.items():
    total_points = sum(score.values())
    if total_points > the_best_score:
        the_best_score = total_points
        the_best_candidate = user
print(f"Best candidate is {the_best_candidate} with total {the_best_score} points.")
# sorting the values by descending order
sorted_results = {key: dict(sorted(val.items(), key=lambda ele: ele[1], reverse=True))
                  for key, val in results.items()}

sorted_results_final = dict(sorted(sorted_results.items(), key=lambda x: (x[0], x[1])))
print("Ranking:")
for user, value in sorted_results_final.items():
    print(f"{user}")
    for content, score in value.items():
        print(f"#  {content} -> {score}")

