string = input()
print('\n'.join([f"{string[i]}{string[i+1]}" for i in range(len(string)) if string[i] == ":"]))
