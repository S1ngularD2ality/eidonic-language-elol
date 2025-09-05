# glyph_594 – DECRYPT_KEY_VAULT
# Decrypt key vault from glyph_593

import json
from cryptography.fernet import Fernet

def glyph_594(encrypted_vault, key):
    fernet = Fernet(key)
    return json.loads(fernet.decrypt(encrypted_vault).decode())
