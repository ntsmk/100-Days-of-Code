import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

program_over = False
def caesar(original_text, shift_amount, encode_or_decode):

    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1 # -1 for decode

        shifted_position = alphabet.index(letter) + shift_amount # creating the number to use from alphabet list
        shifted_position %= len(alphabet) # prevent error for out of list
        output_text += alphabet[shifted_position] # creating the cipher/decipher text
    print(f"Here is the {encode_or_decode}d result: {output_text}")

    # continue_or_not = input("Type yes if you want to go again, otherwise, no:\n")
    # if continue_or_not == 'yes':
    #     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    #     text = input("Type your message:\n").lower()
    #     shift = int(input("Type the shift number:\n"))
    #
    #     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    # elif continue_or_not == 'no':
    #     print("good bye!")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)



