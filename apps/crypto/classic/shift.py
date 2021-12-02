def cifrar(text, key):
    key = int(key)

    sequence = [(ord(i.lower()) - 97 + key) % 26 for i in text]
    cipher = "".join([chr(i + 97).upper() for i in sequence])
    return cipher


def descifrar(cipher, key):
    key = int(key)

    sequence = [(ord(i.lower()) - 97 - key) % 26 for i in cipher]
    text = "".join([chr(i + 97).upper() for i in sequence])
    return text
