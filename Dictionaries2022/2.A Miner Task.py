items_dict = {}


def crating_dict():
    while True:
        word = input()
        if word == "stop":
            break
        quantity = int(input())
        if word not in items_dict:
            items_dict[word] = quantity
        else:
            items_dict[word] += quantity


def printing(items_dict):
    for key, value in items_dict.items():
        print(f"{key} -> {value}")


crating_dict()
printing(items_dict)
