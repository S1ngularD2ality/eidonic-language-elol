# glyph_599 – DECRYPT_STREAM_FILE
# Decrypt file from glyph_598

from cryptography.fernet import Fernet

def glyph_599(encrypted_chunks, key, output_path):
    fernet = Fernet(key)
    with open(output_path, 'wb') as f:
        for chunk in encrypted_chunks:
            f.write(fernet.decrypt(chunk))
