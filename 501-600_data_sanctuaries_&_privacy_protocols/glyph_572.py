# glyph_572 – DECRYPT_IMAGE
# Decrypt image file data from glyph_571

from cryptography.fernet import Fernet

def glyph_572(encrypted_image, key, output_path):
    fernet = Fernet(key)
    with open(output_path, 'wb') as img:
        img.write(fernet.decrypt(encrypted_image))
