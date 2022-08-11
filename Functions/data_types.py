def finding_data_type(data, word):
    if data == "int":
        num = int(word) * 2
        print(num)
    elif data == "real":
        num = float(word) * 1.5
        print(f"{num:.2f}")
    elif data == "string":
        print(f"${word}$")


user_input = input()
number = input()
finding_data_type(user_input, number)
