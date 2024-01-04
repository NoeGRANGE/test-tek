def xor_message(message, key):
    byte_message = list(bytes.fromhex(message))
    byte_key = list(bytes.fromhex(key))
    xored_message = []
    key_length = len(byte_key)
    mess_length = len(byte_message)
    for i in range(mess_length):
        xored_message.append(byte_message[i] ^ byte_key[i % key_length])
    print(bytes(xored_message).hex())
