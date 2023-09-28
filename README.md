# Caesar Cipher

This Python program implements a Caesar Cipher, a simple and classic method of encrypting and decrypting messages. The user can choose to either encrypt or decrypt a message by specifying the direction.

## How to Use

1. Run the program in your Python environment.

2. The program will display an ASCII art logo representing Caesar Cipher.

3. Choose the mode:
   - Type `encode` to encrypt a message.
   - Type `decode` to decrypt a message.

4. Enter your message.

5. Enter the shift number, which determines how many positions each letter in the message will be shifted.

6. The program will encrypt or decrypt the message based on your input and display the result.

7. You can continue encrypting or decrypting messages as many times as you like.

## Code Explanation

The program includes the following key components:

- **ASCII Art Logo**: It displays a stylish logo when the program starts using ASCII art from the `art.py` module.

- **Alphabet**: The English alphabet is stored as a list for reference.

- **caesar() Function**: This function takes the start text, shift amount, and cipher direction as input and returns the encrypted or decrypted text. It preserves numbers, spaces, and symbols in the input text.

- **Loop**: The program uses a `while` loop to ensure the user can continue encrypting or decrypting messages until they choose to exit.

- **Restart**: After each encryption or decryption, the program asks if the user wants to continue. You can type 'yes' to continue or 'no' to exit.

- **Goodbye Message**: When the user decides to exit, the program displays a farewell message.

Feel free to use and modify this code for your encryption and decryption needs. Enjoy using the Caesar Cipher!

### Example

Here's an example of how you can use this program:

1. Choose 'encode' to encrypt a message.

2. Enter your message, e.g., "hello world."

3. Enter the shift number, e.g., 3.

4. The program will display the encrypted message, e.g., "khoor zruog."

5. Choose 'decode' to decrypt the message.

6. Enter the encrypted message, e.g., "khoor zruog."

7. Enter the shift number (in this case, 3).

8. The program will display the original message, e.g., "hello world."

You can keep encoding and decoding messages or exit the program when you're done.
