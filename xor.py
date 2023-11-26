def xor_message(message, key):
    byte_message = list(bytes.fromhex(message))
    byte_key = list(bytes.fromhex(key))
    xored_message = []
    key_length = len(byte_key)
    length = min(len(byte_message), key_length)
    for i in range(length):
        xored_message.append(byte_message[i] ^ byte_key[i % key_length])
    print(bytes(xored_message).hex())
