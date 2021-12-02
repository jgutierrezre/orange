def cifrar(text, a, b):
    a = int(a)
    b = int(b)

    sequence = [(a * (ord(i.lower()) - 97) + b) % 26 for i in text]
    cipher = "".join([chr(i + 97).upper() for i in sequence])
    return cipher


def descifrar(cipher, a, b):
    a = int(a)
    b = int(b)

    a = pow(a, -1, 26)
    sequence = [(a * (ord(i.lower()) - 97 - b)) % 26 for i in cipher]
    text = "".join([chr(i + 97).upper() for i in sequence])
    return text
