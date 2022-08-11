data = input()
force_dict = {}


def printing_info(force_dict):
    for side, value in force_dict.items():
        if len(value) > 0:
            print(f"Side: {side}, Members: {len(value)}")
            for elem in value:
                print(f"! {elem}")


def force_user_check(force_dict, force_name):
    for value in force_dict.values():
        if force_name in value:
            return False
    return True


while not data == "Lumpawaroo":
    if "|" in data:
        force_side, force_user = data.split(" | ")
        if force_side not in force_dict and force_user_check(force_dict, force_user):
            force_dict[force_side] = [force_user]
        elif force_side in force_dict and force_user_check(force_dict, force_user):
            force_dict[force_side].append(force_user)
    elif "->" in data:
        force_user, force_side = data.split(" -> ")
        for key in force_dict:
            if force_user in force_dict[key]:
                force_dict[key].remove(force_user)
        if force_side not in force_dict:
            force_dict[force_side] = [force_user]
            print(f"{force_user} joins the {force_side} side!")
        elif force_side in force_dict and force_user not in force_side:
            force_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    data = input()
printing_info(force_dict)
