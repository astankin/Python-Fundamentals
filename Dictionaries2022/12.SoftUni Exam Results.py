def printing(data, languages_count):
    print("Results:")
    for users_dict in data.values():
        for user, score in users_dict.items():
            print(f"{user} | {score}")

    print(f"Submissions:")
    for lang, count in languages_count.items():
        print(f"{lang} - {count}")


def creating_data(user_input, languages_count, data):
    username, language, points = user_input.split("-")
    points = int(points)
    if language not in languages_count:
        languages_count[language] = 1
    else:
        languages_count[language] += 1
    if language not in data:
        data[language] = {username: points}
    else:
        if username not in data[language]:
            data[language][username] = points
        else:
            if points > data[language][username]:
                data[language][username] = points
    return data, languages_count


def removing_user(user_input, data):
    username = user_input.split("-")[0]
    for users in data.values():
        if username in users.keys():
            del users[username]
    return data


user_input = input()
data = {}
languages_count = {}
while not user_input == "exam finished":
    if "banned" not in user_input:
        data, languages_count = creating_data(user_input, languages_count, data)
    else:
        data = removing_user(user_input, data)

    user_input = input()

printing(data, languages_count)
