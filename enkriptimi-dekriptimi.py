from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64

def encrypt3DES(plaintext, key):
    # Shtimi i padding në tekstin e pastër nëse gjatësia nuk është e plotë me 8 bajtë
    plaintext = pad(plaintext)

    # Krijimi i një objekti 3DES cipher
    cipher = DES3.new(key, DES3.MODE_ECB)

    # Enkriptimi i tekstit të pastër
    ciphertext = cipher.encrypt(plaintext)

    # Kthimi i tekstit të enkriptuar në format base64
    return base64.b64encode(ciphertext).decode('utf-8')

def pad(text):
    # Shtimi i padding në tekstin e pastër
    while len(text) % 8 != 0:
        text += b'\x00'
    return text

# Gjenerimi i një kyçi të rastësishëm me gjatësi 24 bajtë (192 bitë)
key = get_random_bytes(24)

# Teksti i pastër që do të enkriptohet
plaintext = "Ky eshte nje tekst per enkriptim me 3DES"

# Enkriptimi i tekstit të pastër
ciphertext = encrypt3DES(plaintext.encode('utf-8'), key)

# Printimi i tekstit të enkriptuar
print("Teksti i enkriptuar:", ciphertext)


