import art
print(art.logo)
print("Welcome to secret auction program")

new_bids_needed = True
dic = {}

while new_bids_needed:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dic[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "no":
        new_bids_needed = False
    else:
        print("\n" * 20)

who_won = max(dic, key=dic.get)
bid_won = dic[who_won]
print(f"The winner is {who_won} with a bid of ${bid_won}.")
