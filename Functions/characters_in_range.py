def char_list(ch1, ch2):
    result = []
    for i in range(ord(ch1) + 1, ord(ch2)):
        result.append(chr(i))
    return result


char1 = input()
char2 = input()
print(" ".join(char_list(char1, char2)))