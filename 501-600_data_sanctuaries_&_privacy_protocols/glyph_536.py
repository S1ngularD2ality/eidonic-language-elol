# glyph_536 – KEY_ROTATE
# Rotate encryption keys

from cryptography.fernet import Fernet

def glyph_536(old_key, data):
    new_key = Fernet.generate_key()
    fernet_old = Fernet(old_key)
    fernet_new = Fernet(new_key)
    decrypted = fernet_old.decrypt(data)
    encrypted = fernet_new.encrypt(decrypted)
    return encrypted, new_key
