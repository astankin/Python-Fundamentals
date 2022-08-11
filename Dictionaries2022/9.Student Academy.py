n = int(input())
students_dict = {}
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students_dict:
        students_dict[name] = [grade]
    else:
        students_dict[name].append(grade)

for name, grade in students_dict.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        print(f"{name} -> {average_grade:.2f}")
