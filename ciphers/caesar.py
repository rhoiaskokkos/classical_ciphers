"""Caesar Cipher Implementation
This module provides functions to encrypt, decrypt, and crack text using the Caesar cipher."""

def caesar_cipher(text: str, shift: int, encrypt: bool = True) -> str: 
    """Encrypts or decrypts the given text using the Caesar cipher with the specified shift value.
    Args:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The number of positions to shift the letters in the alphabet.
        encrypt (bool): If True, the function will encrypt the text; if False, it will decrypt the text.
    Returns:
        str: The encrypted or decrypted text.
    """

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text: str, shift: int) -> str:
    return caesar_cipher(text, shift)
    
def decrypt(text: str, shift: int) -> str:
    return caesar_cipher(text, shift, encrypt=False)
    

def crack(text: str) -> None: 
   
    for shift in range(1, 26):
        decrypted_text = caesar_cipher(text, shift, encrypt=False)
        print(f'Shift: {shift} - Decrypted Text: {decrypted_text}')
    return
 
