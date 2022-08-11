n = int(input())
word = input()
string_list = []
new_list = []

for i in range(n):
    string_list.append(input())
print(string_list)

for elem in string_list:
    if word in elem:
        new_list.append(elem)
        
print(new_list)

