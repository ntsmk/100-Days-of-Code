import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy ver
# ran_letter = random.choices(letters,k=nr_letters)
# ran_symbols = random.choices(symbols,k=nr_symbols)
# ran_num = random.choices(numbers,k=nr_numbers)
# total_list = ran_letter + ran_symbols + ran_num
# total = "".join(str(x) for x in total_list)
# print(total)

# hard ver
ran_letter = random.choices(letters, k=nr_letters)
ran_symbols = random.choices(symbols, k=nr_symbols)
ran_num = random.choices(numbers, k=nr_numbers)
total_list = ran_letter + ran_symbols + ran_num
random.shuffle(total_list)
total = "".join(str(x) for x in total_list)
print(total)
