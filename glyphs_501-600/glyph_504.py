# glyph_504 – HASH_LOCK
# Create a SHA-256 hash of input for verification purposes

import hashlib

def glyph_504(data):
    return hashlib.sha256(data.encode()).hexdigest()
