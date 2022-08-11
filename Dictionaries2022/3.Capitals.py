cities = input().split(", ")
capitals = input().split(", ")
dictionary = dict(zip(cities, capitals))
[print(f"{city} -> {capital} ") for city, capital in dictionary.items()]
