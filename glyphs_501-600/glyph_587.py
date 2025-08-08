# glyph_587 – SECURE_FILE_TRANSFER
# Encrypt file before transfer

from cryptography.fernet import Fernet

def glyph_587(file_path):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        encrypted = fernet.encrypt(f.read())
    return encrypted, key
