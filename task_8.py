def XOR_cipher(content, cipher):
    data = ''
    for el in str(content):
        el_sh = ord(el) + ord(str(cipher))
        if el_sh > 1114111:
            el_sh -= 1114111
        data = data + str(chr(el_sh))
    return data


def XOR_uncipher(content, cipher):
    data = ''
    for el in str(content):
        el_sh = ord(el) - ord(str(cipher))
        if el_sh < 1:
            el_sh += 1114111
        data = data + chr(el_sh)
    return data


x = XOR_cipher('Hello World!', 5)
print(x)
y = XOR_uncipher(x, 5)
print(y)
