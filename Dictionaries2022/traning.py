contests = {}
submissions = {}
high_scores = {}
#Filling the contests dict---------
first_command = input()
while first_command != 'end of contests':
    command_for_work = first_command.split(':')
    contest = command_for_work[0]
    password = command_for_work[1]
    contests[contest] = password
    first_command = input()
#---------------------------------
#Filling submissions dict----------
second_command = input()
while second_command != 'end of submissions':
    input_for_work = second_command.split('=>')
    contest_name = input_for_work[0]
    current_password = input_for_work[1]
    username = input_for_work[2]
    points = int(input_for_work[3])
    if contest_name in contests:
        if current_password == contests[contest_name]:
            if username in submissions and submissions[username][0] == contest_name:
                if points > submissions[username][1]:
                    submissions[username][1] = points
            else:
                if username not in submissions:
                    submissions[username] = [contest_name, points]
                else:
                    submissions[username] += [contest_name, points]
    second_command = input()
#------------------------------------------------------------------

#Calculating highscore for print--------------------------
for key, value in submissions.items():
    current_points = 0
    for num in range(1, len(value), 2):
        current_points += int(value[num])
    high_scores[key] = current_points

most_points = 0
person_with_highscore = ""
for key, value in high_scores.items():
    if value > most_points:
        most_points = value
        person_with_highscore = key
else:
    print(f'Best candidate is {person_with_highscore} with total {most_points} points.')
#----------------------------------------------------------

print('Ranking:')

#sorting by key-----------------------
my_dict = {k: v for k, v in sorted(submissions.items(), key=lambda item: item[0])}
#-------------------------------------

#sorting by points----------------------
for key, value in my_dict.items():
    nums = [value[num] for num in range(1, len(value), 2)]
    nums.sort(reverse=True)
    new_value = []
    for i in nums:
        index_of_num = value.index(i)
        index_of_course = index_of_num - 1
        new_value += [value[index_of_course], value[index_of_num]]
    my_dict[key] = new_value
#-----------------------------------------

#printing--------------------------------
for key, value in my_dict.items():
    print(key)
    for i in range(0, len(value), 2):
        print(f'#  {value[i]} -> {value[i+1]}')
#---------------------------------------
