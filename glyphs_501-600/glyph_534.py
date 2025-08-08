# glyph_534 – IP_DECRYPT
# Decrypt IP addresses encrypted by glyph_533

from cryptography.fernet import Fernet

def glyph_534(encrypted_ip, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_ip).decode()
