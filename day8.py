alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(original_text,shift_amount):
    original_text = text
    shift_amount = shift
    thislist1 = []
    thislist2 = []
    encrypted_word = ""

    for i in text:
        thislist1.append(alphabet.index(i))
        # z = 25

    for i in thislist1:
        i += shift
        thislist2.append(i)
        # shifted_z = more than 26

    for i in thislist2:
        if i >= 26:
            i -= 26
        encrypted_word += alphabet[i]

    print(encrypted_word)

encrypt("a",1)
