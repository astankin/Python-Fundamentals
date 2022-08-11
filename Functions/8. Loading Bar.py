def loading_bar(number):
    loading = []
    result = number // 10
    for percent in range(result):
        loading.append("%")
    for dot in range(10 - result):
        loading.append(".")
    if number == 100:
        print(f"{number}% Complete!")
        print("[", *loading, "]", sep="")
    else:
       # print(number, "%", " ", "[", *loading, "]", sep="")
        print("Still loading...")
        print(f"{number}% [{''.join(loading)}]")


num = int(input())
loading_bar(num)
