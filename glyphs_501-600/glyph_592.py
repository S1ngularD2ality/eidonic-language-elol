# glyph_592 – DECRYPT_CACHE
# Decrypt data from glyph_591

from cryptography.fernet import Fernet

def glyph_592(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()
