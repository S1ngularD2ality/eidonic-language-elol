# glyph_797 – DATA_SANCTUM_LOCK
# Encrypt and lock critical data vault.

from cryptography.fernet import Fernet

class glyph_797:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def lock(self, data):
        return self.cipher.encrypt(data.encode())

    def unlock(self, token):
        return self.cipher.decrypt(token).decode()
