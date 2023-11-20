#!/usr/bin/python3
from math import *
import sys
import xor
import aes

def main(argv):
    message = input()
    try:
        if (argv[0] == "-xor"):
            if (argv[2] == "-b"):
                key = argv[3]
                if (len(key) != len(message)):
                    sys.exit(84)
            else:
                key = argv[2]
            xor.xor_message(message, key)
        if (argv[0] == "-aes"):
            if (argv[2] == "-b"):
                key = argv[3]
                if (len(key) != 32 or len(message) != 32):
                    sys.exit(84)
            else:
                key = argv[2]
            if (argv[1] == "-c"):
                aes.aes_encrypt(message, key)
            elif (argv[1] == "-d"):
                aes.aes_decrypt(message, key)
            else:
                sys.exit(84)
    except:
        sys.exit(84)
    sys.exit(0)

if __name__ == "__main__":
    sys.argv.pop(0)
    main(sys.argv)
