def caesar_cipher(text, shift, mode):
    result = ""
    
    # Ensure the shift is within the range of 0-25
    shift = shift % 26
    
    # Encrypt or Decrypt the message based on mode
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetic characters are added as is
            result += char

    return result

def main():
    print("Caesar Cipher Encryption/Decryption")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Do you want to encrypt or decrypt? ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose either 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"The resulting message is:{result}")

if __name__ == "__main__":
    main()
