number_of_people = int(input())
capacity = int(input())
counter = 0
while number_of_people > 0:
    number_of_people -= capacity
    counter += 1
print(counter)