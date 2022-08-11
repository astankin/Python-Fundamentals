import re


def validator(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
    symbols_match = re.findall(r"\W", password)
    if symbols_match:
        print("Password must consist only of letters, digits and _!")
    match_uppercase = re.findall(r"[A-Z]+", password)
    if not match_uppercase:
        print("Password must consist at least one uppercase letter!")
    match_lowercase = re.findall(r"[a-z]+", password)
    if not match_lowercase:
        print("Password must consist at least one lowercase letter!")
    match_digits = re.findall(r"\d+", password)
    if not match_digits:
        print("Password must consist at least one digit!")


password = input()
data = input()
while not data == "Complete":
    data = data.split()
    command = data[0]
    if command == "Make":
        if data[1] == "Upper":
            index = int(data[2])
            letter = password[index]
            password = password.replace(letter, letter.upper(), 1)
            print(password)
        elif data[1] == "Lower":
            index = int(data[2])
            letter = password[index]
            password = password.replace(letter, letter.lower(), 1)
            print(password)
    elif command == "Insert":
        index = int(data[1])
        char = data[2]
        if index in range(len(password)):
            password = password[:index] + char + password[index:]
            print(password)
    elif command == "Replace":
        char = data[1]
        value = int(data[2])
        if char in password:
            replacement = chr(ord(char) + value)
            password = password.replace(char, replacement)
            print(password)
    elif command == "Validation":
        validator(password)
    data = input()
