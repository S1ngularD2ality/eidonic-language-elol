# glyph_571 – ENCRYPT_IMAGE
# Encrypt image file data

from cryptography.fernet import Fernet

def glyph_571(image_path):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(image_path, 'rb') as img:
        encrypted = fernet.encrypt(img.read())
    return encrypted, key
