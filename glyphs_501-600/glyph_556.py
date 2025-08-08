# glyph_556 – LOG_DECRYPT
# Decrypt log entries encrypted by glyph_555

import json
from cryptography.fernet import Fernet

def glyph_556(encrypted_logs, key):
    fernet = Fernet(key)
    return json.loads(fernet.decrypt(encrypted_logs).decode())
