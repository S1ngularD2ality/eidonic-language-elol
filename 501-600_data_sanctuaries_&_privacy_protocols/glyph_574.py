# glyph_574 – DECRYPT_TEXT_FILE
# Decrypt a text file encrypted by glyph_573

from cryptography.fernet import Fernet

def glyph_574(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        decrypted = fernet.decrypt(f.read())
    with open(file_path.replace('.enc', ''), 'wb') as f:
        f.write(decrypted)
