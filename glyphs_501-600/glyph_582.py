# glyph_582 – DECRYPT_API_REQUEST
# Decrypt API request encrypted by glyph_581

from cryptography.fernet import Fernet

def glyph_582(encrypted_request, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_request).decode()
