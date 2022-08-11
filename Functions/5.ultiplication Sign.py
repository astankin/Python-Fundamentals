num1 = int(input())
num2 = int(input())
num3 = int(input())
is_negative = False
if num1 == 0 or num2 == 0 or num3 == 0:
    print("zero")
else:
    if num1 < 0 and num2 > 0 and num3 > 0:
        is_negative = True
    elif num1 > 0 and num2 < 0 and num3 > 0:
        is_negative = True
    elif num1 > 0 and num2 > 0 and num3 < 0:
        is_negative = True
    elif num1 < 0 and num2 < 0 and num3 < 0:
        is_negative = True
    if is_negative:
        print("negative")
    else:
        print("positive")