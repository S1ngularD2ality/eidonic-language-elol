# glyph_588 – DECRYPT_FILE_TRANSFER
# Decrypt file from glyph_587

from cryptography.fernet import Fernet

def glyph_588(encrypted_data, key, output_path):
    fernet = Fernet(key)
    with open(output_path, 'wb') as f:
        f.write(fernet.decrypt(encrypted_data))
