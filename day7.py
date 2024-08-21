import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: ").lower()
# placeholder_list = []
# for i in chosen_word:
#     placeholder_list.append("_")
# placeholder = ''.join(placeholder_list)
# print(placeholder)

placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(placeholder)

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display = ""
for letter in chosen_word:
    if letter == guess:
        print("Right")
        display += letter
    else:
        print("Wrong")
        display += "_"
print(display)

# display_list = []
#
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#         display_list.append(letter)
#     else:
#         print("Wrong")
#         display_list.append("_")
#
# display = ''.join(display_list)
# print(display)