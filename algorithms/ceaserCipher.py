def caesar(text, shift):
    """
    Encrypts or decrypts text using the Caesar Cipher.
    Use a positive shift for encryption.
    Use a negative shift for decryption.
    """
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result