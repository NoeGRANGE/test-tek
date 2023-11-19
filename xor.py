def xor_message(message, key):
    xoredMessage = ""
    length = len(key)
    for i in range(length):
        print("char:", message[i], int(message[i], 16), "key:", key[i])
        xoredMessage += format(int(message[i], 16) ^ int(key[i % len(key)], 16), 'x')
    return xoredMessage
