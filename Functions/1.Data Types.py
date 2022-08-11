def int_multiply():
    print(number * 2)


def float_multiply():
    print(f"{number * 1.5:.2f}")


def surround():
    print(f"${number}$")


command = input()
number = input()
if command == "int":
    number = int(number)
    int_multiply()
elif command == "real":
    number = float(number)
    float_multiply()
elif command == "string":
    surround()
