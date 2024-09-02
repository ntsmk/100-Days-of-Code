import random
import hangman_art
import hangman_words

lives = 6
word_list = hangman_words.word_list

print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"*********************** It was {chosen_word} ! YOU LOSE, NEXT TIME **********************")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    print(hangman_art.stages[lives])
