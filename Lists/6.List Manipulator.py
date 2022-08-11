def max_num(odd_even, nums):
    if len(odd_even) == 0:
        return "No matches"
    else:
        for j in range(len(num_list) - 1, -1, -1):
            if nums[j] == max(odd_even):
                return j


def max_even_odd(word):
    if word == "even":
        return max_num(even_list, num_list)
    elif word == "odd":
        return max_num(odd_list, num_list)


def min_num(even_odd):
    if len(even_odd) == 0:
        return "No matches"
    else:
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] == min(even_odd):
                return i


def min_even_odd(word):
    if word == "even":
        return min_num(even_list)
    elif word == "odd":
        return min_num(odd_list)


def last_even_odd(count):
    if count > len(num_list):
        print("Invalid count")
    else:
        if command_list[2] == "even":
            print(even_list[-count:])
        elif command_list[2] == "odd":
            print(odd_list[-count:])


def first_even_odd(count):
    if count > len(num_list):
        print("Invalid count")
    else:
        if command_list[2] == "even":
            print(even_list[:count])
        elif command_list[2] == "odd":
            print(odd_list[:count])


def exchange(index, number_list):
    if index >= len(number_list) or index < 0:
        print("Invalid index")
        return number_list
    else:
        first_list = list(number_list[0:index])
        second_list = list(number_list[index + 1::])
        result = second_list + first_list
        result.append(int(number_list[index]))
        return result


num_list = list(map(int, input().split()))
command = input()

while command != "end":
    command_list = command.split()
    odd_list = list(num for num in num_list if num % 2 != 0)
    even_list = list(num for num in num_list if num % 2 == 0)

    if command_list[0] == "exchange":
        num_list = exchange(int(command_list[1]), num_list)

    elif command_list[0] == "max":
        print(max_even_odd(command_list[1]))

    elif command_list[0] == "min":
        print(min_even_odd(command_list[1]))

    elif command_list[0] == "first":
        first_even_odd(int(command_list[1]))

    elif command_list[0] == "last":
        last_even_odd(int(command_list[1]))

    command = input()
if command == "end":
    print(num_list)
