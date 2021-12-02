def cifrar(text, key):
    key = [(ord(i.lower()) - 97) % 26 for i in key]
    sequence = [
        (ord(text[i].lower()) - 97 + key[i % len(key)]) % 26 for i in range(len(text))
    ]
    cipher = "".join([chr(i + 97).upper() for i in sequence])
    return cipher


def descifrar(cipher, key):
    key = [(ord(i.lower()) - 97) % 26 for i in key]
    sequence = [
        (ord(cipher[i].lower()) - 97 - key[i % len(key)]) % 26
        for i in range(len(cipher))
    ]
    text = "".join([chr(i + 97).upper() for i in sequence])
    return text
