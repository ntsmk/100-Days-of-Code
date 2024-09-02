import art
import random
print(art.logo)

# todo - print the intro
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# todo - set the number to guess. use Capitalized
NUMBER_TO_GUESS = random.randint(1, 100)

# todo - let user choose easy or hard and take it as input
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# todo - if easy, 10 attempt, if hard, 5 attempt, set it
life = 0
if difficulty == 'easy':
    life = 10
elif difficulty == 'hard':
    life = 5
print(f"You have {life} attempts remaining to guess the number.")

# todo - until the user figure it out the number, keep asking 'make a guess'. use while loop
game_continue = True
while game_continue:
    guess = int(input('Make a guess: '))
# todo - compare the user input and the correct number, show too high or low.
    if guess > NUMBER_TO_GUESS:
        print('Too high.\nGuess again.')
        life -= 1
        print(f"You have {life} attempts remaining to guess the number.")
    elif guess < NUMBER_TO_GUESS:
        print('Too low.\nGuess again.')
        life -= 1
        print(f"You have {life} attempts remaining to guess the number.")
# todo - if input = the correct number, game ends. show 'You got it' and tell the number
    elif guess == NUMBER_TO_GUESS:
        print(f"Congrats!! You got it! The answer was {NUMBER_TO_GUESS}.")
        game_continue = False

# todo - if life becomes 0, tell them game over and game ends
    if life == 0:
        print(f"You've run out of guesses, you lose... the number was {NUMBER_TO_GUESS}.")
        game_continue = False
