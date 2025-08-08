# glyph_589 – SECURE_PASSWORD_RESET
# Generate and encrypt password reset token

import secrets
from cryptography.fernet import Fernet

def glyph_589():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    token = secrets.token_urlsafe(16)
    return fernet.encrypt(token.encode()), key
