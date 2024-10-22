import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# todo put exception to catch anything other than alphabet and tell warning.
# KeyError
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


word = input("Enter a word: ").upper()
try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
    word = input("Enter a word: ").upper()
print(output_list)
