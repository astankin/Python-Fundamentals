string1 = list(input())
string2 = list(input())
for i in range(len(string1)):
    if string1[i] != string2[i]:
        string1[i] = string2[i]
        print(("".join(string1)))

