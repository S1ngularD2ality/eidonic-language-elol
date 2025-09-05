# glyph_544 – MULTI_KEY_DECRYPT
# Decrypt data encrypted with glyph_543

from cryptography.fernet import Fernet

def glyph_544(encrypted, keys):
    decrypted = encrypted
    for key in reversed(keys):
        decrypted = Fernet(key).decrypt(decrypted)
    return decrypted.decode()
