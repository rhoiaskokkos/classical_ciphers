"""Classical Ciphers CLI Menu"""
import pyfiglet
from ciphers import caesar, vigenere, rot13

def choice_tree(cipher):
    while True:
        print("-" * 50)
        print(f"\n{cipher.__name__.split('.')[-1].upper()}")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Crack")
        print("4. Return to Main Menu")
        select_function = input("Select an option: ")
        print("-" * 50)
        if select_function not in ["1", "2", "3", "4"]:
            print("Invalid option. Please select a valid function.")
            continue
        
        if select_function == "4":
            return

        text = input("Enter the text: ")

        if select_function == "3":
            print()
            result = cipher.crack(text)
            print(result)
        elif cipher == rot13:
            print()
            print(cipher.encrypt(text) if select_function == "1" else cipher.decrypt(text))
        elif cipher == caesar:
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    print("Shift must be between 1 and 25.")
                except ValueError:
                    print("Shift must be an integer.")
            print()
            print(cipher.encrypt(text, shift) if select_function == "1" else cipher.decrypt(text, shift))
        elif cipher == vigenere:
            while True:
                key = input("Enter the key: ")
                if key.isalpha():
                    break
                print("Key must consist of alphabetic characters only.")
            print()
            print(cipher.encrypt(text, key) if select_function == "1" else cipher.decrypt(text, key))

        print("\nDone! What would you like to do next?")

def main_menu():
    banner = pyfiglet.figlet_format("Classical Ciphers", font = "larry3d")
    print(banner)
    print("=" * 50)
    print("Welcome to the Classical Ciphers!")
    while True:
        print("\nMAIN MENU")
        print("1. Caesar Cipher")
        print("2. ROT13")
        print("3. Vigenère Cipher")
        print("4. Exit")

        select_cipher = input("Select a cipher: ")
        if select_cipher not in ["1", "2", "3", "4"]:
            print("Invalid option. Please select a valid cipher.")
            continue
        if select_cipher == "1":
            choice_tree(caesar)
        elif select_cipher == "2":
            choice_tree(rot13)
        elif select_cipher == "3":
            choice_tree(vigenere)
        elif select_cipher == "4":
            break


if __name__ == "__main__":
    main_menu()

