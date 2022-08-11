data = input()
players_dict = {}
while not data == "Season end":
    if "->" in data:
        player, position, skill = data.split(" -> ")
        skill = int(skill)
        if player not in players_dict:
            players_dict[player] = {position: skill}
        else:
            if position in players_dict[player]:
                if skill > players_dict[player][position]:
                    players_dict[player][position] = skill
            else:
                players_dict[player][position] = skill

    else:
        player1, player2 = data.split(" vs ")
        if player1 in players_dict and player2 in players_dict:
            for position, skill in players_dict[player1].items():
                if position in players_dict[player2]:
                    if skill > players_dict[player2][position]:
                        del players_dict[player2]
                        break
                    elif skill < players_dict[player2][position]:
                        del players_dict[player1]
                        break

    data = input()

sorted_names = dict(sorted(players_dict.items(), key=lambda x: (-sum(x[1].values()), x[0])))
for player, score in sorted_names.items():
    print(f"{player}: {sum(score.values())} skill")
    sorted_items = dict(sorted(score.items(), key=lambda x: (-x[1], x[0])))
    for position, skill in sorted_items.items():
        print(f"- {position} <::> {skill}")



