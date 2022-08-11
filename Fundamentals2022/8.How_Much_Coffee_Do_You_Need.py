command_list = ["coding", "dog", "cat", "movie", "DOG", "CAT", "MOVIE", "CODING"]
coffees = 0
while True:
    command = input()
    if command == "END":
        break
    if command in command_list:
        if command.isupper():
            coffees += 2
        else:
            coffees += 1
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)