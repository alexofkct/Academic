#Library section
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#Identification
UID=120395246
Last_Name="Bharathiraja"
First_Name="Rithik Sarvesh"

#World of funtions
def rsa_enc_public(text,keyPair):
    encryptor=PKCS1_OAEP.new(keyPair)
    cipher=encryptor.encrypt(text)
    print("Encrypted: ",cipher)
    return cipher

def rsa_dec_private(cipher,keyPair):
    decryptor=PKCS1_OAEP.new(keyPair)
    decrypted=decryptor.decrypt(cipher)
    print("Decrypted: ",decrypted)
    return decrypted


def main():
    keyPair = RSA.generate(2048)
    text=b'ENPM693 is the best course'
    cipher=rsa_enc_public(text,keyPair)
    rsa_dec_private(cipher,keyPair)
    
if __name__ == "__main__":
    main()
