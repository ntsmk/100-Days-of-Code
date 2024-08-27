import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

your_cards = [random.choice(cards),random.choice(cards)]
current_score = your_cards[0]+your_cards[1]
com_first_card = random.choice(cards)
print(your_cards)
print(current_score)

#test commit