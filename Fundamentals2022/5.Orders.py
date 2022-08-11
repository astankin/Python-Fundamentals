N = int(input())
total_price = 0
for i in range(N):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    price = price_per_capsule * capsules_per_day * days
    if not 0.01 <= price_per_capsule <= 100:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 <= capsules_per_day <= 2000:
        continue
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")