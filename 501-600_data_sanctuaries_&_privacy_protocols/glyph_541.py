# glyph_541 – SECURE_ARCHIVE
# Archive data with encryption for long-term storage

from cryptography.fernet import Fernet

def glyph_541(data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return {"archive": encrypted, "key": key}
