# glyph_566 – SECURE_SESSION_STORE
# Store encrypted session data

from cryptography.fernet import Fernet

def glyph_566(session_data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    token = fernet.encrypt(session_data.encode())
    return token, key
