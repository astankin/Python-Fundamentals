def printing(courses_info):
    for course, students in courses_info.items():
        print(f"{course}: {len(students)}")
        for student in students:
            print(f"-- {student}")


data = input()
courses_info = {}
while not data == "end":
    course_name, student_name = data.split(" : ")
    if course_name not in courses_info:
        courses_info[course_name] = [student_name]
    else:
        courses_info[course_name].append(student_name)

    data = input()
printing(courses_info)