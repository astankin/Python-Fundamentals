def prime_num(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


number = int(input())
print(prime_num(number))
