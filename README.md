## Caesar-Cipher-for-Beginner
A simple Python project demonstrating basic Caesar Cipher encryption and decryption
This repository contains a Python program that encrypts and decrypts messages using the Caesar Cipher. The cipher works by shifting each letter in the text forward or backward by a set number of positions in the alphabet.

## Prerequisites
You don’t need to install anything else to use this project; just make sure Python is installed on your computer, and you’re ready to go.

## Caeser Cipher Overview
The Caesar Cipher is one of the oldest and simplest encryption methods. It works by shifting each letter in the text by a fixed number of positions in the alphabet.

Encryption: Each letter in the plaintext is replaced with the letter that comes a set number of positions later in the alphabet (the “shift”).

Decryption: To decrypt, the letters are shifted in the opposite direction by the same number of positions.

## Code Walkthrough
The encryption function shifts each letter of the plaintext by a specified number of positions (shift value) in the alphabet:
### Caesar Encryption
The encryption function shifts each letter of the plaintext by a specified number of positions (shift value) in the alphabet:
```python
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

```
The program first checks if each character is a letter.
If it is a letter, it converts it to a number using ord(), adds the shift, and converts it back to a letter using chr().
Non-letter characters, like spaces, punctuation, or numbers, stay the same

### Caeser Decryption
Decryption is simply the reverse of encryption. The same function `caesar_encrypt` is used with the negative shift value:
```python
def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

```

### Example Useage
Here’s an example of how to use the Caesar Cipher functions to encrypt and decrypt a message:

```python
text = "My name is Hpone"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
decrypted = caesar_decrypt(ciphertext, shift)

print("Caesar Cipher - Encrypted:", ciphertext)
print("Caesar Cipher - Decrypted:", decrypted)
```

In this example, the text message `"My name is Hpone"` is encrypted with a shift of 3, resulting in the ciphertext. The ciphertext is then decrypted back to the original message using the same shift value.

### Example Output
```text
Caesar Cipher - Encrypted: Pb qdph lv Ksrqh
Caesar Cipher - Decrypted: My name is Hpone
```

The text `"My name is Hpone"` is shifted by 3 positions to become `"Pb qdph lv Ksrqh"`.
- Decrypting `" Pb qdph lv Ksrqh"` with the same shift (3) gives us the original message `"My name is Hpone"`.

## Conclusion

This project provides a straightforward Python implementation of the Caesar Cipher. While it is not secure by modern cryptographic standards, it serves as a great introductory example for learning the basics of encryption and decryption.


## NOTE
You can try different shift values to see how the encryption and decryption results change.

The Caesar Cipher is not secure by today’s standards, as it can be easily broken using brute-force (there are only 26 possible shifts).

Despite this, it remains a useful tool for learning the fundamentals of encryption and decryption.
