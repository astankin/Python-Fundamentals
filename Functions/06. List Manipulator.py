# finding if number is odd or even and returning the max even or odd number
def max_even_odd(word):
    if word == "even":
        return max_num(even_list, num_list)
    elif word == "odd":
        return max_num(odd_list, num_list)


# finding max number(even or odd)
def max_num(odd_even, nums):
    if len(odd_even) == 0:
        return "No matches"
    else:
        for j in range(len(num_list) - 1, -1, -1):
            if nums[j] == max(odd_even):
                return j


# finding if number is odd or even and returning the min even or odd number
def min_num(even_or_odd_list):
    if len(even_or_odd_list) == 0:
        return "No matches"
    else:
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] == min(even_or_odd_list):
                return i


# finding min number(even or odd)
def min_even_odd(word):
    if word == "even":
        return min_num(even_list)
    elif word == "odd":
        return min_num(odd_list)


# finding if input command is first or last and prints  first or last n even or odd numbers
def first_last(com, count, even_odd):
    if com == "first":
        if even_odd == "even":
            return print(even_list[:count])
        elif even_odd == "odd":
            return print(odd_list[:count])
    elif com == "last":
        if even_odd == "even":
            return print(even_list[-count:])
        elif even_odd == "odd":
            return print(odd_list[-count:])


# manipulate the list by given number
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

    elif command_list[0] == "first" or command_list[0] == "last":
        if int(command_list[1]) > len(num_list):
            print("Invalid count")
        else:
            first_last(command_list[0], int(command_list[1]), command_list[2])

    command = input()
if command == "end":
    print(num_list)
