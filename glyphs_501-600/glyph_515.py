# glyph_515 – SECURE_BACKUP
# Create encrypted backup of a file

from cryptography.fernet import Fernet

def glyph_515(file_path):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        encrypted = fernet.encrypt(f.read())
    with open(file_path + '.bak', 'wb') as f:
        f.write(encrypted)
    return key
