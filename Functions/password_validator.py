def password_check(user_input):
    number_of_digits = 0
    is_valid = True
    if not 6 <= len(user_input) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    for elem in user_input:
        if not elem.isdigit() and not elem.isalpha():
            print("Password must consist only of letters and digits")
            is_valid = False
            break
    for elem in user_input:
        if elem.isdigit():
            number_of_digits += 1
    if number_of_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


command = input()
password_check(command)
