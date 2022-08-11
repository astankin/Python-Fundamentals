import math

students_count = [0] * int(input())
lectures_count = int(input())
additional_bonus = int(input())
max_bonus = 0
if lectures_count == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
    exit()
for i in range(len(students_count)):
    count_of_attendances = int(input())
    students_count[i] = count_of_attendances

    bonus_score = math.ceil(count_of_attendances / lectures_count * (5 + additional_bonus))
    if bonus_score > max_bonus:
        max_bonus = bonus_score

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max(students_count)} lectures.")
