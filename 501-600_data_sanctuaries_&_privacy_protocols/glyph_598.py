# glyph_598 – ENCRYPT_STREAM_FILE
# Encrypt file for streaming in chunks

from cryptography.fernet import Fernet

def glyph_598(file_path, chunk_size=1024):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        encrypted_chunks = [fernet.encrypt(chunk) for chunk in iter(lambda: f.read(chunk_size), b'')]
    return encrypted_chunks, key
