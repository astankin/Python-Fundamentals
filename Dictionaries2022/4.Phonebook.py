def searching(num,phonebook):
    for i in range(num):
        searched_name = input()
        if searched_name not in phonebook:
            print(f"Contact {searched_name} does not exist.")
        else:
            print(f"{searched_name} -> {phonebook[searched_name]}")


data = input()
phonebook = {}
while not data.isdigit():
    name, number = data.split("-")
    phonebook[name] = number
    data = input()

n = int(data)
searching(n, phonebook)
