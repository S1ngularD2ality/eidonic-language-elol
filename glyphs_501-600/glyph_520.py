# glyph_520 – ENCRYPT_STREAM
# Encrypt a continuous data stream

from cryptography.fernet import Fernet

def glyph_520(data_chunks):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return [fernet.encrypt(chunk) for chunk in data_chunks], key
