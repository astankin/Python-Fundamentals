num1 = ord(input())
num2 = ord(input())
string = input()
char_list = [ord(el) for el in string if num1 < ord(el) < num2]
print(sum(char_list))
