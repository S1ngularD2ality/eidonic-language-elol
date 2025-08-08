# glyph_555 – LOG_ENCRYPT
# Encrypt log entries for secure storage

import json
from cryptography.fernet import Fernet

def glyph_555(log_entries):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(json.dumps(log_entries).encode())
    return encrypted, key
