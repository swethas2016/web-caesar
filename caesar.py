import string

def alphabet_position(letter):
    alphabet = string.ascii_lowercase
    value = alphabet.index(letter.lower())
    return value

def rotate_character(char, rot):
    if char.isalpha() == True:
        rotvalue = (alphabet_position(char) + rot)%26
        if char.islower() == True:
            return string.ascii_lowercase[rotvalue]
        elif char.isupper() == True:
            return string.ascii_uppercase[rotvalue]
    else:
        return char

def encrypt(text, rot):
    result = ""
    counter = 0
    for item in text:
        result = result + rotate_character(item, rot)
        counter = counter + 1
    return result
