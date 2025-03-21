import binascii

Sbox = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

def split_list(lst):
    return [lst[i:i + 4] for i in range(0, len(lst), 4)]


rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
def g_function(word, round):
    shift_word = word[1:] + [word[0]]
    s_box_word = []
    for elmt in shift_word:
        s_box_word.append(Sbox[elmt])
    s_box_word[0] = s_box_word[0] ^ rcon[round]
    return s_box_word

def next_key(keys, round):
    xor_with = g_function(keys[-1], round)
    for i in range(4):
        keys.append([keys[-4][j] ^ xor_with[j] for j in range(4)])
        xor_with = keys[-1]
    return keys

def key_expansion(list):
    for i in range(10):
        next_key(list, i)
    keys = split_list(list)
    return keys


def multiply_by_2(v):
    s = v << 1
    s &= 0xff
    if (v & 128) != 0:
        s = s ^ 0x1b
    return s


def multiply_by_3(v):
    return multiply_by_2(v) ^ v

def mix_column(column):
    r = [
        multiply_by_2(column[0]) ^ multiply_by_3(
            column[1]) ^ column[2] ^ column[3],
        multiply_by_2(column[1]) ^ multiply_by_3(
            column[2]) ^ column[3] ^ column[0],
        multiply_by_2(column[2]) ^ multiply_by_3(
            column[3]) ^ column[0] ^ column[1],
        multiply_by_2(column[3]) ^ multiply_by_3(
            column[0]) ^ column[1] ^ column[2],
    ]
    return r

def mix_columns(grid):
    new_grid = [[], [], [], []]
    for i in range(4):
        col = [grid[i][j] for j in range(4)]
        col = mix_column(col)
        for i in range(4):
            new_grid[i].append(col[i])
    _new_grid = []
    for i in  range(4):
        _new_grid.append([new_grid[j][i] for j in range(4)])
    return _new_grid

def aes_encrypt_round(message, key, round):
    words = []
    for i in range(4):
        word = message[i]
        for k in range(4):
            word[k] = Sbox[word[k]]
        for k in range(i):
            word = word[1:] + [word[0]]
        words.append(word)
    first_step = []
    for i in range(4):
        for j in range(4):
            first_step.append(words[(j + i)% 4][-i])
    if (round == 10):
        mixed = split_list(first_step)
    else:
        mixed = mix_columns(split_list(first_step))
    words = []
    for i in range(4):       
        word = [mixed[i][j] ^ key[i][j] for j in range(4)]
        words.append(word)
    return words

def aes_encrypt(message, key):
    byte_message = list(bytes.fromhex(message))
    if (len(byte_message) != 16):
        byte_message = [0] * (16 - len(byte_message)) + byte_message
    byte_key = list(bytes.fromhex(key))
    splited_byte_key = split_list(byte_key)
    keys = key_expansion(splited_byte_key)
    split_message = split_list(byte_message)
    xored_message = []
    for i in range(4):
        xored_message.append([split_message[i][j] ^ keys[0][i][j] for j in range(4)])

    round_res = xored_message
    for round in range(10):
        round_res = aes_encrypt_round(round_res, keys[round + 1], round + 1)
    flat_list = []
    for sublist in round_res:
        for item in sublist:
            flat_list.append(item)
    byte_array_le = bytes(flat_list)
    print(byte_array_le.hex())


def aes_decrypt_round(message, key, round):
    for i in range(4):       
        message[i] = [message[i][j] ^ key[i][j] for j in range(4)]
    if (round != 10):
        message = mix_columns(message)
        message = mix_columns(message)
        message = mix_columns(message)
    for i in range(4):
        message[i] = [InvSbox[message[i][j]] for j in range(4)]
    shifted_message = []
    for i in range(4):
        for j in range(4):
            shifted_message.append(message[(i + 4 - j) % 4][j])
    return split_list(shifted_message)

def aes_decrypt(message, key):
    byte_message = list(bytes.fromhex(message))
    if (len(byte_message) != 16):
        byte_message = [0] * (16 - len(byte_message)) + byte_message
    byte_key = list(bytes.fromhex(key))
    splited_byte_key = split_list(byte_key)
    keys = key_expansion(splited_byte_key)
    round_res = split_list(byte_message)
    for round in range(10, 0, -1):
        round_res = aes_decrypt_round(round_res, keys[round], round)
    xored_message = []
    for i in range(4):
        xored_message.append([round_res[i][j] ^ keys[0][i][j] for j in range(4)])
    flat_list = []
    for sublist in xored_message:
        for item in sublist:
            flat_list.append(item)
    byte_array_le = bytes(flat_list)
    print(byte_array_le.hex().lstrip('0'))
