# glyph_568 – SECURE_TEMP_FILE
# Create a temporary file with encrypted content

import tempfile
from cryptography.fernet import Fernet

def glyph_568(content):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(content.encode())
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(encrypted)
    temp.close()
    return temp.name, key
