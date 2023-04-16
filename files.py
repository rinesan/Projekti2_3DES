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

    encrypted_bytes = cipher.encrypt(file_bytes)
    print(f"Encrypted file: {encrypted_bytes}")

    with open(output_file_path, 'wb') as output_file:
        output_file.write(cipher.nonce)
        output_file.write(encrypted_bytes)

    print(f"Encryption successful. Output file written to {output_file_path}")
    def decrypt_file(input_file_path, output_file_path, key):

    # Compute the 3DES key from the user-supplied key
    key_hash = hashlib.md5(key.encode('ascii')).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)

    # Create a new 3DES cipher object in EAX mode
    cipher = DES3.new(tdes_key, DES3.MODE_EAX)

    # Read the input file into memory
    with open(input_file_path, 'rb') as input_file:
        # Read the nonce from the beginning of the file
        nonce = input_file.read(DES3.block_size)
        encrypted_bytes = input_file.read()
        print(f"Encrypted file: {encrypted_bytes}")



