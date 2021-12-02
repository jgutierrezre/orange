def cifrar(text, key):
    text = text.upper()
    key = key.upper()

    dict_key = dict(zip(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), list(key)))
    cipher = "".join([dict_key[i] for i in text])

    return cipher


def descifrar(cipher, key):
    cipher = cipher.upper()
    key = key.upper()
    dict_key = dict(zip(list(key), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))
    text = "".join([dict_key[i] for i in cipher])

    return text
