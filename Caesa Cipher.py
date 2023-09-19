import string
alphabet = list(string.ascii_lowercase)+list(string.ascii_lowercase)
print(alphabet)
direction = input("Type 'encode' to encrype, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        new_position = alphabet[alphabet.index(letter)+ shift_amount]
        cipher_text +=new_position
    print(f"The Encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        new_position = alphabet[alphabet.index(letter) - shift_amount]
        cipher_text +=new_position
    print(f"The decrypt text is {cipher_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
