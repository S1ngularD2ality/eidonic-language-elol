# glyph_573 – ENCRYPT_TEXT_FILE
# Encrypt a plain text file

from cryptography.fernet import Fernet

def glyph_573(file_path):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        encrypted = fernet.encrypt(f.read())
    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted)
    return key
