def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

text = "Happy New Year"
shift = 3
ciphertext = caesar_encrypt(text, shift)
print("Caesar Cipher - Encrypted:", ciphertext)


def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)
decrypted = caesar_decrypt(ciphertext, shift)
print("Caesar Cipher - Decrypted:", decrypted)  
