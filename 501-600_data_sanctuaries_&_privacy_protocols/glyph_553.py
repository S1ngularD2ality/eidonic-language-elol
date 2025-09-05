# glyph_553 – ENCRYPT_LIST
# Encrypt all strings in a list

from cryptography.fernet import Fernet

def glyph_553(data_list):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_list = [fernet.encrypt(item.encode()) for item in data_list]
    return encrypted_list, key
