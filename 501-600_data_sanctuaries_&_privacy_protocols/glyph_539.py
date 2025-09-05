# glyph_539 – ENCRYPT_CONFIG
# Encrypt configuration files

from cryptography.fernet import Fernet

def glyph_539(config_data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(config_data.encode())
    return encrypted, key
