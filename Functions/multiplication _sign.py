def fined_positive_or_negative(num_list):
    negatives = 0
    for num in num_list:
        if num == 0:
            return print("zero")
        elif num < 0:
            negatives += 1
    if negatives % 2 != 0:
        print("negative")
    else:
        print("positive")


n1, n2, n3 = int(input()), int(input()), int(input())
num_list = [n1, n2, n3]
fined_positive_or_negative(num_list)