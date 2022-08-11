num1 = int(input())
num2 = int(input())


def factorial(number):
    result = 1
    for num in range(1, number+1):
        result *= num
    return result


number1 = factorial(num1)
number2 = factorial(num2)
print(f"{(number1 / number2):.2f}")