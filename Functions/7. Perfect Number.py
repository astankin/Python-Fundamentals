def perfect_number(number):
    result = 0
    for index in range(1, number):
        if number % index == 0:
            result += index
    if result == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())
perfect_number(num)
