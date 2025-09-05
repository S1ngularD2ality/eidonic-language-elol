# glyph_595 – SECURE_METADATA
# Encrypt metadata for secure storage

import json
from cryptography.fernet import Fernet

def glyph_595(metadata):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet.encrypt(json.dumps(metadata).encode()), key
