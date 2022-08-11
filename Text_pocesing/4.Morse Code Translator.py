code_dict = {
    '.-': 'A',
    '-...': 'B',
    "-.-.": "C",
    "-..": "D",
    ".": 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}
data = input().split("|")
for elem in data:
    letters_list = elem.split()
    word = ""
    for letter in letters_list:
        if letter in code_dict:
            word += code_dict[letter]
    print(f"{word}", end=" ")
