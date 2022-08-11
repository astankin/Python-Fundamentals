budget = float(input())
one_kg_flour_price = float(input())
egs_pack_price = one_kg_flour_price * 0.75
liter_milk_price = one_kg_flour_price + one_kg_flour_price * 0.25
used_milk_price = liter_milk_price * 0.250
colored_eggs = 0
loaves = 0
spent_money = 0
while True:
    spent_money += one_kg_flour_price + egs_pack_price + used_milk_price
    if spent_money >= budget:
        spent_money -= one_kg_flour_price + egs_pack_price + used_milk_price
        break
    loaves += 1
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {(budget - spent_money):.2f}BGN left.")