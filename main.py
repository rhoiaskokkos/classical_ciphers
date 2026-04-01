"""Classical Ciphers CLI Menu"""
import pyfiglet
import caesar_cipher
import ROT13
import vigenere_cipher

def choice_tree(cipher):
        while True:
            print("-" * 50)
            print(f"\n{cipher.__name__.upper().replace('_', ' ')}")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Crack")
            print("4. Return to Main Menu")
            select_function = input("Select an option: ")
            print("-" * 50)
            if select_function not in ["1", "2", "3", "4"]:
                print("Invalid option. Please select a valid function.")
                continue
            if select_function == "1":
                cipher.encrypt()
                print("\nDone! What would you like to do next?")
            elif select_function == "2":
                cipher.decrypt()
                print("\nDone! What would you like to do next?")
            elif select_function == "3":
                cipher.crack()
                print("\nDone! What would you like to do next?")
            elif select_function == "4":
                return

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
            choice_tree(caesar_cipher)
        elif select_cipher == "2":
            choice_tree(ROT13)
        elif select_cipher == "3":
            choice_tree(vigenere_cipher)
        elif select_cipher == "4":
            break


if __name__ == "__main__":
    main_menu()

