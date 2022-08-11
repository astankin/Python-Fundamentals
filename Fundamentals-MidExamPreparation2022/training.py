food_quantity = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
guinea_weight = float(input()) * 1000

for day in range(1, 31):
    food_quantity -= 300
    if day % 2 == 0:
        hay -= food_quantity * 0.05
    if day % 3 == 0:
        cover -= guinea_weight / 3
    if food_quantity <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        exit()
print(f"Everything is fine! Puppy is happy! Food: {(food_quantity / 1000):.2f}, Hay: {(hay / 1000):.2f}, Cover: {(cover / 1000):.2f}.")
