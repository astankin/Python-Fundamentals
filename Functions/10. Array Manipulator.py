def exchange(num_list, index):
    if 0 <= index < len(num_list):
        first_part = num_list[0:index + 1]
        second_part = num_list[index + 1:]
        exchanged_list = second_part + first_part
        return exchanged_list
    else:
        print("Invalid index")
        return num_list


def get_max_odd(num_list):
    filter_only_odds = []
    for el in num_list:
        if el % 2 == 1:
            filter_only_odds.append(el)
    if len(filter_only_odds) == 0:
        print("No matches")
    else:
        max_even = max(filter_only_odds)

        for index in range(len(num_list) - 1, -1, -1):
            if num_list[index] == max_even:
                print(index)
                break


def get_max_even(num_list):
    filter_only_even = [num for num in num_list if num % 2 == 0]  # Използване на List Comprehension
    # for el in num_list:
    #     if el % 2 == 0:
    #         filter_only_even.append(el)

    if len(filter_only_even) == 0:
        print("No matches")
    else:
        max_even = max(filter_only_even)

        for index in range(len(num_list) - 1, -1, -1):
            if num_list[index] == max_even:
                print(index)
                break


def get_min_odd(num_list):
    filter_only_odd = []
    for el in num_list:
        if el % 2 == 1:
            filter_only_odd.append(el)
    if len(filter_only_odd) == 0:
        print("No matches")
    else:
        min_even = min(filter_only_odd)

        for index in range(len(num_list) - 1, -1, -1):
            if num_list[index] == min_even:
                print(index)
                break


def get_min_even(num_list):
    filter_only_even = []
    for el in num_list:
        if el % 2 == 0:
            filter_only_even.append(el)
    if len(filter_only_even) == 0:
        print("No matches")
    else:
        min_even = min(filter_only_even)

        for index in range(len(num_list) - 1, -1, -1):
            if num_list[index] == min_even:
                print(index)
                break


def first_even(num_list):
    if int(command.split()[1]) > len(num_list):
        print("Invalid count")
    else:
        even_list = []
        for el in num_list:
            if el % 2 == 0:
                if len(even_list) < int(command.split()[1]):
                    even_list.append(el)
        print(even_list)


def first_odd(num_list):
    if int(command.split()[1]) > len(num_list):
        print("Invalid count")
    else:
        odd_list = []
        for el in num_list:
            if el % 2 == 1:
                if len(odd_list) < int(command.split()[1]):
                    odd_list.append(el)
        print(odd_list)


def last_even(num_list):
    if int(command.split()[1]) > len(num_list):
        print("Invalid count")
    else:
        num = int(command.split()[1])
        even_list = []
        for el in num_list:
            if el % 2 == 0:
                even_list.append(el)
        print(even_list[-num:])


def last_odd(num_list):
    if int(command.split()[1]) > len(num_list):
        print("Invalid count")
    else:
        num = int(command.split()[1])
        odd_list = []
        for el in num_list:
            if el % 2 == 1:
                odd_list.append(el)
        print(odd_list[-num:])


numbers_as_string = input().split()
numbers = list(map(int, numbers_as_string))
command = input()
while command != "end":
    if command.split()[0] == "exchange":
        index = int(command.split()[1])
        numbers = exchange(numbers, index)
    elif command.split()[0] == "max":
        if command.split()[1] == "odd":
            get_max_odd(numbers)
        elif command.split()[1] == "even":
            get_max_even(numbers)
    elif command.split()[0] == "min":
        if command.split()[1] == "odd":
            get_min_odd(numbers)
        elif command.split()[1] == "even":
            get_min_even(numbers)
    elif command.split()[0] == "first":
        if command.split()[2] == "odd":
            first_odd(numbers)
        elif command.split()[2] == "even":
            first_even(numbers)
    elif command.split()[0] == "last":
        if command.split()[2] == "odd":
            last_odd(numbers)
        elif command.split()[2] == "even":
            last_even(numbers)

    command = input()
print(numbers)
