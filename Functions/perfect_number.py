def finding_perfect_num(num):
    num_sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            num_sum += i
    if num_sum / num == 2:
        return True
    return False


number = int(input())
if finding_perfect_num(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect." )
