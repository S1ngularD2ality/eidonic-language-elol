# glyph_559 – SAFE_DESERIALIZE
# Decrypt and deserialize objects encrypted by glyph_558

import pickle
from cryptography.fernet import Fernet

def glyph_559(token, key):
    fernet = Fernet(key)
    return pickle.loads(fernet.decrypt(token))
