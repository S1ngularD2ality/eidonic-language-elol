# glyph_505 – SALT_HASH
# Generate a salted hash for secure password storage

import os, hashlib

def glyph_505(password):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, hashed
