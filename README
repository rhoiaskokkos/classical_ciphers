# Classical Ciphers
A Python CLI implementation of three classical substitution ciphers: Caesar, ROT13, and Vigenère. Includes encryption, decryption, and crackers ranging from brute force to real cryptanalytic techniques.

## Features

### Encrypt
Encrypt plaintext using a chosen cipher. Caesar and Vigenère require a key (shift value or keyword), while ROT13 uses a fixed shift of 13.

### Decrypt
Decrypt ciphertext using the correct key. ROT13 is self-inverse, meaning the same operation encrypts and decrypts.

### Crack
Each cipher includes a cracker demonstrating its real-world weaknesses:
- **Caesar** — brute forces all 25 possible shifts and prints the results
- **ROT13** — single possible key, decrypts immediately
- **Vigenère** — uses Index of Coincidence to determine the key length, then frequency analysis to recover each key letter, with candidate suggestions per position for manual refinement

## How to use
Run the CLI and navigate the menu to select a cipher and operation. All input is handled interactively.
```bash
python main.py
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
- The difference between implementing an algorithm and understanding its security implications
- How the Index of Coincidence exploits statistical properties of natural language to break polyalphabetic ciphers without knowing the key
- How frequency analysis reduces Vigenère to a series of Caesar ciphers once the key length is known