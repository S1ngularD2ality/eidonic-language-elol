# glyph_547 – ENCRYPT_DICT
# Encrypt a dictionary into a single token

import json
from cryptography.fernet import Fernet

def glyph_547(data_dict):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    token = fernet.encrypt(json.dumps(data_dict).encode())
    return token, key
