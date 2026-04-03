"""Vignère Cipher Implementation
This module provides functions to encrypt, decrypt, and crack text using the Vigenère cipher."""
import string
from collections import Counter

ALPHABET = string.ascii_lowercase
ENGLISH_FREQ = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
    'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
    'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
    'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
    'z': 0.00074
}

def calculate_index_of_coincidence(text: str) -> float:
    """A helper function that calculates the Index of Coincidence for the given text.
    Args:
        text (str): The input text for which to calculate the Index of Coincidence.
    Returns:
        float: The calculated Index of Coincidence."""
    text = ''.join(filter(str.isalpha, text)).lower()
    freqs = Counter(text)
    n = len(text)
    if n < 2:
        return 0.0
    index_of_coincidence = sum(f * (f - 1) for f in freqs.values()) / (n * (n - 1))
    return index_of_coincidence

def score_text(text: str) -> float:
    """A helper function that scores the given text based on how closely its letter frequency matches that of typical English text.
    Args:
        text (str): The input text to be scored.
    Returns:
        float: The calculated score, with higher values indicating a closer match to English letter frequencies."""
    text = ''.join(filter(str.isalpha, text)).lower()
    freqs = Counter(text)
    n = len(text)
    if n == 0:
        return 0.0
    score = sum(abs(freqs.get(char, 0) / n - ENGLISH_FREQ[char]) for char in ALPHABET)
    return score


def guess_key_lengths(ciphertext: str, max_key_length: int = 20) -> list[int]:
    """A helper function that attempts to determine the most likely key length for the given ciphertext using the Index of Coincidence.
    Args:
        ciphertext (str): The input text for which to determine the key length.
        max_key_length (int): The maximum key length to consider when analyzing the ciphertext.
    Returns:
        list[int]: A list of candidate key lengths based on the analysis."""
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).lower()
    candidates = []

    for key_length in range(1, max_key_length + 1):
        ic_values = [calculate_index_of_coincidence(ciphertext[i::key_length]) for i in range(key_length)]
        avg_ic = sum(ic_values) / len(ic_values)
        if 0.06 <= avg_ic <= 0.07: # if the average IC is close to that of English text, it may be a candidate for the key length
            candidates.append((key_length))
    
    if not candidates: # fallback if nothing in range
        candidates = [max_key_length // 2]
    return candidates

def guess_key(ciphertext: str, key_length: int) -> str:
    """A helper function that attempts to determine the most likely key for the given ciphertext and key length using frequency analysis.
    Args:
        ciphertext (str): The input text for which to determine the key.
        key_length (int): The length of the key to be determined.
    Returns:
        str: The most likely key based on the analysis."""
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).lower()
    key = ""

    for i in range(key_length):
        subtext = ciphertext[i::key_length]
        best_shift = 0
        best_score = float('inf')
        for shift in range(len(ALPHABET)):
            candidate = ''.join(ALPHABET[(ALPHABET.index(char) - shift) % len(ALPHABET)] for char in subtext)
            score = score_text(candidate)
            if score < best_score:
                best_score = score
                best_shift = shift
        key += ALPHABET[best_shift]
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

def encrypt(text: str, key: str) -> str:
    """Encrypts text using the Vigenère chipher with a user-specified key.
    Returns:        
        str: The encrypted text."""
    return vigenere_cipher(text, key)

def decrypt(text: str, key: str) -> str:
    """Decrypts text using the Vigenère chipher with a user-specified key.
    Returns:        
        str: The decrypted text."""
    return vigenere_cipher(text, key, encrypt=False)
    
def crack(ciphertext: str, max_key_length: int=12) -> tuple[str, str]:
    """Attempts to crack the given ciphertext by analyzing letter frequencies and guessing the most likely key and decrypted text.
    Args:        
        ciphertext (str): The input text to be cracked.
    Returns:         
        str, str: A tuple containing the most likely key and the decrypted text based on the analysis."""
    if len(''.join(filter(str.isalpha, ciphertext))) < 200:
        print("WARNING:Results may be unreliable if the text is under 200 characters long.\n")
    key_lengths = guess_key_lengths(ciphertext, max_key_length)
    best_score = float('inf')
    best_key = ""
    best_plaintext = ""
    for key_length in key_lengths:
        key = guess_key(ciphertext, key_length)
        plaintext = vigenere_cipher(ciphertext, key, encrypt=False)
        score = score_text(plaintext)
        if score < best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext
    return best_key, best_plaintext 