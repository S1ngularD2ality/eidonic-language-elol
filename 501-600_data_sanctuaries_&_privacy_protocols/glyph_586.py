# glyph_586 – DECRYPT_AUDIO_STREAM
# Decrypt audio chunks encrypted by glyph_585

from cryptography.fernet import Fernet

def glyph_586(encrypted_chunks, key):
    fernet = Fernet(key)
    return [fernet.decrypt(chunk) for chunk in encrypted_chunks]
