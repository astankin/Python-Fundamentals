def password_validation(password):
    is_valid = True
    counter = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    for elem in password:
        if not elem.isdigit() and not elem.isalpha():
            print("Password must consist only of letters and digits")
            is_valid = False
            break
    for elem in password:
        if elem.isdigit():
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


passcode = input()
password_validation(passcode)
