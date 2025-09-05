# glyph_590 – VALIDATE_PASSWORD_RESET
# Decrypt and validate password reset token

from cryptography.fernet import Fernet

def glyph_590(encrypted_token, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_token).decode()
