# glyph_564 – ENCRYPT_ZIP
# Compress and encrypt files into a zip archive

import zipfile
from cryptography.fernet import Fernet

def glyph_564(file_paths):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with zipfile.ZipFile('archive.zip', 'w') as zipf:
        for file_path in file_paths:
            with open(file_path, 'rb') as f:
                encrypted = fernet.encrypt(f.read())
            zipf.writestr(file_path + '.enc', encrypted)
    return key
