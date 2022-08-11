first_string = input()
second_string = input()
changed_string = list(first_string)
for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        changed_string[i] = second_string[i]
        print("". join(changed_string))