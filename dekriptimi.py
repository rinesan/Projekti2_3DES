from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad 
import base64

def triple_des_dekripto(key,iv ,ciphertext):
#Konvertojme qelesin,IV-ne dhe tekstin e shifruar nga base64 ne bajta

key= base64.b64decode(key)
iv= base64.b64decode(iv)
ciphertext=base64.b64decode(ciphertext)

#Krijimi i objektit te shifres Triple DES ne menyren CBC dhe mbushjen P
chiper=DES3.new(key,DES3.MODE_CBC,iv)

#Kryejme dekriptimin dhe largojme mbushjen 
plaintext= unpad(cipher.decrypt(ciphertext),DES3.block_size)


#Konvertojme tekstin e dekriptuar nga bajtat ne string 
plaintext=plaintext.decode('utf-8')
return plaintext

#Perdorimi i shembullit 
key = "iFgnsjDEMyDDfD36M7JoA5vX"
iv  ="F5+5qqc0xUI="
ciphertext = "axr8hnZgLdPgbiFnmjKXuA=="

plaintext=triple_des_dekripto(key,iv,ciphertext)
 print ("Teksti i dekriptuar:" plaintext
