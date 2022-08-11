def palindrome(num_list):
    for elem in num_list:
        if elem[::1] == elem[::-1]:
            print("True")
        else:
            print("False")


number_list = input().split(", ")
palindrome(number_list)
