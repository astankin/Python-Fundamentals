data = input()
dwarfs_dict = {}
colors = {}
while not data == "Once upon a time":
    name, hat_color, physics = data.split(" <:> ")
    physics = int(physics)
    if hat_color not in dwarfs_dict:
        if hat_color not in colors:
            colors[hat_color] = 1
        else:
            colors[hat_color] += 1
        dwarfs_dict[hat_color] = {name: physics}
    else:
        if name in dwarfs_dict[hat_color]:
            if physics > dwarfs_dict[hat_color][name]:
                dwarfs_dict[hat_color][name] = physics
        else:
            dwarfs_dict[hat_color][name] = physics

    data = input()

sorted_dwarfs_dict = dict(sorted(dwarfs_dict.items(), key=lambda x: (-sum(x[1].values()), x[0])))
for key, value in sorted_dwarfs_dict.items():
    for name, num in value.items():
        print(f"({key})", end=" ")
        print(f"{name} <-> {num}")

