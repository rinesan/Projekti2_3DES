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


    key_hash = hashlib.md5(key.encode('ascii')).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)


    cipher = DES3.new(tdes_key, DES3.MODE_EAX)


    with open(input_file_path, 'rb') as input_file:
    nonce = input_file.read(DES3.block_size)
     encrypted_bytes = input_file.read()
     print(f"Encrypted file: {encrypted_bytes}")



    # Decrypt the file bytes
    cipher.nonce = nonce
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    print(f"Decrypted file: {decrypted_bytes}")

    # Write the decrypted bytes to the output file

    with open(output_file_path, 'wb') as output_file:
        output_file.write(decrypted_bytes)
    print(f"Decryption successful. Output file written to {output_file_path}")


input_file_path = 'input.txt'
encrypted_file_path = 'encrypted.txt'


