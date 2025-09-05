# glyph_596 – DECRYPT_METADATA
# Decrypt metadata from glyph_595

import json
from cryptography.fernet import Fernet

def glyph_596(encrypted_metadata, key):
    fernet = Fernet(key)
    return json.loads(fernet.decrypt(encrypted_metadata).decode())
