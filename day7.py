import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
matched_letters = []

# TODO-1: - Use a while loop to let the user guess again.
display = placeholder
while "_" in display:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            matched_letters.append(letter)
        elif letter in matched_letters:
            display += letter
        else:
            display += "_"

    print(display)

