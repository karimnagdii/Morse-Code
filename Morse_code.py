"""
This module provides functions to encrypt and decrypt messages between English and Morse code.

The module contains the following functions:
    - encrypt: Encrypts a given phrase to Morse code.
    - decrypt: Decrypts a message from Morse code to English.
"""

dictionary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def encrypt(phrase):
    """
    Encrypts a given phrase to Morse code.

    Args:
        phrase (str): The phrase to be encrypted.

    Returns:
        str: The encrypted Morse code string.
    """
    # Split the input phrase into words, convert each character to Morse code, and join with space.
    return '/'.join(' '.join(dictionary.get(char.upper(), '') for char in word) 
                    for word in phrase.split() if all(char.upper() in dictionary for char in word))

def decrypt(morse_code):
    """
    Decrypts a message from Morse code to English.

    Args:
        morse_code (str): The Morse code message to decrypt.

    Returns:
        str: The decrypted message in English.
    """
    # Create a reverse dictionary mapping Morse code to characters
    reverse_morse_dict = {v: k for k, v in dictionary.items()}
    # Split the Morse code into words, then into characters, and map back to English characters.
    morse_words = morse_code.split('/')
    decrypted_message = ''
    for word in morse_words:
        morse_characters = word.strip().split()
        for char in morse_characters:
            if char in reverse_morse_dict:
                decrypted_message += reverse_morse_dict[char]
        decrypted_message += ' '
    return decrypted_message.strip()

if __name__ == "__main__":
    # Get input from the user
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()  # Convert input to uppercase
    if choice == 'E':
        input_phrase = input("Enter the English phrase to encrypt: ")
        # Encrypt the input phrase and print the Morse code
        encrypted_phrase = encrypt(input_phrase)
        print("Morse Code:", encrypted_phrase)
    elif choice == 'D':
        morse_code = input("Enter the Morse code to decrypt (use space between letters and '/' between words): ")
        # Decrypt the Morse code and print the English phrase
        decrypted_phrase = decrypt(morse_code)
        print("Decrypted Message:", decrypted_phrase)
    else:
        # Handle invalid input
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
