#!/usr/bin/python3
from math import *
import sys
import xor
# import os

def main(argv):
    print(xor.xor_message("68656c6c6f20776f726c64", "7665727920736563726574"))
    sys.exit(0)

if __name__ == "__main__":
    sys.argv.pop(0)
    main(sys.argv)
