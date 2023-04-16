import os
import hashlib
from Crypto.Cipher import DES3

def encrypt_file(input_file_path, output_file_path, key):
    key_hash = hashlib.md5(key.encode('ascii')).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)

    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

     with open(input_file_path, 'rb') as input_file:
         file_bytes = input_file.read()
         print(f"input file: {file_bytes}")




