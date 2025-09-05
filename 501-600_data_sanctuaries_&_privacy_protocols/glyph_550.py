# glyph_550 – SAFE_TRANSMIT
# Transmit encrypted data over a channel

from cryptography.fernet import Fernet

def glyph_550(data, key=None):
    if not key:
        key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()), key
