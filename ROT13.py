"""ROT13 Cipher Implementation
This module provides functions to encrypt, decrypt, and crack text using the ROT13 cipher."""

def rot13(text: str) -> str: 
    """Encrypts or decrypts the given text using the ROT13 cipher.
    Args:
        text (str): The input text to be encrypted or decrypted.
    Returns:
        str: The encrypted or decrypted text.
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[13:] + alphabet[:13]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)


def encrypt() -> str:
    """Encrypts the user-provided text using the ROT13 cipher.
    Returns:        
        str: The encrypted text."""
    text = input("Enter the text to encrypt: ")
    print("\nEncrypting... ", rot13(text))
    
def decrypt() -> str:
    """Decrypts the user-provided text using the ROT13 cipher.
     
    Returns:        
        str: The decrypted text."""
    text = input("Enter the text to decrypt: ")
    print("\nDecrypting... ", rot13(text))

def crack() -> None: 
    """Attempts to decrypt the given text by trying all possible shift values and printing the results.
    Returns:
        None: This function does not return a value; it prints the decrypted text for each shift value."""
    text = input("Enter the text to crack: ")
    decrypted_text = rot13(text)
    print(f'\nROT13 has only one possible key. Decrypting... {decrypted_text}')

 
