def caesar_cipher(text, shift):
    """
    Encrypt or decrypt a given text using Caesar Cipher.

    :param text: The text to be encrypted or decrypted.
    :param shift: The number of positions each letter in the text will be shifted.
    :return: The encrypted or decrypted text.
    """
    result = []

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

# Example usage:
plaintext = "Hello, World!"
shift = 3
encrypted = caesar_cipher(plaintext, shift)
print("Encrypted:", encrypted)

decrypted = caesar_cipher(encrypted, -shift)
print("Decrypted:", decrypted)
