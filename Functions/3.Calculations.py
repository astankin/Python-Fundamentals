def calculator(operator, first_num, second_num):
    if operator == "multiply":
        return first_num * second_num
    elif operator == "divide":
        return first_num // second_num
    elif operator == "add":
        return first_num + second_num
    elif operator == "subtract":
        return first_num - second_num


input_operator = input()
num1 = int(input())
num2 = int(input())

print(calculator(input_operator, num1, num2))
