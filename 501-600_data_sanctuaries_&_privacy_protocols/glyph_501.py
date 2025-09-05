# glyph_501 – DATA_SEAL
# Encrypt data with a unique key using Fernet symmetric encryption

from cryptography.fernet import Fernet

def glyph_501(data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted, key
