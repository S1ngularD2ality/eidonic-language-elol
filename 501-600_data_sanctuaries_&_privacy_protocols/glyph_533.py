# glyph_533 – IP_ENCRYPT
# Encrypt IP addresses for storage

from cryptography.fernet import Fernet

def glyph_533(ip_address, key=None):
    if not key:
        key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(ip_address.encode())
    return encrypted, key
