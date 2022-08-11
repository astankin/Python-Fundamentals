def characters(char1, char2):
    for elem in range(char1 + 1, char2):
        print(chr(elem), end=" ")


cha1 = ord(input())
cha2 = ord(input())

characters(cha1, cha2)
