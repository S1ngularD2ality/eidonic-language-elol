# glyph_579 – DECRYPT_DATABASE
# Decrypt database content from glyph_578

import pickle
from cryptography.fernet import Fernet

def glyph_579(token, key):
    fernet = Fernet(key)
    return pickle.loads(fernet.decrypt(token))
