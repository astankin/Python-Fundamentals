data = input()
courses = {}
while ":" in data:
    name, id, course = data.split(":")
    if course not in courses:
        courses[course] = {}
    courses[course][id] = name
    data = input()
searched_course = data.replace("_", " ")
for id in courses[searched_course]:
    print(f"{courses[searched_course][id]} - {id}")