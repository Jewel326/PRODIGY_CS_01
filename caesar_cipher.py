def encrypt(text, shift):
    result = ""

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Leave non-alphabetic characters unchanged
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").upper()
    text = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))

    if choice == 'E':
        print("Encrypted message:", encrypt(text, shift))
    elif choice == 'D':
        print("Decrypted message:", decrypt(text, shift))
    else:
        print("Invalid choice! Please choose 'E' for encrypt or 'D' for decrypt.")

if __name__ == "__main__":
    main()
