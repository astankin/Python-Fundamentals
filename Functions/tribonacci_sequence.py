def tribonacii(num):
    num_list = ["1", "1", "2"]
    if num <= 3:
        print((" ".join(num_list[:num])))
    else:
        i = 3
        while i < num:
            n = int(num_list[i - 3]) + int(num_list[i - 2]) + int(num_list[i - 1])
            num_list. append(str(n))
            i += 1
        print((" ".join(num_list)))


number = int(input())
tribonacii(number)