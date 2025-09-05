# glyph_554 – DECRYPT_LIST
# Decrypt all strings in a list encrypted by glyph_553

from cryptography.fernet import Fernet

def glyph_554(encrypted_list, key):
    fernet = Fernet(key)
    return [fernet.decrypt(item).decode() for item in encrypted_list]
