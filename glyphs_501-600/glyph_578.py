# glyph_578 – ENCRYPT_DATABASE
# Encrypt serialized database content

import pickle
from cryptography.fernet import Fernet

def glyph_578(database):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    token = fernet.encrypt(pickle.dumps(database))
    return token, key
