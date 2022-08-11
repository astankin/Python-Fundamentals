elem_sequence = input().split()
command = input()
number_of_moves = 0
while not command == "end":
    number_of_moves += 1
    num1, num2 = command.split()
    index1 = int(num1)
    index2 = int(num2)
    if index1 == index2 or 0 > index1 or index1 >= len(elem_sequence) or 0 > index2 or index2 >= len(elem_sequence):
        half = len(elem_sequence) // 2
        added_elem = "-" + str(number_of_moves) + "a"
        for i in range(2):
            elem_sequence.insert(half, added_elem)
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue
    if elem_sequence[index1] == elem_sequence[index2]:
        print(f"Congrats! You have found matching elements - {elem_sequence[index1]}!")
        removed_elem = elem_sequence[index1]
        elem_sequence.remove(removed_elem)
        elem_sequence.remove(removed_elem)
        if not elem_sequence:
            print(f"You have won in {number_of_moves} turns!")
            exit()
    else:
        print("Try again!")

    command = input()
if command == "end" and elem_sequence:
    print("Sorry you lose :(")
    print(" ".join(elem_sequence))
