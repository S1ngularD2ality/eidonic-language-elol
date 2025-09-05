# glyph_948 – CANARY_TOKEN_MAKER
"""
Canary Token Maker

Generates unique tokens that should never be accessed in normal operation.
Any access (HTTP beacon, file open, etc.) signals compromise.

APIs:
- make_token(tag: str) -> bytes
- check_token(token: bytes, access_log: set) -> bool
"""

import os, hashlib

def make_token(tag: str) -> bytes:
    seed = os.urandom(32) + tag.encode()
    return hashlib.blake2b(seed, digest_size=16).digest()

def check_token(token: bytes, access_log: set) -> bool:
    # In practice, access_log would be an external monitor
    return token in access_log
