import random
import art

want_play = False
play_or_not = input("Do you want to play Black Jack? Type 'y' or 'n': ")
if play_or_not == 'y':
    want_play = True
else:
    want_play = False
while want_play:
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    your_cards = [random.choice(cards),random.choice(cards)]
    current_score = sum(your_cards)

    com_cards = [random.choice(cards)]
    com_first_score = sum(com_cards)
    current_com_score = com_first_score

    print(f"Your cards: {your_cards}, current score: {current_score}")
    print(f"Computer's first card : {com_first_score}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    while current_com_score < 17:
        com_cards.append(random.choice(cards))
        current_com_score = sum(com_cards)

    not_end = True
    while not_end:
        if another_card == 'y':
            your_cards.append(random.choice(cards))
            current_score = sum(your_cards)
            if current_score > 21:
                print("You went over, you lose...")
                not_end = False
                final_hand = your_cards
                final_score = sum(your_cards)
                com_final_hand = com_cards
                com_final_score = sum(com_cards)
                print(f"Your final hand: {your_cards}, final score: {final_score}")
                print(f"Computer's final hand : {com_final_hand}, final score: {com_final_score}")
                break
            print(f"Your cards: {your_cards}, current score: {current_score}")
            print(f"Computer's first card : {com_first_score}")
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        # elif current_score > 21 and 11 in your_cards:

        else:
            not_end = False
            final_hand = your_cards
            final_score = sum(your_cards)
            com_final_hand = com_cards
            com_final_score = sum(com_cards)
            print(f"Your final hand: {your_cards}, final score: {final_score}")
            print(f"Computer's final hand : {com_final_hand}, final score: {com_final_score}")

            # todo figure it out how to judge winner vs computer
            if final_score > com_final_score and final_score <= 21:
                print("You win!!!")
                want_play = False
            elif final_score < com_final_score and com_final_score > 21:
                print("You win!!!")
                want_play = False
            elif final_score < com_final_score and com_final_score <= 21:
                print("You lose..")
                want_play = False
            elif final_score == com_final_score:
                print("Draw!")
                want_play = False

    play_or_not = input("Do you want to play Black Jack? Type 'y' or 'n': ")
    if play_or_not == 'y':
        want_play = True
    else:
        want_play = False