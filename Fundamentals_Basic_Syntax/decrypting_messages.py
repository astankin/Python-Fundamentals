key = int(input())
n = int(input())
for i in range(n):
    letter = ord(input()) + key
    print(f"{chr(letter)}", end="")