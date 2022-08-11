def eve_odd(number):
    odd_sum = 0
    even_sum = 0
    for elem in number:
        if int(elem) % 2 == 0:
            even_sum += int(elem)
        else:
            odd_sum += int(elem)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


num = input()
eve_odd(num)
