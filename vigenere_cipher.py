"""Vignère Cipher Implementation
This module provides functions to encrypt, decrypt, and crack text using the Vigenère cipher."""

def calculate_index_of_coincidence(text_to_analyze: str) -> float:
    """A helper function that calculates the Index of Coincidence for the given text.
    Args:
        text_to_analyze (str): The input text for which to calculate the Index of Coincidence.
    Returns:
        float: The calculated Index of Coincidence."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text_to_analyze = text_to_analyze.lower()

    f_i = [text_to_analyze.count(char) for char in alphabet]
    n = len(text_to_analyze)
    if n == 0:
        return 0.0
    index_of_coincidence = sum(f_i * (f_i - 1) for f_i in f_i) / (n * (n - 1))
    return index_of_coincidence

def find_key_length(ciphertext: str, max_key_length: int = 20) -> int:
    """A helper function that attempts to determine the most likely key length for the given ciphertext using the Index of Coincidence.
    Args:
        ciphertext (str): The input text for which to determine the key length.
        max_key_length (int): The maximum key length to consider when analyzing the ciphertext.
    Returns:
        int: The most likely key length based on the analysis."""
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).lower()
    average_ic_values = []

    for key_length in range(1, max_key_length + 1):
        ic_values = []
        for i in range(key_length):
            subtext = ciphertext[i::key_length]
            ic = calculate_index_of_coincidence(subtext)
            ic_values.append(ic)
        
        average_ic_values.append((key_length, sum(ic_values) / len(ic_values)))

    best_length = min(average_ic_values, key = lambda x: abs(x[1] - 0.065))[0] # the key length with the average IC closest to that of English text (0.065)
    for shorter_length, avg_ic in average_ic_values:
        if best_length % shorter_length == 0 and abs(avg_ic - 0.065) <= 0.005: # if a shorter key length is a factor of the best length and has an average IC close to that of English text, it may be the correct key length
            if shorter_length < best_length:
                best_length = shorter_length
    return best_length

def find_key(ciphertext: str, key_length: int) -> str:
    """A helper function that attempts to determine the most likely key for the given ciphertext and key length using frequency analysis.
    Args:
        ciphertext (str): The input text for which to determine the key.
        key_length (int): The length of the key to be determined.
    Returns:
        str: The most likely key based on the analysis."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).lower()
    key = dict()

    for i in range(key_length):
        subtext = ciphertext[i::key_length]
        frequency = {char: subtext.count(char) for char in alphabet}
        most_frequent_chars = sorted(frequency, key=frequency.get, reverse=True)
        shifts = [(alphabet.index(char) - alphabet.index('e')) % len(alphabet) for char in most_frequent_chars[:3]]
        key[i] = [alphabet[shifts[i]] for i in range(len(shifts))]

    return key

def vigenere_cipher(text: str, key: str, encrypt: bool = True) -> str:
    """Encrypts or decrypts the given text using the Vigenère cipher with the specified key.
    Args:
        text (str): The input text to be encrypted or decrypted.
        key (str): The keyword used for encryption or decryption. It should consist of alphabetic characters only.
        encrypt (bool): If True, the function will encrypt the text; if False, it will decrypt the text.
    Returns:
        str: The encrypted or decrypted text.
    Raises:
        ValueError: If the key contains non-alphabetic characters."""
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    key = key.lower()
    processed_text = []
    key_index = 0

    if not key.isalpha():
         raise ValueError("Key must consist of alphabetic characters only.")

    for char in text:
        if char not in alphabet:
            processed_text.append(char)
            continue
        shift = alphabet.index(key[key_index % len(key)])
        if not encrypt:
            shift = -shift
        char_index = (alphabet.index(char) + shift) % len(alphabet)
        processed_text.append(alphabet[char_index])
        key_index += 1
        
    return ''.join(processed_text)

def encrypt() -> str:
    """Encrypts the user-provided text using the Vigenère cipher with a user-specified key.
    Returns:        
        str: The encrypted text."""
        
    text = input("Enter the text to encrypt: ")
    while True:
        key = input("Enter the key: ") 
        if not key.isalpha():
            print("Key must consist of alphabetic characters only.")
            continue
        break
           
    print("\nEncrypting... ", vigenere_cipher(text, key))

def decrypt() -> str:
    """Decrypts the user-provided text using the Vigenère cipher with the user-specified key.
    Returns:
        str: The decrypted text."""
        
    text = input("Enter the text to decrypt: ")
    while True:
        key = input("Enter the key: ")
        if not key.isalpha():
            print("Key must consist of alphabetic characters only.")
            continue
        break

    print("\nDecrypting... ", vigenere_cipher(text, key, encrypt=False))
    
def crack():
    """Attempts to decrypt the given text by trying to determine the most likely key length and key using frequency analysis, and then decrypting the text with the determined key.
    Returns:
        None: This function does not return a value; it prints the decrypted text based on the analysis."""
    ciphertext = input("Enter the text to crack: ")
    key_length = find_key_length(ciphertext)
    key = find_key(ciphertext, key_length)
    best_key = ''.join([str(key[i][0]) for i in range(key_length)])
    best_decrypted_text = vigenere_cipher(ciphertext, best_key, encrypt=False)
    print(f'\nMost likely key length: {key_length}')
    print(f'Most likely key: {best_key}')
    print(f'Decrypted text: {best_decrypted_text}')
    find_new_key = input("Would you like to try to find a different key? (y/n): ")
    if find_new_key.lower() == 'y':
        for position, candidate in key.items():
            print(f'Position {position}: {', '.join(candidate)}\n')
        while True: 
            key = input("Enter a key to try: ") 
            if not key.isalpha():
                print("Key must consist of alphabetic characters only.")
                continue
            break
        decrypted_text = vigenere_cipher(ciphertext, key, encrypt=False)
        print(f'\nDecrypted text with key... "{key}": {decrypted_text}')
