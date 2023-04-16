from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64

# Funksioni për të kriptuar një tekst me 3DES
def encrypt_text_3des(text, key):
    # Gjenerimi i një vektori të rastësishëm
    iv = get_random_bytes(DES3.block_size)

    # Krijimi i objektit të kriptimit me 3DES
    cipher = DES3.new(key, DES3.MODE_CFB, iv)

    # Kriptimi i tekstit
    ciphertext = cipher.encrypt(text.encode())

    # Kombinimi i vektorit të rastësishëm dhe tekstit të kriptuar në një tekst të koduar me base64
    encrypted_text = base64.b64encode(iv + ciphertext).decode()

    return encrypted_text

# Teksti për të kriptuar
text = "Ky është një tekst për të kriptuar me 3DES"

# Ky është kyçi i kriptimit, duhet të jetë i gjatë 16, 24 ose 32 bajtë
key = b'kyqi_sekrete_123'

# Kriptimi i tekstit
encrypted_text = encrypt_text_3des(text, key)

# Printimi i tekstit të kriptuar
print("Teksti i kriptuar: ", encrypted_text)