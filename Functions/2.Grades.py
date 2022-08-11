def grade_calc(num):
    word = ""
    if 2 <= num <= 2.99:
        word = "Fail"
    elif 3 <= num <= 3.49:
        word = "Poor"
    elif 3.50 <= num <= 4.49:
        word = "Good"
    elif 4.50 <= num <= 5.49:
        word = "Very Good"
    elif 5.50 <= num <= 6:
        word = "Excellent"
    return word


grade = float(input())

print(grade_calc(grade))
