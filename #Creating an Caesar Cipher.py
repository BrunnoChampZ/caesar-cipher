#Creating an Caesar Cipher

# Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Create a loop to start the program.
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        break
    else:
        print("Invalid input, please choose 'encode' or 'decode' =)")

# Inputs from the user.
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Combine the encrypt and decrypt functions into a single function called caesar().
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #fix the code to keep the number/space/symbol when the text is encoded/decoded
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}\nYour original text was {text}")

# Add a while loop so that the user can keep encrypting and decrypting messages.
while True:
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Farewell my friend =)")
        break
    elif restart == "yes":
        should_continue = True
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar (start_text=text, shift_amount=shift, cipher_direction=direction)
    else:
        print("Invalid input, please choose 'yes' or 'no' ^^")

# End
