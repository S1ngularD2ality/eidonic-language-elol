# glyph_502 – DATA_UNSEAL
# Decrypt data previously sealed by glyph_501

from cryptography.fernet import Fernet

def glyph_502(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()
