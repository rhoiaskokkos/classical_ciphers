# Classical Ciphers
A Python CLI tool implementing three classical substitution ciphers: Caesar, ROT13, and Vigenère. It's built as part of a self-directed study into cryptography and offensive security. Includes encryption, decryption, and automated crackers ranging from brute force to statistical cryptanalysis.

## Features

### Encrypt & Decrypt
Encrypt or decrypt text using a chosen cipher. Caesar requires a shift value (1–25), Vigenère requires an alphabetic keyword, and ROT13 requires no key as it is its own inverse.

### Crack
Each cipher includes a cracker demonstrating its real-world weaknesses:
- **Caesar** — brute forces all 25 possible shifts
- **ROT13** — single possible key, decrypts immediately
- **Vigenère** — uses Index of Coincidence to identify the key length, then scores each candidate shift against English letter frequency distributions to recover the key automatically. Note: results may be unreliable for texts under 200 characters.

## Project Structure
```
classical_ciphers/
├── ciphers/
│   ├── __init__.py
│   ├── caesar.py
│   ├── rot13.py
│   └── vigenere.py
├── main.py
├── .gitignore
└── README.md
```

## Installation
1. Clone the repository
```bash
git clone https://github.com/rhoiaskokkos/classical_ciphers
cd classical_ciphers
```

2. Install dependencies
```bash
pip install pyfiglet
```

3. Run the CLI
```bash
python main.py
```

## What I learned
- How substitution ciphers work and why keyspace size matters for security
- Using `str.maketrans` and `str.translate` for efficient character mapping
- How the Index of Coincidence exploits statistical properties of natural language to determine Vigenère key length without knowing the key
- How frequency analysis reduces Vigenère to a series of independent Caesar ciphers once the key length is known
- How to score candidate decryptions against English letter frequency distributions to recover keys automatically
- How multiple-of-true-length harmonics can mislead IC-based key length detection, and how to correct for it
- The difference between implementing an algorithm and understanding its security implications