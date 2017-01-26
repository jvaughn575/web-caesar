import string

def alphabet_position(letter):
    alphabet = string.ascii_lowercase
    return alphabet.find(letter.lower())

def rotate_character(char, rot):

    letters = string.ascii_letters
    if str(char) not in letters:
        return char

    charPosition = alphabet_position(char)
    alphabet = string.ascii_lowercase

    if charPosition <= 12:
        if char.isupper():
            return  alphabet[alphabet_position(char) + rot].upper()
        return alphabet[(alphabet_position(char) + rot)%26]
    elif charPosition > 12:
        if char.isupper():
            return alphabet[(charPosition + rot)%26].upper()
        return alphabet[(charPosition + rot)%26]


def encrypt(text, rot):
    encryptedString = ""
    for char in text:
        encryptedString += rotate_character(char,rot)
    return encryptedString
