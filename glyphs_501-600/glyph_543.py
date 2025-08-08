# glyph_543 – MULTI_KEY_ENCRYPT
# Encrypt with multiple keys for layered security

from cryptography.fernet import Fernet

def glyph_543(data, key_count=3):
    keys = [Fernet.generate_key() for _ in range(key_count)]
    encrypted = data.encode()
    for key in keys:
        encrypted = Fernet(key).encrypt(encrypted)
    return encrypted, keys
