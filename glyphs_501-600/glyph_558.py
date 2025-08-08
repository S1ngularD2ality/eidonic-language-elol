# glyph_558 – SAFE_SERIALIZE
# Serialize and encrypt Python objects

import pickle
from cryptography.fernet import Fernet

def glyph_558(obj):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    token = fernet.encrypt(pickle.dumps(obj))
    return token, key
