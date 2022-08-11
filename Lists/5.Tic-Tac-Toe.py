def check(row):
    first_elem = row[0][0]
    are_all_equal = False
    for j in range(3):
        if row[j] == first_elem:
            are_all_equal = True
        else:
            return False
        first_elem = row[j]

    if are_all_equal:
        return True


num_list = []
for i in range(3):
    element = num_list.append(input().split())

first_player_won = False
second_player_won = False

for i in range(len(num_list)):
    elem = num_list[i]
    if check(elem):
        if elem[i] == "1":
            first_player_won = True
            break
        elif elem[i] == "2":
            second_player_won = True
            break

if num_list[0][0] == num_list[1][1] == num_list[2][2]:
    if num_list[0][0] == "1":
        first_player_won = True
    elif num_list[0][0] == "2":
        second_player_won = True

if num_list[0][2] == num_list[1][1] == num_list[2][0]:
    if num_list[0][2] == "1":
        first_player_won = True
    elif num_list[0][2] == "2":
        second_player_won = True

if num_list[0][0] == num_list[1][0] == num_list[2][0]:
    if num_list[0][0] == "1":
        first_player_won = True
    elif num_list[0][0] == "2":
        second_player_won = True

if num_list[0][1] == num_list[1][1] == num_list[2][1]:
    if num_list[0][1] == "1":
        first_player_won = True
    elif num_list[0][1] == "2":
        second_player_won = True

if num_list[0][2] == num_list[1][2] == num_list[2][2]:
    if num_list[0][2] == "1":
        first_player_won = True
    elif num_list[0][2] == "2":
        second_player_won = True

if first_player_won:
    print("First player won")
elif second_player_won:
    print("Second player won")
else:
    print("Draw!")
