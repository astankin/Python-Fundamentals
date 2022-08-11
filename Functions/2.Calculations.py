operator = input()
number1 = int(input())
number2 = int(input())


def calculation(oper, num1, num2):
    result = 0
    if oper == "multiply":
        result = num1 * num2
    elif oper == "divide":
        result = int(num1 / num2)
    elif oper == "add":
        result = num1 + num2
    elif oper == "subtract":
        result = num1 - num2
    return result


print(calculation(operator, number1, number2))
