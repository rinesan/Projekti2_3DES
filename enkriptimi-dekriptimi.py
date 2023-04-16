from Crypto.Cipher import DES3
import binascii

# Funksioni për të enkriptuar tekstin me 3DES
def encrypt3DES(plaintext, key):
    # Konvertojmë çelësin në formën e duhur
    keyHex = key.encode('utf-8').ljust(24, b'\0')
    key1 = keyHex[:8]
    key2 = keyHex[8:16]
    key3 = keyHex[16:]

    # Përgatitim i ndihmës për padding të tekstit
    plaintextPadded = plaintext.encode('utf-8')
    paddingSize = 8 - (len(plaintextPadded) % 8)
    plaintextPadded += bytes([paddingSize] * paddingSize)

    # Enkriptimi i tekstit
    ciphertext = b''
    cipher = DES3.new(key1, DES3.MODE_ECB)
    for i in range(0, len(plaintextPadded), 8):
        block = plaintextPadded[i:i+8]
        ciphertext += cipher.encrypt(block)

    return binascii.hexlify(ciphertext).decode('utf-8')

plaintext = "Teksti që duam të enkriptojmë"
key = "Celesi per 3DES".ljust(24)
ciphertext = encrypt3DES(plaintext, key)
print("Teksti i enkriptuar:", ciphertext)

