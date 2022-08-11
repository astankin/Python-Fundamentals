string = input().split(" ")
A_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_game_stopped = False
for elem in string:
    card = elem.split("-")

    if "A" in card and int(card[1]) in A_team:
        A_team.remove(int(card[1]))
    elif "B" in card and int(card[1]) in B_team:
        B_team.remove(int(card[1]))

    if len(A_team) < 7 or len(B_team) < 7:
        is_game_stopped = True
        break
print(f"Team A - {len(A_team)}; Team B - {len(B_team)}")
if is_game_stopped:
    print("Game was terminated")
