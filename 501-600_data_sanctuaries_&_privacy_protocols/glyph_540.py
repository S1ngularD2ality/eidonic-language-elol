# glyph_540 – DECRYPT_CONFIG
# Decrypt configuration files encrypted by glyph_539

from cryptography.fernet import Fernet

def glyph_540(encrypted_config, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_config).decode()
