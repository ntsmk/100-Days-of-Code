import art
import game_data
import random

# part 0
# todo - play demo game until I understand how it works
# todo - create todo list like this here
# todo - make comments if needed for each todos

# part 1 - variables
# todo - create variables name, followers, description, and nationalities. import the data from dictionaries
# import dic data from the different py file and choose 1 data set randomly
print(art.logo)
game_over = False
current_score = 0
dic = game_data.data
# todo - create new variables, refresh the variables.
while not game_over:
    data_a = random.sample(dic, 1)

    # set variables
    name_a = data_a[0]['name']
    followers_a = data_a[0]['follower_count']
    description_a = data_a[0]['description']
    country_a = data_a[0]['country']
    # todo - print that data as "compare A".
    print(f"Compare A: {name_a}, {description_a}, from {country_a}.")

    print(art.vs)

    # todo - create variables name, followers, description, and nationalities. import the data from dictionaries
    # todo - print that data as "compare B".
    data_b = random.sample(dic, 1)
    name_b = data_b[0]['name']
    followers_b = data_b[0]['follower_count']
    description_b = data_b[0]['description']
    country_b = data_b[0]['country']
    print(f"Against B: {name_b}, {description_b}, from {country_b}.")

    # part 2 - comparison
    # todo -  print "who has more followers? type A or B" take input, let the user choose
    choise = input("Who has more followers? Type 'A' or 'B': ")
    answer = ""

    # todo - compare followers count A and B, which is more
    if followers_a > followers_b:
        answer = 'A'
    else:
        answer = 'B'

    # todo - if the answer is same, add 1 score to current score.
    # todo -  if the answer is not same, print (Sorry, that's wrong. Final score:xx) and end it
    if answer == choise:
        current_score += 1
        print(f"You are right! Current score: {current_score}.")
    else:
        print(f"Sorry, that's wrong. Final score:{current_score}")
        game_over = True
