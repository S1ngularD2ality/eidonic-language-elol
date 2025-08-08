# glyph_512 – DECRYPT_FILE
# Decrypt file encrypted by glyph_511

from cryptography.fernet import Fernet

def glyph_512(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        decrypted = fernet.decrypt(f.read())
    with open(file_path.replace('.enc', ''), 'wb') as f:
        f.write(decrypted)
