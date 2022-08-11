employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
total_people = int(input())
hours = 0
counter = 1
while True:
    if total_people == 0:
        break
    if counter % 4 != 0:
        total_people -= employee1 + employee2 + employee3
        hours += 1
        if total_people < 0:
            break
    else:
        hours += 1
    counter += 1


print(f"Time needed: {hours}h.")
