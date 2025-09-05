# glyph_584 – DECRYPT_VIDEO_STREAM
# Decrypt video chunks encrypted by glyph_583

from cryptography.fernet import Fernet

def glyph_584(encrypted_chunks, key):
    fernet = Fernet(key)
    return [fernet.decrypt(chunk) for chunk in encrypted_chunks]
