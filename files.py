from Crypto.Cipher import DES3
from hashlib import md5

while True:
    print('Choose one of the following operations: \n\t1- encrypt\n\t2- decrypt')
    operation = input("Your choice: ")
    if operation not in['1','2']:
        break
        file_path=input('filepath:')
        key = input('tdes key:')
