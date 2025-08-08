# glyph_548 – DECRYPT_DICT
# Decrypt a token created by glyph_547

import json
from cryptography.fernet import Fernet

def glyph_548(token, key):
    fernet = Fernet(key)
    return json.loads(fernet.decrypt(token).decode())
