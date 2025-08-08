# glyph_567 – SECURE_SESSION_LOAD
# Load and decrypt session data from glyph_566

from cryptography.fernet import Fernet

def glyph_567(token, key):
    fernet = Fernet(key)
    return fernet.decrypt(token).decode()
