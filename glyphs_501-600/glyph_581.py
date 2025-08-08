# glyph_581 – SECURE_API_GATEWAY
# Authenticate and encrypt API requests

from cryptography.fernet import Fernet

def glyph_581(api_request, key=None):
    if not key:
        key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(api_request.encode())
    return encrypted, key
