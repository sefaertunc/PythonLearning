import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
answer = input("Enter your name: ").upper()

output_list = [phonetic_dict[letter] for letter in answer]
print(output_list)
