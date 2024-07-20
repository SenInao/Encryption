from Encryption.Decryption import Decryption
from Encryption.Encryption import Encryption

def main():
    encryption = Encryption()
    decryption = Decryption(encryption.key)
    dir = encryption.encryptDir("test")
    decryption.decryptDir(dir)

if __name__ == "__main__":
    main()
