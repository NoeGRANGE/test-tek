def xor_message(message, key):
    byte_message = list(bytes.fromhex(message))
    byte_key = list(bytes.fromhex(key))
    xored_message = []
    length = len(byte_message)
    for i in range(length):
        xored_message.append(byte_message[i] ^ byte_key[i])
    print(bytes(xored_message).hex())
