# glyph_511 – ENCRYPT_FILE
# Encrypt file contents and save to disk

from cryptography.fernet import Fernet

def glyph_511(file_path):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        encrypted = fernet.encrypt(f.read())
    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted)
    return key
