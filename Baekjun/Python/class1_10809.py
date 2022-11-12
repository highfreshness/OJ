alphabet_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
alphabet = input()

for index, alpha in enumerate(alphabet_list):
    if alpha not in alphabet:
        alphabet_list[index] = -1
    else:
        alphabet_list[index] = alphabet.index(alpha)

for x in alphabet_list:
    print(x, end=" ")

