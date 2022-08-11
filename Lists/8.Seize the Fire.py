fires_cells = input().split("#")
water = int(input())
effort = 0
putted_out_cells = 0
print(f"Cells:")

for elem in fires_cells:
    cell = elem.split(" = ")
    fire_level = cell[0]
    cell_value = 0
    if fire_level == "High" and 81 <= int(cell[1]) <= 125:
        cell_value = int(cell[1])
    elif fire_level == "Medium" and 51 <= int(cell[1]) <= 80:
        cell_value = int(cell[1])
    elif fire_level == "Low" and 1 <= int(cell[1]) <= 50:
        cell_value = int(cell[1])
    if water - cell_value >= 0:
        water -= cell_value
        effort += cell_value * 0.25
        putted_out_cells += cell_value
        if not cell_value == 0:
            print(f" - {cell_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {putted_out_cells}")
