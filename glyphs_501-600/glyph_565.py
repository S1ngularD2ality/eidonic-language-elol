# glyph_565 – DECRYPT_ZIP
# Decrypt files from an encrypted zip archive

import zipfile
from cryptography.fernet import Fernet

def glyph_565(zip_path, key):
    fernet = Fernet(key)
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        for file_name in zipf.namelist():
            encrypted = zipf.read(file_name)
            decrypted = fernet.decrypt(encrypted)
            with open(file_name.replace('.enc', ''), 'wb') as f:
                f.write(decrypted)
