# glyph_591 – SECURE_CACHE
# Encrypt data before adding to cache

from cryptography.fernet import Fernet

def glyph_591(data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()), key
