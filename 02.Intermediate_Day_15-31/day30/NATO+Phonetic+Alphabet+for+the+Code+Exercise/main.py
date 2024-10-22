import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# todo put exception to catch anything other than alphabet and tell warning.
# KeyError
# it ask but not keep asking. should I write while loop?
try:
    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
else:
    print(output_list)
