path = input().split(".")
extension = path[1]
file_name = path[0].split("\\")[-1]
print(f"File name: {file_name}")
print(f"File extension: {extension}")
