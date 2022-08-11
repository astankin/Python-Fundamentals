string = input().split()
shuffles = int(input())
first_half = []
second_half = []
new_cards = []

for shuffle in range(shuffles):
    for i in range(len(string) // 2):
        first_half.append(string[i])

    for elem in string:
        if elem not in first_half:
            second_half.append(elem)

    for j in range(len(first_half)):
        new_cards.append(first_half[j])
        new_cards.append(second_half[j])
    first_half.clear()
    second_half.clear()
    string = new_cards.copy()
    new_cards = []

print(string)
