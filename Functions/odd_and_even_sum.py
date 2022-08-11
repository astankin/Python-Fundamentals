def odd_even_sum(numbers):
    odd_sum = 0
    even_sum = 0
    for num in numbers:
        if int(num) % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


num_list = input()
odd_even_sum(num_list)
