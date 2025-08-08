# glyph_593 – SECURE_KEY_VAULT
# Store multiple keys in encrypted vault

import json
from cryptography.fernet import Fernet

def glyph_593(keys):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_vault = fernet.encrypt(json.dumps(keys).encode())
    return encrypted_vault, key
