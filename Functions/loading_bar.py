def loading_bar(num):
    n = num // 10
    loading = "%" * n + "." * (10 - n)
    if num != 100:
        print(f"{num}% [{loading}]")
        print("Still loading...")
    else:
        print(f"100% Complete!")
        print(f"[{loading}]")


numbers = int(input())
loading_bar(numbers)
