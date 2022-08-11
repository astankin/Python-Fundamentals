import re

n = int(input())
pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
for i in range(n):
    barcode = input()
    match = re.search(pattern, barcode)
    if match:
        digit_pattern = r"\d"
        digit_match = re.findall(digit_pattern, barcode)
        if not digit_match:
            print("Product group: 00")
        else:
            product_group = "".join(digit_match)
            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")


