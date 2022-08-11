def center_point(num1, num2, num3, num4):
    if abs(num1) < abs(num3) and abs(num2) < abs(num4):
        print(f"({num1}, {num2})")
    elif abs(num1) < abs(num3) and abs(num2) == abs(num4):
        print(f"({num1}, {num2})")
    elif abs(num1) == abs(num3) and abs(num2) < abs(num4):
        print(f"({num1}, {num2})")
    else:
        print(f"({num3}, {num4})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
center_point(int(x1), int(y1), int(x2), int(y2))
