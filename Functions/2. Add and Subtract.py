def add_and_subtract():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    def sum_numbers(number1, number2):
        result = number1 + number2
        return result

    def subtract(result, number3):
        result1 = result - number3
        print(result1)

    sum_numbers(num1, num2)
    subtract(sum_numbers(num1, num2), num3)


add_and_subtract()
