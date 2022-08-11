n = int(input())
synonyms_dict = dict()
for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms_dict:
        synonyms_dict[word] = list()
    if synonym not in synonyms_dict[word]:
        synonyms_dict[word].append(synonym)

for key in synonyms_dict:
    print(f"{key} - {', '.join(synonyms_dict[key])}")
# for key, value in synonyms_dict.items():
#     print(f"{key} - {', '.join(value)}")
