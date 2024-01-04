p = "e3"
q = "d3"

def reverse_by_2(x):
    if len(x) % 2 != 0:
        x = "0" + x
    reversed = ''
    for i in range(0, len(x), 2):
        reversed = x[i:i+2] + reversed
    return reversed

def reverse_into_dec(x):
    return int(reverse_by_2(x), 16)

def bin_to_dec(x):
    return int(x, 2)

def gcd(e, phi):
    while phi:
        e, phi = phi, e % phi
    return e

def mod_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = y2 - temp1 * y1
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    if temp_phi == 1:
        d = y2 + phi
    return d

def create_key(p, q):
    p = int(p, 16)
    q = int(q, 16)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while (e < phi):
        if (gcd(e, phi) == 1):
            break
        else:
            e += 1
    d = mod_inverse(e, phi)
    print(f"public key: {e:x}-{n:x}")
    print(f"private key: {d:x}-{n:x}")

def crypt_rsa(message, key):
    _e, _n = key.split("-")
    e = reverse_into_dec(_e)
    n = reverse_into_dec(_n)
    int_message = int(message, 16)
    pow_message = pow(int_message, e, n)
    crypted = reverse_by_2(format(pow_message, "x"))
    print(crypted)

def decrypt_rsa(message, key):
    _d, _n = key.split("-")
    d = reverse_into_dec(_d)
    n = reverse_into_dec(_n)
    int_message = reverse_into_dec(message)
    pow_message = pow(int_message, d, n)
    decrypted = reverse_by_2(format(pow_message, "x"))
    print(decrypted)
