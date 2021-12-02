def cifrar(text, key):
    m = len(key.split(","))
    dict_key = dict(zip(range(m), map(int, key.split(","))))

    try:
        cipher = "".join(
            [text[i // m * m + dict_key[i % m]] for i in range(len(text))]
        ).upper()
    except:
        return "KEYERROR"

    return cipher


def descifrar(cipher, key):
    m = len(key.split(","))
    dict_key = dict(zip(map(int, key.split(",")), range(m)))

    try:
        text = "".join(
            [cipher[i // m * m + dict_key[i % m]] for i in range(len(cipher))]
        ).upper()
    except:
        return "KEYERROR"

    return text
