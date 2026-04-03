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

def encrypt(text: str) -> str:
    return rot13(text)
    
def decrypt(text: str) -> str:
    return rot13(text)

def crack(text: str) -> str: 
    decrypted_text = rot13(text)
    return f'\nROT13 has only one possible key (13): {decrypted_text}'

 
